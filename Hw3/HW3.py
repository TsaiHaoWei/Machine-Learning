import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

sns.set_style("whitegrid")
sns.set_context("paper")
# 設置風格、尺度

import warnings
warnings.filterwarnings("ignore") 
# 不發出警告
# 1、stripplot()
# 按照不同類別對樣本數據進行分布散點圖繪制

tips = sns.load_dataset("tips")
print(tips.head())
# 加載數據

sns.stripplot(x="day",          # x → 設置分組統計字段
              y="total_bill",   # y → 數據分布統計字段
              # 這裏xy數據對調，將會使得散點圖橫向分布
              data=tips,        # data → 對應數據
              jitter = True,    # jitter → 當點數據重合較多時，用該參數做一些調整，也可以設置間距如：jitter = 0.1
              size = 5, edgecolor = "w",linewidth=1,marker = "o"  # 設置點的大小、描邊顏色或寬度、點樣式
              )