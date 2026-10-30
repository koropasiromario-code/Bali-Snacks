# Bali Snack AI — Website UMKM Jajanan Khas Bali

Website demo berbasis Python Flask dengan katalog produk, pencarian dan filter, keranjang simulasi, asisten rekomendasi berbasis aturan, serta generator caption promosi.

## Fitur
- Katalog jajanan dengan harga contoh.
- Pencarian dan filter kategori.
- Keranjang dan ringkasan total pesanan (simulasi, belum checkout sungguhan).
- Asisten lokal untuk rekomendasi jajanan dan pertanyaan sederhana.
- Generator caption promosi untuk media sosial.

## Persyaratan
- Python 3.10 atau lebih baru
- pip

## Cara menjalankan

1. Ekstrak ZIP project ini.
2. Buka terminal di folder `bali_snack_ai`.
3. Buat virtual environment (opsional tetapi disarankan):

   **Windows**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Pasang dependensi:
   ```bash
   pip install -r requirements.txt
   ```
5. Jalankan aplikasi:
   ```bash
   python app.py
   ```
6. Buka browser ke `http://127.0.0.1:5000`.

## Mengubah produk dan harga
Edit daftar `PRODUCTS` di `app.py`. Harga di kode merupakan data contoh; sesuaikan dengan harga aktual UMKM.

## Catatan tentang AI
Asisten pada versi ini adalah prototipe berbasis aturan (rule-based), bukan model bahasa generatif. Untuk menggunakan AI generatif sungguhan, integrasikan API penyedia model di sisi server, simpan API key di environment variable, tambahkan validasi input, pembatasan penggunaan, dan penanganan kesalahan. Jangan pernah menaruh API key di JavaScript frontend.

## Sebelum digunakan secara komersial
Tambahkan database, login admin, manajemen stok, ongkos kirim, validasi pesanan, kebijakan privasi, dan integrasi pembayaran/pesan yang aman. Ganti kontak dan informasi produk demo dengan data usaha yang benar.
