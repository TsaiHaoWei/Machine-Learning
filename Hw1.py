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
    ball_position_history=[]
    ball_center_record = []
    # 2. Inform the game process that ml process is ready before start the loop.
    comm.ml_ready()

    # 3. Start an endless loop.
    while True:
        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()
        ball_position_history.append(scene_info.ball)
        platform_center_x =scene_info.platform[0]+20
        platform_center_y = scene_info.platform[1]
        ball_center = scene_info.ball[0]+2.5#球X位點左上角+2.5為正中央
        ball_height = scene_info.ball[1]#球Y位點
        if platform_center_y-ball_height>=200:
            vx = ball_center
            if platform_center_x < 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_x > 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            pass
        else:
            if  platform_center_x > abs(vx-200):
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            else:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
        if scene_info.status == GameStatus.GAME_OVER or \
            scene_info.status == GameStatus.GAME_PASS:
            # Do some stuff if needed

            # 3.2.1. Inform the game process that ml process is ready
            comm.ml_ready()
            continue
    
        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.


        # 3.3. Put the code here to handle the scene information

        # 3.4. Send the instruction for this frame to the game process
        #comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
