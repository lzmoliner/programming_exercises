"""
calculator ...
"""
import math

class BinaryNode():
    """
     Objects of this class contains an atributte value of any type,
     and atributes left_child, righ_child, parent  also of type BinaryNode.
     It represent a node of a Binary Tree.
    """
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

BINARY_OPERATIONS = ('+', '-', '*', '/', '^', '%')
UNITARY_OPERATIONS = ('log', 'ln', 'sqrt', 'sin', 'cos', 'tan')
PARENTHESIS = ('(', ')')
SYMBOLS = BINARY_OPERATIONS + UNITARY_OPERATIONS + PARENTHESIS
DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def calculator(expression: str) -> float:
    """
    Parameters:
        expression (str): An arithmetric expression to compute
    Returns:
        The computed value of the arithmetric expression passed as parameter
    """
    arithmetric_expression = convert_to_list(expression)
    tree = create_binary_tree(arithmetric_expression)
    result = compute(tree)
    return result

def convert_to_list(expression: str) -> list:
    """
    Parameters:
        expression(str): An arithmetic expression
    Returns:
        A list that contains (separately) the numbers and operations inside the expression 
        passed as parameter
    """
    edited_expression = remove_whitespace(expression)
    number, operation, arithmetric_expression = '', '', []
    for item in edited_expression:
        if item in PARENTHESIS:
            if number != '':
                include_number(arithmetric_expression, float(number))
                number = ''
            if operation != '':
                include_operation(arithmetric_expression, operation)
                number, operation = '', ''
            include_parenthesis(arithmetric_expression, item)
        elif item in BINARY_OPERATIONS:
            if number != '':
                include_number(arithmetric_expression,float(number))
                number = ''
            include_operation(arithmetric_expression, item)
        elif item in DIGITS:
            if operation != '':
                include_operation(arithmetric_expression, operation)
                operation = ''
            number += item
        else:
            if number != '':
                include_number(arithmetric_expression, float(number))
                number = ''
            operation += item
    if number != '':
        include_number(arithmetric_expression, float(number))
    return arithmetric_expression

def remove_whitespace(expression: str) -> str:
    """
    Returns a version of the given string without whitespaces
    Parameters:
        expression (str)
    """
    result = ''
    for item in expression:
        if item !=' ':
            result += item
    return result

def include_number(arithmetric_expression: list, number: float) -> None:
    """
    Include the number into the arithmetric_expression
    Parameters:
        arithmetric_expression (list): An arithmetric espression
        number (str): A number as string
    Returns: the string '' 
    """
    last_item = give_me_the_last(arithmetric_expression)
    if last_item == ')':
        arithmetric_expression.append('*')
    arithmetric_expression.append(number)

def include_parenthesis(arithmetric_expression: list, parenthesis: str) -> None:
    """
    Include the parenthesis passed as the second parameter at the end of the 
    arithmetric expression passed in the first parameteres. Some 1 and *
    could be added before depending the last element in the arithmetric expression

    Paremeters:
        arithmetric_expression (list): An arithmetric expression
        parenthesis (str): A parenthesis
    """
    last_added = give_me_the_last(arithmetric_expression)
    if parenthesis == '(':
        if last_added in ('(', ''):
            arithmetric_expression += [1,'*']
        elif last_added not in BINARY_OPERATIONS and last_added not in UNITARY_OPERATIONS:
            arithmetric_expression += ['*']
    arithmetric_expression.append(parenthesis)

def include_operation(arithmetric_expression: list, operation: str) -> None:
    """
    Include an arithmetric operation to the end of an artihmetric expession
    Parameters:
        arithmetric_expression (list): An arithmetric expression
        operation (str): an arithmetric operation
    """
    last_added = give_me_the_last(arithmetric_expression)
    if operation == '(':
        if last_added in ('(', ''):
            arithmetric_expression += [1,'*']
        elif last_added not in BINARY_OPERATIONS and last_added not in UNITARY_OPERATIONS:
            arithmetric_expression += ['*']
    elif operation in UNITARY_OPERATIONS:
        if last_added == '' or last_added == '(':
            arithmetric_expression += [1, '*']
        elif last_added == ')' or last_added not in SYMBOLS:
            arithmetric_expression.append('*')
    arithmetric_expression.append(operation)

def give_me_the_last(some_list: list) -> str:
    """
        Returns the last element in a list. In case the list to be empty
        returns ''
        Parameteres:
            some_list (list)
    """
    if len(some_list) > 0:
        return some_list[len(some_list) - 1]
    return ''

def create_binary_tree(arithmetric_expression: list) -> BinaryNode:
    """
    Return the root of a binary tree that contains the arithmetric expression passesd as
    first parameters. The numbers are the leaf of the tree and the operations the
    internals node. 
    Parameters:
        arithmetric_expression (list): An arithmetric expression
    """
    root, pivot, subtrees_stack = None, None, []
    for item in arithmetric_expression:
        new_node = BinaryNode(item)
        if item in PARENTHESIS:
            if item == '(':
                [root, pivot, subtrees_stack] = create_subtree(root, pivot, subtrees_stack)
            else:
                [root, pivot, subtrees_stack] = conect_subtree(root, subtrees_stack)
        elif item in BINARY_OPERATIONS:
            if item in ('+', '-'):
                root = set_left_child(new_node, root)
                pivot = root
            else:
                if root == pivot:
                    root = new_node
                else:
                    set_right_child(pivot.parent, new_node)
                pivot = set_left_child(new_node, pivot)
        else:
            if root is None:
                root, pivot = new_node, new_node
            else:
                set_right_child(pivot, new_node)
                if pivot.value != '^' and pivot.value not in UNITARY_OPERATIONS:
                    pivot = new_node
    return root

def create_subtree(root: BinaryNode, pivot: BinaryNode, subtrees_stack: list) -> list:
    """
        Store in the root and the pivot ...
        Parameters:
            current_root (BinaryNode):
            current_pivot (BinaryNode):
            subtrees_stack (list):
    """
    subtrees_stack.append(root)
    subtrees_stack.append(pivot)
    return [None, None, subtrees_stack]

def conect_subtree(root: BinaryNode, subtrees_stack: list) -> list:
    """
    Rerturns a list that  contains ...
    Parameters:
        root (BinaryNode):
        subtrees_stack (list)

    """
    node = subtrees_stack.pop()
    node.right_child = root
    root.parent = node
    new_pivot = root
    new_root = subtrees_stack.pop()
    return [new_root, new_pivot, subtrees_stack]

def set_left_child(parent: BinaryNode, child: BinaryNode) -> BinaryNode:
    """
    Returns ...
    Parameters:
        parent (BinaryNode) ...
        childe (BinaryNode) ...
    """
    parent.left_child = child
    child.parent = parent
    return parent

def set_right_child(parent: BinaryNode, child: BinaryNode) -> BinaryNode:
    """
    Returns ...
    Parameters:
        parent (BinaryNode) ...
        childe (BinaryNode) ...
    """
    parent.right_child = child
    child.parent = parent
    return parent

def compute(root: BinaryNode) -> float:
    """
    Compute an arithmetric expression stored inside a Binary Tree.
    Paramteres:
        root (BinaryNode): Root of an Binary Tree.
    """
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
    """
    Input from the user an arithmetric expression to compute.
    """
    expression = input('Enter the expression to compute: ')
    result = calculator(expression)
    print(result)

if __name__ == '__main__':
    main()
