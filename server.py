from flask import Flask, request, redirect
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import config
from stock_frequency_reddit import *
import pandas

# connect to the client
client = Client(config.account_sid, config.auth_token)

app = Flask(__name__)


@app.route('/server', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'stock' in incoming_msg or 'stonk' in incoming_msg:

        reddit = login()
        r_penny = rpenny_daily_thread(reddit)
        if r_penny is not None:
            r_penny = r_penny[r_penny['freq'] > 3]
            if len(r_penny) > 0:
                stocks = f"{len(r_penny)} potential buys found for tomorrow! "
                for i in range(len(r_penny)):
                    symbol = r_penny[0][i]
                    stocks += symbol + ", "
                stocks = stocks[:-2]
            else:
                stocks = "No viable stocks found for tomorrow"
        else:
            stocks = "No viable thread found for tomorrow"
        msg.body(stocks)
        responded = True

    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True

    if 'meme' in incoming_msg:
        # return a meme
        r = requests.get('https://meme-api.herokuapp.com/gimme')
        data = r.json()
        meme = data['url']
        msg.media(meme)
        responded = True

    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('Hello, I am chatbot. I am great for: quotes, cats, and memes')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
