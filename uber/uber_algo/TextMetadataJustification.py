/*
* 第一轮，给一段text和一个int limit，把text拆分成若干段，每段不能超过limit个字符，但麻烦的是最后要加一个metadata 比如（1/4）(2/4)这样的，所以要做一个估计。
* 根据limit大概估计一下需要的页数，然后预留给metadata
**/
# Based on the poster description, seems like no need to ljust the output style as LC68 requires, maybe only one space between words, but needs to keep
# the metadata information at the end of the line, so needs to consider the total line number. Based on the description, metadata is not included in the limit length
def metaJustify(words, maxWidth):
    text = ' '.join(words)+' '
    if len(text) == ' ':
        return [' '*maxWidth]
    answer = []
    while text:
        index = text.rfind(' ', 0, maxWidth+1)
        line = text[:index].split()
        answer.append(' '.join(line).ljust(maxWidth))
        text = text[index+1:]
    length = len(answer)
    final = []
    for index, each in enumerate(answer):
        final.append(each+'('+str(index+1)+'/'+str(length)+')')
    return final

answer = metaJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print answer

/*
* 短信分割 输入: 长度限制 = 20,"Hey Alice, your Uber is arriving now!" 输出: ["Hey Alice, (1/3)", "your Uber is (2/3)", "arriving now! (3/3)"]
* 要求:1) 词不能截断2) 需要返回短信的条数以及第几条，如(1/3）
**/

# another possible way is to add the metadata into the end of the output, so in this case, roughly allocate the length then adjust based on the total length
# again, this one does not consider the spacing between words, just assume one spacing is fine
# question: for line more than 10, do we output metadata like (01/10) or (1/10), this solution is for (01/10) for easy handling

# The only thing I cannot handle now is when you adjust the total number of lines from 9 to 10, then your total metadata length from 5 to 7, you have to iterally
# go through every line of code and change them, I do not think that needs to be prepared in real cases.
def metaJustifyInclude(words, maxWidth):
    text = ' '.join(words)+' '
    if len(text) == ' ':
        return [' '*maxWidth]
    answer = []
    while text:
        index = text.rfind(' ', 0, maxWidth+1)
        line = text[:index].split()
        answer.append(' '.join(line))
        text = text[index+1:]
    length = len(answer)
    metadata = 0
    if 10 <= length <= 99:
        metadata = 7
    elif 0 < length <= 9:
        metadata = 5
    final = []
    adjust_count = 0
    for line in answer:
        if len(line)+metadata > maxWidth:
            adjust_count += 1
    if not adjust_count:
        for index, line in enumerate(answer):
            final.append((line+'('+str(index+1)+'/'+str(length)+')').ljust(maxWidth))
        return final
    else:
        adjust_answer = []
        adjust_temp = ''
        i = 0
        while i <= len(answer)-1:
            if len(answer[i])+metadata <= maxWidth:
                adjust_answer.append(answer[i])
            else:
                j = len(answer[i].split())-1
                while j >= 0:
                    if len(' '.join(answer[i].split()[:j]))+metadata <= maxWidth:
                        adjust_answer.append(' '.join(answer[i].split()[:j]))
                        adjust_temp = ' '.join(answer[i].split()[j:])
                        if i != length-1:
                            answer[i+1] = adjust_temp+' '+answer[i+1]
                            adjust_temp = ''
                        else:
                            answer.append(adjust_temp)
                        break
                    j -= 1
            i += 1
        for index, line in enumerate(adjust_answer):
            final.append((line+' '*(maxWidth-len(line)-metadata)+'('+str(index+1)+'/'+str(length)+')'))
        return final

# this one will not work as justification. plus metadata will be more than 16, not working anyway
#answer = metaJustifyInclude(["This", "is", "an", "example", "of", "text", "justification."], 16)
answer = metaJustifyInclude(["This", "is", "an", "example", "of", "text", "justification."], 20)
answer = metaJustifyInclude(["Hi", "helloterran,", "your", "uber", "is", "arriving", "soon!"], 20)
print answer
