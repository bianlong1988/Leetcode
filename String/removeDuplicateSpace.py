"""
"hello    word"
      i
          j
 hello word

"""
input = "     hello    word  1    "

def removeDuplicateSpace(input):
    res = ""
    i = 0
    while i < len(input):
        if input[i] != ' ':
            res = res + input[i]
            i = i + 1
        else:
            res = res + ' '
            i = i + 1
            while i < len(input) and input[i] == ' ':
                i = i + 1
    return res

def removeDuplicateSpace1(input):
    res = ""
    flag = True
    for i, v in enumerate(input):
        if v != ' ':
            res = res + v
            flag = True
        else:
            if flag:
                res = res + ' '
                flag = False
    return res


print removeDuplicateSpace1(input)