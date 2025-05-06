from fuzzy import fuzzy_servis, fuzzy_harga
from inferensi import inferensi, defuzzifikasi

def proses(data):
    hasil = []
    for row in data:
        servis_fz = fuzzy_servis(row['servis'])
        harga_fz = fuzzy_harga(row['harga'])
        rules = inferensi(servis_fz, harga_fz)
        skor = defuzzifikasi(rules)
        hasil.append({
            'id': row['id'],
            'servis': row['servis'],
            'harga': row['harga'],
            'skor': skor
        })
    return hasil
