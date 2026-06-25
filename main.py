from clients import initialization
import sys


def main() -> None:
    err = initialization.init()
    if err != None:
        sys.exit(-1)
    


if __name__ == "__main__":
    main()