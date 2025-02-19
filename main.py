def segitiga_a(n):
    for row in range(1, n + 1):
        print(" " * (n - row) + "* " * row)


def segitiga_sama_sisi(n):
    for row in range(1, n + 1):
        print("* " * row)


segitiga_a(5)
segitiga_sama_sisi(5)
