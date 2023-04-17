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
    # 存放 org_key
    openaiOrgKey = ""

    # 在建構子重新賦值
    def __init__(self):
        self.openaiApikey = ""
        self.openaiOrgKey = ""

    # 詢問 OpenAI api_key
    def ask_apikey(self):
        if self.openaiApikey == "":
            openai_apikey = input("請輸入 OPENAI Apikey：")
            if openai_apikey == "":
                self.ask_apikey()
                return

            self.openaiApikey = openai_apikey

    # 詢問 OpenAI OrgKey
    def ask_orgkey(self):
        if self.openaiOrgKey == "":
            openai_orgkey = input("請輸入 OPENAI Orgkey：")
            if openai_orgkey == "":
                self.ask_orgkey()
                return

            self.openaiOrgKey = openai_orgkey

    def send_question(self, question: str):
        openai.api_key = self.openaiApikey
        response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0,
                                            max_tokens=7)
        print("<<< ChatGPT：", response)


if __name__ == '__main__':
    isFirst = True  # 第一次執行需要確認有填入 apikey 等資訊
    openaiClient = OpenAI()
    while True:
        if isFirst:
            show_help()
            openaiClient.ask_apikey()
            openaiClient.ask_orgkey()
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
