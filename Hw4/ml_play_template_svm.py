
"""The template of the main script of the machine learning process
"""

import games.arkanoid.communication as comm
from games.arkanoid.communication import ( \
    SceneInfo, GameInstruction, GameStatus, PlatformAction
)

def ml_loop():
    """The main loop of the machine learning process
    This loop is run in a separate process, and communicates with the game process.
    Note that the game process won't wait for the ml process to generate the
    GameInstruction. It is possible that the frame of the GameInstruction
    is behind of the current frame in the game process. Try to decrease the fps
    to avoid this situation.
    """

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here.
    import pickle
    import numpy as np
    filename="C:\\Users\\ASUS\\Desktop\\108-1\\Mechine_learning\\MLGame-master\\games\\arkanoid\\Train\\svr_example1.sav"
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
        platform_center_x = scene_info.platform[0] #platform length = 40

        if len(ball_position_history) > 1:
            vy = ball_position_history[-1][1] - ball_position_history[-2][1]
            vx = ball_position_history[-1][0] - ball_position_history[-2][0]

        inp_temp=np.array([scene_info.ball[0], scene_info.ball[1], platform_center_x,vx,vy])
        input=inp_temp[np.newaxis, :]
        #print(input)
        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.
        #if scene_info.status == GameStatus.GAME_OVER or \
        if   scene_info.status == GameStatus.GAME_PASS:
            # Do some stuff if needed
            #scene_info = comm.get_scene_info()
            # 3.2.1. Inform the game process that ml process is ready
            comm.ml_ready()
            continue
        platform_center_y = scene_info.platform[1]
        ball_height = scene_info.ball[1]#球Y位點
        # 3.3. Put the code here to handle the scene information
        if(len(ball_position_history) > 1):
            if platform_center_y-ball_height<=150:
                move=model.predict(input)
            else:
                move = 0
        else:
            move = 0

        # 3.4. Send the instruction for this frame to the game process
        #print(ball_destination)
        #print(platform_center_x)
        if move < 0 :
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)

        elif move > 0 :
            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
        else:
            if platform_center_x < 80:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_x > 80:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            pass
