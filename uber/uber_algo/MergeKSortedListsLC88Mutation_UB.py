/*
* LC88 mutation, merge k sorted lists
**/
# we will not use the LC88 in-place replacement, we allocate a new large one for final output
def mergeKlists(lists, k):
    if not lists or not k:
        return []
    answer = []
    heads = [0]*k
    lengths = [len(row) for row in lists]
    while heads != lengths:
        temp_list = []
        for i in range(k):
            if heads[i] != lengths[i]:
                temp_list.append(lists[i][heads[i]])
            else:
                temp_list.append(float('inf'))
        minimum = min(temp_list)
        index = temp_list.index(minimum)
        answer.append(minimum)
        heads[index] += 1
    return answer

answer = mergeKlists([[1,3,5], [7,8], [9]], 3)
print answer
