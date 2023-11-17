import math

def create_point(x, y):
    # inner untuk membuat titik dengan koordinat (x, y)
    def point():
        return x, y
    return point

def translasi(tx, ty):
    # Menghitung translasi
    def transform(point):
        x, y = point()
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return transform

def dilatasi(sx, sy):
    # Menghitung dilatasi
    def transform(point):
        x, y = point()
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return transform

def rotasi(degrees):
    # Menghitung rotasi
    radians = math.radians(degrees)
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)

    def transform(point):
        x, y = point()
        new_x = x * cos_theta - y * sin_theta
        new_y = x * sin_theta + y * cos_theta
        return new_x, new_y
    return transform

# Contoh kasus
initial_point = create_point(3, 5)

# Translasi
translasi_func = translasi(2, -1)
translasi_result = translasi_func(initial_point)
print("Koordinat setelah translasi:", translasi_result)

# Dilatasi
dilatasi_func = dilatasi(2, -1)
dilatasi_result = dilatasi_func(initial_point)
print("Koordinat setelah dilatasi:", dilatasi_result)

# Rotasi
rotasi_func = rotasi(30)
rotasi_result = rotasi_func(initial_point)
print("Koordinat setelah rotasi:", rotasi_result)