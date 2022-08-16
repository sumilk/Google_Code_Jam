
def print_ascii_art(n, R, C):
    print(f'Case #{n + 1}:')
    for i in range(1, 2*R +2):
        for j in range(1, 2*C+2):
            if i in [1,2] and j in [1,2]:
                print('.', end='')
            elif i % 2 == 0:
                if j % 2 == 0:
                    print('.', end='')
                else:
                    print('|', end='')
            else:
                if j % 2 == 0:
                    print('-', end='')
                else:
                    print('+', end='')
        print('')



if __name__ == '__main__':
    # with open("sample_ts1_input.txt", 'r') as input_file:
    #     n_cases = int(input_file.readline().strip())
    #
    #     for n in range(n_cases):
    #         R,C = [int(x.strip()) for x in input_file.readline().split()]
    #         print_ascii_art(n,R,C)
    n_cases = int(input())
    for n in range(n_cases):
        R,C = [int(x.strip()) for x in input().split()]
        print_ascii_art(n,R,C)

