import requests
import pdfplumber
pdf1 = pdfplumber.open('https://vd0186.github.io/VD0186/example.pdf')
text1 = ""
for i in range(len(pdf1.pages)):
    page1 = pdf1.pages[i]
    text1 = text1+page1.extract_text()
pdf2 = pdfplumber.open('https://vd0186.github.io/VD0186/insurance_policy.pdf')
text2 = ""
for i in range(len(pdf2.pages)):
    page2 = pdf2.pages[i]
    text2 = text2+page2.extract_text()

# 設定 API 位置
url = "http://localhost:11434/api/generate"
# 使用者輸入問題
user = input("請輸入你的保險問題：")


# 設定請求內容
payload = {
    "model": "cwchang/llama3-taide-lx-8b-chat-alpha1",
    "prompt": user,
    "text":text1,
    "text":text2,
    "system": "你是台灣保險專家，只回答台灣可用的保險資訊，提供在台灣可取得的壽險險方案及相關資訊，需詳情與舉例",
    "stream": False  # 如果要逐步接收回應，可以設為 True
}

try:
    # 發送 POST 請求
    response = requests.post(url, json=payload)

    # 確認是否成功
    if response.status_code == 200:
        print("\n模型回覆：")
        print(response.json()["response"])
    else:
        print("\n⚠️ 請求失敗")
        print(f"狀態碼：{response.status_code}")
        print(f"錯誤訊息：{response.text}")

except requests.exceptions.RequestException as e:
    print("\n❌ 無法連接到 API")
    print(e)
