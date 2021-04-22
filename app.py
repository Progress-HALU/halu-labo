from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('SsRs2YkduwGNbun/Y7UWEdi30u/HKzsXeMGiHV/rtJgxRgnk0ioUW7CWa1CDqmvLqihHP2ScWQsgxLK1rvO+3AoC6XQOuUMfh5hg6CSTh6lqVegn9w3rCJIMsPDrBDeFuT5J9oofh1BxJFqGT6/FqAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d72bef0ad003e6394d319f04032ee206')

@app.route("/")
def test():
    return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="あやちゃん":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"相変わらず、ウマ娘をやっています。"))
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"あなたは「{event.message.text}」と言ってます。"))
       

if __name__ == "__main__":
    app.run()