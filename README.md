# 🤖 WASAPOTP Notif

<p align="center">
  <b>⚡ Auto War OTP Telegram Bot</b>
  <br>
  Otomatisasi pemantauan pesan, pemilihan layanan, dan konfirmasi pesanan menggunakan Telethon.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Telegram-Telethon-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Active-2ea44f?style=for-the-badge">
</p>

---

## 📖 About

**WASAPOTP Notif** adalah bot otomatisasi Telegram berbasis **Python + Telethon** yang dirancang untuk membantu proses **"war OTP"** dari penyedia layanan. **Pastikan saldo anda cukup sebelum memulai war!**

Program memantau pesan Telegram secara real-time dan secara otomatis menjalankan serangkaian aksi ketika nomor baru tersedia.

Mulai dari mendeteksi pesan, mengirim perintah layanan, memilih layanan yang diinginkan, menentukan jumlah pesanan, hingga melakukan konfirmasi — semuanya dapat dilakukan secara otomatis berdasarkan konfigurasi yang telah ditentukan.

> ⚡ **Tujuan utama:** meminimalkan waktu respons dan mengurangi interaksi manual ketika nomor tersedia.

---

## ✨ Features

### 🔎 Automatic Detection

Memantau pesan dari bot target secara real-time dan mendeteksi pesan yang mengandung keyword:

```text
nomor baru
```

### ⚡ Instant Response

Ketika pesan yang sesuai terdeteksi, program langsung mengirim:

```text
/layanan
```

tanpa perlu melakukan input secara manual.

### 🖱️ Automatic Button Interaction

Program dapat berinteraksi dengan **Telegram Inline Keyboard** secara otomatis:

```text
Nomor Baru
    ↓
/layanan
    ↓
Pilih Layanan
    ↓
Pilih Jumlah
    ↓
Konfirmasi
```

### 🎯 Configurable Service

Layanan yang dipilih dapat ditentukan melalui `config.json`.

Contoh:

```json
"layanan": "shopee"
```

### 🔢 Configurable Order Quantity

Jumlah pesanan juga dapat dikonfigurasi:

```json
"jumlah_pesanan": 2
```

Program akan menyesuaikannya dengan format tombol:

```text
2 → 2x
```

### ⚙️ Centralized Configuration

Tidak perlu mengubah source code setiap kali ingin mengganti target bot, layanan, atau jumlah pesanan.

Semua dapat dikontrol melalui:

```text
config.json
```

### 🔐 Persistent Telegram Session

Setelah login pertama kali, Telethon menyimpan session secara lokal sehingga program dapat digunakan kembali tanpa harus login dari awal.

---

# 🔄 Workflow

```text
┌─────────────────────────┐
│     Telegram Bot        │
│  Mengirim nomor baru    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Message Monitoring    │
│   Detect "nomor baru"   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      /layanan           │
│     Auto Response       │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Select Service       │
│       "shopee"          │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     Select Quantity     │
│          "2x"           │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Confirm           │
└─────────────────────────┘
```

---

# 🧰 Requirements

Sebelum menjalankan program, pastikan sudah tersedia:

* 🐍 Python **3.7 atau lebih baru**
* 📱 Akun Telegram
* 🔑 Telegram API ID
* 🔐 Telegram API Hash
* 🌐 Koneksi internet

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/sevou17/wasapotp-notif.git
cd wasapotp-notif
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Telegram API Configuration

Program membutuhkan **API ID** dan **API Hash** Telegram.

Buka:

[my.telegram.org](https://my.telegram.org/auth)

Kemudian:

1. Login menggunakan akun Telegram.
2. Buka **API development tools**.
3. Buat aplikasi baru.
4. Salin **API ID**.
5. Salin **API Hash**.

---

## 📄 `.env`

Buat file `.env` di direktori utama project:

```env
API_ID=12345678
API_HASH=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> 🔒 Jangan pernah membagikan `API_HASH` atau meng-upload file `.env` ke repository publik.

---

# ⚙️ Configuration

## `config.json`

Konfigurasi utama program berada di:

```text
config.json
```

Contoh:

```json
{
    "target_bot": "@kangwhatsappbot",
    "layanan": "shopee",
    "jumlah_pesanan": 2
}
```

### Configuration Reference

| Parameter        | Type      | Example            | Description                 |
| ---------------- | --------- | ------------------ | --------------------------- |
| `target_bot`     | `string`  | `@kangwhatsappbot` | Username bot yang dipantau  |
| `layanan`        | `string`  | `shopee`           | Layanan yang dipilih        |
| `jumlah_pesanan` | `integer` | `2`                | Jumlah pesanan yang dipilih |

### `target_bot`

Menentukan bot Telegram yang akan dipantau.

```json
"target_bot": "@kangwhatsappbot"
```

### `layanan`

Menentukan layanan yang akan dipilih secara otomatis.

```json
"layanan": "shopee"
```

### `jumlah_pesanan`

Menentukan jumlah pesanan.

```json
"jumlah_pesanan": 2
```

Program secara otomatis menyesuaikan angka tersebut dengan format tombol.

```text
2
↓
2x
```

---

# ▶️ Running

Setelah konfigurasi selesai, jalankan:

```bash
python notif.py
```

### 🔐 First Login

Pada penggunaan pertama, Telethon akan meminta login ke akun Telegram.

Masukkan nomor telepon:

```text
+6281234567890
```

Kemudian masukkan kode OTP yang dikirimkan oleh Telegram.

Jika akun menggunakan **Two-Step Verification**, masukkan password Telegram ketika diminta.

Setelah berhasil login, session akan tersimpan sebagai:

```text
notif.session
```

Pada penggunaan berikutnya, session tersebut akan digunakan kembali secara otomatis.

---

# 📁 Project Structure

```text
WASAPOTP-Notif/
│
├── notif.py
├── config.json
├── .env
├── requirements.txt
├── notif.session
├── .gitignore
└── README.md
```

### File Description

| File               | Description                     |
| ------------------ | ------------------------------- |
| `notif.py`         | Source code utama               |
| `config.json`      | Konfigurasi bot                 |
| `.env`             | Telegram API credentials        |
| `requirements.txt` | Python dependencies             |
| `notif.session`    | Telegram login session          |
| `.gitignore`       | File yang dikecualikan dari Git |
| `README.md`        | Dokumentasi project             |

---

# 🔒 Security

Beberapa file bersifat **private** dan tidak boleh dibagikan:

```text
.env
*.session
```

Gunakan `.gitignore`:

```gitignore
.env
*.session
__pycache__/
*.pyc
```

### ⚠️ Jangan upload:

```text
API_ID
API_HASH
Telegram Session
OTP Telegram
Password Two-Step Verification
```

Telegram session dapat digunakan untuk mengakses akun Telegram yang telah login.

---

# 🛠️ Troubleshooting

## `ModuleNotFoundError: No module named 'telethon'`

Install Telethon:

```bash
pip install telethon
```

---

## `ModuleNotFoundError: No module named 'dotenv'`

Install `python-dotenv`:

```bash
pip install python-dotenv
```

---

## Session Telegram bermasalah

Hentikan program kemudian hapus:

```text
notif.session
```

Jalankan kembali:

```bash
python notif.py
```

Telethon akan meminta proses login ulang.

---

## Program tidak mendeteksi pesan

Periksa:

* `target_bot` sudah benar.
* Bot target dapat diakses oleh akun Telegram.
* Keyword pesan sesuai dengan yang dipantau program.
* Koneksi internet aktif.
* Program masih berjalan di terminal.

---

# 🧪 Example Configuration

Contoh konfigurasi untuk memilih layanan **Shopee** dengan jumlah **2 pesanan**:

```json
{
    "target_bot": "@kangwhatsappbot",
    "layanan": "shopee",
    "jumlah_pesanan": 2
}
```

Workflow:

```text
📩 "Nomor baru tersedia!"
        ↓
⚡ /layanan
        ↓
🛒 Shopee
        ↓
🔢 2x
        ↓
✅ Confirm
```

---

# 💻 Tech Stack

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Telethon-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">
<img src="https://img.shields.io/badge/python--dotenv-3776AB?style=for-the-badge&logo=python&logoColor=white">

</p>

| Technology       | Usage                           |
| ---------------- | ------------------------------- |
| 🐍 Python        | Core programming language       |
| 📡 Telethon      | Telegram client & API           |
| 🔐 python-dotenv | Environment variable management |
| 💬 Telegram      | Messaging platform              |

---

# 📜 License

Copyright © 2026 **sevou17**

Project ini dirilis untuk penggunaan pribadi dan edukasi.

Penggunaan, modifikasi, dan distribusi kode diperbolehkan.
---

# ⚠️ Disclaimer

Project ini merupakan **automation tool** untuk Telegram.

Gunakan secara bertanggung jawab dan pastikan penggunaan program sesuai dengan:

* Ketentuan layanan Telegram.
* Aturan bot atau layanan yang digunakan.
* Peraturan yang berlaku di wilayah Anda.

Developer tidak bertanggung jawab atas penyalahgunaan, kerugian, pemblokiran akun, atau konsekuensi lain yang timbul dari penggunaan program ini.

---

# ⭐ Support

Jika project ini bermanfaat, jangan lupa memberikan ⭐ pada repository.

```text
⭐ Star the repository
🍴 Fork the project
🐛 Report bugs
💡 Suggest improvements
```

---

<div align="center">

## 🤖 WASAPOTP Notif

**Fast. Automatic. Configurable.**

Made with Vibecoding & Limit Token

**© 2026 sevou17**

</div>
