# LLCG_Web

LLCG_Web 是一個組合 Vue 前端和 Python Flask 後端的本地應用程式，目的是為開發者提供一套可以隨時用來生成程式碼的簡單使用工具，可以圖形化體驗、快速原型化，並保持資料隔離與隱私安全性。

## 最大特色
- 輕量化、可本地執行的代碼生成模型
- Vue 3 + Vite 定義前端使用者介面
- Python Flask 後端處理請求與生成
- 有機會接入自己訓練或封裝過的模型
- 隨開即用，隨開即試

## 本地執行
無需網路，同時支援 Windows / macOS / Linux 系統執行，適合工作空間、教學社群或個人學習環境。
> ⚠️ **注意**：目前的版本還需要連接網路。

## 如何使用

### 1️⃣ 安裝後端 (Flask)
```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows 用 venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
後端會啟動在 http://localhost:5000

### 2️⃣ 安裝前端 (Vue)
```bash
cd frontend
npm install
npm run dev
```
前端會啟動在 http://localhost:5173

### 3️⃣ 開始使用
1. 開啟瀏覽器 → 訪問 http://localhost:5173
2. 輸入自然語言描述，例如「寫一個 Python 排序函數」
3. 點擊「產生程式碼」按鈕
4. 程式碼將顯示在下方區塊中

