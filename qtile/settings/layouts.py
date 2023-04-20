
#-----------------#
#  QTILE LAYOUTS  #
#-----------------#


from libqtile.layout.xmonad import MonadTall, MonadWide
# from libqtile.layout.stack import Stack
# from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max
from libqtile.config import Match



layout_theme = {
    "border_width": 2,
    "margin": 3,
    #"border_focus": "#e1acff",
    "border_focus": "#e1acff",
    "border_normal": "#1e2127",
    "single_border_width": 0,
}

layout_max = {
    "margin": 3,
    "single_border_width": 0
}

layouts = [
    Max(**layout_max), 
    MonadTall(**layout_theme), 
    #Columns(**layout_theme),
    #Stack(**layout_theme),
    MonadWide(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)

