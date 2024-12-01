import sys


def main():
    main.__doc__ = "wc a string with lower, upper, space, digit, dot count"
    lower = 0
    upper = 0
    space = 0
    digit = 0
    dot = 0
    if (len(sys.argv) != 2):
        print("argv take a single string in argument")
        return -1
    elif (sys.argv[1] == ""):
        print("argv take a single string in argument")
        return -1
    for i in sys.argv[1]:
        if (i.isalpha() and not i.islower()):
            upper += 1
        elif (i.islower()):
            lower += 1
        elif (i.isdigit()):
            digit += 1
        elif (i == " "):
            space += 1
        else:
            dot += 1
    print(f"The text contains {len(sys.argv[1])} characters:\n{upper} upper letters\n{lower} lower letters\n{dot} punctuation marks\n{space} spaces\n{digit} digits")


# your tests and your error handling
if __name__ == "__main__":
    main()
    print(dir(list))

