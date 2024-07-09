#-*-coding:utf-8 -*-
import pygame
import random
from pygame import *

WIDTH=512 #map
HEIGHT=768 #map
W=86 #jet
H=150 #jet
def pengzhuang(x1,y1,w1,h1,x2,y2,w2,h2):
    if x2>x1:
        if (x2-x1)<w1 and abs(y1-y2)<h1:return True
        else :return False
    else:
        if (x1-x2)<w2 and abs(y1-y2)<h1:return True
        else:return False
pygame.init()#pygame 首先需要初始化

print(pygame.display.list_modes())
if pygame.display.mode_ok((512,768))!=0:
    screen=pygame.display.set_mode((512,768))
    print("分辨率已设为：",pygame.display.get_surface())
else:
    print("显示失败")
    exit(1)

pygame.display.set_caption("超级雷电")#更改窗口标题为“超级雷电”
rpt=True
while rpt:
    # ZITI=pygame.font.get_fonts()
    # print("支持的字体有：")
    # for i in ZITI:
    #     print(i)
    myfont1=pygame.font.SysFont('方正楷体gbk',60)
    myfont2=pygame.font.SysFont('方正楷体gbk',25)
    myfont3=pygame.font.SysFont('方正黑体gbk',30)
    color1=0,0,0#黑色
    color2=255,0,0#红色
    color3=0,255,0
    textimage_bg=myfont1.render('超级雷电',True,color1)
    textimage=myfont1.render('超级雷电',True,color2)
    textimage_GameIntroduction=myfont2.render("游戏说明：WASD控制方向,空格键发射子弹",True,color1)

    win_flag=False
    #第一个页面
    ctn = True
    bg0=pygame.image.load("start_bg0.jpg")
    plane=pygame.image.load("jet.png")
    start_button=pygame.image.load("start.png")
    while ctn:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:#如果按下一个键
                key_pressed=pygame.key.get_pressed()#用pygame内置函数获取这个键的键值
                if key_pressed[K_SPACE] or key_pressed[K_ESCAPE]:
                    ctn=False#如果按下esc或者space则退出
            elif event.type==pygame.QUIT:
              #  pygame.QUIT()#点击叉号退出
                exit(0)
              # 检测鼠标点击事件,点击“开始游戏”进入下一个画面
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # print("鼠标左键点击位置", )
                    mouse_x, mouse_y = event.pos
                    if 200<=mouse_x<=305 and 423<=mouse_y<=467:
                        ctn=False
        screen.blit(bg0, (0, 0))
        screen.blit(plane,((WIDTH-W)/2,500))
        screen.blit(textimage_bg,(145,155))
        screen.blit(start_button,(185,400))
        screen.blit(textimage, (140,150))
        screen.blit(textimage_GameIntroduction,(20,700))

        pygame.display.update()

        # 设置步长、生命、得分
        STEP = 16
        lifenumber = 3
        scores = 0
    for i in range(1,3):
        #第二个页面
        ctn=True
        #设置背景图
        bg1=pygame.image.load("map"+str(i)+".jpg")
        bg2 = pygame.image.load('map'+ str(i) +'.jpg')
        screen_height = 768
        screen_width = 512
        bg1_y =0
        bg2_y = -screen_height
        #装载己方飞机
        plane=pygame.image.load("jet.png")
        x=(WIDTH-W)/2
        y=HEIGHT-H
        fire=pygame.image.load("wsparticle_smoke03.png")
        is_fire_on=False
        fire_W=64
        fire_H=64
        fire_y = y + H
        fire_x = x + W / 2 - fire_W / 2
        #装载敌机
        enemy=pygame.image.load("alien_1.png")
        enemy_W=128
        enemy_H=128
        enemy_x=random.randint(0,WIDTH-enemy_W)#随机生成敌机的初始位置
        enemy_y=0
        #给敌机设置定时器
        enemy_event=pygame.USEREVENT
        pygame.time.set_timer(enemy_event,10)

        #装载敌机子弹
        bullet=pygame.image.load("alien_bullet.png")
        bullet_W=37
        bullet_H=37
        bullet_y=enemy_y+enemy_H/2
        bullet_x = enemy_x + enemy_W / 2 - bullet_W / 2
        #给敌机子弹设置定时器
        bullet_event=pygame.USEREVENT+1
        pygame.time.set_timer(bullet_event,5)

        #装载飞弹
        feidan=pygame.image.load("feidan.png").convert_alpha()
        feidan_W=21
        feidan_H=59
        feidan_y=1000
        feidan_x=1000
        # 控制飞弹是否发射
        is_feidan_shoot = False
        #给飞弹设置定时器
        feidan_event=pygame.USEREVENT+2
        pygame.time.set_timer(feidan_event,1)

        while ctn:
            textimage_Scoring_Panel = myfont3.render("生命：" + str(lifenumber) + "  得分：" + str(scores), True, color3)

            for event in pygame.event.get():
                #按键事件
                if event.type==pygame.KEYDOWN:
                    key_pressed=pygame.key.get_pressed()#获取这个键的键值
                    if key_pressed[K_ESCAPE]:
                        ctn=False#按下esc退出

                    #控制飞机移动
                    elif key_pressed[K_d] or key_pressed[K_RIGHT]:
                        if x+STEP<WIDTH-W : x+=STEP
                        else:x=WIDTH-W
                        is_fire_on = False
                    elif key_pressed[K_a] or key_pressed[K_LEFT]:
                        if x-STEP>0 : x-=STEP
                        else : x=0
                        is_fire_on = False
                    elif key_pressed[K_s] or key_pressed[K_DOWN]:
                        if y+STEP<HEIGHT-H: y+=STEP
                        else : y=HEIGHT-H
                        is_fire_on = False
                    elif key_pressed[K_w] or key_pressed[K_UP]:
                        if  y-STEP>0:
                            y-=STEP
                            fire_y = y + H-10
                            fire_x = x + W / 2 - fire_W / 2
                        else :
                            y=0
                            fire_y = y + H-10
                            fire_x = x + W / 2 - fire_W / 2
                        if not is_fire_on:
                            is_fire_on=True
                            fire_y=y+H-10
                            fire_x=x+W/2-fire_W/2

                    #控制飞弹发射
                    elif key_pressed[K_SPACE]:
                        if not is_feidan_shoot:
                            is_feidan_shoot = True  # 当按下空格键时，准备发射飞弹
                            feidan_y = y + H / 2   # 设置飞弹位置
                            feidan_x = x + W / 2 - feidan_W / 2
                # 鼠标事件
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pressed=pygame.mouse.get_pressed()    #获取鼠标活动
                    if mouse_pressed==(1,0,0):  #如果鼠标左击
                        mouse_x,mouse_y=pygame.mouse.get_pos()  #获取鼠标左击的坐标
                        #通过判断鼠标左击的位置控制飞机的移动
                        if mouse_x<x:
                            if x>STEP:x-=STEP
                            else:x=0
                            is_fire_on = False
                        elif mouse_x > x + W:
                            if x + STEP > WIDTH:x = WIDTH - W
                            else:x += STEP
                            is_fire_on = False
                        if mouse_y<y:
                            if y>STEP:
                                y-=STEP
                                fire_y = y + H - 10
                                fire_x = x + W / 2 - fire_W / 2
                            else:
                                y = 0
                                fire_y = y + H - 10
                                fire_x = x + W / 2 - fire_W / 2
                            if not is_fire_on:
                                is_fire_on = True
                                fire_y = y + H - 10
                                fire_x = x + W / 2 - fire_W / 2
                        elif mouse_y > y + H:
                            if y+STEP>HEIGHT: y =HEIGHT-H
                            else:y +=STEP
                            is_fire_on = False
                #飞弹事件
                elif event.type==feidan_event:
                    if is_feidan_shoot:
                        feidan_y-=1
                        if feidan_y+feidan_H<0:
                            is_feidan_shoot=False
                #敌机事件
                elif event.type==enemy_event:
                    if enemy_y>HEIGHT:#敌机飞出屏幕后刷新
                        enemy = pygame.image.load("alien_" + str(random.randint(1, 5)) + ".png")#随机生成敌机
                        enemy_x=random.randint(0, WIDTH - enemy_W)
                        enemy_y=-enemy_H
                        bullet_y = enemy_y + enemy_H / 2  # 子弹也要刷新
                        bullet_x = enemy_x + enemy_W / 2 - bullet_W / 2
                    else:
                        enemy_y += 1
                # 敌机子弹事件
                elif event.type==bullet_event:
                    bullet_y+=1
                    if bullet_y==HEIGHT:
                        bullet_y=enemy_y+enemy_H/2
                        bullet_x = enemy_x + enemy_W / 2 - bullet_W / 2

                elif event.type==pygame.QUIT:
                    exit(0)
            # 滚动屏幕
            bg1_y += 0.1
            bg2_y += 0.1
            if bg1_y >= screen_height:
                bg1_y = -screen_height
            if bg2_y >= screen_height:
                bg2_y = -screen_height
            screen.blit(bg1, (0, bg1_y))
            screen.blit(bg2, (0, bg2_y))

            if is_feidan_shoot:
                screen.blit(feidan,(feidan_x,feidan_y))
            if is_fire_on:
                screen.blit(fire,(fire_x,fire_y))
            screen.blit(plane,(x,y))#x，y的值随时刷新
            screen.blit(bullet,(bullet_x,bullet_y))
            screen.blit(enemy, (enemy_x, enemy_y))
            screen.blit(textimage_Scoring_Panel,(0,0))
            pygame.display.update()

            #敌机子弹击中我方飞机事件
            if pengzhuang(bullet_x,bullet_y,bullet_W,bullet_H,x,y,W,H):
                bullet_y = enemy_y + enemy_H / 2
                bullet_x = enemy_x + enemy_W / 2 - bullet_W / 2
                lifenumber-=1
            #敌我飞机碰撞事件
            if pengzhuang(enemy_x,enemy_y,enemy_W,enemy_H,x,y,W,H):
                enemy = pygame.image.load("alien_" + str(random.randint(1, 5)) + ".png")  # 随机生成敌机
                enemy_x = random.randint(0, WIDTH - enemy_W)
                enemy_y = -enemy_H
                lifenumber-=1
            #飞弹击中敌机子弹事件
            if pengzhuang(bullet_x,bullet_y,bullet_W,bullet_H,feidan_x,feidan_y,feidan_W,feidan_H):
                bullet_y = enemy_y + enemy_H / 2
                bullet_x = enemy_x + enemy_W / 2 - bullet_W / 2
                is_feidan_shoot = False
                feidan_x=1000

            #飞弹击中敌机事件
            if pengzhuang(enemy_x,enemy_y,enemy_W,enemy_H,feidan_x,feidan_y,feidan_W,feidan_H):
                enemy = pygame.image.load("alien_" + str(random.randint(1, 5)) + ".png")  # 随机生成敌机
                enemy_x = random.randint(0, WIDTH - enemy_W)
                enemy_y = -enemy_H
                is_feidan_shoot=False
                feidan_x=1000
                scores+=1000
            #死亡事件
            if lifenumber<=0:
                break
            #进入下一关
            if scores>=5000*i:
                ctn=False
        #第三个页面(boss战)
        bullet_x=1000
        ctn = True
        bg1 = pygame.image.load("map"+str(i)+".jpg")
        bg2 = pygame.image.load('map'+str(i)+'.jpg')
        # 装载己方飞机
        plane = pygame.image.load("jet.png")
        x = (WIDTH - W) / 2
        y = HEIGHT - H
        # 装载Boss
        boss = pygame.image.load("boss_"+str(i)+".png").convert_alpha()
        boss_W = 270
        boss_H = 175
        bosslife = 500 # 设置Boss血量
        boss_x = (WIDTH - boss_W) / 2
        boss_y = -boss_H

        # 装载Boss子弹
        boss_bullet = pygame.image.load("alien_bullet.png").convert_alpha()
        boss_bullet_W = 37
        boss_bullet_H =37
        boss_bullet_x = boss_x + boss_W / 2 - boss_bullet_W / 2
        boss_bullet_y = boss_y + boss_H

        # Boss移动定时器
        boss_event = pygame.USEREVENT + 3
        pygame.time.set_timer(boss_event, 10)

        # Boss子弹定时器
        boss_bullet_event = pygame.USEREVENT + 4
        pygame.time.set_timer(boss_bullet_event, 3)

        while ctn:
            textimage_Scoring_Panel = myfont3.render("生命：" + str(lifenumber) + "  BOSS剩余血量" + str(bosslife), True, color3)
            for event in pygame.event.get():
                # 按键事件
                if event.type == pygame.KEYDOWN:
                    key_pressed = pygame.key.get_pressed()  # 获取这个键的键值
                    if key_pressed[K_ESCAPE]:
                        ctn = False  # 按下esc退出
                        # 控制飞机移动
                    elif key_pressed[K_d] or key_pressed[K_RIGHT]:
                        if x + STEP < WIDTH - W:
                            x += STEP
                        else:
                            x = WIDTH - W
                        is_fire_on = False
                    elif key_pressed[K_a] or key_pressed[K_LEFT]:
                        if x - STEP > 0:
                            x -= STEP
                        else:
                            x = 0
                        is_fire_on = False
                    elif key_pressed[K_s] or key_pressed[K_DOWN]:
                        if y + STEP < HEIGHT - H:
                            y += STEP
                        else:
                            y = HEIGHT - H
                        is_fire_on = False
                    elif key_pressed[K_w] or key_pressed[K_UP]:
                        if y - STEP > 0:
                            y -= STEP
                            fire_y = y + H - 10
                            fire_x = x + W / 2 - fire_W / 2
                        else:
                            y = 0
                            fire_y = y + H - 10
                            fire_x = x + W / 2 - fire_W / 2
                        if not is_fire_on:
                            is_fire_on = True
                            fire_y = y + H - 10
                            fire_x = x + W / 2 - fire_W / 2
                    # 控制飞弹发射
                    elif key_pressed[K_SPACE]:
                        if not is_feidan_shoot:
                            is_feidan_shoot = True  # 当按下空格键时，准备发射飞弹
                            feidan_y = y + H / 2  # 设置飞弹位置
                            feidan_x = x + W / 2 - feidan_W / 2
                # 鼠标事件
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pressed = pygame.mouse.get_pressed()  # 获取鼠标活动
                    if mouse_pressed == (1, 0, 0):  # 如果鼠标左击
                        mouse_x, mouse_y = pygame.mouse.get_pos()  # 获取鼠标左击的坐标
                        # 通过判断鼠标左击的位置控制飞机的移动
                        if mouse_x < x:
                            if x > STEP:
                                x -= STEP
                            else:
                                x = 0
                            is_fire_on = False
                        elif mouse_x > x + W:
                            if x + STEP > WIDTH:
                                x = WIDTH - W
                            else:
                                x += STEP
                            is_fire_on = False
                        if mouse_y < y:
                            if y > STEP:
                                y -= STEP
                                fire_y = y + H - 10
                                fire_x = x + W / 2 - fire_W / 2
                            else:
                                y = 0
                                fire_y = y + H - 10
                                fire_x = x + W / 2 - fire_W / 2
                            if not is_fire_on:
                                is_fire_on = True
                                fire_y = y + H - 10
                                fire_x = x + W / 2 - fire_W / 2
                        elif mouse_y > y + H:
                            if y + STEP > HEIGHT:
                                y = HEIGHT - H
                            else:
                                y += STEP
                            is_fire_on = False
                # 飞弹事件
                elif event.type == feidan_event:
                    if is_feidan_shoot:
                        feidan_y -= 1
                        if feidan_y + feidan_H < 0:
                            is_feidan_shoot = False
                        # Boss事件
                elif event.type == boss_event:
                    if boss_y < 100:
                        boss_y += 1

                    # Boss子弹事件
                elif event.type == boss_bullet_event:
                    boss_bullet_y += 1  # Boss子弹的移动速度
                    if boss_bullet_y > HEIGHT:
                        boss_bullet_y = boss_y + boss_H
                        boss_bullet_x = boss_x + boss_W / 2 - boss_bullet_W / 2

                elif event.type == pygame.QUIT:
                    exit(0)
            # 滚动屏幕
            bg1_y += 0.1
            bg2_y += 0.1
            if bg1_y >= screen_height:
                bg1_y = -screen_height
            if bg2_y >= screen_height:
                bg2_y = -screen_height

            screen.blit(bg1, (0, bg1_y))
            screen.blit(bg2, (0, bg2_y))
            if is_feidan_shoot:
                screen.blit(feidan,(feidan_x,feidan_y))
            if is_fire_on:
                screen.blit(fire, (fire_x, fire_y))
            screen.blit(plane,(x,y))#x，y的值随时刷新
            screen.blit(boss_bullet,(boss_bullet_x,boss_bullet_y))
            screen.blit(boss, (boss_x, boss_y))
            screen.blit(textimage_Scoring_Panel,(0,0))
            pygame.display.update()

            # boss子弹击中我方飞机事件
            if pengzhuang(boss_bullet_x, boss_bullet_y, boss_bullet_W, boss_bullet_H, x, y, W, H):
                boss_bullet_x = boss_x + boss_W / 2 - boss_bullet_W / 2
                boss_bullet_y = boss_y + boss_H
                lifenumber -= 1

            # 检测碰撞，玩家飞弹与Boss碰撞
            if pengzhuang(feidan_x, feidan_y, feidan_W, feidan_H, boss_x, boss_y, boss_W, boss_H):
                scores += 50
                bosslife -= 100
                is_feidan_shoot = False
                feidan_x = 1000
                if bosslife <= 0:
                    # 进入下一个界面
                    win_flag=True
                    ctn = False  # 停止当前界面
            # 飞弹击中敌机子弹事件
            if pengzhuang(boss_bullet_x, boss_bullet_y, boss_bullet_W, boss_bullet_H, feidan_x, feidan_y, feidan_W, feidan_H):
                boss_bullet_x = boss_x + boss_W / 2 - boss_bullet_W / 2
                boss_bullet_y = boss_y + boss_H
                is_feidan_shoot = False
                feidan_x = 1000
            # 死亡事件
            if lifenumber <= 0:
                ctn = False
    #第四个页面
    ctn=True
    bg0=pygame.image.load("map1.jpg")
    restart_button=pygame.image.load("restart.png")
    win_image=pygame.image.load("success.png")
    color1=0,0,0#黑色
    color2=0,0,255#蓝色
    color3=255,255,0#黄色
    textimage_bg=myfont1.render('GAME OVER!',True,color1)
    textimage=myfont1.render('GAME OVER!',True,color2)
    wintext_bg = myfont1.render('YOU WIN!', True, color1)
    wintext = myfont1.render('YOU WIN!', True, color2)
    textimage_GameIntroduction1=myfont3.render("按r重新开始",True,color3)
    textimage_GameIntroduction2=myfont3.render("按q退出游戏",True,color3)
    while ctn:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:#如果按下一个键
                key_pressed=pygame.key.get_pressed()#用pygame内置函数获取这个键的键值
                if key_pressed[K_r]:
                    ctn=False#按下r重玩
                if key_pressed[K_q]:
                    ctn = False  # 按下q退出
                    rpt=False
            elif event.type==pygame.QUIT:
              #  pygame.QUIT()#点击叉号退出
                exit(0)
              # 检测鼠标点击事件,点击“重玩”即可重玩
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if 200<=mouse_x<=297 and 500<=mouse_y<=597:
                        ctn=False
        screen.blit(bg0, (0, 0))
        screen.blit(restart_button,(200,500))
        if win_flag:
            screen.blit(win_image,(180,300))
            screen.blit(wintext_bg, (125, 155))
            screen.blit(wintext, (120, 150))
        else:
            screen.blit(textimage_bg,(85,155))
            screen.blit(textimage, (80,150))
        screen.blit(textimage_GameIntroduction1,(190,700))
        screen.blit(textimage_GameIntroduction2, (190, 730))
        pygame.display.update()
pygame.quit()
exit(0)

