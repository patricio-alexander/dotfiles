
#---------------------#
#  QTILE KEYBINDINGS  #
#---------------------#


import json
from libqtile.config import Key
from libqtile.lazy import lazy
from .settings import mod, terminal, file_manager, browser 
from pathlib import Path
import os





keys = [

    #---    Switch between windows  ---# 
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    #---    Move windows    ---# 
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
   
    #---    Resize windows  ---# 
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    
    # Keybindings for resizing windows in MonadTall layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),

    # Full screen
    #Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    

    # Para lanzar rofi
    #Key([mod], "s",  lazy.spawn("rofi -show drun"), desc="Rofi Menu" ),
    
    #---    Powermenu   ---#
    #Key([mod], "p", lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/type-2/powermenu.sh"))),

    #--- Logout Session ---#
    Key([mod], "p", lazy.spawn(os.path.expanduser("archlinux-logout"))),
    
    #-- Tweak Tool ---#
    Key([mod], "t", lazy.spawn(os.path.expanduser("archlinux-tweak-tool"))),

    #---    Launcher   ---#
    Key([mod], "s", lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/launchers/launcher.sh"))),

    #-- Set Wallpapaer ---#
    Key([mod], "g", lazy.spawn(os.path.expanduser("~/.config/qtile/MyScripts/pyScripts/changeWallpaper"))),


    #---    Toogle layout   ---# 
    Key([mod], "Tab", lazy.next_layout()),

    #--- Move to the group on the left ---# 
    Key([mod, "shift"], "Tab", lazy.prev_layout()),



   
    #---    Kill window      ---#
    Key([mod], "w", lazy.window.kill()),
   
    #---    Reload Qtile      ---#
    Key([mod, "control"], "r", lazy.reload_config()),
    
    #---    Exit Qtile      ---#
    Key([mod, "control"], "q", lazy.shutdown()),
    
    #---    Prompt widget ---#
    Key([mod], "r", lazy.spawncmd()),

    #---    FileManager   ---#
    Key([mod], "e", lazy.spawn(file_manager)), 
    
    #---    Brave Browser ---#
    Key([mod], "b", lazy.spawn(browser)), 




    
    #---    Audio down   ---#
    #Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5"))
    Key([], "XF86AudioLowerVolume",
        lazy.spawn(os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/volume_check.sh minus")
        )),
    

    #---    Audio up   ---#
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioRaiseVolume", 
        lazy.spawn(os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/volume_check.sh up")
        )),
    


    #---    Adio mute   ---#
    #Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")), 
    Key([], "XF86AudioMute", 
        lazy.spawn(os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/volume_check.sh muted")
        )),
    


    #---    Brightness up   ---#
    #Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessUp",  
        lazy.spawn(os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/brightness_change.sh up")
        )),
    


    #---    Brightness down   ---#
    #Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    Key([], "XF86MonBrightnessDown",  
        lazy.spawn(os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/brightness_change.sh down")
        )),
    



    
    #--  Capture all screen  ---#
    Key([mod], "c", lazy.spawn(os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/screenshot_notify.sh"))),

    Key([mod, "shift"], "s", lazy.spawn(
            os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/screenshot_notify.sh select")
    )),

    Key([mod, "shift"], "a", lazy.spawn(
            os.path.expanduser("~/.config/qtile/MyScripts/bashScripts/screenshot_notify.sh window")
    )),







]
