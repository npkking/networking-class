import time


def isPerfectNum(mode, n):
    if(mode == 1):
        if(PerfectCheckSimple(n)):
            print("Is perfect number")
        else:
            print("Not perfect number")

def PerfectCheckSimple(n):
    sum = 0
    for i in range (1, n):
        if(n % i == 0):
            sum += i
    if(sum == n):
        return True
    else: 
        return False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def PerfectCheckPrime(n):
    flag = True
    p = 2
    while(flag):
        if (is_prime(2**p-1)) and (2**(p-1)*(2**p - 1) == n):
            return True
        elif 2**(p-1)*(2**p - 1) > n:
            return False
        else:
            p += 1

low, high = input("Enter two positive integers: ").split()
low = int(low)
high = int(high)
print("Finding perfect numbers within " + str(low) + "~" + str(high) + ":")
print("Using simple iterative method:")
arraySIM = []
startSIM = time.time()
for i in range(low, high+ 1):
    if(PerfectCheckSimple(i)):
        arraySIM.append(i)
endSIM = time.time()
elapsedSIM = endSIM - startSIM
print(arraySIM)
countSIM = len(arraySIM)
print("Found " + str(countSIM) + " perfect numbers in " + str(elapsedSIM) + " Seconds.")
print("Using prime iterative method:")
arrayPIM = []
startPIM = time.time()
for i in range(low, high+ 1):
    if(PerfectCheckPrime(i)):
        arrayPIM.append(i)
print(arrayPIM)
endPIM = time.time()
elapsedPIM = endPIM - startPIM
countPIM = len(arrayPIM)
print("Found " + str(countPIM) + " perfect numbers in " + str(elapsedPIM) + " Seconds.")
fasterby = elapsedPIM-elapsedSIM
faster = 0 if fasterby > 0 else 1
fasterby = abs(fasterby)
if faster == 1:
    print("Prime iterative method is faster by " + str(fasterby) + " Seconds.")
else:
    print("Simple iterative method is faster by " + str(fasterby) + " Seconds.")
