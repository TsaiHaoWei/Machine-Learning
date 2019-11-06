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
    test=-1
    test2=-1
    test_x=0
    test_y=0
    test2_x=0
    test2_y=0
    two_down =-1
    two_down1 =-1
    new_downHeight=0
    new_down=0
    new_downHeight1=0
    new_down1=0
    # 2. Inform the game process that ml process is ready before start the loop.
    comm.ml_ready()
    mx =0
    # 3. Start an endless loop.
    while True:
        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()
        ball_position_history.append(scene_info.ball)
        if len(ball_position_history) == 1:
            ball_going_down = 0
        elif ball_position_history [-1][1] - ball_position_history[-2][1] >0 :
            ball_going_down =1
            my = ball_position_history[-1][1] - ball_position_history[-2][1]
            mx = ball_position_history[-1][0] - ball_position_history[-2][0]
            #print(ball_going_down)
        platform_center_x = scene_info.platform[0]+20
        platform_center_y = scene_info.platform[1]

          #400 球初始 100
          #球一步X，Y= 7 平台一步 = 5

        ball_center = scene_info.ball[0]#球X位點左上角+2.5為正中央
        ball_height = scene_info.ball[1]#球Y位點
        #if scene_info.status == GameStatus.GAME_OVER or \
        if  scene_info.status == GameStatus.GAME_PASS:
            print("succcess")
            comm.ml_ready()
            continue
            #scene_info = comm.get_scene_info()

            # Do some stuff if needed
            # 3.2.1. Inform the game process that ml process is ready


            # Do some stuff if needed
            # 3.2.1. Inform the game process that ml process is ready

        if platform_center_y-ball_height>=125:
            vx = ball_center #紀錄 在100 x是多少
            one_mx = mx
            record_vx = 1
            test = -1
            test2 = -1
            if platform_center_x < 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            elif platform_center_x > 100:
                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
            pass
        else:  ##第一次回擊

            if platform_center_y-ball_height>=112:
                vx = ball_center #紀錄 在100 x是多少
                one_mx = mx

            if record_vx ==1:
                if ball_position_history[-1][1] - ball_position_history[-2][1] >0:
                    up = platform_center_x
                    print(one_mx)
                    print(vx)
                    if one_mx > 0 :
                        if vx<=88: ##在左邊往右
                            if platform_center_x < vx+112:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > vx+112:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                        else:
                            if mx>0:
                                test = 0
                                test_x = ball_center
                                test_y = platform_center_y-ball_height
                                if test_x>170:
                                    test = 1
                                    if platform_center_x < 200-abs(88-vx):
                                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                    elif platform_center_x > 200-abs(88-vx):
                                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                    pass
                                else:
                                    if platform_center_x < (200-abs(88-vx)+150)/2:
                                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                    elif platform_center_x > (200-abs(88-vx)+150)/2:
                                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                    pass
                            elif test ==0 :

                                if platform_center_x < test_x-test_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > test_x-test_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            elif one_mx == 5 or one_mx == 4:
                                if platform_center_x < vx-112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x >vx-112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            elif test != 1:
                                print("在112以上撞到反彈下")
                                print(test)
                                if platform_center_x < vx-112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > vx-112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            else:
                                print("HALO1")
                                print(test2_x-test2_y)
                                if platform_center_x < test_x-test_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > test_x-test_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                    elif one_mx < 0 :
                        if vx>=112:##在又邊往左
                            if platform_center_x < vx-112:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > vx-112:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                        else:
                            if mx<0:
                                print(test2)
                                print(platform_center_x)
                                test2 = 0
                                test2_x = ball_center
                                test2_y = platform_center_y-ball_height
                                if test2_x<30:
                                    test2 = 1
                                    if platform_center_x < abs(vx-112):
                                            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                    elif platform_center_x > abs(vx-112):
                                            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                    pass
                                else:
                                    if platform_center_x < (abs(vx-112)+70)/2:
                                            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                    elif platform_center_x > (abs(vx-112)+70)/2:
                                            comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                    pass
                            elif test2 == 0 :
                                print(test2_x+test2_y)
                                if platform_center_x < test2_x+test2_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > test2_x+test2_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            elif one_mx == -5 or one_mx == -4 or one_mx == -2:
                                print(vx+112)
                                if platform_center_x < vx+112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x >vx+112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            elif test2 != 1:
                                print("在112以上撞到反彈下")
                                print(test2)
                                if platform_center_x < vx+112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > vx+112:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            else:
                                print("HALO")
                                print(test2_x+test2_y)
                                if platform_center_x < test2_x+test2_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > test2_x+test2_y:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                else:
                    record_vx = 0

            else:
                if ball_position_history[-1][1] - ball_position_history[-2][1] >0:##第二次下降

                    if down_mx > 0:
                        print("down_mx又")
                        print(mx)
                        if mx>0 :
                            two_down=1
                            new_downHeight = platform_center_y-ball_height
                            newdown =ball_center
                            if newdown<190:
                                two_down=0
                                if platform_center_x <200-abs(down + down_height-200):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > 200-abs(down + down_height-200):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            else:
                                if platform_center_x <(330-abs(down + down_height-200))/2:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > (330-abs(down + down_height-200))/2:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                        elif two_down==1:
                            print(newdown)
                            print(new_downHeight)
                            if platform_center_x <abs(newdown - new_downHeight):
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > abs(newdown - new_downHeight):
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                        else:
                            if mx>0:
                                if platform_center_x <200-abs(200-(down+down_height)):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x >200-abs(200-(down+down_height)):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            else:
                                if platform_center_x <abs(down - down_height):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > abs(down - down_height):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                    else:

                        if mx<0:
                            two_down1=1
                            new_downHeight1 = platform_center_y-ball_height
                            newdown1 =ball_center
                            print(newdown1)
                            if newdown1>10:
                                two_down1=0
                                print(abs(down - down_height))
                                if platform_center_x <abs(down - down_height):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > abs(down - down_height):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            else:
                                if platform_center_x <(abs(down - down_height)+100)/2:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > (abs(down - down_height)+100)/2:
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                        elif two_down1 ==1:
                            if platform_center_x <abs(newdown1 + new_downHeight1):
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > abs(newdown1 + new_downHeight1):
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                        else:
                            if mx>0:
                                if platform_center_x <200-abs(200-(down+down_height)):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x >200-abs(200-(down+down_height)):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass
                            else:
                                if platform_center_x <abs(down - down_height):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                                elif platform_center_x > abs(down - down_height):
                                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                                pass


                else: #回擊後上去
                    print("回擊後上去")
                    print(up) #回擊後托盤X位置
                    print(platform_center_x)
                    down = ball_center

                    down_height = platform_center_y-ball_height
                    down_mx = ball_position_history[-1][0] - ball_position_history[-2][0]
                    newdown=ball_center
                    new_downHeight=platform_center_y-ball_height
                    newdown1=ball_center
                    new_downHeight1=platform_center_y-ball_height
                    if up > 160: #UP第一次回及時托盤X
                        if mx>0:
                            if platform_center_x <up -30:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > up-30:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                        else:
                            if platform_center_x < 70:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > 70:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                    elif up < 40 :
                        if mx<0:
                            if platform_center_x < up +30:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > up +30:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                        else:
                            if platform_center_x < 130:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > 130:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                    else:
                        if mx<0:
                            if platform_center_x < 70:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > 70:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass
                        elif mx>0:
                            if platform_center_x < 130:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                            elif platform_center_x > 130:
                                comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                            pass


        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.
