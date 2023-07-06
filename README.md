# Python Project 1
Membuat sistem kasir self-input
# Latar Belakang
Diperlukan (diminta) pembuatan program dimana user bisa menginput daftar belanjaan mereka sendiri, dengan ketentuan-ketentuan yang tertera pada file final project pacmann.
# Requirement
1. Pembuatan object dari class Transaction()
2. Penambahan item dengan add_item(name, amount, price)
3. koreksi item name dengan update_item_name(name, new_name)
4. koreksi quantity dengan update_item_qty(name, amount)
5. Koreksi harga dengan update_item_price(name, price)
6. Delete item dengan delete_item(name)
7. reset daftar belanja dengan reset_transaction()
8. Cek daftar belanja dengan check_order() yang dapat mengeluarkan statement belanjaan sudah benar atau ada data yang kurang
9. Apply diskon 10% if price > 500k, 8% if 500k > price > 300k, and 5% if 300k > price > 200k
# Penjelasan Code & flow
1. Transaction() -> Class, basic class, tujuannya seperti function tapi class, sehingga bisa define kelasnya on the spot, kaya misal ingin buat Makansiang = Transaction(1)
2. kode dibuat jadi dictionary agar mudah dikontrol
3. add_item dibuat untuk mengisi dictionary nya
4. Functions "update" digunakan untuk koreksi atribut item yg telah dibuat. Untuk quantity dan harga menggunakan redefining, sementara untuk nama menggunakan pop.
5. delete menggunakan del untuk hapus item dari dictionary
6. reset menggunakan redefine dan jadikan dictionary nya kosong lagi
7. Check menggunakan raise ValueError apabila ada missing value (meskipun agak redundant karena apabila kita isi add_item dengan variable kurang juga pasti akan error)
8. Check juga hitung total harga apabila tidak ada missing value dan apply diskon apabila harga melebihi requirement tertnetu
   
# Cara Menggunakan Program
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Definisikan variabel-variabel di module init_variable.py dan simpan.
3. Buka terminal dan sesuaikan lokasi direktori lokal.
4. Jalankan module python start.py di terminal.
5. Jalankan module python main.py di terminal.
6. Anda cukup menjalankan module python start.py satu kali, dan dapat menjalankan module python main.py saja setelahnya.

# Hasil Test Case
Test case bisa dilihat di video youtube terkait
https://youtu.be/3qeB0iqysk8

# Conclusion
Program ini menggunakan fitur Class dan Dictionary, dengan reset dan update mayoritas menggunakan metode redefine, yang dirasa cukup simple dan efisien untuk membuat cashier program yang diminta.
