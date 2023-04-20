#!/bin/bash

case $1 in
    its) xrandr --output "eDP-1" --primary --auto --output "HDMI-2" --mode 1366x768 --pos 0x0 --same-as "eDP-1" ;;
    casa) xrandr --output "eDP-1" --primary --auto --output "HDMI-2" --mode 1360x768 --pos 0x0 --right-of "eDP-1" ;;
esac
