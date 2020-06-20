# -*- coding: utf-8 -*-
"""圖片轉CSV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10p6yDFMX1J0LCYLDAsQN9uRWBadza1p2
"""

#製作訓練資料
import cv2,csv,os
from keras.preprocessing.image import ImageDataGenerator

def convert_img_to_csv(img_dir):
  with open('train.csv','w',newline='') as csvfile: #train.csv 為要儲存的檔案
    fieldnames = ["label"] #設置第一列元素 label
    fieldnames.extend(["pixel%d"%i for i in range(100*100)]) #每列以 pixel1 2 3 ....去跑 直到10000次
    writer = csv.writer(csvfile) #建立CSV檔寫入器
    writer.writerow(fieldnames) #寫入一列資料內容
    for i in range(3):
      print(i)
      #取得目錄路徑
      img_temp_dir = os.path.join(img_dir,str(i)) #資料夾 0:皮卡丘  1:快龍  2:阿伯蛇
      #取得目錄下所有的文件
      img_list = os.listdir(img_temp_dir)
      #print(len(img_list))
      #跑所有目錄下文件
      for img_name in img_list:
        #判斷文件是否為目錄,如果是就不處理
        if not os.path.isdir(img_name): #沒判斷會有出錯可能
          #圖片的路径
          img_path = os.path.join(img_temp_dir,img_name)
          #轉灰階
          img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
          #縮小圖片為100*100
          pic = cv2.resize(img, (100, 100), interpolation=cv2.INTER_CUBIC)
          #圖片名稱 label  0:皮卡丘  1:快龍  2:阿伯蛇
          row_data = [i]
          #圖片的像素
          row_data.extend(pic.flatten())
          #將圖片數據寫到csv文件中
          writer.writerow(row_data)
convert_img_to_csv("./TrainData") #圖檔路徑

#製作測試資料
import cv2,csv,os
from keras.preprocessing.image import ImageDataGenerator

def convert_img_to_csv2(img_dir):
  with open('test.csv','w',newline='') as csvfile:
    fieldnames = []
    fieldnames.extend(["pixel%d"%i for i in range(100*100)])
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)

    for i in range(3):
      #取得目錄路徑
      img_temp_dir = os.path.join(img_dir,str(i))
      #取得目錄下所有的文件
      img_list = os.listdir(img_temp_dir)
      #跑所有目錄下文件
      for img_name in img_list:
        #判斷文件是否為目錄,如果是就不處理
        if not os.path.isdir(img_name):
          #圖片的路径
          img_path = os.path.join(img_temp_dir,img_name)
          #轉灰階
          img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
          #縮小圖片為100*100
          pic = cv2.resize(img, (100, 100), interpolation=cv2.INTER_CUBIC)
          #圖片名稱 label
          row_data = []
          #圖片的像素
          row_data.extend(pic.flatten())
          #將圖片數據寫到csv文件中
          writer.writerow(row_data)
convert_img_to_csv2("./TestData") #若發生圖檔路徑錯誤 可能裡面含有非圖像檔 ex:gif...

import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print(len(train)) #總共有多少張圖片

#取得csv內 label那行資料
Y_train = train["label"]

#取得標籤內第一列
X_train = train.drop(labels = ["label"],axis = 1)

#繪製圖表
g = sns.countplot(Y_train)
Y_train.value_counts()

import pandas as pd
import numpy as np

X_train.isnull().any().describe()
#正規化
X_train = X_train / 255.0
X_train = X_train.values.reshape(-1,100,100,1)
#原本矩陣直的 然後把它變成矩陣形狀 共3個寶可夢
Y_train = to_categorical(Y_train,num_classes = 3) 

random_seed = 1 #種子碼 隨便數字

#train_test_split將會自動把資料分類為 x_train, x_test, y_train, y_test 這四種
#測試資料佔的比例暫訂為20%, 因此test_size = 0.2
X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size = 0.2, random_state=random_seed)
print(len(X_train))
print(len(X_test))
print(len(Y_train))
print(len(Y_test))
plt.imshow(X_train[106][:,:,0]) #隨便抓一張看結果



