def numtonum(num):
    numlist = [int(x) for x in str(num)]
    romannumlist = []
    length = len(numlist) - 1
    i = len(numlist) - 1
    while i >= 0:
        print(numlist[i])
        if numlist[i] > 5:
            if numlist[i] == 9:
                romannumlist = [1 * 10**(length-i), 10 * 10**(length-i)] + romannumlist
            else:
                romannumlist = ([5 * 10**(length-i)] + ([1 * 10**(length-i)] * (numlist[i] - 5))) + romannumlist
        elif numlist[i] < 5: 
            if numlist[i] == 4:
                romannumlist = [1 * 10**(length-i), 5 * 10**(length-i)] + romannumlist
            else: 
                romannumlist = ([1 * 10**(length-i)] * numlist[i]) + romannumlist
        i -= 1
    finaloutputlist = []
    for j in romannumlist:
        if j == 1:
            finaloutputlist += ['I']
        elif j == 5:
            finaloutputlist += ['V']
        elif j == 10:
            finaloutputlist += ['X']
        elif j == 50:
            finaloutputlist += ['L']
        elif j == 100:
            finaloutputlist += ['C']
        elif j == 500: 
            finaloutputlist += ['D']
        elif j == 1000: 
            finaloutputlist += ['M']
        elif j == 5000:
            finaloutputlist += ['V̅']
        elif j == 10000:
            finaloutputlist += ['X̅']
        elif j == 50000:
            finaloutputlist += ['L̅']
        elif j == 100000:
            finaloutputlist += ['C̅']
        elif j == 500000:
            finaloutputlist += ['D̅']
        elif j == 1000000:
            finaloutputlist += ['M̅']
        else:
            finaloutputlist += ['']
    return ''.join(finaloutputlist)
