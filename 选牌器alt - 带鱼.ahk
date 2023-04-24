MsgBox, [ 卡牌选牌器, 注意使用管理员方式启动！alt+1、2、3分别对应蓝红黄牌]
MsgBox, [ 请将游戏窗口调整到 3440*1440 的无边框模式，并将用户界面缩放调整至35]

~!1::
PixelGetColor,check_color,1566,1350,RGB
If(check_color = 0xCD916B)
    {
        send {w}
        loop{
        PixelGetColor,color,1566,1350,RGB
        If (color = 0x101043)
        {
            send {w}
            break
        }
        }
    }
return


~!2::
PixelGetColor,check_color,1566,1350,RGB
If(check_color = 0xCD916B)
    {
        send {w}
        loop{
        PixelGetColor,color,1566,1350,RGB
        If (color = 0x410808)
        {
            send {w}
            break
        }
        }
    }
return


~!3::
PixelGetColor,check_color,1566,1350,RGB
If(check_color = 0xCD916B)
    {
        send {w}
        loop{
        PixelGetColor,color,1566,1350,RGB
        If (color = 0x403300)
        {
            send {w}
            break
        }
        }
    }
return

