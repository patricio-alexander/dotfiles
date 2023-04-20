#!/bin/sh

#wallpaper
feh --bg-fill /home/patricio/Images/wallpapers/wallp14.png
#picom
 
#picom --experimental-backends 
picom --config $HOME/.config/qtile/picom/picom.conf &

#wifi icon
nm-applet &

#start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#USB



#udiskie -t & 

# systray battery icon
#cbatticon -u 1 &

# systray volume
#volumeicon &

killall dunst
dunst -conf ~/.config/qtile/dunst/dunstrc &
