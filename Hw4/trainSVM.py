"""The template of the main script of the machine learning process
"""
import pickle
import numpy as np
import pygame
from os import listdir
from os.path import isfile, join

path = 'C:\\Users\\ASUS\\Desktop\\108-1\\Mechine_learning\\MLGame-master\\games\\arkanoid\\log'
Frame = []
Status = []
BallPosition = []
PlatformPosition = []
Brick = []
data_list=[]
n=0
files = listdir(path)    ## import os 取路徑底下檔名

for f in files:         ##將路徑底下的檔名與路徑結合
  allpath = join(path, f)
  if isfile(allpath):
    with open(allpath , "rb") as f1:
        data_list1 = pickle.load(f1)
        data_list.append(data_list1)
    n=n+1
N=n-1
for n in range(0 , N):
    for i in range(0,len(data_list[n])):
        BallPosition.append(data_list[n][i].ball)
        PlatformPosition.append(data_list[n][i].platform)
        Frame.append(data_list[n][i].frame)
        Status.append(data_list[n][i].status)
        Brick.append(data_list[n][i].bricks)
###############################################################################

PlatX = np.array(PlatformPosition) [:,0][:,np.newaxis]
PlatX_next = PlatX[1:,:]
instrust = (PlatX_next-PlatX[0:len(PlatX_next),0][:,np.newaxis])/5

PlatY = np.array(PlatformPosition) [:,1][:,np.newaxis]
PlatY_next = PlatY[1:,:]

Ballarray = np.array(BallPosition[:-1])

BallX_position = np.array(BallPosition)[:,0][:,np.newaxis]
BallX_position_next = BallX_position[1:,:]
Ball_Vx = BallX_position_next - BallX_position[0:len(BallX_position_next),0][:,np.newaxis]

BallY_position = np.array(BallPosition)[:,1][:,np.newaxis]
BallY_position_next = BallY_position[1:,:]
Ball_Vy = BallY_position_next - BallY_position[0:len(BallY_position_next),0][:,np.newaxis]

Ball_Plat_Y = PlatY_next-BallY_position_next

x = np.hstack((Ballarray,PlatX[0:-1,0][:,np.newaxis],Ball_Vx,Ball_Vy))
print(x)

y = instrust
#np.set_printoptions(threshold=np.inf)
#--------------------------- train & test data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 41)
#--------------------------- train model
"""from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svm = SVC(gamma='auto')

svm.fit(x_train,y_train)

yp_bef_scaler = svm.predict(x_test)
acc_arc_before_scaler = accuracy_score(yp_bef_scaler,y_test)
"""
from sklearn.svm import SVR

svr = SVR(gamma=0.001,C = 1,epsilon = 0.1,kernel = 'rbf')


svr.fit(x_train,y_train)
y_predict = svr.predict(x_test)

from sklearn.metrics import r2_score#R square

R2 = r2_score(y_test,y_predict)
print('R2 = ',R2)
print(len(Frame))




#--------------------------- save
filename = "C:\\Users\\ASUS\\Desktop\\108-1\\Mechine_learning\\MLGame-master\\games\\arkanoid\\Train\\svr_example1.sav"
pickle.dump(svr,open(filename,"wb"))
