#!/usr/bin/python3
import smtplib,json
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def uploadPicture(path,id_name):
    # 指定图片为当前目录
    fp = open(path, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<'+id_name+'>')
    msgImage["Content-Disposition"] = 'attachment; filename="' + id_name +'.jpg"'
    return msgImage

def sendEmail(html_page,ComputerName,attach1,attach2,towhos):
    try:
        # 第三方 SMTP 服务
        mail_host="smtp.163.com"  #设置服务器
        mail_user="jyzyg129@163.com"    #用户名
        mail_pass="oW12ExECC3ERhCWn"   #口令 
        
        message = MIMEMultipart()
        sender = 'jyzyg129@163.com'
        receivers = ['Hylan<zhaoyg@qxaiot.com>'] + towhos # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        
        message['From'] = "Robot_Check<jyzyg129@163.com>"
        message['To'] = ','.join(receivers)

        subject = '【请查阅】机器人' + ComputerName + '系统配置检查报告！'
        message['Subject'] = Header(subject, 'utf-8')

        #添加附件1，正文。
        #message.attach(MIMEText('大家好！请查阅机器人' + ComputerName + '系统配置检查报告！如有异常，请尽快修复！\n', 'plain', 'utf-8'))

        #message['From'] = Header("Hylan129<jyzyg129@163.com>", 'utf-8')
        #message['To'] =  Header("ZYG<zhaoyg@qxaiot.com>", 'utf-8')

        #添加附件2，网页表单。
        message.attach(MIMEText(html_page, 'html', 'utf-8'))
        
        #添加附件照片1：
        message.attach(uploadPicture(attach1,'logo'))
        message.attach(uploadPicture(attach2,'foreward'))
        message.attach(uploadPicture(attach2,'camera'))

        try:
            # 构造附件1，传送当前目录下的 test.csv 文件
            att3 = MIMEText(open('files/dll_version_information.csv', 'rb').read(), 'base64', 'utf-8')
            att3["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att3["Content-Disposition"] = 'attachment; filename="dll_version_information.csv"'

            att4 = MIMEText(open('files/android_softwares_version.txt', 'rb').read(), 'base64', 'utf-8')
            att4["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att4["Content-Disposition"] = 'attachment; filename="android_softwares_version.txt"'

            message.attach(att3)
            message.attach(att4)
        except Exception as e:
            with open('error.txt','a') as code:
                code.write(str(e)+ "附件添加故障，请检查是否生成文件！\n")

        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        
    except Exception as e:
        with open('error.txt','a') as code:
            code.write(str(e) + "邮件发送失败！\n")
