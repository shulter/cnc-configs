# ~ W = root_window.tk.call


##########################################################################################
##########     MODIFYING AXIS KEYBINDING MADE EASY BUT NOT TOO EASY   ##########
##########################################################################################


###   this file goes into the same folder as your config
###     add this line to your ini file, under the display section (without the #)
###     USER_COMMAND_FILE = usercommand_keybind.py

###   unbind a key first (if needed), then rebind  to your new thing, for example
###         the down key is unbound
#######    root_window.unbind('<Down>')
#          then rebind it to your new command
#          root_window.bind('<Down>', select_next)

####   this is for binding axis jog keys , the number at the end is the joint
#   bind right and left keys to joint 0, usually x
#   bind_axis("Right", "Left", 0)
#   bind down and up keys to joint 1, usually y
#   bind_axis("Down", "Up", 1)


#####   example for a user on the forum doing jog things

root_window.unbind("9")
root_window.unbind("0")
bind_axis("9", "0", 4)
