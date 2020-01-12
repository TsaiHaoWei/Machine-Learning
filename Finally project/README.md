
  # 需求
  ## 1、功能需求	
利用Machine Learning 來學習如何回擊球
在遊戲速度達到20以前不會輸
減少計算的難度，在對方回擊後盡可能地計算落點位置並移動
## 2、環境需求
作業系統:WIN7以上版本
軟體版本:python3.6
最後需在B504教室實測
## 3、效能需求
在FPS 60 以下能正常運作

  # 分析
   ## 1、功能模組 
  訓練模型程式 :利用機器學習訓練出一個有效的模型
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/Hw3_%E6%9E%B6%E6%A7%8B%E5%9C%96.png) 
執行模型程式
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/Hw3_%E6%9E%B6%E6%A7%8B%E5%9C%96.png) 
     
 ## 2、遊戲分析
   ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/Hw3_%E6%9E%B6%E6%A7%8B%E5%9C%96.png) 
    紅色為1P，藍色為2P。
    1P的Y座標為420，2P的Y座標為80
    物件速度:
    球速:(7,7)
    平板移動速度:(5,0)
    初始位置:
    1P發球的球起始位置:(120,395)
    2P發球的球起始位置:(75,100)

     
 ## 3、遊戲參數
    ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/Hw3_%E6%9E%B6%E6%A7%8B%E5%9C%96.png) 
 ## 4、實現方法
   訓練方式:
        使用KNN(K-nearest neighbors algorithm)完成
        抓取相關特徵進行特徵學習

   訓練資料來源:
        使用Rule-base提供大量有效的樣本
  ## 5、KNN
   KNN演算法，全名叫K-nearest neighbors algorithm
KNN屬於機器學習中的監督式學習(Supervised learning)，但是在KNN其實並沒有做training的動作
在K近鄰分類算法中，對於預測的新樣本數據，將其與訓練樣本一一進行比較，找到最為相似的K個訓練樣本，並以這K個訓練樣本中出現最多的分類標籤作為最終新樣本數據的預測標籤。


 # 設計
  為了考量機器學習的樣本數，加入亂數初始球的座標位置，以及考量初始球移動的角度來增加，多樣性的樣本數。
  在rule base中，在回擊球後將托盤移動正中央，在球落下到一定高度時再去計算落下來的托盤位置。
## KNN訓練架構圖
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/Hw3_%E6%9E%B6%E6%A7%8B%E5%9C%96.png) 
## Rule_Base簡易流程
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/HW3_%E6%B5%81%E7%A8%8B.png)
## KNN簡易流程
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/HW3_Knn%E6%B5%81%E7%A8%8B.png)
## 球座標1000Frame
  ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/%E7%90%83%E5%BA%A7%E6%A8%991000Frame.JPG)
