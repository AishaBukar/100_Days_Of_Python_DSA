#  Q1 Check if an inputs parenthesis is closed

from collections import deque

def isBalanced(somevariable):
    stack=deque()
    for i in somevariable:
        if i=="(":
            stack.appendleft(i)
        elif i==")":
            if len(stack)<1 or i==stack[0]:
                return False
            else:
                stack.popleft()
    
    if len(stack)>0:
        return False
    return True

