
vowel_matrix = [
    [2.3, -3.3, -0.8, 1.6, -1.7, -2.7, -7.2, -0.6, -3.9, -4.8, -3.9, -1.0, -1.7, -3.3, -3.9],
    [0, 2.1, -1.5, -6.6, -1.9, -3.3, -1.5, -3.4, -1.8, -2.0, -4.3, -4.6, -4.5, -3.7, -6.7],
    [0, 0, 2.2, -1.2, -1.4, -1.4, -0.6, -0.2, -1.7, -0.3, -3.0, -1.0, -0.6, -0.9, -1.5],
    [0, 0, 0, 3.1, -1.0, -3.8, -6.5, -1.1, -3.9, -4.2, -6.3, -0.3, -0.4, 1.1, -3.3],
    [0, 0, 0, 0, 3.8, -0.3, -6.0, -4.2, -5.7, -6.0, -5.7, -2.0, -2.9, -4.5, -1.4],
    [0, 0, 0, 0, 0, 2.5, -4.2, -1.1, -7.0, -1.8, -3.2, -4.3, -1.1, -5.7, -6.4],
    [0, 0, 0, 0, 0, 0, 1.9, -1.2, -1.5, 0.2, -2.1, -7.0, -4.5, -6.1, -4.3],
    [0, 0, 0, 0, 0, 0, 0, 3.9, -5.6, -1.5, -5.5, -1.6, -2.7, -1.3, -2.6],
    [0, 0, 0, 0, 0, 0, 0, 0, 2.5, -3.4, -2.7, -4.4, -4.3, -5.8, -6.5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2.0, -0.9, -7.1, 0.2, -2.2 - 3.7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.4, -4.4, -4.2, -5.8, -6.4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.8, -4.0, -2.5, -1.5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.9, 0.1, -3.7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.6, -0.5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.1],
]

consonant_matrix = [
    [4.3, -4.8, 1.1, 0.4, -5.5, 1.9, 1.9, -6.9, -0.3, -0.5, -1.6, -5.5, 0.1, -0.9, -1.6, -4.6, -1.0, -4.3, 2.3, 0.3,
     -2.5, -0.6, -1.5],
    # 23
    [0, 4.2, -1.6, -4.9, -0.3, 0.3, 0.4, 1.5, -6.8, -6.6, -2.8, -5.5, 1.1, -6.7, 0.3, 0.6, 0.9, 1.4, -6.1, -2.0, -2.5,
     -6.0, -2.6],
    # 23
    [0, 0, 2.3, -7.0, -7.6, 0.1, 0.2, -3.1, -1.7, -2.2, -2.2, -3.0, -1.8, -0.9, -9.0, -2.1, 0.2, 0.0, -0.2, 0.0, -4.6,
     -0.2, 1.2],
    [0, 0, 0, 3.5, -5.6, -5.1, -4.2, -0.4, -0.2, -2.0, -7.5, -5.6, -6.2, -1.4, -7.0, -4.8, -0.3, 1.3, 2.8, 1.1, -2.6,
     -6.0, -3.4],
    [0, 0, 0, 0, 3.4, -1.2, -4.9, -0.3, -1.5, -1.3, -3.5, -1.6, 1.1, -2.7, 1.1, 1.2, -0.9, 4.0, 0.6, -7.3, -3.2, -1.4,
     -2.9],
    [0, 0, 0, 0, 0, 4.2, 1.9, 0.0, -0.2, -1.0, -1.9, -5.7, -0.6, -0.8, -2.5, -4.9, -1.1, -4.5, 0.3, -0.3, -2.7, -0.9,
     -2.8],
    [0, 0, 0, 0, 0, 0, 5.2, -6.3, -1.5, 0.1, -0.5, -4.8, -0.2, -0.3, -0.6, 0.6, -1.1, -3.6, 1.4, 1.0, 4.1, -5.3, 0.5],
    [0, 0, 0, 0, 0, 0, 0, 2.6, -2.9, -2.1, -2.6, -1.3, 1.7, -2.1, -0.7, -0.6, 0.9, 0.5, -1.8, -3.1, -4.7, -1.0, -1.8],
    [0, 0, 0, 0, 0, 0, 0, 0, 2.8, -1.8, -1.8, -2.8, -8.1, -0.5, -2.9, -6.6, -2.9, -6.3, -1.3, -1.6, -4.5, 0.4, -1.0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2.7, 1.8, 0.7, -3.2, -1.2, -2.9, -1.1, -2.5, 0.4, -0.6, -3.7, -4.2, -0.8, -1.7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.2, 1.2, -2.5, -1.0, -2.3, -0.7, -1.5, -0.6, -1.5, -2.1, -5.1, -0.4, -2.3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.1, -6.8, -2.7, -2.3, -5.3, -3.5, -5.0, -2.1, -2.0, -3.2, 0.2, -3.9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.3, -2.0, -1.1, -0.7, 1.1, 0.9, -0.6, -7.9, -3.8, -0.7, -0.8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.8, -2.3, -0.8, -1.2, -6.1, -2.1, -2.2, -4.3, 1.7, -0.7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.6, 2.4, -1.0, 1.0, -2.4, 0.5, 0.0, 0.6, 0.6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5.2, -0.6, -4.1, -1.3, -0.2, 3.6, -5.8, -7.7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.7, 1.6, -0.9, -9.2, -5.2, 0.0, 0.7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.4, 0.5, -6.1, -2.0, -5.4, -0.6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.9, -0.4, 1.6, -1.2, -1.7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.6, 3.0, -1.3, 1.1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6.8, -3.7, -5.6],
]

if __name__ == '__main__':
    print(len(consonant_matrix))
    for row in consonant_matrix:
        print(len(row))