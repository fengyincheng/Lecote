
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff=[0]*(n+1)  #可以理解，但是有点难想呢。怎么让后面座位按顺序对其好，从1往后加

        for l,r,seats in bookings:
            #不懂为什么r不减一只有l减了
            diff[l-1]+=seats  # ----> 开始加
            diff[r]-=seats    #-----> 在r+1停止加

        ans=[0]*n
        ans[0]=diff[0]  #还原必要步骤，虽然我不是很懂为什么，主要是没有细致的想过
        
        # nums[0]=diff[0]
        # for i in range(1,len(nums)):
        #     nums[i]=nums[i-1]+diff[i]

        for i in range(1,n):
            ans[i]=ans[i-1] +diff[i]
        return ans

        

        diff=[0]*n
        for l,r,seats in bookings:
            diff[l-1]+=seats
            diff[r]-=seats
        #还原
        ans=[0]*n
        ans[0]=diff[0]
        for i in range(1,n):
            ans[i]=ans[i-1]+diff[i]
            