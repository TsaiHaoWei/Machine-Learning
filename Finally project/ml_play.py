
"""The template of the main script of the machine learning process
"""

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
    # 1. Put the initialization code here.
    import pickle
    import numpy as np
    filename="C:\\Users\\su021\\OneDrive\\桌面\\sav\\svr_1P.sav"
    model = pickle.load(open(filename, 'rb'))
    #print(model)
    ball_position_history=[]
    ball_center_record = []
    # 2. Inform the game process that ml process is ready
    comm.ml_ready()
    vx =0
    vy =0
    ball_going_down = -1
    ball_going_x =-1
    oldvx=0


    # 3. Start an endless loop.
    while True:

        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()
        ball_position_history.append(scene_info.ball)
        platform_center_x = scene_info.platform_1P[0] #platform length = 40

        if len(ball_position_history) > 1:
            vy = ball_position_history[-1][1] - ball_position_history[-2][1]
            vx = ball_position_history[-1][0] - ball_position_history[-2][0]

        inp_temp=np.array([scene_info.ball[0], scene_info.ball[1], platform_center_x,vx,vy])
        input=inp_temp[np.newaxis, :]

        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.

        if scene_info.status == GameStatus.GAME_1P_WIN or \
            scene_info.status == GameStatus.GAME_2P_WIN:
            comm.ml_ready()
            continue

        # 3.3. Put the code here to handle the scene information
        if(len(ball_position_history) > 1):
            move=model.predict(input)
            #print(move)

        else:
            move = 0

        # 3.4. Send the instruction for this frame to the game process
        #print(ball_destination)
        #print(platform_center_x)
        if move < 0 :
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
        elif move > 0 :
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)

def ml_loop_for_2P():

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here.
    import pickle
    import numpy as np
    filename="C:\\Users\\su021\\OneDrive\\桌面\\sav\\svr_2P.sav"
    model = pickle.load(open(filename, 'rb'))
    #print(model)
    ball_position_history=[]
    vx = 0
    vy = 0
    ball_destination = 0
    ball_going_down = 0
    # 2. Inform the game process that ml process is ready before start the loop.
    comm.ml_ready()

    # 3. Start an endless loop.
    while True:
        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()
        ball_position_history.append(scene_info.ball)
        platform_center_x = scene_info.platform_2P[0]#platform length = 40

        if len(ball_position_history) > 1:
            vy = ball_position_history[-1][1] - ball_position_history[-2][1]
            vx = ball_position_history[-1][0] - ball_position_history[-2][0]

        inp_temp=np.array([scene_info.ball[0], scene_info.ball[1], platform_center_x,vx,vy])
        input=inp_temp[np.newaxis, :]
        #print(input)
        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.
        #if scene_info.status == GameStatus.GAME_OVER or \
        if scene_info.status == GameStatus.GAME_1P_WIN or \
            scene_info.status == GameStatus.GAME_2P_WIN:
            comm.ml_ready()
            continue

        # 3.3. Put the code here to handle the scene information
        if(len(ball_position_history) > 1):
            move=model.predict(input)
        else:
            move = 0

        # 3.4. Send the instruction for this frame to the game process
        #print(ball_destination)
        #print(platform_center_x)
        if move < 0 :
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)

        elif move > 0 :
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
