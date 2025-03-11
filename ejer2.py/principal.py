from Gales import Gales
from Spencer import Spencer
from Middleton import Middleton
from Windsor import Windsor

def main():
    carlos = Gales("Carlos")
    diana = Spencer("Diana")
    guillermo = Gales("Guillermo")
    kate = Middleton("Kate")

    print(carlos)
    print(diana)
    print(guillermo)
    print(kate)

if __name__ == "__main__":
    main()