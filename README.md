# LOL_Card_Master_Auto_Select_Card
Automatic card selection based on autohotkey

该脚本基于autohotkey的取色函数,所以只是检测屏幕上当前活动界面的某个坐标点的RGB颜色信息,因此对系统的开销很小。实测,极小概率会出现的选错牌事件。
The script is based on the color picking function of autohotkey, so it only detects the RGB color information of a certain coordinate point on the current active interface on the screen. Therefore, the system overhead is very small. Actual tests show that wrong card selection events occur with an extremely small probability.

该应用曾发布在Bilibili.com,但因违反游戏脚本审核规定而被下架。在被下架前,短短两天就获得了近3万次观看量。
The app was previously posted on Bilibili.com, but was taken down due to issues with game script review. By the time it was removed, it had received nearly 30,000 views in just two days.

2023/4/24更新:
重构为python脚本。
Updated on 2023/4/24:
Refactored into a Python script.
- 首先按下键盘上的prt sc按键,截图选取卡牌技能栏中w中心任意一点
- First press the prt sc key on the keyboard to take a screenshot and select any point at the center of the w skill bar
- 将截图粘贴到画图软件中,鼠标放在w上的任意一个像素点(最好选择w技能框中心的像素点)
- Paste the screenshot into a drawing software, place the mouse on any pixel on w (best to select a pixel at the center of the w skill frame)
- ![img_1.png](img_1.png)
- 记录下坐标值,将其填入config.py中的target_x 和 target_y变量中
- Record the coordinate values and fill them into the target_x and target_y variables in config.py
- 运行color_detector.py,将会在终端打印出当前坐标点的RGB值
- Run color_detector.py, which will print the RGB value of the current coordinate point in the terminal
- 打开游戏,卡牌按下w之后,随着w技能框颜色的变化,会打印出多个rgb值
- Open the game, after the card presses w, as the color of the w skill frame changes, multiple rgb values will be printed
- 找到对应牌的rgb值,填入config.py中的color_dict变量中,可以借助网页判断rgb值的颜色,方便区分不同颜色的牌 https://www.rapidtables.org/zh-CN/convert/color/index.html
- Find the rgb value corresponding to the card, fill it into the color_dict variable in config.py, you can use a web page to judge the color of the rgb value to easily distinguish cards of different colors https://www.rapidtables.org/zh-CN/convert/color/index.html
- 管理员权限启动cmd,运行auto_selector.py
- Start cmd with admin privileges and run auto_selector.py

Here is the English-Chinese combined description for the old usage instructions:

## 使用说明【旧】
## Usage Instructions [Old]
1. 环境要求:
1. Environmental Requirements:
\- 本人开发环境为win11/10,其他系统没有测试。
- My development environment is Win11/10, other systems have not been tested.  
\- 需要安装autohotkey运行环境,具体百度去autohotkey官网上下载安装包即可
- Autohotkey runtime needs to be installed, you can simply search on Baidu and download the installation package from the official autohotkey website.
\- 运行脚本务必右键`以管理员身份运行`方可成功
- When running the script, you must right-click `Run as Administrator` for it to work properly.
\- 需要将LOL中`Esc`->`界面`->`用户界面缩放`设置为35,以便取色
- You need to set `User Interface Scaling` to 35 under `Esc` -> `Interface` in LOL for easy color picking.
2. 使用步骤:
2. Usage Steps:
\- 确认自己LOL中`Esc`->`视频`->`分辨率` 大部分用户是`1920*1080`或者`2560*1440`(还没有上传后者的exe文件,如果有需要联系我主页的微信),我是带鱼屏`3440*1440`
- Confirm your own LOL `Resolution` under `Esc` -> `Video`, most users are `1920*1080` or `2560*1440` (I haven't uploaded exe files for the latter yet, contact me on WeChat from my homepage if needed), I'm using an ultrawide screen `3440*1440`.
\- 下载仓库中对应的代码或exe文件 
- Download the corresponding code or exe file from the repository.
\- 右键`以管理员身份运行`
- Right click `Run as Administrator`.
\- 将弹出的提示框点击确定,测试,`alt+1`是蓝牌、`alt+2`是红牌、`alt+3`是黄牌
- Click OK on the popped up prompt box, test it: `alt+1` for blue card, `alt+2` for red card, `alt+3` for yellow card.
\- 结束程序将右下角的exe程序关闭即可
- To end the program, simply close the exe program on the bottom right corner.
