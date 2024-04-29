class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        
        for x in strs:
            sorted_word = sorted(x)
            word = ''.join(sorted_word)
            mp[word].append(x)
        
        ans = []
        for group in mp.values():
            ans.append(group)
        
        return ans
    
#     Initialize an empty defaultdict mp to store groups of anagrams.
# For each string x in strs:
# Current x: "eat"
# Sort the characters of x: "aet"
# Convert the sorted characters back to a string: "aet"
# Add the original string x to the list associated with the key "aet" in the dictionary mp.
# Repeat this process for all strings in strs.
# mp now contains groups of anagrams, where keys are the sorted strings and values are lists of original strings.
# Initialize an empty list ans to store the grouped anagrams.
# For each value (list of strings) group in mp.values():
# Append group to the list ans.
# Return ans as the final result.