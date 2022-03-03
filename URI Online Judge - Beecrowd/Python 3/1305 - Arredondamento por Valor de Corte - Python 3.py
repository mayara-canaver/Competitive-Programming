while True:
    try:

        num = input()
        cutoff = input()

        if "." not in num:
            num += "."

        num = "0" + num + "0"
        cutoff = "0" + cutoff + "0"

        num_antes_ponto, num_depois_ponto = num.split(".")
        cutoff_antes, cutoff_depois = cutoff.split(".")

        num_a, num_b = float("0." + num_depois_ponto), float("0." + cutoff_depois)
        num_antes_ponto = int(num_antes_ponto)

        if num_a - num_b > 0:
            num_antes_ponto += 1

        print(num_antes_ponto)

    except EOFError:
        break
