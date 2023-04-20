#!/bin/bash

save_as="/home/patricio/Images/screenshot/%Y-%m-%d-%T-screenshot.png"
icon="/home/patricio/.config/qtile/MyScripts/bashScripts/icons/screenshot_notify/screenshotImg.png"

case $1 in 
  window) scrot "$save_as" --focused --border ;;
  select) scrot "$save_as" --select --line mode=edge ;;
  *) scrot "$save_as" ;;

esac

dunstify -i $icon "Captura de pantalla hecha" -t 4000

