n = len(s)
lgS = 0
left = 0
seen = set()
for right in range(len(s)):
    if s[right] not in seen:
        seen.add(s[right])
        lgS = max(lgS,((right-left)+1))
    else:
        while s[right] in seen:
            seen.remove()
            left+= 1