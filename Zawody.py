import math
slownik = {}
results = {}
def zawody(input, output):
    input = open(input , "r+")
    if input is None:
        print("Cannot open file for write.\n")
        exit(1)
    else:
        number = 0
        n = input.readline()
        for word in n.split():
            if word.isdigit():
                number = (int(word))
        counter = 0
        if number < 0:
            print("No date")
        else:
            while number > 0:
                i = counter
                slownik.setdefault(i, [])
                results.setdefault(i, [])
                line = input.readline()
                for modif in line.split():
                    if modif.isdigit():
                        slownik[i].append(modif)
                        results[i]
                counter += 1
                number -= 1
    input.close()

    k=0
    while k < 4:
        lis={}
        lis1=[]
        j = 0
        for slowa in slownik.values():
            for s in slowa:
                lis.setdefault(j, [])
                lis[j] = s
                j += 1
        for lis in lis.values():
            ok=0
            j=0
            for slowa in slownik.values():
                if lis in slowa:
                    ok +=1
            if ok ==1:
                    lis1.append(lis)
        for li in lis1:
            for key,slowa in slownik.items():
                if li in slownik[key]:
                    results[key] = li
                    slownik[key].clear()
        k += 1
        if k == 3:
            output = open(output, "w+")
            empty = 0

            for key, result in results.items():
                if not bool(results[key]):
                    empty += 1
            if empty > 0:
                possibilities = math.factorial(empty)
                output.write("NIE \n" + str(possibilities))
                results.clear()
                slownik.clear()
            elif empty == 0:
                output.write("TAK" + "\n")
                for k, res in results.items():
                    output.write(str(results[k]) + "\n")
                results.clear()
                slownik.clear()

            output.close()



zawody("wejscie.txt", "wyjscie.txt")
zawody("wejscie1.txt", "wyjscie1.txt")
zawody("wejscie2.txt", "wyjscie2.txt")