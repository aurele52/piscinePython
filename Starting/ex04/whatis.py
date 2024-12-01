import sys as sys
if (len(sys.argv) > 1):
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
    elif (not (sys.argv[1].isdigit() or (sys.argv[1][0] == '-' and sys.argv[1][1:].isdigit()))):
        print("AssertionError: argument is not an integer")
    elif (int(sys.argv[1]) % 2):
        print("I'm Odd.")
    elif (not int(sys.argv[1]) % 2):
        print("I'm Even.")
