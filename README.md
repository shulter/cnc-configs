# cnc-configs
HAL for EMC2, LinuxCNC, MachineKit machines in our workshop

# Useful commands

Halmeter with indicating the current line of g-code. 0 if finished:
loadusr halmeter -s pin motion.program-line

Specify window location:
loadusr halmeter -s pin motion.program-line -g 0 500
