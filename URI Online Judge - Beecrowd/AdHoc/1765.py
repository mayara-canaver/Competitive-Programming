roupas = int(input())

la, lb = list(map(int, input().split()))
sa, sb = list(map(int, input().split()))

if la <= roupas <= lb:
    if sa <= roupas <= sb:
        print("possivel")
    else:
        print("impossivel")
else:
    print("impossivel")
