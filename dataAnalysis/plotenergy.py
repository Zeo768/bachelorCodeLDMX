#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:53:39 2020

@author: danmag
"""


import numpy as np
import sys

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D


Elist=np.load("0-3GeVAng160-180100000ArrayElist.npy")
Elist2=np.load("0-3GeVAng160-180100000ArrayRecElist.npy")
Elist3=np.load("0-3GeV100000ArrayElist.npy")
Elist4=np.load("0-3GeVRec100000ArrayElist.npy")
Classifier=np.load("0-3GeVAng160-180100000ArrayClassifier.npy")

Classifier3=np.load("0-3GeV100000ArrayClassifier.npy")

#Erec=EReclist[2599][0]
E=Elist[2599][0]
#Elist1=[i[0] for i in Elist]
#Elist2=[i[1] for i in Elist]
#EReclist1=[i[0] for i in EReclist]
#EReclist2=[i[1] for i in EReclist]

print(Classifier[:50])
#print(EReclist1[:50])
print(Classifier[15023:15100])
#print(EReclist1[15023:15100])
print(Classifier[39950:])
#print(EReclist1[39950:])

#Elist3=[i*Erec/E for i in Elist1]
#Esum=0
#Esumlist=[]
#for i in range(len(Classifier)):
#    Esum+=Classifier[i]
#    if i %100==0:
#        Esumlist.append(Esum/100)
#        Esum=0
#
#plt.scatter(range(len(Classifier)),Esumlist)

#nevents=len(EReclist1)
#msesum=0
#msesum2=0
#print(nevents)
#for i in range(nevents):
#    msesum+=(Classifier[i]-EReclist2[i])**2
#    msesum2+=(Classifier[i]-Elist3[i])**2
#mse=msesum/nevents
#print(mse)
#mse=msesum2/nevents
#print(mse)
linpopt=np.load('E0-3GeVlinrecfitkm.npy')
linpcov=np.load('E0-3GeVlinrecfitcovarmatrix.npy')
def lin_func(x,k,m):
    return k*x+m
#modelElist=Elist
#modelClassifier=Classifier
#linpopt, linpcov=curve_fit(lin_func,xdata=modelElist[:,0],ydata=modelClassifier,p0=[1,1000])
linylist=[]
linylisterr=[]
plt.figure()
xtemp=np.linspace(0,3200,1000)
plt.hist2d(Elist4[:,0],Classifier3,bins=60,cmap=plt.cm.jet)
plt.colorbar()
plt.plot(xtemp,lin_func(xtemp,*linpopt),color='k')
plt.ylim(0,3000)
plt.xlabel('Sum of hit Energy(MeV)')
plt.ylabel('True Energy(MeV)')
plt.title('Linear fit 0-3 GeV no angle set')
plt.savefig('graphs/E0-3GeVlinrecfit.png',dpi=200)
plt.close()



k,m=np.polyfit(Elist3[:,0],Classifier3,1)
print(k,m)

k2,m2=np.polyfit(Elist4[:,0],Classifier3,1)
print(k2,m2)
plt.hist(Elist[:,0],bins=100)
plt.show()
plt.hist(Classifier,bins=100)
plt.show()
plt.hist(Elist2[:,0],bins=100)
plt.show()

plt.hist(Elist3[:,0],bins=100)
plt.show()
plt.hist(Classifier3,bins=100)
plt.show()
plt.hist(Elist4[:,0],bins=100)
plt.show()

#Ehist3,bins=np.histogram(Elist3[:,0]*k+m,bins=35,range=(0,4500))
#Ehist4,temp=np.histogram(Elist4[:,0]*k2+m2,bins=35,range=(0,4500))
#Classifierhist,bins=np.histogram(Classifier,bins=33,range=(0,4500))
#binscenters = np.array([0.5 * (bins[j] + bins[j+1]) for j in range(len(bins)-1)])
#binerr=np.array([(bins[j+1]-bins[j])/2 for j in range(len(bins)-1)])
#
##plt.scatter(binscenters,Classifier)
##plt.show()
#
##plt.errorbar(binscenters,Ehist,xerr=binerr,fmt='o',color='navy',markersize=3,capsize=0,label='SimHits(scaled)')
##plt.errorbar(xlist,ylist,yerr=ylisterr,fmt='^',capsize=5,color='navy',label='CNN(S2)')
##plt.errorbar(binscenters,Ehist2,xerr=binerr,fmt='o',color='darkorange',markersize=3,capsize=0,label='RecHits(scaled)')
#plt.errorbar(binscenters,Classifierhist,xerr=binerr,fmt='o',color='red',markersize=3,capsize=0,label='True')
#plt.legend()
#plt.xlabel('Energy(MeV)')
#plt.ylabel('Counts')
#plt.title('Energy distribution Angle: 160-180')
#plt.savefig('graphs/EnergydistE0-3GeVAng160-180100000onlyC.png',dpi=200)
#plt.close()

#plt.errorbar(binscenters,Ehist3,xerr=binerr,fmt='o',color='navy',markersize=3,capsize=0,label='SimHits(scaled)')
##plt.errorbar(xlist,ylist,yerr=ylisterr,fmt='^',capsize=5,color='navy',label='CNN(S2)')
#plt.errorbar(binscenters,Ehist4,xerr=binerr,fmt='o',color='darkorange',markersize=3,capsize=0,label='RecHits(scaled)')
#plt.errorbar(binscenters,Classifier3hist,xerr=binerr,fmt='o',color='red',markersize=3,capsize=0,label='True')
#plt.legend()
#plt.xlabel('Energy(MeV)')
#plt.ylabel('Counts')
#plt.title('Energy distribution no angle set')
#plt.show()
##plt.savefig('graphs/EnergydistE0-3GeV100000.png',dpi=200)
#plt.close()

#plt.hist(Elist[:,0]*k+m,bins=100,range=(0,4500),alpha=0.5,label='SimHits')
#plt.hist(Classifier,bins=100,range=(0,4500),alpha=0.5,label='True')
#plt.xlabel('Energy(MeV)')
#plt.legend()
#plt.show()
#plt.hist([Elist[:,1]*k+m,Classifier,Elist2[:,1]*k2+m2],bins=30,range=(0,4500),label=['SimHits(scaled)','True','RecHits(scaled)'])
#plt.xlabel('Energy(MeV)')
#plt.legend()
#plt.show()

#plt.hist(EReclist1,bins=100)
#plt.show()
##plt.hist(Elist3,bins=100)
#plt.show()
##plt.hist(EReclist,bins=100)
#plt.show()

#plt.hist([EReclist1,Classifier],bins=50,range=(0,4500))
#plt.show()
#plt.hist(EReclist1,bins=50,range=(0,4500),alpha=0.9,label='RecHits')
#plt.hist(Classifier,bins=50,range=(0,4500),alpha=0.9,label='True')
#plt.legend()
#plt.show()
#plt.hist(Elist[:,0]*k2+m2,bins=100,range=(0,4500),alpha=0.9,label='SimHits(scaled)')
#plt.hist(Classifier,bins=100,range=(0,4500),alpha=0.9,label='True')
#plt.xlabel('Energy(MeV)')
#plt.legend()
#plt.savefig('graphs/EnergydistE0-3GeV100000.png',dpi=200)
#plt.close()
#plt.hist(Elist[:,0]*k+m,bins=100,range=(0,4500),alpha=0.5,label='SimHits(scaled)',edgecolor='black',linewidth=1.2)
#plt.hist(Elist2[:,0]*k2+m2,bins=100,range=(0,4500),alpha=0.5,label='RecHits(scaled)',edgecolor='black',linewidth=1.2)
#plt.hist(Classifier,bins=100,range=(0,4500),alpha=0.5,label='True',edgecolor='black',linewidth=1.2)
#plt.xlabel('Energy(MeV)')
#plt.legend()
#plt.show()
#plt.savefig('graphs/EnergydistE0-3GeVA160-180100000.png',dpi=200)
#plt.close()
#plt.plot(EReclist1[:],Classifier[:],'g.',label='Prediction vs True (Training)',markersize=0.3)
#x=np.linspace(0,3000,100)
#plt.xlabel('Prediction Energy(MeV)')
#plt.ylabel('True Energy(MeV)')
#plt.plot(x,x*k+m,label='linear')
#plt.show()
#plt.plot(Elist3[:],Classifier[:],'g.',label='Prediction vs True (Training)',markersize=0.3)
#x=np.linspace(0,3000,100)
#plt.xlabel('Prediction Energy(MeV)')
#plt.ylabel('True Energy(MeV)')
#plt.plot(x,x,label='linear')
#plt.show()
#plt.hist(Classifier,bins=100)
#plt.show()