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


OPERATIONS = ('+', '-', '*', '/', '^','(', ')')

def calculator(expression):
    list_expression = string_to_list(expression)
    tree = built_binary_tree_to_compute(list_expression)
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
    last_element_in_expression = last_element(list_expression)
    if operation == '(':
        if last_element_in_expression in ('(', ''):
            list_expression += [1,'*', '(']
        elif last_element_in_expression in OPERATIONS:
            list_expression.append('(')
        else: 
            list_expression += ['*','(']
    else:
        list_expression.append(operation)

def last_element(list):
    if len(list):
        return list[len(list) - 1]
    return ''

def built_binary_tree_to_compute(arithmetric_expression):
    root = None
    last_added = root
    stack = []
    for i in range(0, len(arithmetric_expression)):
        new_node = Binary_Tree(arithmetric_expression[i])
        if root == None:
            root = new_node
            last_added = new_node
        else:
            if arithmetric_expression[i] in ('*','/', '^'):
                new_node.left_child = last_added
                if root == last_added:
                    root = new_node
                else:
                    new_node.parent = last_added.parent
                    new_node.parent.right_child = new_node
                last_added.parent = new_node
                last_added = new_node
            elif arithmetric_expression[i] == '+' or arithmetric_expression[i] == '-':
                new_node.left_child = root
                root.parent = new_node
                root = new_node
                last_added = new_node
            elif arithmetric_expression[i] == '(':
                stack.append(root)
                stack.append(last_added)
                root = None
                last_added = None
            elif arithmetric_expression[i] == ')':
                last_added = root
                node = stack.pop()
                node.right_child = last_added
                last_added.parent = node
                root = stack.pop()
            else:
                last_added.right_child = new_node
                new_node.parent = last_added
                if last_added != '^':
                    last_added = new_node
    return root

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