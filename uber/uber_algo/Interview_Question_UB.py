## Given a nested list of integers A = [1, [2], [[3], 4], 5]
## write a flatten function, flatten(A) => [1, 2, 3, 4, 5]
# [1, [2]]
import collections
class FlattenInteger(object):
    def __init__(self, nestedList):
        self.queue = collections.deque()
        for element in nestedList:
            if isinstance(element, int):
                self.queue.append(element)
            else:
                nextlist = FlattenInteger(element)
                while nextlist.hasNext():
                    self.queue.append(nextlist.next())

    def hasNext(self):
        if self.queue:
            return True
        return False

    def next(self):
        return self.queue.popleft()

print FlattenInteger([1, [2], [[3], 4], 5]).queue
# Then the interview said not to use class, so.....
def flatten(list):
    if not list:
        return []
    queue = []
    for element in list:
        if isinstance(element, int):
            queue.append(element)
        else:
            nextlist = flatten(element)
            while nextlist:
                queue.append(nextlist.pop(0))
    return queue

answer = flatten([1, [2], [[3], 4], 5])
print answer
# The the interview gives a deadloop case, asking what to do, I am thinking using dict to prevent, but up to 45 minutes, failed to finish
# A = [1, [2], [A], [[3], 4], 5]
# flatten(A) => [1, 2, 3, 4, 5]
# This is what I wrote during the interview, not able to make it working
def flattenitself(list, dictionary):
    print list
    if tuple(list) in dictionary and dictionary[tuple(list)]:
        return []
    dictionary[tuple(list)] = True
    #print dictionary
    if not list:
        return []
    queue = []
    for element in list:
        if isinstance(element, int):
            queue.append(element)
            dictionary[tuple(element)] = True
        else:
            nextlist = flatten1(element, dictionary)
            while nextlist:
                queue.append(nextlist.pop(0))
    print queue
    return queue

#FlattenInteger([1, [2], [[3], 4], 5])
A = [1, [2], [[3], 4], 5]
A.append([A])
flatten1(A, {})

# After study one whole night, here comes with a solution, but this limits the repetion to more than 2 times, you cannot tell if this is infinite repetition or several times repetitions
def flattenitself(list, dictionary, level):
    if not list:
        return []
    queue = []
    level += 1
    for element in list:
        if isinstance(element, int):
            if element not in dictionary or dictionary[element][1] == False:
                queue.append(element)
                if element not in dictionary:
                    dictionary[element] = (level, False)
                else:
                    dictionary[element] = (level, True)
            else:
                break
        else:
            nextlist = flattenitself(element, dictionary, level)
            while nextlist:
                queue.append(nextlist.pop(0))
    return queue

#A = [1, [2], [[3], 4], 1, [2], [[3], 4], 1, [2], [[3], 4]]
A = [1, [2], [[3], 4]]
A.append(A)
answer = flattenitself(A, {}, 0)
print answer[:len(answer)/2]
