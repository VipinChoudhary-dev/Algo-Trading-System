import requests                                    # a library used to communicate with Telegram’s servers


# this will be used to send Strategy Return, Win Ratio & ML Accuracy for each stocks
def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=payload)
    return response.status_code == 200