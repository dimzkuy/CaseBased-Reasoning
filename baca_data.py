import csv

def baca_data(file):
    data = []
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        print("Header yang dibaca:", reader.fieldnames)
        for row in reader:
            data.append({
                'id': int(row['id']),
                'servis': int(row['servis']),
                'harga': float(row['harga'])
            })
    return data
