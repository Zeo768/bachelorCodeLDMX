#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:44:46 2020

@author: danmag
"""


import ROOT as r
import numpy as np
import sys
from optparse import OptionParser
sys.path.insert(0, '../')
import time

class roottoarray:
    
    def __init__(self,infile,outfile):
        
        self.fin=r.TFile(infile)
        self.tin = self.fin.Get("LDMX_Events")
        self.fout=outfile
        self.simParticles = r.TClonesArray('ldmx::SimParticle')
        self.ECalSimHits = r.TClonesArray('ldmx::SimCalorimeterHit');
        #self.ecalHits = r.TClonesArray('ldmx::EcalHit')
        self.tin.SetBranchAddress("EcalSimHits_sim",  r.AddressOf( self.ECalSimHits ))
        self.tin.SetBranchAddress("SimParticles_sim",  r.AddressOf( self.simParticles ))
        #self.tin.SetBranchAddress("ecalDigis_recon",  r.AddressOf( self.ecalHits ));
        
    
    
    def loop(self):
        nent = self.tin.GetEntriesFast()
        print("nent = ", nent)
        i=0
        y_min=-27
        y_max=27
        #27,26,24!!!
#        z_min=230
#        z_max=390
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        x_min=-16#!!!!!!!!!!!!!!!!!!
        x_max=16
        #12,14,16!!!
        zLayerPosList=[223.8000030517578, 226.6999969482422, 233.0500030517578, 237.4499969482422, 245.3000030517578,
        251.1999969482422, 260.29998779296875, 266.70001220703125, 275.79998779296875, 282.20001220703125,
        291.29998779296875, 297.70001220703125, 306.79998779296875, 313.20001220703125, 322.29998779296875,
        328.70001220703125, 337.79998779296875, 344.20001220703125, 353.29998779296875, 359.70001220703125,
        368.79998779296875, 375.20001220703125, 384.29998779296875, 390.70001220703125, 403.29998779296875,
        413.20001220703125, 425.79998779296875, 435.70001220703125, 448.29998779296875,
        458.20001220703125, 470.79998779296875, 480.70001220703125, 493.29998779296875, 503.20001220703125]
        start=time.time()
        EventEcalArray=np.zeros((nent,x_max-x_min,y_max-y_min,26))
        #26,28
        #EcalRecArray=np.zeros((nent,x_max-x_min,y_max-y_min,28))
        EventEcalClassifier=np.zeros(nent)
        end=time.time()
        eventEList=[]
        inithitlist=[]
        inithitlistextra=[]
        inithitlisttest=[]
        #print(end-start)
        fraction=0
        nHits1=0
        nHits2=0
        sumeventenergy=0
        sumhitsenergy=0

        for i in range(nent):
            self.tin.GetEntry(i)
            print("Event:",i)
            tothitenergy=0
            hitenergy=0
            eventenergy=0
            #print(end-start)
            for ip,p in enumerate(self.simParticles):
                if p.getPdgID() == 11:
                    if p.getParentCount() == 0:
                        EventEcalClassifier[i]=p.getEnergy()
                        eventenergy=p.getEnergy()
                
            for ip,p in enumerate(self.ECalSimHits):
                x=p.getPosition()[0]/4.3
                y=p.getPosition()[1]/2.5
                z=p.getPosition()[2]
                tothitenergy+=p.getEdep()
                nHits1+=1
                if x_min<x<x_max and y_min<y<y_max and zLayerPosList[0] <= z <= zLayerPosList[-9]:
                    x1=int(round(x+x_max))
                    y1=int(round(y+y_max))
                    z1=zLayerPosList.index(z)
                    hitenergy+=p.getEdep()
                    nHits2+=1
                    EventEcalArray[i,x1,y1,z1]=p.getEdep()
                    if z1==0:
                        inithitlisttest.append((x,y))
                        inithitlist.append((x1,y1))
            #print(end-start)
            eventEList.append([hitenergy,tothitenergy])
            print("Eventsim energy=", hitenergy)
            print("Eventorg energy=",eventenergy)
            sumeventenergy+=eventenergy
            sumhitsenergy+=hitenergy
            #i+=1
        fraction=1.*nHits2/nHits1
        print(nHits1)
        print(nHits2)
        print("AvgEventenergy=",sumeventenergy/i)
        print("AvgHitenergy=",sumhitsenergy/i)
        print("Number of hits in the array/Number of hits in the Ecal:",fraction)
            
        
        return EventEcalArray,eventEList,EventEcalClassifier, inithitlist,inithitlisttest
            



def main(options,args):
    print ("Executing main()")
    ex = roottoarray(options.ifile,options.ofile) 
    EventArray,Elist,Classifier,inithitlist,inithitslisttest=ex.loop()
    
    #copy the root output into the output directory
    np.save(options.ofile,EventArray)
    np.save(options.ofile+'Elist',Elist)
    np.save(options.ofile+'Classifier',Classifier)
    np.save(options.ofile+'initxydist',inithitlist)
    np.save(options.ofile+'initxydisttest',inithitslisttest)
    print ("Completed main()")
    



if __name__ == "__main__":
    used_setup_path='/home/lene/LDMX/simulation/sw/'
    parser = OptionParser()
    parser.add_option('-b', action='store_true', dest='noX', default=False, help='no X11 windows')
	#parser.add_option("--lumi", dest="lumi", type=float, default = 30,help="luminosity", metavar="lumi")
    parser.add_option('-i','--ifile', dest='ifile', default = 'file.root',help='directory with data', metavar='idir')
    parser.add_option('-o','--ofile', dest='ofile', default = 'ofile.root',help='directory to write plots', metavar='odir')
	#parser.add_option('--swdir', dest='swdir', default = '/u/ey/ntran/ldmx/biasing/iss94/ldmx-sw',help='directory to write plots', metavar='odir')

    (options, args) = parser.parse_args()


	# Get the Event library 
#	r.gSystem.Load("%s/ldmx-sw/install/lib/libEvent.so" % used_setup_path)
#	r.gSystem.Load("%s/ldmx-sw/build/Event/libEvent.so" % used_setup_path)
    r.gSystem.Load("/projects/hep/fs7/scratch/pflorido/ldmx-singularity-reloaded/libs/ldmx-sw-install/lib/libEvent.so")
    main(options,args)