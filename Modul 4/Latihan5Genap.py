# Membuat titik dengan koordinat (x, y)
def point(x, y):
    return x, y

# Menghitung persamaan garis lurus yang melalui dua titik
def line_equation_of(p1, p2):
    # Menghitung nilai M (gradien)
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])

    # Menghitung nilai C (konstanta)
    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

# Contoh penggunaan fungsi untuk NIM Genap (contoh: 1022)
print("Persamaan Garis Yang Melalui Titik A Dan B:")
print(line_equation_of(point(1, 0), point(2, 2)))