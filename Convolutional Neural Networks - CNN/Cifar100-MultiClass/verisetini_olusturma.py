# -*- coding: utf-8 -*-
"""
Cifar0 Verisetini Klasörlere Dagitma
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from keras.datasets import cifar100

# Cifar100 datasetini keras ın datasetlerinden yüklüyoruz.
(x_train, y_train), (x_test, y_test) = cifar100.load_data()

# Ana klasöre yüklediğimiz datasetlerin classlarını bir dataset klasörü oluşturulup içerisine train ve test klasörlerini oluşturuyoruz..
os.mkdir('dataset')
os.mkdir('dataset\\train')
os.mkdir('dataset\\test')

# 100 tane class için ayrı ayrı klasör oluşturuyoruz.
for i in range(100):
    path=os.path.join('dataset\\train',str(i))
    os.mkdir(path)
    path=os.path.join('dataset\\test',str(i))
    os.mkdir(path)

# Oluşturulan dataset klasörünün içerisindeki train ve test klasörlerinin herbirine gerekli classların image dosyalarını yüklüyoruz. 
import matplotlib.pyplot as plt

# train dosyası için gerekli classların image dosyalarını png olarak yüklüyoruz.
for i in range(50000):
    path='dataset/train/'+str(int(y_train[i]))+'/'+str(i)+'.png'  
    plt.imsave(path,x_train[i])

# test dosyası için gerekli classların image dosyalarını png olarak yüklüyoruz.    
for i in range(10000):
    path='dataset/test/'+str(int(y_test[i]))+'/'+str(i)+'.png'  
    plt.imsave(path,x_test[i])

    