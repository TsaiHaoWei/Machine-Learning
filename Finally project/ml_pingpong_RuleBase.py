"""
The template of the script for the machine learning process in game pingpong
"""

# Import the necessary modules and classes
import games.pingpong.communication as comm
from games.pingpong.communication import (
    SceneInfo, GameInstruction, GameStatus, PlatformAction
)
def ml_loop(side: str):
    """
    The main loop for the machine learning process

    The `side` parameter can be used for switch the code for either of both sides,
    so you can write the code for both sides in the same script. Such as:
    ```python"""
    if side == "1P":
        ml_loop_for_1P()
    else:
        ml_loop_for_2P()
    """```

    @param side The side which this script is executed for. Either "1P" or "2P".
    """

def ml_loop_for_1P():

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here
    ball_position_history=[]
    ball_center_record = []
    # 2. Inform the game process that ml process is ready
    comm.ml_ready()
    vx =0
    ball_going_down = -1
    ball_going_x =-1
    oldvx=0
    # 3. Start an endless loop
    while True:
        # 3.1. Receive the scene information sent from the game process
        scene_info = comm.get_scene_info()
        ball_position_history.append(scene_info.ball)
        platform_center_x =scene_info.platform_1P[0]+20
        platform_center_y = scene_info.platform_1P[1]
        if (len(ball_position_history)) == 1 :
            ball_going_down = 0
        elif ball_position_history [-1][1] - ball_position_history [-2][1] > 0:
            ball_going_down = 1  #下降
        else:
            ball_going_down = 0
            vx = ball_center


        ball_center = scene_info.ball[0]#球X位點左上角+2.5為正中央
        ball_height = scene_info.ball[1]#球Y位點


        if ball_going_down ==1:
            if platform_center_y-ball_height>=310:
                oldvx=ball_center
                if ball_position_history[-1][0] - ball_position_history[-2][0]>0:
                    ball_going_x=1
                else :
                    ball_going_x=0 #左"""

        if scene_info.status == GameStatus.GAME_1P_WIN or \
            scene_info.status == GameStatus.GAME_2P_WIN:
            comm.ml_ready()
            continue


        if ball_going_down ==0:
            if platform_center_x < 100 :
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_x > 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            pass
        else:#開始計算落下點
            if ball_going_x ==1: #右
                if oldvx<90:
                    if platform_center_x <  round(abs(oldvx-90)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x > round(abs(oldvx-90)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass
                else:
                    if platform_center_x < round((oldvx-90)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x > round((oldvx-90)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass
            else:
                if oldvx>110:
                    if platform_center_x < round((-oldvx+310)/5.0,0)*5 :
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x > round((-oldvx+310)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass
                else:
                    if platform_center_x < round((oldvx+90)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x > round((oldvx+90)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass


def ml_loop_for_2P():
    ball_position_history = []
    ball_center_record = []
    # 2. Inform the game process that ml process is ready
    comm.ml_ready()
    vx = 0
    ball_going_down = -1
    ball_going_x =-1
    oldvx=0
    mx = 0
    # 3. Start an endless loop
    while True:
        # 3.1. Receive the scene information sent from the game process
        scene_info = comm.get_scene_info()
        ball_position_history.append(scene_info.ball)
        platform_center_x =scene_info.platform_2P[0]+20
        platform_center_y = scene_info.platform_2P[1]

        if (len(ball_position_history)) == 1 :
            ball_going_down = 0
        elif ball_position_history [-1][1] - ball_position_history [-2][1] > 0:
            ball_going_down = 1  #下降
        else:
            ball_going_down = 0
            if ball_height>=390:
                mx = ball_position_history[-1][0] - ball_position_history[-2][0]




          #400 球初始 100
          #球一步X，Y= 7 平台一步 = 5

        ball_center = scene_info.ball[0]#球X位點左上角+2.5為正中央
        ball_height = scene_info.ball[1]#球Y位點
        if ball_going_down ==0:
            if ball_height>=390:
                oldvx = ball_center
                if mx>0:
                    ball_going_x=1
                else :
                    ball_going_x=0 #左"""

        if scene_info.status == GameStatus.GAME_1P_WIN or \
            scene_info.status == GameStatus.GAME_2P_WIN:
            comm.ml_ready()
            continue

            #scene_info = comm.get_scene_info()

            # Do some stuff if needed
            # 3.2.1. Inform the game process that ml process is ready


            # Do some stuff if needed
            # 3.2.1. Inform the game process that ml process is ready
        if ball_going_down ==1:
            if platform_center_x < 100 :
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_x > 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            pass
        else:
            if ball_going_x ==1: #右
                if oldvx<80:
                    if platform_center_x < round((-oldvx+80)/5.0,0)*5 :
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x > round((-oldvx+80)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass
                else:
                    if platform_center_x < round((oldvx-80)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x > round((oldvx-80)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass
            else:
                if oldvx>120:
                    if platform_center_x < round((-oldvx+320)/5.0,0)*5 :
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x >round((-oldvx+320)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass
                else:
                    if platform_center_x < round((oldvx+80)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    elif platform_center_x > round((oldvx+80)/5.0,0)*5:
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    pass
