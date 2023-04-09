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


OPERATIONS = ('+', '-', '*', '/','(', ')', '^', '%', 'log', 'len', 'sqrt', 'sin', 'cos', 'tan')
BINARY_OPERATIONS = ('+', '-', '*', '/', '^', '%')
UNITARY_OPERATIONS = ('log', 'len', 'sqrt', 'sin', 'cos', 'tan')
PARENTHESIS = ('(', ')')

def calculator(expression):
    tree = built_binary_tree(string_to_list(expression))
    result = compute(tree)
    return result

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

def include_number(list_expression, number):
    last_element_in_expression = last_element(list_expression) 
    if len(number) > 0: 
        if last_element_in_expression == ')':
            list_expression.append('*')
        list_expression.append(float(number))

def include_operation(list_expression, operation):
    last_item_inserted = last_element(list_expression)
    if operation == '(':
        if last_item_inserted in ('(', ''):
            list_expression += [1,'*', '(']
        elif last_item_inserted in OPERATIONS:
            list_expression.append('(')
        else: 
            list_expression += ['*','(']
    else:
        list_expression.append(operation)

def last_element(list_expression):
    if len(list_expression):
        return list_expression[len(list_expression) - 1]
    return ''

def built_binary_tree(arithmetric_expression_list):
    [root, last_added] = [None, None] 
    stack = []
    for item in arithmetric_expression_list:
        new_node = Binary_Tree(item)
        if item in PARENTHESIS:
            [root, last_added, stack] = resolve_parenthesis(item, stack, root, last_added)
        elif item in BINARY_OPERATIONS:
            if item == '+' or item == '-':
                root = set_left_child(new_node, root)
                last_added = root
            else:
                if root == last_added:
                    root = new_node
                else:
                    set_right_child(last_added.parent, new_node)
                last_added = set_left_child(new_node, last_added)
        else:
            if root == None:
                [root, last_added] = [new_node, new_node]
            else:
                set_right_child(last_added, new_node)
                if last_added.value != '^': last_added = new_node
    return root

def resolve_parenthesis(item, stack, root, last_added):
    if item == '(':
        stack.append(root)
        stack.append(last_added)
        [root, last_added] = [None, None]
    else:
        node = stack.pop()
        node.right_child = root
        root.parent = node
        last_added = root
        root = stack.pop()
    return [root, last_added, stack]

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
    else:
        return root.value

def main():
    s = input('Enter the expression to compute: ')
    result = calculator(s)
    print(result)

if __name__ == '__main__':
    main()