import pythonds.basic.stack

def convert(deci):
    resto = Stack()
    while deci > 0:
        rem = deci % 2
        resto.push(rem)
        deci = deci // 2
    bin = ""
    while not resto.isEmpty():
        bin = bin + str(resto.pop())
    return bin

print("os números convertidos são 32, 57, 101 e 77")
print(convert(32), convert(57), convert(101), convert(77), sep="\n")