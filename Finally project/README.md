
  # 需求
  ## 1、功能需求	
利用Machine Learning 來學習如何回擊球 <br />
在遊戲速度達到20以前不會輸 <br />
減少計算的難度，在對方回擊後盡可能地計算落點位置並移動<br />
## 2、環境需求
作業系統:WIN7以上版本<br />
軟體版本:python3.6<br />
最後需在B504教室實測<br />
## 3、效能需求
在FPS 60 以下能正常運作<br />

  # 分析
   ## 1、功能模組 
  訓練模型程式 :利用機器學習訓練出一個有效的模型

 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Finally%20project/%E5%8A%9F%E8%83%BD%E6%A8%A1%E7%B5%84%E4%B8%80.png) 

執行模型程式

 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Finally%20project/%E5%8A%9F%E8%83%BD%E6%A8%A1%E7%B5%842.png) 
     
 ## 2、遊戲分析
   ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Finally%20project/%E9%81%8A%E6%88%B2%E5%88%86%E6%9E%901.png) 

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
   KNN演算法，全名叫K-nearest neighbors algorithm<br />
KNN屬於機器學習中的監督式學習(Supervised learning)，但是在KNN其實並沒有做training的動作
在K近鄰分類算法中，對於預測的新樣本數據，將其與訓練樣本一一進行比較，找到最為相似的K個訓練樣本，並以這K個訓練樣本中出現最多的分類標籤作為最終新樣本數據的預測標籤。


 # 設計

## break down
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Finally%20project/%E8%A8%AD%E8%A8%88BreakDown.png) 
## rule base流程
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Finally%20project/RuleBase%E6%B5%81%E7%A8%8B.png)
## rule base球落點計算
 2P擊球回來且球往右跑	
當球X座標>60，則最後落點X-60(彈兩次模式)
當球X座標<=60，則最後落點60-X(彈一次模式)

2P擊球回來且球往左跑	<br />
當球X<140，則最後落點X+60(兩次彈模式)<br />
當球X>=140，則球會因為變成一次彈模式，最後球落點分別為:<br />
140為200(+60)<br />
150為190(+40)<br />
160為180(+20)<br />
170為170(+0)<br />
180為160(-20)<br />
190為150(-40)<br />
200為兩次模式140(變相變成球往右邊模式)(-60)

## KNN
  ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Finally%20project/KNN%E6%9E%B6%E6%A7%8B.png)
