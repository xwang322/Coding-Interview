/*
* Given a String contains of '(' and ')'
* and an integer k represent the maximum time of replacement
* replacement operation : replace ')' with '()'
* calculate whether can make it balanced
* 第一题是括号匹配，function signature是 int[] balanceOrnot(String[] strs, int[] maxReplacement), strs[i] 对应的是一个像“<<>>>>”这样字符串, 函数判断strs 是否可以通过maxReplaement次的替换，变成括号匹配的形式。注意替换的规则是 >可以替换为<>, 这样就匹配了。但是 <无法替换为<>。函数返回一个数组，数组代表strs能否被成功替换。
**/
def validParenthesis(self, lists, number):
    if not lists:
      return True
    stack = []
    count = 0
     for each in lists:
     if each == ‘<’:
           stack.append(each)
     elif each == ‘>’:
          if not stack:
                     count += 1
      else:
         stack.pop()
     if not stack and count <= number:
    return True
     return False
