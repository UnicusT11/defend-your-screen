#   
<p align="right">  
  🌏 语言: 中文 | <a href="./README.md">English</a>  
</p>  
  
# 🔐 Defend Your Screen  
  
> 一个用于保护桌面操作的轻量工具，在不影响程序运行的情况下锁定屏幕  
  
---  
  
## 📖 简介  
  
平时离开电脑时，如果直接使用系统锁屏，往往会影响当前正在运行的程序（尤其是远程连接、挂机任务等场景）。  
  
这个项目的出发点很简单：  
  
> 在不改变当前系统状态的情况下，把屏幕“挡住”。  
  
它更像一个覆盖层式的锁定方案，而不是系统级锁屏。  
  
---  
  
## 🧠 核心思路  
  
> 🔒 限制操作，而不是中断运行  
  
它不会：  
  
- 暂停程序    
- 终止进程    
  
而是通过：  
  
- 全屏覆盖界面    
- 输入检测    
  
来实现锁定效果  
  
---  
  
## ⚙️ 功能特性  
  
- 🔐 密码解锁    
- ⚡ 检测到操作立即锁定    
- ⌨️ 全局快捷键开启监控模式    
- 🖥 托盘运行（设置 / 退出）    
- 🔁 可重复使用（启动 → 锁定 → 解锁）    
- 🧩 轻量级（约9MB内存，CPU几乎为0）    
- 🛠 基于 Python 编写，方便修改    
  
---  
  
## 👀 截图  
  
  
### 设置界面  
  
<p align="center">  
  <img src="./assets/screenshots/settings_panel.png" width="300">  
</p>  
  
### 托盘菜单  
  
<p align="center">  
  <img src="./assets/screenshots/tray_menu.png" width="200">  
</p>  
  
### 锁屏界面  
  
<p align="center">  
  <img src="./assets/screenshots/lock_screen.png" width="500">  
</p>  
  
### 应用图标  
  
<p align="center">  
  <img src="./assets/screenshots/app_icon.png" width="120">  
</p>  
  
---  
  
## 🚀 使用流程  
  
1. 启动程序    
2. 设置密码和快捷键    
3. 开启监控模式    
4. 检测到输入后：  
   - 立即锁定屏幕    
   - 阻止操作    
5. 输入密码解锁    
6. 可重复使用    
  
---  
  
## 📦 安装方式  
  
从 GitHub 下载发布版本。  
  
确保以下文件在同一目录：  
defend your screen.exe  
defend your screen.png  
  
然后直接运行即可。  
  
---  
  
## 🧭 使用说明  
  
### 1. 初始设置  
  
- 在 **Set a password** 设置密码    
- 在 **Set a start hotkey** 设置快捷键    
- 点击 **Save**    
  
> ⚠️ 如果未设置密码，按 Enter 可直接解锁    
  
---  
  
### 2. 开启监控  
  
- 按快捷键（默认：`Alt + C`）    
- 听到提示音表示已开启    
  
---  
  
### 3. 锁定 / 解锁  
  
- 检测到输入后自动锁定    
- 输入密码并按 Enter 解锁    
  
---  
  
### 4. 托盘功能  
  
右键托盘图标：  
  
- **View** → 打开设置    
- **Quit** → 退出程序    
  
---  
  
## 🧩 技术栈  
  
- Python    
- tkinter    
- pystray    
- keyboard    
  
---  
  
## 📄 License  
  
MIT License  
  
---  
  
## 📄 说明  
  
该工具更适合作为一个补充工具使用：  
  
- 不替代系统锁屏    
- 只解决“不中断运行但需要防操作”的问题    
