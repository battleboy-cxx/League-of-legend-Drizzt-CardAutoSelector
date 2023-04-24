MsgBox, [ 卡牌选牌器, 注意使用管理员方式启动！alt+1、2、3分别对应蓝红黄牌]
MsgBox, [ 请将游戏窗口调整到 2560*1440 的无边框模式，并将用户界面缩放调整至35]



~!3::
PixelGetColor,check_color,1130,1337,RGB
If(check_color = 0x4713A4)
    {
        send {w}
        loop{
        PixelGetColor,color,1130,1337,RGB
        ; 黄牌
        If (color = 0x655300)
        {
            send {w}
            break
        }
        }
    }
return

; 红牌
~!2::
PixelGetColor,check_color,1130,1337,RGB
If(check_color = 0x4713A4)
    {
        send {w}
        loop{
        PixelGetColor,color,1130,1337,RGB
        ; 红牌
        If (color = 0xD41010)
        {
            send {w}
            break
        }
        }
    }
return


~!1::
PixelGetColor,check_color,1130,1337,RGB
If(check_color = 0x4713A4)
    {
        send {w}
        loop{
        PixelGetColor,color,1130,1337,RGB
        ; 蓝牌
        If (color = 0x5F61E1)
        {
            send {w}
            break
        }
        }
    }
return

