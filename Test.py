import MoveRobot

moverobot = MoveRobot.MoveRobot()


def AllZeros():
    moverobot.Test(.0,.75,0, 0,0,0,0)

def MoveX():
    moverobot.Test(.0,.75,0, .5,0,0,0)
    moverobot.Test(.0,.75,0, .75,0,0,0)
    moverobot.Test(.0,.75,0, 1,0,0,0)

def MoveY():
    moverobot.Test(.0,.75,0, 0,0.25,0,0)
    moverobot.Test(.0,.75,0, 0,0.3,0,0)
    moverobot.Test(.0,.75,0, 0,0.4,0,0)
    moverobot.Test(.0,.75,0, 0,-0.4,0,0)

def MoveZ():
    moverobot.Test(.0,.75,0, 0,0,1,0)
    moverobot.Test(.0,.75,0, 0,0,-1,0)
    moverobot.Test(.0,.75,0, 0,0,.223,0)
    moverobot.Test(.0,.75,0, 0,0,.5,0)

def MoveW():
    moverobot.Test(.0,.75,0, 0,0,1,0)
    moverobot.Test(.0,.75,0, 0,0,1,.5)
    moverobot.Test(.0,.75,0, 0,0,1,.25)
    moverobot.Test(.0,.75,0, 0,0,1,1)



#AllZeros(); #Error possible Gimble Lock?

MoveX()  #Should move?
MoveY() #Should move?
MoveZ() #Should Move?
MoveW() #Moves!



