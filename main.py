from baca_data import baca_data
from proses import proses
from simpan import simpan_output

if __name__ == "__main__":
    data = baca_data('restoran.csv')
    hasil = proses(data)
    simpan_output(hasil, 'peringkat.csv')
    print("Selesai. Output disimpan di peringkat.csv")
