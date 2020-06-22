二下師徒制
----------------------------------------------------------
CNNtest3.py
1)將從Image_to_csv製作出來的train.csv與test.csv上傳至colab上

2)將此程式碼copy到colab上執行即可訓練神經網路並進行辨識
----------------------------------------------------------
Image_to_csv
1)先到colab新增兩個父資料夾(Train_Data與Test_Data)

2)在這兩個父資料夾,各別新增0~N個子資料夾(請注意,資料夾名稱務必從0開始至N,要辨識幾種類型圖片N可自行設定)

3)把要製作的圖片分成Train(每種至少有1000張)與Test(每種至少有200張)

4)依照不同種類,分別丟入Train_Data與Test_Data的0~N子資料夾
  (請注意,這兩者必須互相對應 ex:Train_Data/0為皮卡丘 則Test_Data/0也要是皮卡丘的圖片檔)

5)修改code第20 56 104行的'3'改為自行設定的'N'

6)新增兩個csv檔案至colab上(train.csv與test.csv)

7)將此程式碼copy到colab上執行即可至做train.csv與test.csv