/*
* 给一个不合法的linux指令路径， 让你把他变成合法的路径，这个题可以在glassdoor他家面筋里面找到
* Given an string containing absolute or relative path, get the correct path as output. For .e.g ../var../logs should give ../logs
**/
LC 71
def simplifyPath(self, path):
    places = [p for p in path.split('/') if p !='.' and p!='']
    stack = []
    for p in places:
        if p == '..':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(p)
    return '/'+'/'.join(stack)

# '/' only join between element in a list
