def removeEvens(k):
    potato = k
    numPopped = 0
    for i in range (0, len(potato)):
        if potato[i - numPopped] % 2  == 0 and potato [i - numPopped] != 0:
            potato.pop(i - numPopped)
            numPopped = numPopped + 1

    return potato

print (removeEvens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))