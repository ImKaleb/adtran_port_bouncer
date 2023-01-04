# Overview

This is a simple script that will build the config to bounce ports on an Adtran chassis.

## On the Adtran Chassis

Run the command:

`show table interfaces gigabit-ethernet @1/1 | i @`

This will give you similar output to below

```
giga-eth 1/0/1@1/1/9.gpon is IS and up
giga-eth 1/0/2@1/1/9.gpon is OOS-UAS and down
giga-eth 2/0/1@1/1/9.gpon is IS and up
giga-eth 2/0/2@1/1/9.gpon is IS and down
giga-eth 3/0/1@1/1/9.gpon is IS and up
giga-eth 3/0/2@1/1/9.gpon is IS and down
giga-eth 4/0/1@1/1/9.gpon is IS and up
giga-eth 4/0/2@1/1/9.gpon is IS and down
giga-eth 1/0/1@1/1/10.gpon is IS and up
giga-eth 1/0/2@1/1/10.gpon is OOS-UAS and down
giga-eth 2/0/1@1/1/10.gpon is IS and up
giga-eth 2/0/2@1/1/10.gpon is IS and down
giga-eth 3/0/1@1/1/10.gpon is IS and up
giga-eth 3/0/2@1/1/10.gpon is OOS-UAS and down
giga-eth 1/0/1@1/1/11.gpon is IS and down
giga-eth 1/0/2@1/1/11.gpon is OOS-UAS and down
giga-eth 2/0/1@1/1/11.gpon is OOS-UAS and down
giga-eth 2/0/2@1/1/11.gpon is IS and up
giga-eth 3/0/1@1/1/11.gpon is IS and up
giga-eth 3/0/2@1/1/11.gpon is IS and up
giga-eth 4/0/1@1/1/11.gpon is IS and up
giga-eth 4/0/2@1/1/11.gpon is OOS-UAS and down
giga-eth 1/0/1@1/1/12.gpon is IS and up
giga-eth 1/0/2@1/1/12.gpon is OOS-UAS and down
giga-eth 2/0/1@1/1/12.gpon is OOS-UAS and down
giga-eth 2/0/2@1/1/12.gpon is OOS-UAS and down
giga-eth 3/0/1@1/1/12.gpon is IS and up
giga-eth 3/0/2@1/1/12.gpon is OOS-UAS and down
giga-eth 4/0/1@1/1/12.gpon is IS and down
giga-eth 4/0/2@1/1/12.gpon is IS and up\
```

Copy the output of this command and save it to a .txt file

## In the main.py file

Edit line 1 with the correct filepath to the textfile you just created

`filepath = "path\to\interfaces.txt"`

Edit line 25 to have the output filepath & name that you want

`with open('path\to\output\file.txt', 'w') as f:`

## Run main.py

When you run the file it will create the file with the name/location you added into line 25 of the script

The configuration it gives should be the correct syntax to copy/paste directly into the Adtran chassis to reboot all the ports for the Card/Slot you specified in the [first command](##-On-the-Adtran-Chassis)
