# AutoInstallWindowsUpdates
**用于安装win7补丁包，解决了用户对比系统是否已安装补丁编号、系统bit、补丁包和安装操作等操作，一键式安装conf.json中配置补丁文件**

**使用步骤：**
- 从windows官方网站下载补丁包，然后配置json文件(kb漏洞编号-补丁包名字-系统位数一一对应)。
- 将补丁包、json配置文件和AutoInstallWindowsUpdates.exe放在同一个目录下。
- 运行AutoInstallWindowsUpdates.exe，如果某些补丁包需要重启，会提示重启。
