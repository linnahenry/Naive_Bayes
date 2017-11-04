import os
import csv
import numpy as np
import array
import struct
#from collections import Counter

def nbc(trainingDataFilename, testDataFilename, classLabelIndex, printTopWords):
    with open(trainingDataFilename, 'rt') as ifile:
        reader = csv.reader(ifile)
        texts = [row[7] for row in reader]

    with open(trainingDataFilename, 'rt') as ifile:
        reader = csv.reader(ifile)
        stars = [row[classLabelIndex-1] for row in reader]

    trying = texts[1]
    trying = trying.replace(".", "")
    trying = trying.replace(";", "")
    trying = trying.replace(",", "")
    trying = trying.replace("?", "")
    trying = trying.replace("!", "")
    trying = trying.replace("(", "")
    trying = trying.replace(")", "")
    trying = trying.replace("{", "")
    trying = trying.replace("}", "")
    trying = trying.replace("[", "")
    trying = trying.replace("]", "")
    trying = trying.replace("/", "")
    trying = trying.replace("-", "")
    trying = trying.replace('"', "")
    trying = trying.replace("\n", " ")
    trying = trying.replace("~", "")

    trying = trying.replace("#", "")
    trying = trying.replace("$", "")
    trying = trying.replace("*", "")
    trying = trying.replace("&", "")
    trying = trying.replace("'", "")
    trying = trying.replace("+", "")
    trying = trying.replace("%", "")
    trying = trying.replace("@", "")
    trying = trying.replace("^", "")

    trying = trying.lower()
    words = trying.split(" ")
    words.sort()

    for w in words:
        if w == "":
          words.remove("")

    wordlist=0
    itlist=0
    freq=[]
    freqwords=[]
    while wordlist != len(words):
        if not freqwords:
            freqwords.append(words[wordlist])
            #freqwords[0] = words[itlist]
            wordlist = wordlist + 1
            freq.append(1)
        else:
            if words[wordlist] == words[wordlist-1]:
                itlist = itlist + 1
                #freq[wordlist-itlist] = freq[wordlist-itlist] + 1
            else:
                x = len(freq)
                freq[x-1] = freq[x-1] + itlist
                freqwords.append(words[wordlist])
                freq.append(1)
                itlist = 0
            wordlist = wordlist + 1    
    if words[wordlist-1] == freqwords[len(freqwords)-1]:
        freq[len(freq)-1] = freq[len(freq)-1] + itlist
    else:
        freqwords.append(words[wordlist])
        freq.append(1)

    count = 0
    for i in texts:
        #print(count)
        if count==0 or count==1:
            count = count + 1
            next
        else:
            count = count + 1
            num2 = i
            num2 = num2.lower()
            num2 = num2.replace(".", "")
            num2 = num2.replace(";", "")
            num2 = num2.replace(",", "")
            num2 = num2.replace("?", "")
            num2 = num2.replace("!", "")
            num2 = num2.replace("(", "")
            num2 = num2.replace(")", "")
            num2 = num2.replace("{", "")
            num2 = num2.replace("}", "")
            num2 = num2.replace("[", "")
            num2 = num2.replace("]", "")
            num2 = num2.replace("/", "")
            num2 = num2.replace("-", "")
            num2 = num2.replace('"', "")
            #num2 = num2.replace(" quote??
            num2 = num2.replace("\n", " ")
            num2 = num2.replace("~", "")
            num2 = num2.replace("@", "")
            num2 = num2.replace("#", "")
            num2 = num2.replace("$", "")
            num2 = num2.replace("%", "")
            num2 = num2.replace("^", "")
            num2 = num2.replace("&", "")
            num2 = num2.replace("*", "")
            num2 = num2.replace("'", "")
            num2 = num2.replace("+", "")
            num2 = num2.split(" ")
            num2.sort()

            for n in num2:
                if n == "":
                    num2.remove("")
            #num2.remove("")

            inda=0
            indb=0
            while inda != len(freqwords) and indb != len(num2):
                if freqwords[inda] == num2[indb]:
                    freq[inda] = freq[inda] + 1
                    indb = indb + 1
                else:
                    if freqwords[inda] < num2[indb]:
                        if inda+1 == len(freqwords):
                            freqwords.append(num2[indb])
                            freq.append(1)
                            indb = indb + 1
                        else:
                            inda = inda + 1
                    else:
                        if inda-1==-1 or inda+1 == len(freqwords) or freqwords[inda+1] > num2[indb]:
                            freqwords.insert(inda, num2[indb])
                            freq.insert(inda, 1)
                            indb = indb + 1
                        else:
                            #if freqwords[inda+1] > num2[indb]:
                            inda=inda+1

    if freqwords[0] == "":
        freqwords.remove("")
        del freq[0]

    index = sorted(range(len(freq)), key=lambda k: freq[k])

    topwords=[]
    ch = len(texts)
    if len(freq) < 1801:
        binfeat = [[1 for x in range(len(freq) - 200)] for x in range(ch+2)]
        #why did i change columns to 196?
        for i in range(len(freq)-1-200):
            h = len(index)-201-i
            newword = freqwords[index[h]]
            topwords.append(newword)
    else:
        binfeat = [[1 for x in range(1801)] for x in range(ch+2)]
        for i in range(1801):
            h = len(index)-1-i-200
            newword = freqwords[index[h]]
            topwords.append(newword)
            
    count = 0
    rating = [1]*(len(texts)+2)
    for i in texts:
        if count == len(texts)+1:
            #rating[count]=0
            #count = count + 1
            #next
            break
        else:
            #print(count)
            num2 = i
            num2 = num2.lower()
            num2 = num2.replace(".", "")
            num2 = num2.replace(";", "")
            num2 = num2.replace(",", "")
            num2 = num2.replace("?", "")
            num2 = num2.replace("!", "")
            num2 = num2.replace("(", "")
            num2 = num2.replace(")", "")
            num2 = num2.replace("{", "")
            num2 = num2.replace("}", "")
            num2 = num2.replace("[", "")
            num2 = num2.replace("]", "")
            num2 = num2.replace("/", "")
            num2 = num2.replace("-", "")
            num2 = num2.replace('"', "")
            num2 = num2.replace("\n", " ")
            num2 = num2.replace("~", "")
            num2 = num2.replace("@", "")
            num2 = num2.replace("#", "")
            num2 = num2.replace("$", "")
            num2 = num2.replace("%", "")
            num2 = num2.replace("^", "")
            num2 = num2.replace("&", "")
            num2 = num2.replace("*", "")
            num2 = num2.replace("'", "")
            num2 = num2.replace("+", "")
            num2 = num2.split(" ")
            num2.sort()
            for j in range(len(topwords)-1):
                t = (p == topwords[j] for p in num2)
                x = sum(t)
                if x > 0:
                    #smoothing
                    binfeat[count][j] = 2
                if classLabelIndex == 7:
                    if stars[count] == '5':
                        #binfeat[count][1800] = 2
                        rating[count] = 2
                else:
                    if stars[count] != '0':
                        #binfeat[count][1800] = 2
                        rating[count] = 2
            count = count+1
            if count == len(texts):
                break
        

    #for i in range(len(binfeat[0])-1):
    #    binfeat[0][i] = 0
    #    binfeat[1][i] = 0

    posword = []
    negword = []
    posnoword =[]
    negnoword =[]

    pposgword = []
    pposgnoword = []
    pneggword = []
    pneggnoword = []
    x = np.array(binfeat)
    for i in range(len(binfeat[0])):
        #print(i)
        #bf = binfeat[i]
        #pn = binfeat[1800]
        bf = x[:,i]
        #pn = x[:,1800]
        pn = rating
        bf = np.array(bf)
        pn = np.array(pn)
    
        pw = np.logical_and(bf ==2, pn == 2)      
        posword.append(sum(pw))
        nw = np.logical_and(bf == 2, pn == 1)
        negword.append(sum(nw))
        pnw = np.logical_and(bf == 1, pn == 2)
        posnoword.append(sum(pnw))
        nnw = np.logical_and(bf == 1, pn == 1)
        negnoword.append(sum(nnw))
    
        if posword[i] == 0:
            ppw = 1.00000000/(posword[i] + negword[i] + 2.00000000)
        else:
            ppw = (0.00000000+posword[i])/(posword[i] + negword[i]+0.00000000)
        #dppw = struct.pack('d', ppw)
        pposgword.append(ppw)

        if posnoword[i] == 0:
            ppnw = 1.000000000000/(posnoword[i] + negnoword[i] + 2.000000000000)
        else:
            ppnw = (0.0000000000+posnoword[i])/(posnoword[i] + negnoword[i]+0.00000000)
        #dppnw = struct.pack('d', ppnw)
        pposgnoword.append(ppnw)

        if negword[i] == 0:
            pnw = 1.00000000000/(posword[i] + negword[i] + 2.00000000000)
        else:
            pnw = (0.00000000+negword[i])/(posword[i] + negword[i]+0.000000000)
        #dpnw = struct.pack('d', pnw)
        pneggword.append(pnw)

        if negnoword[i] == 0:
            pnnw = 1.000000000/(posnoword[i] + negnoword[i] + 2.000000000)
        else:
            pnnw = (0.000000000+negnoword[i])/(posnoword[i] + negnoword[i]+0.000000000)
        #dpnnw = struct.pack('d', pnnw)
        pneggnoword.append(pnnw)

    c = 0
    with open(testDataFilename, 'rt') as ifile:
        reader = csv.reader(ifile)
        test = [row[7] for row in reader]
    with open(testDataFilename, 'rt') as ifile:
        reader = csv.reader(ifile)
        cstar = [row[classLabelIndex-1] for row in reader]
    classify = []
    correct = []
    for w in test:
        #print(c)
        #c = c + 1
        trying = w
        trying = trying.replace(".", "")
        trying = trying.replace(";", "")
        trying = trying.replace(",", "")
        trying = trying.replace("?", "")
        trying = trying.replace("!", "")
        trying = trying.replace("(", "")
        trying = trying.replace(")", "")
        trying = trying.replace("{", "")
        trying = trying.replace("}", "")
        trying = trying.replace("[", "")
        trying = trying.replace("]", "")
        trying = trying.replace("/", "")
        trying = trying.replace("-", "")
        trying = trying.replace('"', "")
        trying = trying.replace("\n", " ")
        trying = trying.replace("~", "")
    
        trying = trying.replace("#", "")
        trying = trying.replace("$", "")
        trying = trying.replace("*", "")
        trying = trying.replace("&", "")
        trying = trying.replace("'", "")
        trying = trying.replace("+", "")
        trying = trying.replace("%", "")
        trying = trying.replace("@", "")
        trying = trying.replace("^", "")
    
        trying = trying.lower()
        words = trying.split(" ")
        words.sort()

        count = 0
        indofwords = []
    
        #ppos = struct.pack('d',1)
        #pneg = struct.pack('d',1)
        ppos = 1.000000000000000000000000
        pneg = 1.000000000000000000000000
        for j in topwords:
            if pneg < 0.2**300 or ppos < 0.2**300:
                ppos = ppos/0.2**225
                pneg = pneg/0.2**225
            if j in words:
                indofwords.append(count)
                #pos = struct.pack('d', pposgword[count])
                ppos = ppos*pposgword[count]
                #neg = struct.pack('d', pneggword[count])
                pneg = pneg*pneggword[count]
            else:
                #pos = struct.pack('d', pposgnoword[count])
                ppos = ppos*pposgnoword[count]
                #neg = struct.pack('d', pneggnoword[count])
                pneg = pneg*pneggnoword[count]
            count = count + 1
    
        if ppos > pneg:
            classify.append(1)
        else:
            classify.append(0)

        if classLabelIndex == 7:
            if cstar[c] == '5' and classify[c] == 1:
                correct.append(1)
            if cstar[c] == '5' and classify[c] == 0:
                correct.append(0)
            if cstar[c] == '1' and classify[c] == 1:
                correct.append(0)
            if cstar[c] == '1' and classify[c] == 0:
                correct.append(1)
        else:
            if cstar[c] != '0' and classify[c] == 1:
                correct.append(1)
            if cstar[c] != '0' and classify[c] == 0:
                correct.append(0)
            if cstar[c] == '0' and classify[c] == 1:
                correct.append(0)
            if cstar[c] == '0' and classify[c] ==0:
                correct.append(1)
        c = c+1

    if printTopWords == 1:
        print("WORD1 " + topwords[0] + "\n WORD2 " + topwords[1] + "\n WORD3 " + topwords[2] + "\n WORD4 " + topwords[3] + "\n WORD5 " + topwords[4] + "\n WORD6 " + topwords[5] + "\n WORD7 " + topwords[6] + "\n WORD8 " + topwords[7] + "\n WORD9 " + topwords[8] + "\n WORD10 " + topwords[9])
    print("ZERO-ONE-LOSS")
    print(1-(sum(correct)+0.00000000)/(len(correct)+0.000000000000))
    
    
        

