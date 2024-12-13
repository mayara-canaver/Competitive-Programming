tempo = int(input())

presentes = list(map(int, input().split()))
a, b = presentes[0], presentes[1]

if (a + b) > tempo:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")
