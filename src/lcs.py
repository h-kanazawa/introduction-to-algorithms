# -*- coding: utf-8 -*-


def lcs_length(x, y):
    """
    15.4
    Longest Common Subsequence
    """
    m = len(x)
    n = len(y)
    b = [[0 for i in range(n)] for j in range(m)]
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i - 1][j - 1] = '\\'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i - 1][j - 1] = '|'
            else:
                c[i][j] = c[i][j - 1]
                b[i - 1][j - 1] = '-'
    return (c, b)


def print_lcs(b, x, i, j):
    if i == 0 or j == 0:
        return
    if b[i - 1][j - 1] == '\\':
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1], end=' ')
    elif b[i - 1][j - 1] == '|':
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)


if __name__ == '__main__':
    x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    y = ['B', 'D', 'C', 'A', 'B', 'A']
    (c, b) = lcs_length(x, y)

    print('--- c ---')
    for a in c:
        print(a)

    print('--- b ---')
    for a in b:
        ''.join(a)
        print(''.join(a))

    print('--- lcs ---')
    print_lcs(b, x, len(x), len(y))
