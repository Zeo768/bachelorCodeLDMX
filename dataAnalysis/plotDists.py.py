#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:33:39 2020

@author: danmag
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.load('0-3GeVA160-180xvalues.npy')
y=np.load('0-3GeVA160-180yvalues.npy')
z=np.load('0-3GeVA160-180zvalues.npy')
#x=np.load('0-3GeVxvalues.npy')
#y=np.load('0-3GeVyvalues.npy')
#z=np.load('0-3GeVzvalues.npy')

#temp='Entries: '+str(nHits1)
plt.figure()
plt.title('X distribution, 0-3 GeV Angle: 160-180')
#plt.title('X distribution, 0-3 GeV no angle set')
plt.hist(x,bins=93,range=(-100,100))

plt.xlabel('x [mm]')
plt.ylabel('Counts')
#plt.legend()
plt.tight_layout()
plt.savefig('datagraphs/0-3GeVA160-180xdist.png',dpi=200)
#plt.savefig('datagraphs/0-3GeVxdist.png',dpi=200)
plt.close()

#temp='Entries: '+str(nHits1)
plt.figure()
plt.title('Y distribution, 0-3 GeV Angle: 160-180')
#plt.title('Y distribution, 0-3 GeV no angle set')
plt.hist(y,bins=95,range=(-120,120))

plt.xlabel('y [mm]')
plt.ylabel('Counts')
#plt.legend()
plt.tight_layout()
plt.savefig('datagraphs/0-3GeVA160-180ydist.png',dpi=200)
#plt.savefig('datagraphs/0-3GeVydist.png',dpi=200)
plt.close()

#temp='Entries: '+str(nHits1)
plt.figure()
plt.title('Z distribution, 0-3 GeV Angle: 160-180')
#plt.title('Z distribution, 0-3 GeV no angle set')

plt.hist(z,bins=110,range=(200,450))

plt.xlabel('z [mm]')
plt.ylabel('Counts')
#plt.legend()
plt.tight_layout()
plt.savefig('datagraphs/0-3GeVA160-180zdist.png',dpi=200)
#plt.savefig('datagraphs/0-3GeVzdist.png',dpi=200)
plt.close()