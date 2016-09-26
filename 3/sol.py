import math

def idf(T, D):
    count = 0
    for i in xrange(len(D)):
        if D[i].find(T) != -1:
            count += 1

    if count != 0:
        return math.log(len(D)/float(count), 10)
    else:
        return 0 # to avoid dividing by zero

def main():
    N = input()

    D = []
    for i in xrange(N):
       D.append(raw_input())
    T = raw_input()

    idfValue = idf(T, D)
    
    for i in xrange(len(D)):
        print (i+1), "{0:.6f}".format(D[i].count(T) * idfValue)
main()
