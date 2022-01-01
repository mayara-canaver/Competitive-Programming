vezes = int(input())

for x in range(vezes):
    frase1, frase2 = list(input().split("mek"))
    conta_a_1 = frase1.count("a")
    conta_a_2 = frase2.count("a")

    total = conta_a_1 * conta_a_2

    print("k" + "a" * total)

