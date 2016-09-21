import sys, math, random 
# Program ran with Python 2.7.10

def partition(liste, left, right, pivotIndex):
    pivotValue = liste[pivotIndex][2] # third is the distance
    liste[pivotIndex], liste[right] = liste[right], liste[pivotIndex]
    storeIndex = left

    for i in range(left, right):
        if liste[i][2] < pivotValue:
            liste[storeIndex], liste[i] = liste[i], liste[storeIndex]
            storeIndex += 1 
    
    liste[right], liste[storeIndex] = liste[storeIndex], liste[right]
    return storeIndex

def select(liste, left, right, n):
    while True:
        pivotIndex = random.randint(left, right)
        pivotNewIndex = partition(liste, left, right, pivotIndex)
        pivotDist = pivotNewIndex - left

        if pivotDist == n:
            return liste[pivotNewIndex]
        elif n < pivotDist:
            right = pivotNewIndex - 1
        else:
            n -= pivotDist + 1
            left = pivotNewIndex + 1
def main(): 
    will_x, will_y = map(int,sys.stdin.readline().split())

    K = input()
    N = input()

    babes = []
    for i in range(N):
        x, y = map(int,sys.stdin.readline().split())
        
        # Use pyth theorem to compute distance 
        z = math.sqrt( math.pow(abs(x - will_x), 2 ) + math.pow(abs(y - will_y), 2))
        
        babes.append((x,y,z))

    for i in range(K):
        printVal = select(babes, 0, N-1, i)
        print printVal[0], printVal[1] 
main()
