#!/bin/bash

max_icon=~/.config/qtile/MyScripts/bashScripts/icons/brightness_icon/brightness_max.png
medium_icon=~/.config/qtile/MyScripts/bashScripts/icons/brightness_icon/brightness_medium.png

function change_brigntness() { 
  brightness_level=`brightnessctl | grep "brightness:" | grep -P -o "[0-9]+(?=%)"`
  
  if [[ $brightness_level -gt 50 ]]; then
    dunstify -u low "Brillo: $brightness_level%" -i $max_icon -h int:value:"$brightness_level" -r 100 -t 2000
  
  elif [ $brightness_level -le 50 ]; then
    dunstify -u low "Brillo: $brightness_level%" -i $medium_icon -h int:value:"$brightness_level" -r 100 -t 2000 
  
  fi
  
}

 case $1 in
    up)
      brightnessctl set +5%
      change_brigntness 
      ;;
    down)
      brightnessctl set 5%-
      change_brigntness 
    ;;
  esac


