# HOF
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan  # Mengembalikan fungsi inner operator

# Penggunaan HOF
fungsi_perkalian_dengan_5 = perkalian(5)
hasil = fungsi_perkalian_dengan_5(3)
print(hasil)  # Output: 15

# Currying
def curry_perkalian(a):
    def inner(b):
        return a * b
    return inner

# Penggunaan currying
fungsi_curry_perkalian_dengan_5 = curry_perkalian(5)
hasil_curry = fungsi_curry_perkalian_dengan_5(3)
print(hasil_curry)  # Output: 15
