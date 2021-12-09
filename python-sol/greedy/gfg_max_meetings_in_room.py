
# https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/

#User function Template for python3

# ordering => end time in asc

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        arr = []
        for i in range(n):
            arr.append((start[i], end[i]))
        
        arr = sorted(arr, key = lambda x: x[1])
        pos = 0
        ans = []
        ans.append(pos)
        end_time = arr[0][1]

        for i in range(1,n):
            if arr[i][0] > end_time:
                ans.append(i)
                end_time = arr[i][1]
        return len(ans)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends