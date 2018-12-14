Retrofit of Weeke BP12 Optimat

LinuxCNC uspace Debian 1kHz on Lenovo laptop, Mesa 7i80DB, Mesa 7i77

Y: STMBL V3.4, servo motor motor has a faulty tachogenerator hence the Indramat servo amp can't be used. STMBL closes loop with encoder, no need for tacho.

X, Z: Indramat TDM Analog Servo Amps

ISO30 Spindle: 0-10V VFD

Custom M Codes:
============================

REMAP= M200  modalgroup=10 ngc=m200 #iso30 dust hood down
REMAP= M201  modalgroup=10 ngc=m201 #iso30 dust hood up
REMAP= M202  modalgroup=10 ngc=m202 #iso30 down
REMAP= M203  modalgroup=10 ngc=m203 #iso30 up, HOR up

REMAP= M205  modalgroup=10 ngc=m205 #drills on
REMAP= M206  modalgroup=10 ngc=m206 #drills off

REMAP= M210  modalgroup=10 ngc=m210 #TC all up
REMAP= M211  modalgroup=10 ngc=m211 #TC all down

REMAP= M220  modalgroup=10 ngc=m220 #saw on and down
REMAP= M221  modalgroup=10 ngc=m221 #saw off and up
REMAP= M222  modalgroup=10 ngc=m222 #saw swivel to X
REMAP= M223  modalgroup=10 ngc=m223 #saw swivel to Y
REMAP= M224  modalgroup=10 ngc=m224 #saw down

REMAP= M230  modalgroup=10 ngc=m230 #reg pins and lifts back down
REMAP= M231  modalgroup=10 ngc=m231 #reg pins left up
REMAP= M232  modalgroup=10 ngc=m232 #reg pins right up
REMAP= M233  modalgroup=10 ngc=m233 #left and right lift bars up
REMAP= M235  modalgroup=10 ngc=m235 #all lift bars and reg pins up
REMAP= M236  modalgroup=10 ngc=m236 #all lift bars and reg pins down, vac power on

REMAP= M240  modalgroup=10 ngc=m240 #vac pump power on
REMAP= M241  modalgroup=10 ngc=m241 #vac pump power off


REMAP= M299  modalgroup=10 ngc=m299 #horizontal aggregate down
REMAP= M300  modalgroup=10 ngc=m300 #all drills retreat up, power off, including horizontal aggregate
#REMAP= M301  modalgroup=10 ngc=m301 #drill 1
#REMAP= M302  modalgroup=10 ngc=m302 #drill 2
#REMAP= M303  modalgroup=10 ngc=m303 #drill 3
#REMAP= M304  modalgroup=10 ngc=m304 #drill 4
#REMAP= M305  modalgroup=10 ngc=m305 #drill 5
#REMAP= M306  modalgroup=10 ngc=m306 #drill 6
#REMAP= M307  modalgroup=10 ngc=m307 #drill 7

REMAP= M250  modalgroup=10 ngc=m250 #draw bar release
REMAP= M251  modalgroup=10 ngc=m251 #draw bar clamp
REMAP= M252  modalgroup=10 ngc=m252 #draw bar 2sec tool release + clamp again




IO mapping:
============================

200..300 Inputs, ie. signals coming from the machine generated with switches, 0..24V

300..400 Outputs, switched with 24V = high

1000=< limit switches


| Con No|  Descr                            | 7177 pin                    | Con No2|
|------:|-----------------------------------|-----------------------------|-----------|
| #224 |  Saw is down                       |                             | 
| #225 |  Saw is up                         |                             | 
| #226 |                                    |                             | 
| #227 |                                    |                             | 
| #228 |                                    |                             | 
| #229 |                                    |                             | 
| #230 |                                    |                             | 
| #231 |                                    |                             | 
| #232 |                                    |                             | 
| #233 |                                    |                             | 
| #234 |                                    |                             | 
| #235 |                                    |                             | 
| #236 | Draw Bar is down                   |00                           | 7i77.0.0.input-00
| #237 | Draw Bar is up                     |01                           | 7i77.0.0.input-01
| #238 |  ISO 30 Tool present               |13                           | 7i77.0.0.input-13
| #239 |  Manual Tool Change BTN            |02                           | 7i77.0.0.input-02
| #240 |  TC Pocket#1 is up                 |07  (net tc1is-up)           | 
| #241 |  TC Pocket#2 is up                 |08                           | 
| #242 |  TC Pocket#3 is up                 |09                           | 
| #243 |  TC Pocket#4 is up                 |10                           | 
| #244 |  TC Pocket#5 is up                 |11                           | 
| #245 |  TC Pocket#6 is up                 |12                           | 
| #246 |  TC Cover closed                   |03                           | 
| #247 |  TC Cover open                     |04                           | 
| #247 |  TC Cover close BTN                |05                           | 
| #247 |  TC Cover open BTN                 |06                           | 
|      |                                    |                             | 
|      |                                    |                             | 
|      |                                    |                             | 
| #308 |  vac loop left  pneumatic valve    |0.gpio.027.out DIO38                           | 
| #309 |  vac loop right pneumatic valve    |0.gpio.027.out DIO39                           | 
| #310 |  pneumatic registration pins left  |gpio.022.out   DIO35              | 
| #311 |  pneumatic registration pins right |gpio.024.out   DIO36              | 
| #312 |  ?                                 |                             | 
| #314 |  right lifts                       |gpio.018.out                 | 
| #315 |  left lifts                        |gpio.018.out                 | 
| #316 |  ISO30+HOR up                      |15                           | 6A4  4, via relay 2K1, via #1000
| #317 |  Drill Aggregate ON                |01                           | 6A4 25, grey - gold stripes
| #318 |  Saw ON                            |00                           | 6A4 24, white - pink stripes
| #319 |  Saw Down (hold, up automatic)     |10                           | 6A4 20, pink - gold stripes
| #320 |  Saw Swivel unlock, high=unlock    |11                           | 6A4 21  white - blue stripes
| #321 |  Saw Swivel into position Y        |12                           | 6A4 22, dark blue - gold stripes
| #322 |  Saw Swivel into position X        |13                           | 6A4 23, white - red stripes
| #323 |  Horizontal Drills down            |14                           | 6A4  1, brown - red stripes
| #324 |                                    |	                          | 
| #325 |  ISO30 ON                          |01 (at VFD)                  | 6A?  1, brown - red stripes
| #326 |                                    |                             | 
| #327 |                                    |                             | 
| #328 |  ISO30 Aggregate Push Down         |03                           | 6A5 35|
| #329 |  'Flood Coolant' / Fan ISO30       |25                           | 
| #330 |  ISO30 Draw Bar + Flush Air        |02                           | 6A5 33|
| #331 |  TC All Down                       |06                           | 6A5 32, Relais 27K2|
| #332 |  TC Pocket#1 up (is up: 240)       |07                           | 6A5 13|
| #333 |  TC Pocket#2 up (is up: 241)       |                             | 6A5 31, brown?
| #334 |  TC Pocket#3 up (is up: 242)       |                             | 
| #335 |  TC Pocket#4 up (is up: 243)       |                             | 
| #336 |  TC Pocket#5 up (is up: 244)       |                             | 
| #337 |  TC Pocket#6 up (is up: 245)       |                             | 
| #338 |  TC Cover Down (Open)              |                             | 
| #339 |  TC Cover Up (Close)               |                             | 
| #340 |  ISO30 Dust Hood Down              |04                           | 6A5 4, white - ? stripes
| #341 |  ISO30 Dust Hood Up                |05                           | 6A5 25, grey - gold stripes 
|      |                                    |                             | 
| #348 |  drill down 1 (rightmost)          |16                           | 
| #349 |  drill 2 (second to right)         |17                           | 
| #350 |  drill 3                           |18                           | 
| #351 |  drill 4                           |19                           | 
| #352 |  drill 5                           |                             | 
| #353 |  drill 6                           |                             | 
| #354 |  drill 7                           |                             | 
| #355 |  drill 8                           |                             | 
| #356 |  drill ?                           |                             | 
| #363 |  drill (frontmost)                 |                             | 
| #364 |  drill (second to left)            |                             | 
| #365 |  drill (forstner,leftmost?)        |             |
|  |                             |                             | 
| #1000 |  ISO30, hor aggregate up          |15                             | 
| #1001 |  Limit X                                 | 7i77.0.0.input-21-not                            | 
| #1002 |  Limit Y                                | 7i77.0.0.input-18-not                            | 
| #1003 |  Limit Z                                 | 7i77.0.0.input-22-not                            | 
| #1004 |  ISO30 through spindle air        |                             | 
| #1005 |  ISO30 draw bar release tool      |                             | 

| # |  vac pump power      | gpio.026.out                            | 
| # |  net.coolant-flood   | gpio.025.out                            | 