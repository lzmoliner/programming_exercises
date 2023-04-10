import math

class Binary_Tree():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def left_child(self):
        return self.left_child
    def right_child(self):
        return self.righ_child
    def parent(self):
        return self.parent
    def value(self):
        return self.value

    def left_child(self, node):
        self.left_child = node
    def right_child(self, node):
        self.righ_child = node
    def parent(self, node):
        self.parent = node
    def value(self, value):
        self.value = value

BINARY_OPERATIONS = ('+', '-', '*', '/', '^', '%')
UNITARY_OPERATIONS = ('log', 'ln', 'sqrt', 'sin', 'cos', 'tan')
PARENTHESIS = ('(', ')')
OPERATIONS = BINARY_OPERATIONS + UNITARY_OPERATIONS + PARENTHESIS
DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def calculator(expression):
    tree = built_binary_tree(convert_to_list(expression))
    result = compute(tree)
    return result

def convert_to_list(expression):
    number = ''
    operation = ''
    list_expression = []
    for item in expression:
        if item != ' ':
            if item in BINARY_OPERATIONS:
                number = include_number(list_expression, number)
                include_operation(list_expression, item)
            elif item in DIGITS:
                operation = include_operation(list_expression, operation)
                number += item
            else:
                number = include_number(list_expression, number)
                operation += item
    include_number(list_expression, number)
    return list_expression

def string_to_list(expression):
    number = ''
    list_expression = []
    for item in expression:
        if item != ' ':
            if item in OPERATIONS:
                include_number(list_expression, number)
                number = ''
                include_operation(list_expression, item)
            else:
                number += item
    include_number(list_expression, number)
    return list_expression

def include_number(arithmetric_expression, number):
    if len(number) > 0: 
        last_item = last_element(arithmetric_expression) 
        if last_item == ')':
            arithmetric_expression.append('*')
        arithmetric_expression.append(float(number))
    return ''

def include_operation(arithmetric_expression, operation):
    if operation != '':
        last_added = last_element(arithmetric_expression)
        if operation == '(':
            if last_added in ('(', ''):
                arithmetric_expression += [1,'*']
            elif last_added not in BINARY_OPERATIONS and last_added not in UNITARY_OPERATIONS:
                arithmetric_expression += ['*']
        elif operation in UNITARY_OPERATIONS:
            if last_added == '' or last_added == '(':
                arithmetric_expression += [1, '*']
            elif last_added == ')' or last_added not in OPERATIONS:
                arithmetric_expression.append('*')
        arithmetric_expression.append(operation)
    return ''

def last_element(arithmetric_expression):
    if len(arithmetric_expression) > 0:
        return arithmetric_expression[len(arithmetric_expression) - 1]
    return ''

def built_binary_tree(arithmetric_expression):
    [root, pivot, subtrees_stack] = [None, None, []] 
    for item in arithmetric_expression:
        new_node = Binary_Tree(item)
        if item in PARENTHESIS:
            if item == '(': [root, pivot, subtrees_stack] = create_subtree(root, pivot, subtrees_stack)
            else: [root, pivot, subtrees_stack] = conect_subtree(root, pivot, subtrees_stack)
        elif item in BINARY_OPERATIONS:
            if item in ('+', '-'):
                root = set_left_child(new_node, root)
                pivot = root
            else:
                if root == pivot: root = new_node
                else: set_right_child(pivot.parent, new_node)
                pivot = set_left_child(new_node, pivot)
        else:
            if root == None: [root, pivot] = [new_node, new_node]
            else:
                set_right_child(pivot, new_node)
                if pivot.value != '^': pivot = new_node
    return root

def create_subtree(current_root, current_pivot, subtrees_stack):
    subtrees_stack.append(current_root)
    subtrees_stack.append(current_pivot)
    return [None, None, subtrees_stack]

def conect_subtree(current_root, current_pivot, subtrees_stack):
    node = subtrees_stack.pop()
    node.right_child = current_root
    current_root.parent = node
    new_pivot = current_root
    new_root = subtrees_stack.pop()
    return [new_root, new_pivot, subtrees_stack]

def set_left_child(parent, child):
    parent.left_child = child
    child.parent = parent
    return parent 

def set_right_child(parent, child):
    parent.right_child = child
    child.parent = parent
    return parent

def compute(root):
    if root.value == '+':
        return compute(root.left_child) + compute(root.right_child)
    if root.value == '-':
        return compute(root.left_child) - compute(root.right_child)
    if root.value == '*':
        return compute(root.left_child) * compute(root.right_child)
    if root.value == '/':
        return  compute(root.left_child) / compute(root.right_child)
    if root.value == '^':
        return pow(compute(root.left_child), compute(root.right_child))
    if root.value == '%':
        return compute(root.left_child) * compute(root.right_child)/100
    if root.value == 'sin':
        return math.sin(compute(root.right_child))
    if root.value == 'cos':
        return math.cos(compute(root.right_child))
    if root.value == 'tan':
        return math.tan(compute(root.right_child))
    if root.value == 'log':
        return math.log(compute(root.right_child), 10)
    if root.value == 'ln':
        return math.log(compute(root.right_child))
    if root.value == 'sqrt':
        return math.sqrt(compute(root.right_child))
    return root.value

def main():
    s = input('Enter the expression to compute: ')
    result = calculator(s)
    print(result)    

if __name__ == '__main__':
    main()