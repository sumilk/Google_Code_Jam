def generate_output(printers):
    TOTAL_INK_REQUIRED = 1e6
    C = min(printers[0][0], printers[1][0], printers[2][0])
    M = min(printers[0][1], printers[1][1], printers[2][1])
    Y = min(printers[0][2], printers[1][2], printers[2][2])
    K = min(printers[0][3], printers[1][3], printers[2][3])

    sum = C + M + Y + K

    if sum < TOTAL_INK_REQUIRED:
        return 'IMPOSSIBLE'
    elif sum == TOTAL_INK_REQUIRED:
        return ' '.join([str(C), str(M), str(Y), str(K)])
    else:
        #diff = sum - TOTAL_INK_REQUIRED
        C = int(C / sum * TOTAL_INK_REQUIRED)
        M = int(M / sum * TOTAL_INK_REQUIRED)
        Y = int(Y / sum * TOTAL_INK_REQUIRED)
        K = TOTAL_INK_REQUIRED - (C + M + Y)
        # while diff > 0:
        #     C = max(C -diff//4,0)
        #     M = max(M - diff//4,0)
        #     Y = max(Y - diff//4,0)
        #     K = max(TOTAL_INK_REQUIRED - (C+M+Y),0)
        #     sum = C+M+Y+K
        #     diff = sum - TOTAL_INK_REQUIRED
        return ' '.join([str(int(C)), str(int(M)), str(int(Y)), str(int(K))])


if __name__ == '__main__':
    # with open("input.txt", 'r') as input_file:
    #     n_cases = int(input_file.readline().strip())
    #
    #     with open("output.txt", 'w') as output_file:
    #         for n in range(n_cases):
    #             printers = []
    #             printers.append([int(x) for x in input_file.readline().split()])
    #             printers.append([int(x) for x in input_file.readline().split()])
    #             printers.append([int(x) for x in input_file.readline().split()])
    #             output_file.write(f'Case #{n+1}: {generate_output(printers)}\n')

    n_cases = int(input())
    for n in range(n_cases):
        printers = []
        printers.append([int(x) for x in input().split()])
        printers.append([int(x) for x in input().split()])
        printers.append([int(x) for x in input().split()])
        print(f'Case #{n + 1}: {generate_output(printers)}')

