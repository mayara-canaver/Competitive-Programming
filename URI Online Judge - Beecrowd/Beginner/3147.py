h, e, a, o, w, x = list(map(int, input().split()))

bem, mal = h + e + a, o + w

if bem <= mal:
    bem += x

    if bem < mal:
        print("Sauron has returned.")
    else:
        print("Middle-earth is safe.")

else:
    print("Middle-earth is safe.")
