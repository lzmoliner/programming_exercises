"""
    To be written ...
"""
from random import randint

def inversions(numbers: list, lower_idx: int, upper_idx: int) -> int:
    """
    Returns the number of (i, j) such that:
    lower_idx <= i < j <= upper_idx and 
    numbers[j] < 2 * numbers[i]
    """
    if lower_idx == upper_idx:
        return 0
    middle_point = lower_idx + (upper_idx - lower_idx) // 2
    response = inversions(numbers, lower_idx, middle_point)
    response += inversions(numbers, middle_point + 1, upper_idx)
    response += intercale_and_count(numbers, lower_idx, middle_point, upper_idx)
    return response

def intercale_and_count(numbers: list, lower_idx: int, inner_idx: int, upper_idx: int) -> int:
    """
    To be written ...
    """
    if lower_idx == upper_idx:
        return 0
    auxiliar_array = built_auxiliar_array(numbers, lower_idx, inner_idx, upper_idx)
    number_of_inversions = 0
    i = 0
    j, k = -1, -1
    for index in range(len(auxiliar_array)):
        if auxiliar_array[i] <= auxiliar_array[j]:
            numbers[lower_idx + index] = auxiliar_array[i]
            while 2 * auxiliar_array[k] < auxiliar_array[i] and k > j:
                number_of_inversions += inner_idx - lower_idx - i + 1
                k -= 1
            i+= 1
        else:
            numbers[lower_idx + index] = auxiliar_array[j]
            j -= 1
    return number_of_inversions


def built_auxiliar_array(numbers: list, lower_idx: int, inner_idx: int, upper_idx: int) -> list:
    """
    To be written ...
    """
    first_part = numbers[lower_idx: inner_idx + 1]
    second_part = numbers[inner_idx + 1: upper_idx + 1]
    second_part.reverse()
    return first_part + second_part

def brute_force_inversions(numbers: list) -> int:
    """
    Returns the numbers of inversions comparing each pair of elements
    in numbers
    """
    response = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                if 2 * numbers[j] < numbers[i]:
                    response += 1
    return response
def test():
    """
    Test the function inversions against the function brute_force
    for list of numbers genereted randomly.
    Returns True in case the results of the two functions be equals
    over all the list of numbers tested. Otherwise return False, printing
    the first list where a dismatch was found.
    """
    numbers = []
    for i in range(200):
        numbers.append(randint(1,600))
    real_inversions = brute_force_inversions(numbers)
    candidate = inversions(numbers[:], 0, len(numbers) - 1)
    if real_inversions != candidate:
        print(numbers)
        print(f'real number of inversions: {real_inversions}')
        print(f'candidate number of inversions: {candidate}')
        return False
    return True
def main():
    """
    Call the function test
    """
    test()

if __name__ == '__main__':
    main()
