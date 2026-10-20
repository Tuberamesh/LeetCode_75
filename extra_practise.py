#Kadane’s Algorithm
#problem no: 53
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        Max = nums[0]
        sum = nums[0]

        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            Max = max(sum, Max)

        return Max

#LeetCode 283 — Move Zeroes
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = []
        l = []

        for i in range(len(nums)):
            if nums[i] == 0:
                k.append(nums[i])
            else:
                l.append(nums[i])

        nums[:] = l + k




#anagram problem 242
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        s1={}
        s2={}

        for c in s:
            s1[c]=s1.get(c,0)+1

        for c1 in t:
            s2[c1]=s2.get(c1,0)+1
        
        return s1==s2


#problem 929
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        
        unique=set()

        for email in emails:

            local,domain=email.split("@")

            local=local.split("+")[0]
            local=local.replace(".","")

            unique.add(local+"@"+domain)
        
        return len(unique)