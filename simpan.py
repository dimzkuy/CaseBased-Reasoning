import csv

def simpan_output(hasil, file):
    hasil.sort(key=lambda x: x['skor'], reverse=True)
    top5 = hasil[:5]
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'servis', 'harga', 'skor'])
        writer.writeheader()
        for row in top5:
            writer.writerow(row)
