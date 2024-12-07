def prtSquare(num):  # Function to print square of the given number
    print("Square: {}\n".format(num * num))

def prtCube(num):  # Function to print cube of the given number
    print("Cube: {}\n".format(num * num * num))

import threading

def prtSquare(num):
    print("Square: {}\n".format(num * num))

def prtCube(num):
    print("Cube: {}\n".format(num * num * num))

if __name__ == "__main__":
    # Creating threads
    t1 = threading.Thread(target=prtSquare, args=(10,))
    t2 = threading.Thread(target=prtCube, args=(10,))

    # Starting thread 1
    t1.start()
    # Starting thread 2
    t2.start()

    # Wait until thread 1 is completely executed
    t1.join()
    # Wait until thread 2 is completely executed
    t2.join()

    # Both threads completely executed
    print("Done!")
