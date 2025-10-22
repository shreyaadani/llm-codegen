def is_balanced_parentheses(expr):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in expr:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != mapping[char]:
                return False
                
    return not stack