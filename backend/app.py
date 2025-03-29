# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    # 這裡先假裝產生程式碼，未來接模型
    result = f"# 模擬產生的程式碼\nprint('你輸入的是：{prompt}')"
    return jsonify({"code": result})

if __name__ == "__main__":
    app.run(port=5000)
