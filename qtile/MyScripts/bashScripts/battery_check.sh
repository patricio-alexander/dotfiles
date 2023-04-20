#!/bin/bash

export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"


WARNING_BATTERY=25
BATTERY_DISCHARGING=`acpi -b | grep "Battery 0" | grep -c "Discharging"`
BATTERY_LEVEL=`acpi -b | grep "Battery 0" | grep -P -o '[0-9]+(?=%)'`
ICON_ALERT_BATT=~/.config/qtile/MyScripts/bashScripts/icons/battery_icons/battery-alert.png
ICON_CHAR_BATT=~/.config/qtile/MyScripts/bashScripts/icons/battery_icons/battery-charging.png
ICON_FULL_BATT=~/.config/qtile/MyScripts/bashScripts/icons/battery_icons/battery.png

CHARGING=/tmp/battery_Charging
DISCHARGING=/tmp/battery_Discharging

# If the battery is charging and is full (and has not shown notification yet)
if [ $BATTERY_LEVEL -gt 95 ] && [ $BATTERY_DISCHARGING -eq 0 ] && [ ! -f $CHARGING ]; then
  notify-send "Batería Cargada" "Batería totalmenta cargada" -u low -i $ICON_FULL_BATT -r 9991
  touch $CHARGING

# If the battery is low and is not charging (and has not shown notification yet)
elif [ $BATTERY_LEVEL -le $WARNING_BATTERY ] && [ $BATTERY_DISCHARGING -eq 1 ] && [ ! -f $DISCHARGING ]; then
  notify-send "Batería baja" "${BATTERY_LEVEL}% conecte el cargador." -u critical -i $ICON_ALERT_BATT -r 9991
  touch $DISCHARGING

#elif [ $BATTERY_DISCHARGING -eq 0 ]; then
#  notify-send "Battery Status" "Battery level: ${BATTERY_LEVEL}%" -i $ICON_CHAR_BATT

fi

# Reset notifications if the computer is charging/discharging
if [ $BATTERY_DISCHARGING -eq 1 ] && [ -f $CHARGING ]; then
    rm $CHARGING
elif [ $BATTERY_DISCHARGING -eq 0 ] && [ -f $DISCHARGING ]; then
    rm $DISCHARGING
fi 

