# 常见问题

## 系统与使用

### Q1：首次启动后出现应用出错、鼠标卡顿等情况怎么办？
**A**：
首次完成引导配置后，部分系统设置尚未完全生效，建议**重启一次设备**，重启后系统将恢复正常。

### Q2：如果忘记了登录密码，如何重置？
**A**：  
1. 使用串口线连接 MUSE Book 与上位机（电脑）。  
2. 在上位机上打开串口通信软件，使用管理员账号登录：
   - 用户名：`root`
   - 密码：`bianbu`
3. 登录后根据需要执行以下命令之一：
   - 若需保留用户资料：  
     ```bash
     userdel 用户名
     ```
   - 若不保留用户资料：  
     ```bash
     userdel -r 用户名
     ```
4. 重启设备，即可重新进入引导界面设置新用户名和密码。

## 系统支持

### Q3：MUSE 系列产品支持哪些操作系统？
**A**：
目前已适配的系统包括：
- Bianbu Desktop（出厂预装）
- Bian Linux
- Deepin
- OpenKylin
- OpenHarmony  

更多操作系统正在持续适配中，请关注进迭时空官方发布。

### Q4：MUSE 系列产品支持 Windows 系统吗？
**A**：
目前暂不支持 Windows 系统。MUSE Book 出厂预装基于 Ubuntu 深度优化的 **Bianbu Desktop**，内置 LibreOffice、浏览器、媒体查看器等常用软件，开箱即用。用户也可通过 Bianbu 软件源安装更多应用。

## 固件与驱动

### Q5：MUSE 系列产品支持自行刷写固件吗？
**A**：支持。用户可通过命令行工具或 Titan 工具进行固件刷写，具体操作方法请参考对应产品的《用户使用指南》。

### Q6：如何获取 MUSE Pi 配套串口线驱动？
**A**：驱动下载地址：  
[https://www.ftdichip.cn/Drivers/D2XX.htm](https://www.ftdichip.cn/Drivers/D2XX.htm)
