'''
While traceling to Zortan, Louis packed lots of stuff. Let's
see if he has anything that matches your favorite color.

INFO -
-----

`match` is a new operator introduced in Python 3.10
'''

fav_color = input("Enter your favorite color:")

match fav_color.lower():
    case "black":
        print("Louis has a BLACK T-shirt")
        print("-------------------------")
    case "red":
        print("Louis has a RED car")
        print("-------------------------")
    case "yellow":
        print("Louis has a Yellow bag")
        print("-------------------------")
    case "green":
        print("Louis has a Green money")
        print("-------------------------")
    case _:
        print(f"Louis has nothing in {fav_color} color.")
        print("-------------------------")