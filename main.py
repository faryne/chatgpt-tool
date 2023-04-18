import json

import openai


# show_error 顯示錯誤訊息
def show_error(msg: str):
    print("[error] %s" % msg)


# show_help 顯示幫助訊息 @TODO
def show_help():
    print("""========= HELP Start =========
    1. 首先輸入 OpenAI 的 apikey 
    2. 接著發問
    
    輸入 help 後顯示本頁內容
    輸入 quit 離開本程式
========= Help End =========
    """)


# OpenAI 執行用 class
class OpenAI:
    # 存放 api_key
    openaiApikey = ""

    # 在建構子重新賦值
    @classmethod
    def __init__(cls):
        cls.openaiApikey = ""

    # 詢問 OpenAI api_key
    @classmethod
    def ask_apikey(cls):
        if cls.openaiApikey == "":
            openai_apikey = input("請輸入 OPENAI Apikey：")
            if openai_apikey == "":
                cls.ask_apikey()
                return

            cls.openaiApikey = openai_apikey

    @classmethod
    def send_question(cls, question: str):
        openai.api_key = cls.openaiApikey
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": question}
        ])
        print("<<< ChatGPT：", response.choices[0].message.content)


if __name__ == '__main__':
    isFirst = True  # 第一次執行需要確認有填入 apikey 等資訊
    openaiClient = OpenAI()
    while True:
        if isFirst:
            show_help()
            openaiClient.ask_apikey()
            isFirst = False

        rawInput = input(">>>我：")
        if rawInput.lower() == "help":
            show_help()
            continue
        elif rawInput.lower() == "quit":
            print("離開程序")
            break
        else:
            try:
                openaiClient.send_question(rawInput)
            except openai.error.RateLimitError as e:
                show_error(e.user_message)
                break

