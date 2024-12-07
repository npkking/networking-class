address = input("IPv6 address: ").split(':')
checker = [0,0,0,0,0,0,0,0]
print()

def IPv6Shortening():  
    rule1(checker, address)
    print("Rule1 result:", end=" ")
    for i in range (8):
        if i != 7:
            print(address[i] + ":", end='')
        else:
            print(address[i])
            print()
    length, indexStart, indexEnd = rule2(checker, address)
    print("Rule2 result:", end=" ")
    flag = True
    iterator = 0
    while(flag):
        if(indexStart == 0 and iterator == 0):
            iterator = length 
            print("::", end='')
            pass
        else:
            if(address[iterator] != '' and iterator != 7):
                print(address[iterator] + ':', end='')
                iterator+=1
            elif(address[iterator] != '' and iterator == 7):
                print(address[iterator])
                iterator+=1
            elif(address[iterator] == ''):
                iterator += length
                print(':', end='')
        if iterator > 7:
            flag = False
            print()
    print("Rule3 result:", end=" ")
    rule3(checker, address)
    iterator = 0
    flag = True
    stringRes = ""
    while(flag):
        if(indexStart == 0 and iterator == 0):
            iterator = length 
            print("::", end='')
            stringRes += "::"
            pass
        else:
            if(address[iterator] != '' and iterator != 7):
                print(address[iterator] + ':', end='')
                stringRes += (address[iterator] + ":")
                iterator+=1
            elif(address[iterator] != '' and iterator == 7):
                print(address[iterator])
                stringRes += address[iterator]
                iterator+=1
            elif(address[iterator] == ''):
                iterator += length
                stringRes += ":"
                print(':', end='')
        if iterator > 7:
            flag = False
            print()
    shortLen = len(stringRes)
    ratio = shortLen/39
    shortLen = str(shortLen)
    ratio = str(ratio)
    print("Shortening ratio = " + shortLen +"/39 = " + ratio)

def rule1(checker, adress):
    for i in range(8):
        counter = 0
        index = 0
        for j in range(4):
            if address[i][j] == '0':
                counter+=1
                index+=1
            else:
                break
        if counter == 4: #all are 0 nothing happen
            checker[i] = 1
        else:
            address[i] = address[i][index:]

def rule2(checker, address):
    index = -1
    max_length = 0
    for i in range (7):
        cur_length = 0
        if checker[i] == 1:
            cur_length+=1
            for j in range (i+1, 8):
                if checker[j] == 1:
                    cur_length+=1
                else:
                    break
            if(cur_length > max_length and cur_length >= 2):
                index = i
                max_length = cur_length
    for i in range(index, index+max_length):
        address[i] = ''
        checker[i] = 0
    indexEnd = index + max_length - 1
    return max_length, index, indexEnd

def rule3(checker, address):
    for i in range (8):
        if checker[i] == 1:
            address[i] = '0'

IPv6Shortening()