# Simple ChatGPT CLI

## 緣由

---
本專案是一個簡單展示串接 [OpenAI ChatGPT](https://chat.openai.com/) 服務的 Command Line 工具。
透過一個簡單的介面得以向 ChatGPT 發問並求得回答。


## 流程說明

---
* 初始化一個自定義的 class，名字叫作 `OpenAI`。裡面會實作以下方法：
  * `ask_apikey`：詢問使用者要使用的 APIKEY。如果沒輸入的話會持續詢問
  * `send_question`：將使用者輸入的問題丟到 ChatGPT 發問
* 開始執行一個無窮迴圈，並依序執行以下指令：
  * 判斷是否為第一次執行，如果是的話會先顯示一段幫助文字
  * 接著開始詢問 APIKEY
  * 顯示提示使用者輸入問題的文字，並等候使用者輸入
  * 使用者輸入問題後按下 enter 後將問題丟回 ChatGPT 處理並準備接收其回應。
  * 顯示回應並回到前兩步驟繼續。

## 使用方式

---
首先需要到 [OpenAI API](https://platform.openai.com/) 申請一組 API Key。
第一次註冊的話會有一定時間的免費試用期間。

接著依序執行以下指令：
```shellscript
python3 -m pip install -r requirements.txt
python3 main.py 
```

接著應該會看到以下畫面：
![貼入APIKEY](https://i.imgur.com/ECDQguN.jpg)
請將稍早申請到的 API KEY（通常是 `sk-` 字眼開頭）貼上後按下 `enter`。

接著就能看到發問的輸入框：
![發問](https://i.imgur.com/06otUcE.jpg)


輸入問題後等一會就會輸出回應：
![輸出回應](https://i.imgur.com/RuuIe6p.jpg)

如果想要顯示使用方法的話，直接輸入：`help` 即可（大小寫不拘）

如果要離開介面，可以直接輸入：`quit`

## TODO

---
- 目前是採取同步方式進行操作，理想上應該需要使用非同步方式列出 ChatGPT 的所有回應。
- 詢問 APIKEY 的部分考慮要放進設定檔中，可以省去貼上 APIKEY 的步驟。