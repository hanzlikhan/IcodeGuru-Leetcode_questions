# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         result = []
        
#         # Check each character from 'a' to 'z'
#         for char in range(ord('a'), ord('z') + 1):
#             char = chr(char)
#             min_count = float('inf')  # Start with a very high number
            
#             # Find the minimum count of the character in all words
#             for word in words:
#                 count = word.count(char)  # Count the current character in the current word
#                 min_count = min(min_count, count)  # Keep track of the smallest count
#                 if min_count == 0:
#                     break  # If the character is not in one of the words, we can skip further checking
            
#             # Add the character to the result list the required number of times
#             result.extend([char] * min_count)
        
#         return result
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
       
        if len(words) == 1:
            return words[0]

        result = []
        chars = set(words[0])
        
        for char in chars:
            frequency = min([word.count(char) for word in words])
            result += frequency * [char]

        return result