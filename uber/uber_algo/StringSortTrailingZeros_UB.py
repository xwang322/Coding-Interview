/*
* 字母string+数字string组合string数组排序
* 用回归式split后compare，数字头0要去除...
* Arrays.sort(myComparator) 秒...
**/
def AlNumSortTrailingZero(string):
    list = sorted(string)
    while list and list[0] == '0':
        list.pop(0)
    return ''.join(list)

answer = AlNumSortTrailingZero('01hAOEPC320lcnsl3l2')
print answer
