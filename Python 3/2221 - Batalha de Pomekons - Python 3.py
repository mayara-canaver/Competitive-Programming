while True:
    try:
        kage_bushin = int(input())
        count = 0

        while kage_bushin > 1:
            kage_bushin /= 2
            count += 1

        print(count)

    except EOFError:
        break
