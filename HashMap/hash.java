package HashMap;


//question no 2215
// Find the Difference of Two Arrays
//time complexity: O(n)
//space complexity: O(n)     
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        
       Set <Integer> set1=new HashSet<>();
       Set <Integer> set2=new HashSet<>();

       for(int num : nums1){

            set1.add(num);
       }

       for(int num : nums2){
            set2.add(num);
       }

       List<Integer> ans1=new ArrayList<>();
       List<Integer> ans2=new ArrayList<>();

        for(int num : set1){
            if(!set2.contains(num)){
                ans1.add(num);
            }
       }
        for(int num : set2){
            if(!set1.contains(num)){
                ans2.add(num);
            }
       }
       return Arrays.asList(ans1,ans2);

    }
}



//question no 1207
// Unique Number of Occurrences
//time complexity: O(n)
//space complexity: O(n)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count={}

        for num in arr:
            count[num]=count.get(num,0)+1

        frequency=set()

        for n in count.values():
            if n in frequency:
                return False
            frequency.add(n)
        return True



//question no 1657
// Determine if Two Strings Are Close
//time complexity: O(n)
//space complexity: O(n)
        class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        
        if len(word1) != len(word2):
            return False

        count1 = {}
        count2 = {}

        
        for ch in word1:
            count1[ch] = count1.get(ch, 0) + 1

        for ch in word2:
            count2[ch] = count2.get(ch, 0) + 1

      
        if set(count1.keys()) != set(count2.keys()):
            return False

        
        return sorted(count1.values()) == sorted(count2.values())