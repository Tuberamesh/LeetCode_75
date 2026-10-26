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

#problem 49
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        group={}

        for word in strs:
            key=" ".join(sorted(word))

            if key not in group:
                group[key]=[]

            group[key].append(word)

        return list(group.values())


#problem 128 longest consecutive sequence
#time complexity: O(nlogn)
#space complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        count=longest=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
            
            longest=max(longest, count)
    
        return longest


#problem 811 subdomain visit count
#time complexity: O(n)
#space complexity: O(n)
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts=defaultdict(int)

        for entry in cpdomains:
            count, domain=entry.split()
            count=int(count)

            parts=domain.split(".")

            for i in range(len(parts)):
                subdomain=".".join(parts[i:])
                counts[subdomain]+=count
            
        return [f"{count} {domain}" for domain, count in counts.items()]


#problem 146 LRU Cache
#time complexity: O(1)
#space complexity: O(n)

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
      



#problem 167 two sum II
#time complexity: O(n)
#space complexity: O(1)
    class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1

        while left<right:
            total=numbers[left]+numbers[right]

            if total==target:
                return [left+1, right+1]
            elif target > total:
                left+=1
            else:
                right-=1
            
        return []



#problem 15 three sum
#time complexity: O(n^2)
#space complexity: O(n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                   
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
  
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

#problem 283 move zeroes
#time complexity: O(n)
#space complexity: O(n)
    class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums)==0:
            return 
        if len(nums)==1:
            return
        k=[]
        l=[]
    
        for i in range(len(nums)):
            if nums[i]==0:
                k.append(nums[i])
            else:
                l.append(nums[i])
        nums[:]=l+k


#problem 125 valid palindrome
#time complexity: O(n)
#space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1

        while left<right:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1

            elif s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1
                right-=1
            
        return True