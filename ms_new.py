# -*- encoding=utf8 -*-
__author__ = "Kyuu"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.api import *
# airtest.core.api中包含了一个名为ST的变量，即为全局设置
ST.THRESHOLD = 0.85

auto_setup(__file__)

# script content
log("start...")

auto_setup(__file__)

free_count = 0
light_lock = False
auto_task_temp = Template(r"tpl1658164859868.png", record_pos=(-0.169, 0.228), resolution=(1280, 720))
auto_nav_temp = Template(r"tpl1658156262845.png", record_pos=(-0.087, -0.125), resolution=(1280, 720))
mission_temp = Template(r"tpl1658155662997.png", record_pos=(-0.427, -0.122), resolution=(1280, 720))
next_temp = Template(r"tpl1658155992222.png", record_pos=(0.448, 0.112), resolution=(1280, 720))
accept_temp = Template(r"tpl1658156074983.png", record_pos=(0.362, 0.045), resolution=(1280, 720))
finish_temp = Template(r"tpl1658156339504.png", record_pos=(0.362, 0.046), resolution=(1280, 720))
ok_temp = Template(r"tpl1658156596398.png", record_pos=(0.366, 0.047), resolution=(1280, 720))
award_temp = Template(r"tpl1658160944184.png", record_pos=(0.004, 0.22), resolution=(1280, 720))
auto_skill_temp = Template(r"tpl1658156481752.png", record_pos=(0.116, -0.009), resolution=(1280, 720))
auto_equip_temp = Template(r"tpl1658157013067.png", record_pos=(0.101, 0.026), resolution=(1280, 720))
light_temp = Template(r"tpl1658222839643.png", record_pos=(0.089, 0.075), resolution=(1280, 720))
maple_book_temp = Template(r"tpl1658159739966.png", record_pos=(0.151, 0.077), resolution=(1280, 720))
start_mission_temp = Template(r"tpl1658211983991.png", record_pos=(-0.176, 0.166), resolution=(1280, 720))
finish_mission_temp = Template(r"tpl1658212236510.png", record_pos=(-0.174, 0.166), resolution=(1280, 720))
hot_and_new_temp = Template(r"tpl1658248457448.png", record_pos=(-0.352, -0.227), resolution=(1280, 720))
map_loading_temp = Template(r"tpl1658249095159.png", record_pos=(0.333, -0.212), resolution=(1280, 720))


multi_task_finish = Template(r"tpl1658387323206.png", record_pos=(-0.169, 0.228), resolution=(1280, 720))

while(True):
    #如果空置次数为0就重置灯泡点击事件
    if(light_lock == True and free_count == 0):
        log("重置灯泡点击锁定")
        light_lock = False
    
    #开局截图     
    screen = G.DEVICE.snapshot()
    
    auto_task_pos = auto_task_temp.match_in(screen)
    if(auto_task_pos):
        log("检测到正在执行自动任务 等待")
        sleep(2)
        free_count = 0
        continue

    auto_nav_pos = auto_nav_temp.match_in(screen)
    if(auto_nav_pos):
        log("正在进行自动寻路")
        sleep(2)
        free_count = 0
        continue

    map_loading_pos = map_loading_temp.match_in(screen)
    if(map_loading_pos):
        log("过图加载中。。。")
        sleep(2)
        free_count = 0
        continue


    if(free_count >= 2):
        log("空置回数到达 %d 回 寻找新任务" %(free_count))
        mission_pos = mission_temp.match_in(screen)
        if(mission_pos):
            #直接点击第一栏任务区域
            touch([395, 318])
            log("主动点击任务")
            free_count = 0
            continue
    
    
    cur_screen = G.DEVICE.snapshot()
    multiple_next=False
    while(True):
        next_pos = next_temp.match_in(cur_screen)
        if next_pos:
            multiple_next=True
            touch(next_pos)
            log("点击下一步")
            free_count = 0
            time.sleep(1)
            cur_screen=G.DEVICE.snapshot()
        else:
            break
    if multiple_next:
        continue
    else:
        pass
#     next_pos = next_temp.match_in(screen)
#     if(next_pos):
#         touch(next_pos)
#         log("点击下一步")
#         sleep(2)
#         free_count = 0
#         continue
    
    award_pos = award_temp.match_in(screen)
    log(award_pos)
    if(award_pos):
#         touch(award_pos)
        touch([1240,950])
        log("领取奖励")
        sleep(2)
        continue
        
    multi_finish_mission_pos = multi_task_finish.match_in(screen)
    if(multi_finish_mission_pos):
        touch(multi_finish_mission_pos)
        log("点击结束多任务")
        sleep(2)
        continue
    
    finish_pos = finish_temp.match_in(screen)
    if(finish_pos):
#         touch(finish_pos)
        touch([2128,614])
        log("点击完成")
        free_count = 0
        sleep(2)
        continue
    
    accept_pos = accept_temp.match_in(screen)
    if(accept_pos):
        touch(accept_pos)
        log("点击接受")
        free_count = 0
        sleep(2)
        continue



    
    ok_pos = ok_temp.match_in(screen)
    if(ok_pos):
        touch(ok_pos)
        log("点击确认")
        free_count = 0
        sleep(2)
        continue
        


    
    auto_skill_pos = auto_skill_temp.match_in(screen)
    if(auto_skill_pos):
        touch(auto_skill_pos)
        free_count = 0
        log("自动加点")
        sleep(2)
        continue
    
    auto_equip_pos = auto_equip_temp.match_in(screen)
    if(auto_equip_pos):
        touch(auto_equip_pos)
        log("自动装备")
        free_count = 0
        sleep(2)
        continue
    
    light_pos = light_temp.match_in(screen)
    if(light_pos):
        if(light_lock):
            log("灯泡已经点过了 忽略这次点击")
        else:
            touch(light_pos)
            log("点击附近任务灯泡")
            light_lock = True
            free_count = 1
            sleep(2)
            continue
        
    maple_book_pos = maple_book_temp.match_in(screen)
    if(maple_book_pos):
        touch(maple_book_pos)
        log("点击附近任务枫叶书")
        free_count = 0
        sleep(2)
        continue
    
    start_mission_pos = start_mission_temp.match_in(screen)
    

    
    finish_mission_pos = finish_mission_temp.match_in(screen)
    if(finish_mission_pos):
        touch(finish_mission_pos)
        log("点击结束任务")
        sleep(2)
        continue
        
    if(start_mission_pos):
        touch(start_mission_pos)
        log("多选任务开始")
        sleep(2)
        continue
    
    hot_and_new_pos = hot_and_new_temp.match_in(screen)
    if(hot_and_new_pos):
        log("关闭广告 HOT & NEW")
        touch([1143,70])
        sleep(2)
        continue
    
    free_count+=1
    log("空置 %d 回" %(free_count))

   
    
        
        




