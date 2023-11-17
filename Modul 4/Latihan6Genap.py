def point(x, y):
    return x, y

def line_equation_of(p1, M):
    # Inner function menghitung nilai C
    def calculate_c(p1, M):
        return p1[1] - M * p1[0]

    # Menghitung nilai C dan memanggil inner function
    C = calculate_c(p1, M)

    return f"y = {M:.2f}x + {C:.2f}"

# Contoh penggunaan fungsi untuk NIM Genap (contoh: 022)
print("Persamaan Garis Yang Melalui Titik (6,-2) Dan Bergradien -2:")
print(line_equation_of(point(0, 2), 2))
