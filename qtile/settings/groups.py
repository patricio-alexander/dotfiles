#--------------------#
#  QTILE WORKSPACES  #
#--------------------#



from .keys import keys
from libqtile.config import Group, Key
from libqtile.lazy import lazy
from .settings import mod




groups = [Group(i) for i in ["", "", "", "", ""]]

for i, group in enumerate(groups):
    numberdesktop = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numberdesktop,
                lazy.group[group.name].toscreen(),
                desc = "Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numberdesktop,
                lazy.window.togroup(group.name)
                #lazy.window.togroup(group.name, switch_group=True),
                #desc = "Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
