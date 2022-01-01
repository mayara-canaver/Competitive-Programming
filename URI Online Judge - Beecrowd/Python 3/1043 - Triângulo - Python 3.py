vezes = int(input())


for x in range(1, vezes+1):
    convert_bin, convert_hex, convert_dec = 0, 0, 0

    print("Case %d:" % x)
    caso = input().split()
    base = caso[1]
    numero = caso[0]

    if base == "bin":
        convert_dec = int(numero, 2)
        print("%d dec" % convert_dec)

        convert_hex = list(hex(convert_dec))
        convert_hex = convert_hex[2:]
        convert_hex = ''.join(convert_hex)
        print("%s hex" % convert_hex)

    if base == "dec":
        numero = int(numero)
        convert_hex = list(hex(numero))
        convert_hex = convert_hex[2:]
        convert_hex = ''.join(convert_hex)
        print("%s hex" % convert_hex)

        convert_bin = bin(numero)
        convert_bin = convert_bin[2:]
        convert_bin = ''.join(convert_bin)
        print("%s bin" % convert_bin)

    if base == "hex":
        convert_dec = int(numero, 16)
        print("%d dec" % convert_dec)

        convert_bin = list(bin(convert_dec))
        convert_bin = convert_bin[2:]
        convert_bin = ''.join(convert_bin)
        print("%s bin" % convert_bin)

    if x != (vezes+1):
        print()
