'''
* 题目是给你一个hashmap<String,Integer> China 1; US 2; Canada 3;
* 后面数字代表权重，写一个函数随机返回值，返回值得概率和权重相比配，像例子中就是China 1/6 几率，US 1/3 几率。。。
* 面试管蛮nice会一步步引导你，我分两步作，第一步，把数据改成China 1; US 3; Canada 6; 第二步就是在1-6中取个随机数回去搜索 (要求binary search)。
* 在写code的时候忘记第一步了，直接搜索了，debug了一会。
* 等完全做完(0 bug)+题目讨论还剩5分钟。就扯了下关于uber技术的问题。
*最后面试官问我recruiter有没有说我是面哪个level的，我就说我申请的general SDE，level没有具体说。可能是觉得我有experience 应该期望更高一点吧。
**/
# this one you need to use collections to Counter the appearance of each color with their ball numbers
给一个各种色球的 array，one pass，抽出一颗球，并且各个颜色出现的机率正比于该颜色的球数。很深入的讨论数据结构，时间複杂度，OO设计，测试
'''
import random
import bisect
def RandomReturnProbability(dictionary):
    if not dictionary:
        return 0
    temp_dictionary = {}
    temp = 1
    for key in sorted(dictionary.iteritems(), key=lambda x:x[1]):
        if key[1] == 1:
            temp_dictionary[key[0]] = ((temp, temp))
            temp += 1
        else:
            temp_dictionary[key[0]] = ((temp, key[1]+temp-1))
            temp += key[1]
    temp_dictionary = sorted(temp_dictionary.iteritems(), key=lambda (k,v): (v,k))
    answer = []
    range_start = [item[1][0] for item in temp_dictionary]
    trial = random.randint(1,temp-1)
    print trial
    index = bisect.bisect_left(range_start, trial)
    if index == len(temp_dictionary):
        return temp_dictionary[-1][0]
    elif trial <= range_start[index]-1:
        return temp_dictionary[index-1][0]
    return temp_dictionary[index][0]

answer = RandomReturnProbability({'China':1, 'USA':2, 'Canada':3})
print answer

'''
* 给一个function，输入是{("a",1), ("b",2), ("c",3)}这样的，
* 表示a有1个b有2个c有3个。自己定义输入的格式输出是a或b或c，按概率分布，也就是这个function调用600次，大概有100次输出a，200次b，300次
'''
import bisect
import random
def RandomReturnProbability(lists):
    if not lists:
        return -1
    dictionary = {}
    lists = sorted(lists, key=lambda x:x[1])
    boundary = 1
    for item in lists:
        if item[1] == 1:
            dictionary[item[0]] = (boundary, boundary)
            boundary += 1
        else:
            dictionary[item[0]] = (boundary, item[1]+boundary-1)
            boundary += item[1]
    dictionary_list = sorted(dictionary.iteritems(), key=lambda (k,v):(v,k))
    range_start = [item[1][0] for item in dictionary_list]
    answer = []
    trial = random.randint(1, boundary-1)
    print trial, dictionary_list
    found_index = bisect.bisect_left(range_start, trial)
    if found_index == len(dictionary_list):
        return dictionary_list[-1][0]
    elif trial <= range_start[found_index]-1:
        return dictionary_list[found_index-1][0]
    return dictionary_list[found_index][0]

answer = RandomReturnProbability([('a', 1),('b',2),('c', 3), ('d',6)])
print answer
