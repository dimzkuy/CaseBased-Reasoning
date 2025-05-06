def inferensi(servis_fuzzy, harga_fuzzy):
    aturan = [
        ('tinggi', 'murah', 90),
        ('tinggi', 'sedang', 80),
        ('tinggi', 'mahal', 60),
        ('sedang', 'murah', 80),
        ('sedang', 'sedang', 60),
        ('sedang', 'mahal', 40),
        ('rendah', 'murah', 50),
        ('rendah', 'sedang', 30),
        ('rendah', 'mahal', 10)
    ]
    rules = []
    for s, h, nilai in aturan:
        alpha = min(servis_fuzzy[s], harga_fuzzy[h])
        rules.append((alpha, nilai))
    return rules

def defuzzifikasi(rules):
    atas = sum(alpha * z for alpha, z in rules)
    bawah = sum(alpha for alpha, _ in rules)
    return atas / bawah if bawah != 0 else 0
