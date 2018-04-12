class Solution(object):
    def reconstructQueue(self, people):
        heightdict = {}
        height = []
        answer = []
        for i, person in enumerate(people):
            if person[0] in heightdict:
                heightdict[person[0]] += [(person[1], i)]
            else:
                height.append(person[0])
                heightdict[person[0]] = [(person[1], i)]
        height.sort()
        for h in height[::-1]:
            heightdict[h].sort()
            for p in heightdict[h]:
                answer.insert(p[0], people[p[1]])
        return answer