from random import randint

def max_len_subequence_matrix(sequence_1, sequence_2):
    c = [[]]
    for i in range(len(sequence_1) + 1):
        c.append([])
        for j in range(len(sequence_2) + 1):
            c[i].append(0)
    i = len(sequence_1) - 1
    while i >= 0:
        j = len(sequence_2) - 1
        while j >= 0:
            if sequence_1[i] == sequence_2[j]:
                c[i][j] = 1 + c[i + 1][j + 1]
            if c[i + 1][j] > c[i][j]:
                c[i][j] = c[i + 1][j]
            if c[i][j + 1] > c[i][j]:
                c[i][j] = c[i][j + 1]
            j -= 1

        i -= 1
    return c

def max_len_common_subsequence(sequence_1, sequence_2):
    c = max_len_subequence_matrix(sequence_1, sequence_2)
    return c[0][0]

def subsequence_of_len_max(sequence_1, sequence_2):
    c = max_len_subequence_matrix(sequence_1, sequence_2)
    i = 0
    j = 0
    sub_sequence = []

    while i < len(sequence_1) and j < len(sequence_2):
        if c[i][j] == c[i + 1][j]:
            i += 1
        elif c[i][j] == c[i][j + 1]:
            j += 1
        else:
            sub_sequence.append(sequence_1[i])
            i += 1
            j += 1

    return sub_sequence

def main():
    sequence_1 = []
    sequence_2 = []
    for i in range(10):
        sequence_1.append(randint(1, 25))
    for i in range(8):
        sequence_2.append(randint(1, 25))
    
    print(f'sequence_1 = {sequence_1}')
    print(f'sequence_2 = {sequence_2}')
    print('lenght of one maximal subsequence in sequence_1 and sequence_2 is:')
    print(max_len_common_subsequence(sequence_1, sequence_2))
    print('One common subsequence of maximal lengh is:')
    print(subsequence_of_len_max(sequence_1, sequence_2))

if  __name__ == '__main__':
    main()
