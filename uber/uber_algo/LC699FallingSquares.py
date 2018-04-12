class Solution(object):
    def fallingSquares(self, positions):
        answer = []
        dictionary = {}
        for position in positions:
            left = position[0]
            right = left+position[1]-1
            overlap = []
            for key in dictionary.keys():
                if key[0] > right or key[1] < left:
                    pass
                else:
                    overlap.append(key)
            if len(overlap) == 0:
                height = position[1]
            else:
                height = max(dictionary[key] for key in overlap) + position[1]
            dictionary[(left, right)] = height
            if not answer:
                answer.append(height)
            else:
                answer.append(max(dictionary.values()))
        return answer
                