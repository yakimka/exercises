# Links:
# https://www.hackerrank.com/challenges/string-similarity
# http://codeforces.com/blog/entry/3107
def string_similarity(string):
    n = len(string)
    z = [0 for _ in range(n)]
    z[0] = n
    left = right = 0
    for i in range(1, n):
        if i > right:
            left = right = i
            while right < n and string[right - left] == string[right]:
                right +=1
            z[i] = right - left
            right -=1
        else:
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < n and string[right - left] == string[right]:
                    right += 1
                z[i] = right - left
                right -= 1
    return sum(z)
