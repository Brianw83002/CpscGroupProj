
# Stack is printed with quotes like ['$', 'Q', 'R']
# Output matches assignment style.

TAB = {
    ('E', 'a'): ['T','Q'],
    ('E', '('): ['T','Q'],
    ('Q', '+'): ['+','T','Q'],
    ('Q', '-'): ['-','T','Q'],
    ('Q', ')'): [],
    ('Q', '$'): [],
    ('T', 'a'): ['F','R'],
    ('T', '('): ['F','R'],
    ('R', '*'): ['*','F','R'],
    ('R', '/'): ['/','F','R'],
    ('R', '+'): [],
    ('R', '-'): [],
    ('R', ')'): [],
    ('R', '$'): [],
    ('F', 'a'): ['a'],
    ('F', '('): ['(','E',')'],
}

TERMINALS = set(['a','+','-','*','/','(',')','$'])
NONTERMINALS = set(['E','Q','T','R','F'])

def tokenize(inp):
    s = inp.replace(' ', '')
    if not s.endswith('$'):
        s = s + '$'
    return list(s)

def trace_parse(input_str):
    tokens = tokenize(input_str)
    index = 0
    a = tokens[index]
    stack = ['$','E']   # bottom left, top right

    print(f"Input: {input_str}")
    print("Stack:", [str(x) for x in stack])

    accepted = False

    while stack:
        top = stack[-1]

        if top in TERMINALS:
            if top == a:
                stack.pop()
                index += 1
                if index < len(tokens):
                    a = tokens[index]
                else:
                    a = '$'
                print("Stack:", [str(x) for x in stack])
                if stack == [] and a == '$':
                    accepted = True
                    break
            else:
                break
        elif top in NONTERMINALS:
            key = (top, a)
            prod = TAB.get(key, None)
            stack.pop()
            if prod:
                for sym in reversed(prod):
                    stack.append(sym)
            print("Stack:", [str(x) for x in stack])
        else:
            break

    if accepted:
        print("Output: String is accepted / valid\n")
    else:
        print("Output: String is NOT accepted / invalid\n")


"""""""""""""""""""""""""""
MAIN
"""""""""""""""""""""""""""
if __name__ == '__main__':
    tests = [
        "(a +a)$",
        "a*(a/a)$",
        "a(a+a)$",
    ]
    for t in tests:
        print("=============================================")
        trace_parse(t)
