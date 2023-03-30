from random import randint

# given two arrays x = [x[0],..,x[n - 1]] and y = [y[0],..,y[m - 1]], max_len_subsequence_matrix returns 
# a (n + 1)X(m + 1) matix c such that, c[i][j] is the lenght of the maximal of a common subsequence in the arrasys 
# [x[i],..,x[n]] and [y[j],..,y[m]] for 0 <= i <= n - 1 , 0 <= j <= m - 1
# and for c[n,j] = c[i,m] = 0 for all 1 <= i <= n , 1 <= j <= m
# The algorithm run in O(nm)

def max_len_subequence_matrix(x, y):
    c = [[]]
    for i in range(len(x) + 1):
        c.append([])
        for j in range(len(y) + 1):
            c[i].append(0)
    i = len(x) - 1
    while i >= 0:
        j = len(y) - 1
        while j >= 0:
            if x[i] == y[j]:
                c[i][j] = 1 + c[i + 1][j + 1]
            if c[i + 1][j] > c[i][j]:
                c[i][j] = c[i + 1][j]
            if c[i][j + 1] > c[i][j]:
                c[i][j] = c[i][j + 1]
            j -= 1

        i -= 1
    return c

# given two arrays x = [x[0],.., x[n-1]] and y = [y[0], .., y[m - 1]] 
# max_len_ommon_subsequence returns the lenght of a maximal common subsequence
# in the arrays x and y

def max_len_common_subsequence(x, y):
    c = max_len_subequence_matrix(x, y)
    return c[0][0]

# given two arrays x = [x[0],.., x[n-1]] and y = [y[0], .., y[m - 1]] 
# subsequence_of_len_max returns a common subsequence of maximal lenght among 
# all common subsequence in x and y

def subsequence_of_len_max(x, y):
    c = max_len_subequence_matrix(x, y)
    i = 0
    j = 0
    sub_sequence = []

    while i < len(x) and j < len(y):
        if c[i][j] == c[i + 1][j]:
            i += 1
        elif c[i][j] == c[i][j + 1]:
            j += 1
        else:
            sub_sequence.append(x[i])
            i += 1
            j += 1

    return sub_sequence

def main():
    x = []
    y = []
    for i in range(10):
        x.append(randint(1, 25))
    for i in range(8):
        y.append(randint(1, 25))
    
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'lenght of one maximal subsequence in x and y is { max_len_common_subsequence(x, y)}')
    print(f'One common subsequence of maximal lengh is {subsequence_of_len_max(x, y)}')

if  __name__ == '__main__':
    main()
