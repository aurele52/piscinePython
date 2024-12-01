from ft_filter import ft_filter
import sys
def main():
    try:
        if (len(sys.argv) != 3):
            raise Exception("Wrong Number of Argument")
        nbr = int(sys.argv[2])
        lst = sys.argv[1].split()
        print(ft_filter(lambda x: len(x) < nbr, lst))
    except:
        print("AssertionError")

# your tests and your error handling
if __name__ == "__main__":
    main()

