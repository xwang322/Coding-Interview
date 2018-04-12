/*
* Given a positive integer target, count all the combinations of contiguous positive
* integers that sum up to the target.
* For Example,
* target = 15
* return 3
* since
* 15 = 4 + 5 + 6
* 15 = 1 + 2 + 3 + 4 + 5
* 15 = 7 + 8
* */
def numofComb(num):
    if num <= 0:
        return 0
    count = 0
    k = 2
    while k*(k-1)/2 < num:
        if (num-k*(k-1)/2)%k == 0:
            count += 1
        k += 1
    return count
