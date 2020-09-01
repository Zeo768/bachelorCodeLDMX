#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:38:47 2020

@author: danmag
"""



import numpy as np
import tensorflow as tf
import time
import argparse
#import seaborn as sns
from tensorflow import keras
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Conv3D, MaxPooling3D, Dense, Flatten,Dropout, Input, Activation, BatchNormalization
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

#import pandas as pd

#from sklearn.metrics import *


def main(args):
    start=time.time()
    print ("Executing main()")
    model = Sequential()
    name=args.file[2]
    Array=np.load(args.file[0])
    Classifier=np.load(args.file[1])
    #classifier4=np.zeros(1000)
    #classifier8=np.zeros(1000)
    #classifier48=np.concatenate((classifier4,classifier8))
    
    nevents,x,y,z=Array.shape
    print(nevents,x,y,z)
    #dataarray=np.concatenate((array48,classifier48),axis=1)
    #dataarray=[]
    #t=nevents/nclasses
    start=time.time()
    #np.random.shuffle(Array)
    end=time.time()
    print(end-start)
    #array_max=Array.max(axis=(1,2,3),keepdims=True)
    #Array=Array/array_max
    
    xtest,xtrain=np.split(Array,[int(nevents/8)])
    ytest,ytrain=np.split(Classifier,[int(nevents/8)])
    #print(len(xtrain))
    #print(xtrain.shape)
    xtrain=xtrain.reshape(len(xtrain),x,y,z,1)
    xtest=xtest.reshape(len(xtest),x,y,z,1)
    input_shape1=(x,y,z,1)
    
#    model.add(Conv3D(30,kernel_size=(8,8,8),padding='same',input_shape=input_shape1))
#    #model.add(BatchNormalization())
#    model.add(Activation('relu'))
#    model.add(MaxPooling3D(pool_size=(4,4,4)))
#    model.add(Conv3D(32,kernel_size=(6,6,6),padding='same'))
#    #model.add(BatchNormalization())
#    model.add(Activation('relu'))
#    model.add(MaxPooling3D(pool_size=(2,2,2)))
    
    D=0.04
    NN=512
    model.add(Flatten(input_shape=input_shape1))
    model.add(Dropout(D))
    model.add(Dense(NN,activation='relu'))
    model.add(Dropout(D))
    model.add(Dense(NN,activation='relu'))
    model.add(Dropout(D))
    model.add(Dense(NN,activation='relu'))
    model.add(Dropout(D))
    model.add(Dense(NN,activation='relu'))
    model.add(Dropout(D))
    model.add(Dense(NN,activation='relu'))
    model.add(Dropout(D))
#    model.add(Dense(NN,activation='relu'))
#    model.add(Dropout(D))
    model.add(Dense(1,activation='linear'))
    
    opt=Adam(lr=0.00001)
    
    model.compile(loss='mean_squared_error',optimizer=opt,metrics=['mse'])
    model.summary()
    mc=ModelCheckpoint('models/model'+name+'.h5', monitor='val_loss', verbose=1, save_best_only=True, mode='min')
    estimator=model.fit(xtrain,ytrain,validation_data=(xtest,ytest)
                        ,epochs=10,batch_size=128,verbose=1,callbacks=[mc])
    

#    #print(estimator.history.keys())
    #lossplot
    plt.plot(estimator.history['loss'])
    plt.plot(estimator.history['val_loss'])
    plt.title("Model training")
    plt.ylabel("MSE")
    plt.xlabel("epoch")
    plt.legend(['train','test'],loc=0)
    plt.savefig('graphs/lossgraph'+name+'.png')
#    
#    #Scatterplot
    ytrainpred=model.predict(xtrain)
    ytestpred=model.predict(xtest)
    
    plt.figure()
    plt.plot(ytrainpred[:],ytrain[:],'g.',label='Prediction vs True (Training)')
    x=np.linspace(500,3000,100)
    plt.plot(x,x,label='linear')
    plt.xlabel('Prediction')
    plt.ylabel('True')
    plt.savefig('graphs/trainscatter'+name+'.png')
    
    plt.figure()
    plt.plot(ytestpred[:],ytest[:],'g.',label='Prediction vs True (Test)')
    x=np.linspace(500,3000,100)
    plt.plot(x,x,label='linear')
    plt.xlabel('Prediction')
    plt.ylabel('True')
    plt.savefig('graphs/testscatter'+name+'.png')
    
    
    
#    y_pred=model.predict_classes(xtest)
#    con_mat = tf.math.confusion_matrix(labels=ytest, predictions=y_pred).numpy()
#    
#    
#    con_mat_norm = np.around(con_mat.astype('float') / con_mat.sum(axis=1)[:, np.newaxis], decimals=2)
#    
#    classes=[4,8,12,16]
#    
#    con_mat_df = pd.DataFrame(con_mat_norm,
#                     index = classes, 
#                     columns = classes)
#    
#    figure = plt.figure(figsize=(4, 4))
#    #sns.heatmap(con_mat_df, annot=True,cmap=plt.cm.Blues)
#    #plt.tight_layout()
#    plt.plot(con_mat_df)
#    plt.ylabel('True label')
#    plt.xlabel('Predicted label')
#    plt.savefig('Confusionmatrix.png')
    
    print ("Completed main()")
    end=time.time()
    print(end-start)
    



if __name__ == "__main__":
    used_setup_path='/home/lene/LDMX/simulation/sw/'
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