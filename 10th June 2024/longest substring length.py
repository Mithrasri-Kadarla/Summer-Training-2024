def longest_unique_substring_length(s):
    d = {}
    max_length = 0
    start = 0

    for i in range(len(s)):
        if s[i] in d:
            start = max(start, d[s[i]] + 1)
        d[s[i]] = i
        max_length = max(max_length, i - start + 1)

    return max_length

n = "abfgresagtyuiofde"

print(longest_unique_substring_length(n))
