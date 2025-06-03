
# insurance-replier-api

這是保險問題助手的 Flask API，可部署在 Render。

## 🚀 一鍵部署

1. 將這份專案上傳至你的 GitHub Repository
2. 前往 Render 並點擊下方連結部署：

👉 https://render.com/deploy

3. 選擇剛上傳的 GitHub 專案，按一下就完成！

## 📦 功能

- 提供 /api POST 接口
- 使用本地 LLM（如 gemma:9b via Ollama）
- 支援 CORS，可與 GitHub Pages 前端整合

## ✅ 前端請用 JavaScript 這樣呼叫：

```js
fetch("https://your-render-url.onrender.com/api", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ question: "我想買醫療險" })
})
```
