#查询数据库equip表中配置动态库的名称清单；
#提供动态库文件固定存储的空间 D:\AlarmCenter\dll
#根据以上生成完整的文件路径清单
#查询全部文件的版本信息等
#存储到csv文件中。
import sql_match,take_picture,web_produce
import file_version,FileMailTo
import os,csv,information_record
import socket,time,gaussian

def getDllResult(defalut_path,dll_names):
    dll_paths = [defalut_path + dll_name for dll_name in dll_names]
    dll_versions = []

    for dll_name,dll_path in zip(dll_names,dll_paths):
        try:
            if os.path.isfile(dll_path):
                try: 
                    dll_versions.append(file_version.getVersion(dll_path))
                except:
                    dll_versions.append("文件" + dll_name + "版本信息解析出错！")
            else:
                dll_versions.append("目录中无" + dll_name + "文件")
        except Exception as e:
            with open('error.txt','a') as code:
                code.write(str(e) + "getDllResult\n")
    
    return dll_versions

def getComputerInformation():
    return socket.gethostbyname_ex(socket.gethostname())

def getMachineCode(path):
    return open(path,encoding='utf-8').read().strip()

def getTimeNow():
    timeArray = time.localtime(time.time())
    TimeNow = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
    return TimeNow

def getSetting_Information(rows_inSQL,version_inSys):
    software_content = ""
    number = 1
    for i,j in zip(rows_inSQL,version_inSys):
        software_content += "<tr><td>" + str(number) + "</td>"
        for m in i:
            if len(str(m)) ==32 and m.isalnum():
                m = m[0:15] + "-" + m[15:]
            software_content += "<td>"  + str(m) + "</td>"
        if type(j) == str:
            software_content += "<td></td><td></td><td></td><td></td><td>"+ str(j[1]) + "</td><td></td><td></td>"
        else:
            for n in j.values():
                software_content += "<td>"  + str(n) + "</td>"
        software_content += "</tr>"
        number += 1
    
    return software_content

if __name__ == "__main__":
    try:
        #1
        defalut_dll_path = r"C:\AlarmCenter\dll\\"

        defalut_code_path = r"C:\AlarmCenter\QXDataService\mac\mackey.txt"

        dll_information_inSQL = sql_match.getDllinformation_inSQL()

        dllnames_inSQL = [dll[2] for dll in dll_information_inSQL]

        computer_information = getComputerInformation()

        MachineCode = getMachineCode(defalut_code_path)

        CheckTime = getTimeNow()

        dll_version_inSys = getDllResult(defalut_dll_path,dllnames_inSQL)

        robot_setting_information = getSetting_Information(dll_information_inSQL,dll_version_inSys)

        gaussian_setting_information = gaussian.getGaussianVersion("http://10.7.5.88:8080/gs-robot/info")

        final_page = web_produce.makePage("cid:logo",computer_information[0],MachineCode,' || '.join(computer_information[2]),
            CheckTime,robot_setting_information,gaussian_setting_information)

        #信息写入存储！
        with open('files/version_information_' + computer_information[0] + '.html','w',encoding='utf-8') as code:
            code.write(final_page)
        
        information_record.csv_record(dll_version_inSys,['ProductName', 'ProductVersion','FileDescription','FileVersion','Comments','File_Size','Last_Modify_Time'])

        #检测结果邮件发送通报
        FileMailTo.sendEmail(final_page,computer_information[0],'files/logo.jpg','files/foreward.jpg')

    except Exception as e:
        with open('error.txt','a') as code:
            code.write(str(e) + "\n")
