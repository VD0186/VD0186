
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["POST"])
def reply():
    data = request.get_json()
    question = data.get("question", "")

    prompt = question + "請使用繁體中文進行回覆,只回答台灣可用的保險資訊，提供在台灣可取得的保險方案及相關資訊，需詳情與舉例,並且推薦適合的保險公司與商品"              "必要範例輸出:推薦保險方案時，方案的每月大約繳的保費，一定要輸出，根據保額來評估與理賠金額且從年齡來去判斷現階段適不適合保保險"              "從保額來去推薦適用的保險商品(至少兩個),一定要輸出"

    payload = {
        "model": "gemma:9b",
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post("http://localhost:11434/api/generate", json=payload)
        if res.status_code == 200:
            return jsonify({"reply": res.json().get("response", "")})
        else:
            return jsonify({"error": f"模型錯誤：{res.status_code} - {res.text}"}), 500
    except Exception as e:
        return jsonify({"error": f"❌ 無法連接本地 LLM API：{str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
