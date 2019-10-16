#!/usr/bin/env python
# coding=utf-8

position_list =  ['116','118','119','4','5','6']

"""
      "LOCALIZATION_FAILED":"定位失败",
      "GOAL_NOT_SAFE","目的地有障碍物"
      "TOO_CLOSE_TO_OBSTACLES":"离障碍物太近",
      "UNREACHABLE":"目的地无法到达",
      "REACHED":"已到达目的地",
      "HEADING":"正在前往目的地",
      "PLANNING":"正在规划路径",
      "UNREACHED":"到达目的地附近，目的地有障碍物"
"""

text_list = ['欢迎光临！深圳市奇信智能科技有限公司（以下简称：奇信智能）隶属于深圳市奇信建设集团股份有限公司（股票代码：002781），拥有电子与智能化工程专业承包资质，依托上市母公司平台积极探索物联网+生态进化与智慧城市构建，具备了领先的产业链协同能力和装饰物联网平台先发优势。第1个点讲解完毕，即将前往下一个点。',
 '我们依托物联网、云计算、大数据与人工智能等新技术，奇信智能提出“1+1+N”的发展战略，通过“1”个自主研发的奇π物联网云平台和“1”个奇信小π机器人产品（办公商用版、家居健康版）来为用户提供以“云+端+行业深度应用解决方案”为核心的全产业链服务，在智慧办公、园区、酒店、体育、政务、展厅、物流、农业、医疗、养老等领域全面落地，构建从细分场景到行业全领域的智慧城市应用图谱。第2个点讲解完毕，即将前往下一个点。',
 '公司秉承开放合作心态，坚持创新创业，致力于成为世界级智慧城市综合管理运营服务引领者。第3个点讲解完毕，即将前往下一个点。','我们的奇π物联网云平台是一个面向智慧城市全领域应用的物联网生态管理系统。第4个点讲解完毕，即将前往下一个点。',
 '平台具备三大特性（高效安全、方便灵活、界面友好）和四层次核心价值（物联全链接、多场景联动、大数据盘活、运营智慧化）。第5个点讲解完毕，即将前往下一个点。',
 '在园区、办公、体育、政务、酒店、展馆等智慧城市细分场景应用中，帮助运营方与管理者实现提升系统安全、简化业务流程、节省各项能耗、优化运营服务、创新企业增值等多类价值。第6个点讲解完毕，即将再次前往第1个点。'
 
 
 ]

time_list = [0.3 * len(time_) for time_ in text_list]