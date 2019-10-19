# Machine-Learning
  # 需求
  1、Mechine_Learning過3關:能利用KNN過完三關
  
  2、效能FPS:將效能調到一定高度(>=100)
  
  3、機器學習樣本多樣化 
      (1)、球初始位置
      (2)、球速度調整
  # 分析
  1、input 
  
   球座標、磚塊座標、托盤座標
     
  2、output 
  
   托盤移動
     
  3、parameter 
  
   效能FPS
   
 # 設計
  為了考量機器學習的樣本數，加入亂數初始球的座標位置，以及考量初始球移動的角度來增加，多樣性的樣本數。
  在rule base中，在回擊球後將托盤移動正中央，在球落下到一定高度時再去計算落下來的托盤位置。

 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/Hw3_%E6%9E%B6%E6%A7%8B%E5%9C%96.png) 
 ![image](https://github.com/TsaiHaoWei/Machine-Learning/blob/master/Hw3/HW3_%E6%B5%81%E7%A8%8B.png)
 
