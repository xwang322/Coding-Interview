/*
* Find the longest palindrome in a string.
**/
# This code is actually interviewed in Sumo Logic interview, but takes too much time
def findLongestPalindrome(string):
    if not string:
        return 0
    answer = [0 * i for i in range(len(string))]
    if len(string) == 1:
        return string
    for i in range(len(string)-1):
        head = i
        j = len(string)-1
        step = 0
        while i < j:
            while i< j and string[j] != string[i]:
                j -= 1
            temp = j
            while i < j and string[i] == string[j]:
                i += 1
                j -= 1
                step += 2
            if i == j:
                step += 1
                answer[head] = step
                break
            elif j+1 == i:
                answer[head] = step
                break
            else:
                step = 0
                j = temp-1
                i = head
            answer[head] = step
    return string[answer.index(max(answer)):answer.index(max(answer))+max(answer)]

answer = findLongestPalindrome('eddabbbebbbade')
print answer
