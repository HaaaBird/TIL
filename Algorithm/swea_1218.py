# swea_1218.py
# 괄호 짝짓기

left = ['(', '[', '{', '<']
right = [')', ']', '}', '>']
b_key = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
for case in range(1, 11):
    N = int(input())
    word = input()
    d_stack = {
        '(': [],
        '[': [],
        '{': [],
        '<': []
    }
    flag = True
    for i in range(len(word)):
        if word[i] in left:
            d_stack[word[i]].append(word[i])
        elif word[i] in right:
            if len(d_stack[b_key[word[i]]]) == 0:
                flag = False
                break
            else:
                d_stack[b_key[word[i]]].pop()
    for val in d_stack.values():
        if len(val) != 0:
            flag = False
            break
    if flag:
        print(f"#{case} 1")
    else:
        print(f"#{case} 0")
