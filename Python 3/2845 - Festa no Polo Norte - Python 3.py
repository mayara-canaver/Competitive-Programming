from itertools import combinations

while True:
    try:
        sequencia = list(input())
        all_combinations = []

        for x in range(1, len(sequencia) + 1):
            combinations_list = list(combinations(sequencia, x))
            all_combinations += combinations_list

        all_combinations.sort()
        all_combinations_true = list(dict.fromkeys(all_combinations))

        for x in all_combinations_true:
            print("".join(map(str, x)))

    except EOFError:
        break
