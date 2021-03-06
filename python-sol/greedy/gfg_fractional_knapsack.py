# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

#User function Template for python3

# ordering: value/weight asc

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        arr = sorted(Items, key = lambda x : x.value/x.weight, reverse=True)
        iw = 0
        i = 0
        pr = 0
        while iw<W and i < len(arr):
            if iw + arr[i].weight > W :
                
                pr = pr + ((W - iw) * arr[i].value/ arr[i].weight)
                break
            else:
                iw = iw + arr[i].weight
                pr = pr + arr[i].value
            i = i + 1
        return pr

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends