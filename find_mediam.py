# mediam_of_two_sorted_lists recive two sorted list of number (numbers_1 and numbers_2) and returns the mediam
# of the elements of theseslists. In case the total number of elements be even, the method returns 
# the smaller one of the two possibilities. The method does a binary search simultaneously on both lists,
# hence the number of steps is O(log(m)), where m = min(len(numbers_1), len(numbers_2))

# mediam_when_one_pivot_is_zero is an axuliar method to apply when the binary search made in mediam_of_two_sorted_lists 
# finish without return the result.

from datetime import datetime
from pathlib import Path

FILE_FOR_TEST = 'lists.txt'  

def convert_line_to_list(line):
    list = []
    number = ''
    for char in line:
        if char not in ['[',']',',','\n',' ']:
            number += char
        if char in [',', ']']:
            list.append(int(number))
            number =''
    return list

def mediam_for_short_lists(numbers_1, numbers_2):
    all_numbers = numbers_1 + numbers_2
    all_numbers.sort()
    if len(all_numbers) == 2:
        return all_numbers[0]
    return all_numbers[1]

def mediam_of_two_sorted_lists(numbers_1, numbers_2): 
    total_of_elements = len(numbers_1) + len(numbers_2)
    if total_of_elements <= 4:
        return mediam_for_short_lists(numbers_1, numbers_2)
        
    [smaller_list, biggest_list] = [numbers_1, numbers_2] 
    if len(numbers_1) > len(numbers_2):
        [smaller_list, biggest_list] = [numbers_2, numbers_1]

    i = len(smaller_list) // 2      
    j =  total_of_elements// 2 - i
    if total_of_elements % 2 == 0:  # to reach the smaller of the two mediam when the total # of elements is even   
        j -= 1                          
    binary_search_step_size = max((len(smaller_list) - i) // 2, 1) 

    while i > 0  and i < len(smaller_list) and j > 0:   # there is no way that j gets out of range before i reachs zero
        if smaller_list[i] >= biggest_list[j - 1] and biggest_list[j] >= smaller_list[i - 1]:
            return min(smaller_list[i], biggest_list[j])
        elif smaller_list[i] < biggest_list[j - 1]:
            i += binary_search_step_size
            j -= binary_search_step_size
        else:
            i -= binary_search_step_size
            j += binary_search_step_size
        binary_search_step_size = max(binary_search_step_size // 2, 1)

    if i == 0:
        return mediam_when_one_pivot_is_zero(smaller_list, biggest_list, j)
               
    if j == 0:
        return mediam_when_one_pivot_is_zero(biggest_list, smaller_list, i)

    return max(smaller_list[i - 1], biggest_list[j])


def mediam_when_one_pivot_is_zero(numbers_1, numbers_2, k):
    if numbers_1[0] > numbers_2[k - 1]:
        if k < len(numbers_2):
            return min(numbers_1[0], numbers_2[k])
        return numbers_1[0]                 
    return numbers_2[k - 1]  

def is_the_computed_mediam_ok(computed_mediam, numbers):
    if len(numbers) % 2 == 0:
        real_mediam = numbers[len(numbers) // 2 - 1]
    else:
        real_mediam = numbers[len(numbers) // 2] 

    if computed_mediam != real_mediam:
        print('There is something worng here!')
        print(f'The computed mediam is {computed_mediam} and the real mediam is {real_mediam}')
        return False
    return True

def test():
    if not Path(FILE_FOR_TEST).exists():
        print(f'There is no {FILE_FOR_TEST} file.')
        return False
    
    begining_of_the_test = datetime.now()
    print(f'starting the at {begining_of_the_test}')
    file = open(FILE_FOR_TEST)
    line = file.readline()
    while line != 'end':
        numbers_1 = convert_line_to_list(line)
        numbers_2 = convert_line_to_list(file.readline())
        all_numbers = convert_line_to_list(file.readline())
        computed_mediam = mediam_of_two_sorted_lists(numbers_1, numbers_2)

        if not is_the_computed_mediam_ok(computed_mediam, all_numbers):
            return False
        line = file.readline()    
    file.close()
    end_of_the_test = datetime.now()
    print(f'tests finished at {end_of_the_test}')
    return True

def main():
    numbers_1 = [5, 22, 37, 38, 42, 43, 48, 58, 69, 93]
    numbers_2 = [-94, -77, -52, -32, -8, 82]
    mediam = mediam_of_two_sorted_lists(numbers_1, numbers_2)
    
    all_numbers = numbers_1 + numbers_2
    all_numbers.sort()
    
    print('The mediam for the lits of numbers:')
    print(numbers_1)
    print('and')
    print(numbers_2)
    print(f'is {mediam}')
    print('Notice that the list with all the numbers is')
    print(all_numbers)



if __name__ == '__main__':
    main()


    

    