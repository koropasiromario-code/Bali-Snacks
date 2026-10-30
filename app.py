from flask import Flask, render_template, request, jsonify
import random
import re

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Pie Susu Bali", "category": "Kue", "price": 35000,
     "description": "Pie renyah dengan isian susu lembut. Cocok untuk oleh-oleh.",
     "emoji": "🥧", "tag": "Favorit"},
    {"id": 2, "name": "Kacang Disco", "category": "Camilan", "price": 25000,
     "description": "Kacang berbalut tepung berbumbu yang renyah dan gurih.",
     "emoji": "🥜", "tag": "Gurih"},
    {"id": 3, "name": "Klepon Bali", "category": "Kue Tradisional", "price": 18000,
     "description": "Kue tradisional berisi gula merah dengan taburan kelapa.",
     "emoji": "🍡", "tag": "Tradisional"},
    {"id": 4, "name": "Kue Laklak", "category": "Kue Tradisional", "price": 20000,
     "description": "Kue mungil khas Bali yang nikmat disajikan dengan kelapa dan gula merah.",
     "emoji": "🥞", "tag": "Khas Bali"},
    {"id": 5, "name": "Pia Kacang Hijau", "category": "Kue", "price": 30000,
     "description": "Pia dengan kulit berlapis dan isian kacang hijau manis.",
     "emoji": "🥮", "tag": "Oleh-oleh"},
    {"id": 6, "name": "Keripik Pisang", "category": "Camilan", "price": 22000,
     "description": "Irisan pisang yang renyah untuk teman bersantai.",
     "emoji": "🍌", "tag": "Renyah"},
]

def rupiah(value):
    return "Rp{:,.0f}".format(value).replace(",", ".")

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip().lower()
    if not message:
        return jsonify({"reply": "Silakan tulis pertanyaan tentang jajanan khas Bali."})

    if any(word in message for word in ["murah", "hemat", "budget", "terjangkau"]):
        choices = sorted(PRODUCTS, key=lambda p: p["price"])[:3]
        reply = "Pilihan yang ramah di kantong: " + ", ".join(
            f'{p["name"]} ({rupiah(p["price"])})' for p in choices
        ) + ". Harga ini contoh dan dapat disesuaikan oleh pemilik UMKM."
    elif any(word in message for word in ["oleh-oleh", "oleh oleh", "souvenir", "dibawa"]):
        reply = "Untuk oleh-oleh, Anda bisa mempertimbangkan Pie Susu Bali, Kacang Disco, atau Pia Kacang Hijau. Periksa masa simpan dan kemasan dari penjual sebelum bepergian."
    elif any(word in message for word in ["gurih", "asin", "renyah"]):
        picks = [p for p in PRODUCTS if p["category"] == "Camilan"]
        reply = "Jika suka camilan gurih atau renyah, coba " + " dan ".join(p["name"] for p in picks) + "."
    elif any(word in message for word in ["manis", "kue", "tradisional"]):
        picks = [p for p in PRODUCTS if p["category"] in ["Kue", "Kue Tradisional"]]
        reply = "Untuk jajanan manis, pertimbangkan " + ", ".join(p["name"] for p in picks[:4]) + "."
    elif any(word in message for word in ["promo", "caption", "iklan", "promosi"]):
        reply = "Contoh caption: “Jelajahi rasa Bali dari gigitan pertama! 🥧 Cicipi jajanan khas Bali pilihan kami—cocok untuk teman santai dan buah tangan. Pesan sekarang dan dukung UMKM lokal!” Sesuaikan harga, stok, dan kontak sebelum dipublikasikan."
    elif any(word in message for word in ["harga", "berapa", "biaya"]):
        reply = "Harga contoh tersedia di katalog. Pilihan mulai dari " + rupiah(min(p["price"] for p in PRODUCTS)) + ". Harga pada website ini adalah data demo yang dapat diubah di app.py."
    elif any(word in message for word in ["halo", "hai", "hello", "selamat"]):
        reply = "Om Swastyastu! Selamat datang di Bali Snack AI. Saya bisa membantu memilih jajanan, mencari pilihan hemat, atau membuat ide promosi."
    else:
        product_names = ", ".join(p["name"] for p in PRODUCTS[:4])
        reply = f"Saya bisa membantu rekomendasi jajanan, pilihan hemat, oleh-oleh, atau caption promosi. Beberapa produk kami: {product_names}. Apa yang Anda cari?"
    return jsonify({"reply": reply})

@app.route("/api/promo", methods=["POST"])
def promo():
    data = request.get_json(silent=True) or {}
    product = str(data.get("product", "")).strip()
    platform = str(data.get("platform", "Instagram")).strip()
    tone = str(data.get("tone", "hangat")).strip()
    if not product:
        return jsonify({"caption": "Masukkan nama produk terlebih dahulu."}), 400
    caption = (
        f"🌺 Cita rasa Bali hadir untuk menemani harimu!\\n\\n"
        f"Yuk, coba {product} dari UMKM lokal kami. Nikmati camilan pilihan dengan "
        f"nuansa khas Bali—pas untuk teman santai maupun buah tangan.\\n\\n"
        f"📩 Hubungi kami untuk informasi stok dan pemesanan.\\n"
        f"#JajananBali #UMKMLokal #BanggaBuatanIndonesia"
    )
    if tone == "ceria":
        caption = f"🎉 Ngemil makin seru dengan {product}! 🌴\\n\\n" + caption.split("\\n\\n", 1)[1]
    elif tone == "formal":
        caption = f"Kami memperkenalkan {product}, pilihan jajanan untuk menemani aktivitas dan buah tangan Anda.\\n\\n" + caption.split("\\n\\n", 1)[1]
    return jsonify({"caption": caption, "platform": platform})

if __name__ == "__main__":
    app.run(debug=True)
