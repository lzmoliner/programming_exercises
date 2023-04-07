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

def string_to_expression(s):
    number = ''
    expression = []
    for letter in s:
        if letter in ('+', '-', '*', '/', '^', '(', ')'):
            if len(number) > 0: expression.append(float(number))
            number = ''
            expression.append(letter)
        else:
            if letter != ' ': number += letter
    if len(number) > 0 :
        expression.append(float(number))
    return expression

def processing_expresion(expression):
    processeced_expresion = []
    for i in range(len(expression)):
        if expression[i] == '(':
            if i == 0:
                processeced_expresion.append(1)
                processeced_expresion.append('*')
            elif expression[i - 1] not in ('+','-','/','*'):
                processeced_expresion.append('*')
        processeced_expresion.append(expression[i])
    return processeced_expresion

def calculator(string_expression):
    expression = string_to_expression(string_expression)
    expression = processing_expresion(expression)
    tree = built_data_structure_to_compute(expression)
    result = compute(tree)
    return result

def built_data_structure_to_compute(arithmetric_expression):
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
    expresion = input('Enter the expression to compute: ')
    print(calculator(expresion))


if __name__ == '__main__':
    main()