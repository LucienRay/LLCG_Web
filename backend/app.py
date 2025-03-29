# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)
CORS(app)

# 選擇模型（你可以改成你自己的，例如 CodeGen、LLaMA、StarCoder...）
model_name = "Salesforce/codegen-350M-mono"

# 載入模型與 tokenizer（建議在應用啟動時載入一次）
print("載入模型中...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()
print("模型載入完成！")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    print(f"收到 prompt：{prompt}")

    # 編碼輸入
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    # 產生輸出
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"code": result})

if __name__ == "__main__":
    app.run(port=5000)
