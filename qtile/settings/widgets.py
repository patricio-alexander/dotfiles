#-----------------#
#  QTILE WIDGETS  #
#-----------------#




from libqtile.config import Screen
from .colors import theme
from .settings import font, font_size, icon_size, bar_size
from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

def separator():
    return widget.Sep(
        linewidth=0, 
        padding=6, 
        background=theme["background"]
    )

def workspace():
    return widget.GroupBox(
        active=theme["white"],
        fontsize=icon_size,
        highlight_method="line",
        borderwidth = 2,
        inactive=theme["black"],
        highlight_color = theme["background"],
        margin_x=0,
        margin_y=3,
        padding_x=10, 
        padding_y=4,
        #urgent_alert_method="block",
        this_current_screen_border=theme["orange"],
        #block_highlight_text_color=theme["white"], 
    )






widget_defaults = dict(
    font = font,
    fontsize = font_size,
    padding = 1,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [ 
                
                workspace(),
                separator(),
                
                #widget.Prompt(),
                #widget.WindowName(foreground = theme["foreground"]), 
                widget.Spacer(),
                widget.Systray(background=theme["background"], padding=6),
                separator(),
                widget.UPowerWidget(
                    battery_width=22,
                    battery_height=13,
                    fill_normal=theme["white"],
                    fill_charge=theme["green"],
                    fill_low=theme["orange"],
                    fill_critical=theme["red"],
                    border_critical_colour=theme["red"],
                    border_colour=theme["black"],
                    percentage_low = 0.25,
                    percentage_critical = 0.20,
                ),
                
                widget.Battery(
                    fontsize=font_size,
                    font=font,
                    low_percentage=0.25,
                    low_background=theme["background"],
                    low_foreground=theme["orange"],
                    foreground=theme["white"],
                    background=theme["background"],
                    charge_char="",
                    discharge_char="",
                    full_char="",
                    unknown_char="",
                    format='{percent:2.0%} {char}', 
                    
                ),

                
              
                widget.PulseVolume(
                    foreground=theme["background"],
                    limit_max_volume=True,
                    padding=3,
                    fmt=" 墳 {} ",
                    update_interval=0.001,
                    decorations = [
                        RectDecoration(
                            colour= theme["blue"],
                            filled=True,
                            padding_y=3 
                        )
                    ]
                ),

                #separator(),


                #widget.Clock(
                    #format="%d/%m/%y %I:%M %p",
                #    format="%A, %d/%m",
                #    foreground=theme["magenta"],
                #    padding=5,
                #),
                

                separator(),
                widget.Memory(
                    measure_mem='G',
                    format="  {MemUsed:.1f}/{MemTotal:.1f} GiB ",
                    foreground=theme["background"],
                    padding=3,
                    decorations = [
                        RectDecoration(
                            colour= theme["green"],
                            filled=True,
                            padding_y=3 
                        )
                    ]
                ),

                separator(),
                widget.Clock(
                    format="  %I:%M -  %a,%d/%m " , 
                    foreground=theme["background"],
                    decorations = [
                        RectDecoration(
                            colour= theme["magenta"],
                            filled=True,
                            padding_y=3 
                        )
                    ]
                ),
                separator()
                #icon(theme["red"], " "),
                #widget.CurrentLayout(foreground=theme["red"]),

                
                

                

                
                
               
                #widget.QuickExit(background=custom_color[7], padding=10),
            ],
            bar_size,
            background = theme["background"],
            margin = [3, 3, 2, 3], #North , East, South, West  
            #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

