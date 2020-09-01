#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:19:29 2020

@author: danmag
"""

import numpy as np
import time
import argparse
#import seaborn as sns
from tensorflow.keras.models import Model,load_model
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

#import pandas as pd

#from sklearn.metrics import *


def main(args):
    print ("Executing main()")
    start=time.time()
    K.clear_session()


    
#    Dname='modelDCE0-3RecfixNSD0.04N551210.000051032.h5'
#    name='CE0-3RecfixC208M2C104M2D0.1N5150010.00120128'
#    name='CE0-3RecfixC208M2C104M2D0.1N5150010.0012064'
    
    Dname='modelDCE0-3fixNSD0.04N551210.000051064.h5'
#    Dname='modelDCE0-3fixNSD0.04N551210.000051032.h5'
#    name='CE0-3fixC208M2C104M2D0.1N5150010.00120256'
    name='CE0-3fixNSC208M2C104M2D0.1N5150010.00120256'
#    name='CE0-3fixC208M2C104M2D0.1N5150010.00120128'

#    Dname='modelDCE0-3A160-180RecfixNSD0.04N540010.000011032.h5' #best
#    Dname='modelDCE0-3A160-180RecfixNSD0.04N551210.000011064.h5'
#    name='CE0-3A160-180RecfixNSC208M2C104M2D0.1N5150010.00120256'
#    name='CE0-3A160-180RecfixNSC208M2C104M2D0.12N5150010.00120256'

#    Dname='modelDCE0-3A160-180D0.04N551210.0000510128.h5'
#    name='CE0-3fixC208M2C104M2D0.1N5150010.00120256'

    titlestring='Energy resolution 0-3 GeV no angle set sim hits'
    print('models/goodval/model'+name+'.h5')
    xlist=[]
    ylist=[]
    ylisterr=[]
    Dylist=[]
    Dylisterr=[]
    model = load_model('models/goodval/model'+name+'.h5')
    DNNmodel= load_model('models/goodval/'+Dname)
    model.summary()
    def fit_function(x, A, mu, sigma):
        return ( A * np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2)))
    end=time.time()
    print(end-start)
    def lin_func(x,k,m):
        return k*x+m
#    modelElist=np.load(args.file[-2])
#    modelClassifier=np.load(args.file[-1])
#    linpopt, linpcov=curve_fit(lin_func,xdata=modelElist[:,0],ydata=modelClassifier,p0=[1,1000])
    linylist=[]
    linylisterr=[]
#    plt.figure()
#    xtemp=np.linspace(0,3200,1000)
#    plt.hist2d(modelElist[:,0],modelClassifier,bins=60,cmap=plt.cm.jet)
#    plt.colorbar()
#    plt.plot(xtemp,lin_func(xtemp,*linpopt),color='k')
#    plt.ylim(0,3000)
#    plt.xlabel('SimHit Energy(MeV)')
#    plt.ylabel('True Energy(MeV)')
#    plt.savefig('graphs/E0-3GeVlinfit'+name+'.png')
#    plt.close()
#    np.save('E0-3GeVlinfitkm.npy',linpopt)
#    np.save('E0-3GeVlinfitcovarmatrix.npy',linpcov)
    linpopt=np.load('E0-3GeVlinfitkm.npy')
    linpcov=np.load('E0-3GeVlinfitcovarmatrix.npy')
    alist=np.arange(0,9,1)
    rangelist=[(-250,200),(-400,300),(-400,400),(-500,500),(-600,500),(-600,500),(-700,600),(-600,700),(-500,700)]
    linrangelist=[(-400,200),(-500,300),(-600,400),(-600,500),(-700,600),(-700,600),(-750,700),(-800,750),(-800,800)]
    Drangelist=[(-300,250),(-450,300),(-500,400),(-600,500),(-600,500),(-750,700),(-750,700),(-700,700),(-600,700)]
    print(alist)
    for i in alist:
        print('array:', i)
        TestArray=np.load(args.file[3*i])
        Elist=np.load(args.file[3*i+1])
        Classifier=np.load(args.file[3*i+2])
        nevents,x,y,z=TestArray.shape
        E=Classifier[30]
        xtest=TestArray.reshape(nevents,x,y,z,1)
        ytestpred=model.predict(xtest)
    
        ydeltatest=np.asarray([E - ytestpred[j][0] for j in range(nevents)])
        xlist.append(E)
        msesum=0
        maesum=0
        for j in range(nevents):
            msesum+=(E-ytestpred[j][0])**2
            maesum+=abs(E-ytestpred[j][0])
        mse=msesum/nevents
        mae=maesum/nevents
        print('MSE: ',mse)
        print('MAE: ',mae)
#        data_entries,bins,temp=plt.hist(ydeltatest,bins=100,range=(rangelist[i][0]-200,rangelist[i][1]+200)) 
        data_entries,bins,temp=plt.hist(ydeltatest,bins=100) 
        #plt.savefig('graphs/deltaEhist'+name+'.png')
        binscenters = np.array([0.5 * (bins[j] + bins[j+1]) for j in range(len(bins)-1)])
        #,sigma=[np.sqrt(j) for j in data_entries]
        popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=data_entries, p0=[ydeltatest.max(),0,200])
        
        print(popt)
        print(pcov)
        ylist.append(popt[2]/E)
        ylisterr.append(np.sqrt(pcov[2][2])/E)
        np.save('covarmatrices/network'+name,pcov)
        xspace = np.linspace(rangelist[i][0]-200, rangelist[i][1]+200, 100000)
        plt.figure()
        plt.bar(binscenters, data_entries, width=bins[1] - bins[0], color='navy', label=r'Histogram entries')
        plt.plot(xspace, fit_function(xspace, *popt), color='darkorange', linewidth=2.5, label=r'Fitted function')
        plt.legend()
        s='graphs/networkdEhistfit'+str(E)+name+'.png'
        plt.tight_layout()
        plt.savefig(s)
        plt.close()

        ####Linear

        linydeltatest=np.asarray([E-lin_func(Elist[j][0], *linpopt) for j in range(nevents)])
#        linydeltatesterr=np.asarray([np.sqrt(ydeltatest[j]) for j in range(nevents)])
#        linydeltaerr=np.asarray([E-lin_func(Elist[j][0],np.sqrt(linpcov[0][0]),np.sqrt(linpcov[1][1])) for j in range(nevents)])
        msesum=0
        maesum=0
        for j in range(nevents):
            msesum+=(E-lin_func(Elist[j][0],*linpopt))**2
            maesum+=abs(E-lin_func(Elist[j][0],*linpopt))
        mse=msesum/nevents
        mae=maesum/nevents
        print('linMSE:',mse)
        print('linMAE: ',mae)

#        lindata_entries,bins,temp=plt.hist(linydeltatest,bins=100,range=linrangelist[i])
        lindata_entries,bins,temp=plt.hist(linydeltatest,bins=100)
        binscenters = np.array([0.5 * (bins[j] + bins[j+1]) for j in range(len(bins)-1)])
        #,sigma=[np.sqrt(j) for j in lindata_entries]
        popt2, pcov2 = curve_fit(fit_function, xdata=binscenters, ydata=lindata_entries, p0=[linydeltatest.max(),0,400])
        
        print(popt2)
        print(pcov2)
        linylist.append(abs(popt2[2]/E))
        linylisterr.append(np.sqrt(pcov[2][2])/E)
        np.save('covarmatrices/lin'+name,pcov2)
        xspace = np.linspace(linrangelist[i][0]-200, linrangelist[i][1]+200, 100000)
        plt.figure()
        plt.bar(binscenters, lindata_entries, width=bins[1] - bins[0], color='navy', label=r'Histogram entries')
        plt.plot(xspace, fit_function(xspace, *popt2), color='darkorange', linewidth=2.5, label=r'Fitted function')
        plt.legend()
        s='graphs/reclindEhistfit'+str(E)+name+'.png'
        plt.tight_layout()
        plt.savefig(s)
        plt.close()
        
        ###DNN
        
#        xtest=TestArray.reshape(nevents,x,y,z,1)
        ytestpred=DNNmodel.predict(xtest)
    
        ydeltatest=np.asarray([E - ytestpred[j][0] for j in range(nevents)])
#        ydeltatesterr=np.asarray([np.sqrt(ydeltatest[j]) for j in range(nevents)])
        msesum=0
        maesum=0
        for j in range(nevents):
            msesum+=(E-ytestpred[j][0])**2
            maesum+=abs(E-ytestpred[j][0])
        mse=msesum/nevents
        mae=maesum/nevents
        print('MSE: ',mse)
        print('MAE: ',mae)
#        data_entries,bins,temp=plt.hist(ydeltatest,bins=100,range=Drangelist[i]) 
        data_entries,bins,temp=plt.hist(ydeltatest,bins=100) 
        #plt.savefig('graphs/deltaEhist'+name+'.png')
        binscenters = np.array([0.5 * (bins[j] + bins[j+1]) for j in range(len(bins)-1)])
        #,sigma=[np.sqrt(j) for j in data_entries]
        popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=data_entries, p0=[ydeltatest.max(),0,300])
        
        print(popt)
        print(pcov)
        Dylist.append(popt[2]/E)
        Dylisterr.append(np.sqrt(pcov[2][2])/E)
        np.save('covarmatrices/network'+name,pcov)
        xspace = np.linspace(Drangelist[i][0]-200, Drangelist[i][1]+200, 100000)
        plt.figure()
        plt.bar(binscenters, data_entries, width=bins[1] - bins[0], color='navy', label=r'Histogram entries')
        plt.plot(xspace, fit_function(xspace, *popt), color='darkorange', linewidth=2.5, label=r'Fitted function')
        plt.legend()
        s='graphs/networkdEhistfit'+str(E)+Dname+'.png'
        plt.tight_layout()
        plt.savefig(s)
        plt.close()
    
    
    
    def Eres_func(E,a):
        return a/np.sqrt(E)
    
    Erespopt,Erespcov = curve_fit(Eres_func,xdata=xlist,ydata=ylist,p0=[4],sigma=ylisterr)
    DErespopt,DErespcov = curve_fit(Eres_func,xdata=xlist,ydata=Dylist,p0=[4],sigma=Dylisterr)
    linErespopt,linErespcov = curve_fit(Eres_func,xdata=xlist,ydata=linylist,p0=[4],sigma=linylisterr)
    Espace=np.linspace(400,3000,10000)
    print(Erespopt,np.sqrt(Erespcov[0][0]))
    print(linErespopt,np.sqrt(linErespcov[0][0]))
    print(DErespopt,np.sqrt(DErespcov[0][0]))
    plt.figure()
    plt.grid(True)
    plt.title(titlestring)
    plt.plot(Espace,Eres_func(Espace,*Erespopt),color='navy',label=r'$ \frac{{\sigma(\Delta E)}}{{E_{{true}}}}=\frac{{{:.2f}}}{{\sqrt{{E_{{true}}}}}}$'.format(*Erespopt))
    plt.errorbar(xlist,ylist,yerr=ylisterr,fmt='^',capsize=5,color='navy',label='CNN(S2)')
    plt.plot(Espace,Eres_func(Espace,*linErespopt),color='darkorange',label=r'$ \frac{{\sigma(\Delta E)}}{{E_{{true}}}}=\frac{{{:.2f}}}{{\sqrt{{E_{{true}}}}}}$'.format(*linErespopt))
    plt.errorbar(xlist,linylist,yerr=linylisterr,fmt='o',capsize=5,color='darkorange',label='Linear fit')
    plt.plot(Espace,Eres_func(Espace,*DErespopt),color='red',label=r'$ \frac{{\sigma(\Delta E)}}{{E_{{true}}}}=\frac{{{:.2f}}}{{\sqrt{{E_{{true}}}}}}$'.format(*DErespopt))
    plt.errorbar(xlist,Dylist,yerr=Dylisterr,fmt='s',capsize=5,color='red',label='DNN')
    plt.legend()
    plt.xlabel('True Energy(MeV)',fontsize=10)
    plt.ylabel(r'$\frac{\sigma(\Delta E)}{E_{true}}$',fontsize=14)
    plt.tight_layout()
    plt.savefig('graphs/sigmadeltaEplot9pointsnoconst'+name+Dname+'.png',dpi=200)
    
    
    print ("Completed main()")
    



if __name__ == "__main__":

    #used_setup_path='/home/lene/LDMX/simulation/sw/'
    parser = argparse.ArgumentParser()
    #parser.add_option('-b', action='store_true', dest='noX', default=False, help='no X11 windows')
	#parser.add_option("--lumi", dest="lumi", type=float, default = 30,help="luminosity", metavar="lumi")
    #parser.add_option('-i','--ifile', dest='ifile', default = 'file.root',help='directory with data', metavar='idir')
    #parser.add_option('-o','--ofile', dest='ofile', default = 'ofile.root',help='directory to write plots', metavar='odir')
	#parser.add_option('--swdir', dest='swdir', default = '/u/ey/ntran/ldmx/biasing/iss94/ldmx-sw',help='directory to write plots', metavar='odir')

    parser.add_argument('file',nargs='*')

    args = parser.parse_args()


	# Get the Event library 
#	r.gSystem.Load("%s/ldmx-sw/install/lib/libEvent.so" % used_setup_path)
#	r.gSystem.Load("%s/ldmx-sw/build/Event/libEvent.so" % used_setup_path)
    #r.gSystem.Load("/projects/hep/fs7/scratch/pflorido/ldmx-singularity-reloaded/libs/ldmx-sw-install/lib/libEvent.so")
    main(args)
