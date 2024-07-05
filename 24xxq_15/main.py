#-*-coding:utf-8 -*-
import pygame
import random
from pygame import *

WIDTH=512 #map
HEIGHT=768 #map
W=86 #jet
H=150 #jet

pygame.init()#pygame 首先需要初始化
ctn=True
print(pygame.display.list_modes())
if pygame.display.mode_ok((512,768))!=0:
    screen=pygame.display.set_mode((512,768))
    print("分辨率已设为：",pygame.display.get_surface())
else:
    print("显示失败")
    exit(1)

pygame.display.set_caption("超级雷电")#更改窗口标题为“超级雷电”
# ZITI=pygame.font.get_fonts()
# print("支持的字体有：")
# for i in ZITI:
#     print(i)

myfont1=pygame.font.SysFont('方正楷体gbk',60)
myfont2=pygame.font.SysFont('方正楷体gbk',25)
color1=0,0,0#黑色
color2=255,0,0#红色
textimage_bg=myfont1.render('超级雷电',True,color1)
textimage=myfont1.render('超级雷电',True,color2)
textimage_GameIntroduction=myfont2.render("游戏说明：WASD控制方向,空格键发射子弹",True,color1)

#第一个页面
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

#第二个页面
ctn=True
#设置步长
STEP=16
bg0=pygame.image.load("map1.jpg")
#装载己方飞机
plane=pygame.image.load("jet.png")
x=(WIDTH-W)/2
y=HEIGHT-H
#装载敌机
enemy=pygame.image.load("alien_1.png")
enemy_W=128
enemy_H=128
enemy_x=random.randint(0,WIDTH-enemy_W)#随机生成敌机的初始位置
enemy_y=-enemy_H
#给敌机设置定时器
enemy_event=pygame.USEREVENT
pygame.time.set_timer(enemy_event,10)

#装载敌机子弹
bullet=pygame.image.load("alien_bullet.png")
bullet_W=44
bullet_H=48
bullet_y=enemy_y+enemy_H/2#子弹在敌机的肚子里出来
bullet_x=enemy_x+enemy_W/2-bullet_W/2
#给敌机子弹设置定时器
bullet_event=pygame.USEREVENT+1
pygame.time.set_timer(bullet_event,5)

#装载飞弹
feidan=pygame.image.load("feidan.png")
feidan_W=21
feidan_H=59
feidan_y=y+H/2#子弹在敌机的肚子里出来
feidan_x=x+W/2-feidan_W/2
# 控制飞弹是否发射
is_feidan_shoot = False
#给飞弹设置定时器
feidan_event=pygame.USEREVENT+2
pygame.time.set_timer(feidan_event,5)

while ctn:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:#如果按下一个键
            key_pressed=pygame.key.get_pressed()#获取这个键的键值
            if key_pressed[K_ESCAPE]:
                ctn=False#按下esc退出

                #控制飞机移动
            elif key_pressed[K_d] or key_pressed[K_RIGHT]:
                if x+STEP<WIDTH-W : x+=STEP
                else:x=WIDTH-W
            elif key_pressed[K_a] or key_pressed[K_LEFT]:
                if x-STEP>0 : x-=STEP
                else : x=0
            elif key_pressed[K_s] or key_pressed[K_DOWN]:
                if y+STEP<HEIGHT-H: y+=STEP
                else : y=HEIGHT-H
            elif key_pressed[K_w] or key_pressed[K_UP]:
                if  y-STEP>0:y-=STEP
                else :y=0

            #控制飞弹发射
            elif key_pressed[K_SPACE]:
                is_feidan_shoot = True  # 当按下空格键时，准备发射飞弹
                feidan_y = y + H / 2   # 设置飞弹位置
                feidan_x = x + W / 2 - feidan_W / 2

        elif event.type==pygame.MOUSEBUTTONDOWN:    #如果点击鼠标
            mouse_pressed=pygame.mouse.get_pressed()    #获取鼠标活动
            if mouse_pressed==(1,0,0):  #如果鼠标左击
                mouse_x,mouse_y=pygame.mouse.get_pos()  #获取鼠标左击的坐标
                #通过判断鼠标左击的位置控制飞机的移动
                if mouse_x<x:
                    if x>STEP:x-=STEP
                    else:x=0
                elif mouse_x > x + W:
                    if x + STEP > WIDTH:x = WIDTH - W
                    else:x += STEP
                if mouse_y<y:
                    if y>STEP: y-=STEP
                    else:y = 0
                elif mouse_y > y + H:
                    if y+STEP>HEIGHT: y =HEIGHT-H
                    else:y +=STEP
        elif event.type==enemy_event:
            if enemy_y>HEIGHT:#敌机飞出屏幕后刷新
                enemy = pygame.image.load("alien_" + str(random.randint(1, 5)) + ".png")#随机生成敌机
                enemy_x=random.randint(0, WIDTH - enemy_W)
                enemy_y=-enemy_H
                bullet_y = enemy_y + enemy_H / 2  # 子弹也要刷新
                bullet_x = enemy_x + enemy_W / 2 - bullet_W / 2
            else:
                enemy_y += 1

        elif event.type==bullet_event:
            bullet_y+=1
            if bullet_y==HEIGHT:
                bullet_y=enemy_y+enemy_H/2

        elif event.type==pygame.QUIT:
            ctn = False#点击叉号退出

    if is_feidan_shoot:
        screen.blit(feidan, (feidan_x, feidan_y))
        feidan_y -= 5  # 飞弹向上移动
        if feidan_y < -feidan_H:  # 如果飞弹移出屏幕顶部，则重置状态
            is_feidan_shoot = False
    screen.blit(bg0, (0, 0))

    screen.blit(plane,(x,y))#x，y的值随时刷新
    screen.blit(bullet,(bullet_x,bullet_y))
    screen.blit(enemy, (enemy_x, enemy_y))


    pygame.display.update()

exit(0)

