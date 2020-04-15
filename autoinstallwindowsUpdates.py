# -*- coding: utf-8 -*-
# @Time : 2020/3/11 16:17
# @Author : onliang
# @File : autoinstallwindowspackages.py
# @Useage: autoinstallwindowspackages.py
# @Notes:用于安装win7补丁包，解决了用户查看系统bit及其补丁的操作，一键式安装conf.json中配置的KB编号及其对应的补丁文件
import re
import os
import platform
import json
import time

def install(packagename=''):
    '''
    安装windows补丁包
    :param packagename: 补丁包文件名
    :return:
    '''
    if os.path.exists(packagename):
        #os.startfile('.\\'+packagename) #os.startfile（）打开外部应该程序，与windows双击相同
        cmd = 'wusa.exe '+os.getcwd()+'\\'+packagename+' /quiet /promptrestart'
        #print(str(cmd))
        res = os.system(cmd)  #静默安装
        if res == 0:
            return res
    else:
        print('当前目录中未检测到补丁包：'+packagename)
def getsystempackge():
    '''
    获取系统信息
    :return:
    '''
    res = os.popen('systeminfo')
    result = re.findall(r'KB\d*', str(res.readlines()))
    return result
def getpackageconf():
    '''
    读取补丁配置文件
    :return:
    '''
    if os.path.exists('conf.json'):
        with open('conf.json','r+') as f:
            config = json.load(f)
        return config
    else:
        print('当前目录中未检测到配置文件conf.json')
def main():
    print('您的系统是：' + str(platform.platform(True)) + ' : ' + str(platform.architecture()[0]))
    package = getpackageconf()
    if '64' in str(platform.architecture()[0]):sysbit = '64'
    if '32' in str(platform.architecture()[0]): sysbit = '32'
    list = []
    res = getsystempackge()
    for row in package.keys():
        if row not in res:
            print('{}\t未安装'.format(row))
            list.append(row)
        else:
            print('{}\t已安装'.format(row))
    time.sleep(1)
    if list:
        for key in range(len(list)):
            print('开始安装{}补丁包...'.format(list[key]))
            install(package[list[key]][sysbit])
            time.sleep(3)
    else:
        print("恭喜您，已经成功安装完配置的补丁！！！")
if __name__ == "__main__":
    if '7' not in str(platform.platform(True)):
        print('您的系统是：'+str(platform.platform(True))+' ，该工具目前只支持windows7系统\r\n'+'*'*30+'\r\n') #    #Windows-10-10.0.18362-SP0
        time.sleep(3)
    else:
        print('*'*30+'\r\n')
        main()