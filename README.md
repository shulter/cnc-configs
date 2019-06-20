# cnc-configs
HAL for EMC2, LinuxCNC, MachineKit machines in our workshop

# Useful commands

Halmeter with indicating the current line of g-code. 0 if finished:
loadusr halmeter -s pin motion.program-line

Specify window location:
loadusr halmeter -s pin motion.program-line -g 0 500

Set XY max acceleration to 8000:
M100P8000


#loadrt hostmot2
#loadrt hm2_eth board_ip="192.168.42.121" config=" num_encoders=6 num_pwmgens=0 num_stepgens=0 sserial_port_0=000xxx"
#loadrt threads
#addf hm2_7i92.0.read thread1
#addf hm2_7i92.0.write thread1 
#start
