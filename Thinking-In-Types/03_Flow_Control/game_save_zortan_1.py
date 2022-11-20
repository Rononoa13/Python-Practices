"""
Zortan is under attack!!! Thanos has arrived!
---------------------------------------------
Since Zortan is under attack, Louis calls his Avenger friends from earth.
Avengers receive his call and sends 4 avengers to save Zortan.

1. Ironman
4. Black Widow
2. Spiderman
3. Hulk

Each avenger has its attacking power and they have to fight Thanos
to save Zortan.

Avengers can attack only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill avengers and we loose the game.
"""
from typing import Final
# declare our constants
IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life: int = 1500
choice = 0
attack_num = 0

# Declare helper message
WIN_MSG: Final[str] = "You successfully save Zortan!!!"
LOOSE_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!!!"

MSG = '''
==================================================================
Zortan is under attack, choose the pairs no. that will attack Thanos.

1) Ironman and Black Widow
2) Black Widow and Spiderman
3) Spiderman and Hulk
4) Hulk and Ironman
===================================================================
'''
while True:
    # Win / Loose
    if thanos_life <= 0 and attack_num <=3:
        # win
        print(WIN_MSG)
        break
    elif attack_num >= 3:
        # loose
        print(LOOSE_MSG)
        break
    print(MSG)
    choice = int(input("Enter your pair no >>> "))

    if choice == 1:
        print("Ironman and Black Widow are attacking Thanos...")
        thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 2:
        print("Black Widow and Spiderman are attacking Thanos...")
        thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 3:
        print("Spiderman and Hulk are attacking Thanos...")
        thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 4:
        print("Hulk and Ironman are attacking Thanos...")
        thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
        attack_num = attack_num + 1
