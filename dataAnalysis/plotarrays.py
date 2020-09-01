#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:14:52 2020

@author: danmag
"""

import numpy as np
import sys

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


Data=np.load("0-3GeVAng160-180100000ArrayRec.npy")
Classifier=np.load("0-3GeVAng160-180100000ArrayRecClassifier.npy")
nevents,x,y,z=Data.shape
name='0-3GeVAng160-180Rec'
#Classifier=npzfile['classifier']
#Data=npzfile['array']
#print(Classifier[:300])
#num1=0
#num2=0
#num3=0
#numx=0
#for i in Classifier:
#    if i==1:
#        num1+=1
#    if i==2:
#        num2+=1
#    if i==3:
#        num3+=1
#    if i>3:
#        numx+=1
#
#print(num1,num2,num3,numx)

arr1=Data[5003]
ene1=Classifier[5003]
arr2=Data[56405]
ene2=Classifier[56405]
arr3=Data[70543]
ene3=Classifier[70543]
#
print(ene1)
print(ene2)
print(ene3)
strene1='{:.2f}'.format(ene1)
strene2='{:.2f}'.format(ene2)
strene3='{:.2f}'.format(ene3)

x1,y1,z1=np.nonzero(arr1)
x2,y2,z2=np.nonzero(arr2)
x3,y3,z3=np.nonzero(arr3)
#plt.figure()
#plt.hist(x1,bins=24,range=(0,24))
#plt.savefig('datagraphs/xdist'+name+'set2'+strene1+'.png')
#plt.figure()
#plt.hist(y1,bins=48,range=(0,48))
#plt.savefig('datagraphs/ydist'+name+'set2'+strene1+'.png')
#plt.figure()
#plt.hist(z1,bins=34,range=(0,34))
#plt.savefig('datagraphs/zdist'+name+'set2'+strene1+'.png')
#plt.figure()
#plt.hist(x2,bins=24,range=(0,24))
#plt.savefig('datagraphs/xdist'+name+'set2'+strene2+'.png')
#plt.figure()
#plt.hist(y2,bins=48,range=(0,48))
#plt.savefig('datagraphs/ydist'+name+'set2'+strene2+'.png')
#plt.figure()
#plt.hist(z2,bins=34,range=(0,34))
#plt.savefig('datagraphs/zdist'+name+'set2'+strene2+'.png')






x1true=[4.3*x for x in x1]
y1true=[2.5*y for y in y1]

fig = plt.figure()
fig.suptitle(name+' '+strene1+' MeV')
ax1 = Axes3D(fig)

ax1.scatter(x1, y1, z1, c='r', marker='.',s=40)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_xlim3d(0,32)
ax1.set_ylim3d(0,54)
ax1.set_zlim3d(0,26)


ax1.view_init(elev=27., azim=310)
plt.savefig('datagraphs/'+name+'set2array'+strene1+'.png',dpi=300)
#elevv=20.
#for elevv in np.linspace(18,22,3):
#    for ii in np.linspace(300,340,4):
#            ax1.view_init(elev=elevv, azim=ii)
#            plt.savefig('datagraphs/'+name+'set2array'+strene1+'{}degree{}elev.png'.format(ii,elevv))

fig = plt.figure()
fig.suptitle(name+' '+strene2+' MeV')

ax2 = Axes3D(fig)

ax2.scatter(x2, y2, z2, c='r', marker='.',s=40)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_xlim3d(0,32)
ax2.set_ylim3d(0,54)
ax2.set_zlim3d(0,26)
ax2.view_init(elev=27., azim=310)
plt.savefig('datagraphs/'+name+'set2array'+strene2+'.png',dpi=300)




fig=plt.figure()
fig.suptitle(name+' '+strene3+' MeV')
ax3 = Axes3D(fig)

ax3.scatter(x3, y3, z3, c='r', marker='.',s=40)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_xlim3d(0,32)
ax3.set_ylim3d(0,54)
ax3.set_zlim3d(0,26)
ax3.view_init(elev=27., azim=310)
plt.savefig('datagraphs/'+name+'set2array'+strene3+'.png',dpi=300)



#layer distribution

#
#for i in range(z):
#    events,x4,y4=np.nonzero(Data[:,:,:,i])
#    print(i)
#    plt.figure()
#    numy=np.bincount(y4)
#    print(numy)
#    numx=np.bincount(x4)
#    print(numx)
#    plt.hist2d(x4,y4,bins=(31,53),cmap=plt.cm.jet)
#    plt.colorbar()
#    t=str(i)
#    plt.savefig('datagraphs/'+name+'set2z='+t+'xydist.png')
#    plt.close()
#
#events,x5,y5,z5=np.nonzero(Data)
#
#plt.figure()
#plt.hist2d(x5,y5,bins=(31,53),cmap=plt.cm.jet)
#plt.colorbar()
#plt.savefig('datagraphs/'+name+'set2totxydist.png')
#plt.close()
#
#xdist=np.bincount(x5)
#ydist=np.bincount(y5)
#
#print(xdist)
#print(ydist)
#
#plt.figure()
#plt.hist(xdist,bins=32)
#plt.savefig('datagraphs/'+name+'set2totxdist.png')
#plt.close()
#
#plt.figure()
#plt.hist(ydist,bins=54)
#plt.savefig('datagraphs/'+name+'set2totydist.png')
#plt.close()
#





