MsgBox, [ 卡牌选牌器, 注意使用管理员方式启动！alt+1、2、3分别对应蓝红黄牌]
MsgBox, [ 请将游戏窗口调整到 1920*1080 的无边框模式，并将用户界面缩放调整至35]

~!3::
PixelGetColor,check_color,856,1005,RGB
If(check_color = 0xD49171)
    {
        send {w}
        loop{
        PixelGetColor,color,856,1005,RGB
        If (color = 0xBFB600)
        {
            send {w}
            break
        }
        }
    }
return


~!2::
PixelGetColor,check_color,856,1005,RGB
If(check_color = 0xD49171)
    {
        send {w}
        loop{
        PixelGetColor,color,856,1005,RGB
        If (color = 0x580708)
        {
            send {w}
            break
        }
        }
    }
return


~!1::
PixelGetColor,check_color,856,1005,RGB
If(check_color = 0xD49171)
    {
        send {w}
        loop{
        PixelGetColor,color,856,1005,RGB
        If (color = 0x292884)
        {
            send {w}
            break
        }
        }
    }
return

