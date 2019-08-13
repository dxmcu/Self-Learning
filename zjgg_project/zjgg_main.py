#!/usr/bin/env python
# coding=utf-8
import time
import navigation_model,sixmic_control
from multiprocessing import Process

#position_list = ['11','12','13','14','15','16','17','18']
#position_list = ['4','56','2']
position_list =  ['13','14','15','16','17','18','19','20','21','22']

text_list = ['请大家移步至下一讲解点。',
            '呈现在您面前的，是本馆的重点展品之一——在2001年9月十一日恐怖袭击中倒塌的美国纽约世界贸易中心钢构件残骸。本展品长二点五米，宽一点七米，高零点八五米，重约3吨，属于世贸北塔顶部天线八边形部分，位于铭牌所指示的红圈位置，由美国纽约与新泽西港务局无偿捐赠本馆。世贸中心的倒塌一度让人们对钢结构的安全性和可靠性产生怀疑，我们展示这件钢构件的目的，一是谴责恐怖主义，二是要澄清人们对钢结构认识上的误区。因为“9·11恐怖袭击”是一次极端事件，事后的调查表明，无论建筑使用的是钢结构还是其他材料，均难以承受如此猛烈的撞击和如此高强度的燃烧，恰恰因为钢结构的良好表现，为撞击部位以下的人员逃生争取到更多的时间，北塔和南塔在遭受撞击后仍然分别坚持了一百零三分钟和五十七分钟。2014年在世贸中心原址附近落成的世贸中心1号楼，主体仍然采用钢结构，再次证明了人们对钢结构的信心。',
            '您背后的展墙，是新的里程碑板块，讲述第二次世界大战到20世纪末钢结构在世界各国的普遍应用。如美国的圣路易斯拱门、加拿大蒙特利尔世博会的美国馆、澳大利亚的悉尼歌剧院、法国的蓬皮杜国家艺术文化中心、日本的福冈体育馆等，当然也包括纽约世界贸易中心。这些地标建筑，展示着钢结构在人类生活中越来越广泛的应用，印证着世界工业文明发展的新的辉煌成就。',
            '讲解完毕，小派在这停留三分钟，三分钟之后小派将带大家去下一个讲解点呢。',
            '请大家移步至下一讲解点。',
            '新中国成立以后，中国的钢铁工业从废墟中起步，但由于钢铁资源的短缺，仅在一些重大工程上，如武汉长江大桥、人民大会堂等使用了钢结构。改革开放以后，中国的钢结构产业进入逐渐发展期，截至二十世纪末，中国陆续建成了深圳发展中心、深圳地王大厦、上海金茂大厦等标志性钢结构建筑。最初，这些建筑由外国人设计，用外国的钢材，在外国加工，中国的企业只是承担施工，到后来，越来越多的钢结构建筑由中国人设计，用国产钢材，在国内加工。中国的钢结构产业沿着正确的轨道奋起直追。',
            '二十一世纪堪称钢结构的世纪，新千年以来，世界各地不断涌现出新的钢结构建筑和桥梁，钢结构高度、跨度和精度的纪录不断刷新。在您右侧，通过三个屏幕展示这一时期的钢结构建设成就。左侧屏介绍的是2000年以来世界范围内钢结构经典建筑，如目前世界最高的哈利法塔，高度达到八百二十八米；中间屏介绍的是本世纪前十年中国的钢结构建设成就，包括上海环球金融中心、北京国家体育场和中央电视台、武汉火车站等；右侧屏则是2010年以来中国建成的钢结构建筑和桥梁，如深圳宝安国际机场T3航站楼、上海中心大厦、深圳平安金融中心等。中国的高端钢结构工程从设计到钢材供应、构件加工、现场施工已全部实现国产化，而且，钢结构乃至整个建筑业的技术水平已进入世界前列。',
            '历史厅就为大家讲解完了，如果还有其他吩咐，请按照小派的屏幕提示给我下达指令哦。',
            '您现在进入本馆的科技厅。在这一部分，我们以科技为主线，介绍钢结构体系、设计、制造、安装、防腐、防火、防震、检测、监测等内容，同时也追溯这些技术的演进过程。您现在穿行在一座钢桥上，它是不是有点像上海的外白渡桥？在钢桥的两侧，我们以多媒体搭配模型的方式，重点介绍8种重要的结构体系。它们是：立体桁架结构、单层刚架、框架结构、框架-支撑结构、框架-筒体结构、巨型框架-筒体-支撑结构、索结构、网架结构。',
            '讲解完毕，小派在这停留三分钟，三分钟之后小派将带大家去下一个讲解点呢。',
            ]
time_list = [0.3 * len(time) for time in text_list]

def zjgg_xunhang():
    try:
        sixmic_control.port_open()

        i =3
        while(i):
            sixmic_control.send(sixmic_control.buildShakePacket())
            i -= 1

        while True:
            for go_point,text_point,time_point in zip(position_list,text_list,time_list):
                
                navigation_model.navigation_position(go_point)
                
                navigation_model.status_navigtion_monitor()
                
                time.sleep(2)
                
                sixmic_control.send(sixmic_control.text_broadcast(text_point))
                
                time.sleep(time_point)
                
    except Exception as e:
        with open('err.txt','a') as code:
            code.write(str(e) + '\n')


def notice():
    navigation_model.status_status_monitor()
    
if __name__ == '__main__':
    t1 = Process(target = zjgg_xunhang)
    t2 = Process(target = notice)
    t1.start()
    t2.start()
    
    
    
    
    




