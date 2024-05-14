class Solution:
    def isValid(self, s):
        if len(s) < 3:
            return False
        
        vowels = 0
        consonants = 0
        
        for c in s:
            if c.isalpha():
                if c.lower() in 'aeiou':
                    vowels += 1
                else:
                    consonants += 1
            elif not c.isdigit():
                return False  # Invalid character        if not a letter or digit
        
        return vowels >= 1 and consonants >= 1
