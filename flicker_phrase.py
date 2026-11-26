import random
import os


def main():
    for i in range(100000):
        r = random.randrange(1, 6)
        if r==1:
            first()
        if r==2:
            second()
        
        os.system("clear")  # clear console

    print("I pledge allegiance to the flag.");


def first():
    print("I                               ");


def second():
    print("  pledge                        ");


def third():
    print("         allegiance             ");


def fourth():
    print("                    to the      ");


def fifth():
    print("                           flag.");


if __name__ == "__main__":
    main()