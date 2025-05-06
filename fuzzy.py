def fuzzy_servis(servis):
    rendah = max(0, min(1, (60 - servis) / 40))
    sedang = max(0, min((servis - 40) / 20, (80 - servis) / 20))
    tinggi = max(0, min(1, (servis - 60) / 40))
    return {'rendah': rendah, 'sedang': sedang, 'tinggi': tinggi}

def fuzzy_harga(harga):
    murah = max(0, min(1, (40000 - harga) / 15000))
    sedang = max(0, min((harga - 30000) / 10000, (50000 - harga) / 10000))
    mahal = max(0, min(1, (harga - 40000) / 15000))
    return {'murah': murah, 'sedang': sedang, 'mahal': mahal}
