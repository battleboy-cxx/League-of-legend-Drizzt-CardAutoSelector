MsgBox, [ 卡牌选牌器, 注意使用管理员方式启动！alt+1、2、3分别对应蓝红黄牌]

!3::
PixelGetColor,check_color,1113,1315,RGB
If(check_color = 0x5A249C)
    {
        send {w}
        loop{
        PixelGetColor,color,1113,1315,RGB
        ; 蓝牌
        If (color = 0x423CB5)
        {
            send {w}
            break
        }
        }
    }
return

; 红牌
!2::
PixelGetColor,check_color,1113,1315,RGB
If(check_color = 0x5A249C)
    {
        send {w}
        loop{
        PixelGetColor,color,1113,1315,RGB
        ; 红牌
        If (color = 0xEF1F20)
        {
            send {w}
            break
        }
        }
    }
return


!1::
PixelGetColor,check_color,1113,1315,RGB
If(check_color = 0x5A249C)
    {
        send {w}
        loop{
        PixelGetColor,color,1113,1315,RGB
        ; 黄牌
        If (color = 0xE7E300)
        {
            send {w}
            break
        }
        }
    }
return

