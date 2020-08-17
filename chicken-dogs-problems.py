#!/usr/bin/python3

"""
This solves the problems
Total chicks and dogs is 36
!00 legs total
How many dogs and chicks
"""

def main():
    chick, dogs = 0, 0

    for i in range(0,100):
        chick = i
        dogs = 36 - chick
        legs = dogs * 4 + chick * 2
        if legs == 100:
            break
    return (chick, dogs)

if __name__ == "__main__":
    c, d = main()
    print(f"Chicken: {c}")
    print(f"Dogs: {d}")

