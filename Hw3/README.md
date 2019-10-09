# Machine-Learning
  # 需求
  1、Mechine_Learning過3關
  
  2、效能FPS
  
  3、機器學習樣本多樣化 ex:球初始點
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

