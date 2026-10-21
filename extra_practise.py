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

#problem 819
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        
        words=re.findall(r"[a-z]+", paragraph.lower())
        banned=set(banned)
        freq={}

        for word in words:
            if word not in banned:
                freq[word]=freq.get(word,0)+1
        
        return max(freq, key=freq.get)


#problem 151
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


#problem 1
#time complexity: O(n^2)
#space complexity: O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

        return []