from flask import Flask, request, jsonify
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)

def process_image(image_data):
    """Proses screenshot untuk menemukan tile dan langkah terbaik"""
    image = Image.open(BytesIO(image_data))
    img_np = np.array(image)
    img_gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

    # TODO: Implementasi deteksi tile dengan OpenCV
    # Contoh hasil deteksi langkah terbaik (harus diganti dengan yang sesuai)
    moves = [{"from": (100, 200), "to": (150, 200)}]

    return moves

@app.route("/process", methods=["POST"])
def process():
    """Menerima gambar dari client dan mengembalikan langkah terbaik"""
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image_file = request.files["image"].read()
    moves = process_image(image_file)
    
    return jsonify(moves)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
