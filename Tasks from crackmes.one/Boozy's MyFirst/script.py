def script():
    for b in range(65, 127):
        if 7326 % b == 0 and 12321 % b == 0:
            a = 7326 // b
            c = 12321 // b
            if 32 <= a <= 126 and 32 <= c <= 126:
                e = (c - 100) * (b - 100)
                if 32 <= e <= 126:
                    d = e + 1
                    if 32 <= d <= 126:
                        return ''.join(chr(x) for x in [a, b, c, d, e])
    return None

result = script()
print(f"{result}")


