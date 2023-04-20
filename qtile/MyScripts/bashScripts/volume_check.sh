#!/bin/bash

volume_minus=~/.config/qtile/MyScripts/bashScripts/icons/volume_icons/volume-minus.png
volume_plus=~/.config/qtile/MyScripts/bashScripts/icons/volume_icons/volume-plus.png
volume_muted=~/.config/qtile/MyScripts/bashScripts/icons/volume_icons/volume-muted.png
volume_no_muted=~/.config/qtile/MyScripts/bashScripts/icons/volume_icons/volume-no-muted.png


function send_volume() {
  #volume=
  dunstify -u low "$1: $2%"  -i $3 -h int:value:"$2" -r 100 -t 2000
  
}

case $1 in
  up)
    pamixer -i 5
    send_volume "Volumen" $(pamixer --get-volume) $volume_plus ;;
    
  minus)
    pamixer -d 5 
    send_volume "Volumen" $(pamixer --get-volume) $volume_minus  ;;

  muted)
    pamixer --toggle-mute
    if $(pamixer --get-mute); then
      dunstify "Volumen: Muteado"  -i $volume_muted -r 100 -t 2000 
    else
      send_volume "Volumen" $(pamixer --get-volume) $volume_no_muted  
    fi
  ;;
esac

