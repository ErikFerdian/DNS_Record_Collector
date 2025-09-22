# DNS_Record_Collector 
DNS Record Collector adalah tool sederhana berbasis Python untuk mengumpulkan berbagai record DNS (A, MX, TXT, NS) dari sebuah domain.  
Hasil query akan ditampilkan dalam format JSON yang rapi, sehingga mudah dipakai untuk analisis atau dokumentasi.
# Fitur
Mendapatkan record:
- A (alamat IP)
- MX (Mail Exchange)
- TXT (text record, misalnya SPF, verifikasi domain)
- NS (nameserver)
Hasil disimpan ke file JSON (`dns_report.json`)
Penanganan error (timeout, domain tidak ditemukan)
# Pastikan Python 3 sudah terinstall. Install dependency:
pip install dnspython
# Cara Menggunakan
Jalankan perintah berikut di terminal:
python dns_collector.py <domain>
# Contoh
python dns_collector.py google.com
# Output
<img width="1917" height="1076" alt="image" src="https://github.com/user-attachments/assets/28567856-f3fb-42b3-988c-81636814f7a6" />
# Struktur Objek
  📂 DNS_Record_Collector
   ├── dns_collector.py   # Script utama untuk query DNS
   ├── dns_report.json    # Hasil query dalam format JSON
   └── README.md          # Dokumentasi proyek
