a = input()
b = input()
c = input()

print("".join("%s%s%s" % (a, b, c)))
print("".join("%s%s%s" % (b, c, a)))
print("".join("%s%s%s" % (c, a, b)))

print("".join("%s%s%s" % (a[:10], b[:10], c[:10])))
