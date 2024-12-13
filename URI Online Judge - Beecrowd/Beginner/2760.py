while True:
    try:
        mystring = str(input())

        newstring = ""

        odd = True

        for c in mystring:
            if odd:
                newstring = newstring + c.upper()
            else:
                newstring = newstring + c.lower()

            if c != " ":
                odd = not odd

        print(newstring)
    except EOFError:
        break
