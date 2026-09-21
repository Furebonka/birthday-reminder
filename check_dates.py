import json
import os
import datetime
import requests

with open("dates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

today = datetime.datetime.utcnow()
today_month = today.month
today_day = today.day

matches = []
for item in data["dates"]:
    if item["month"] == today_month and item["day"] == today_day:
        matches.append(item["name"])

if matches:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    if len(matches) == 1:
        text = f"🔔 Сегодня: {matches[0]}"
    else:
        text = "🔔 Сегодня важные даты:\n" + "\n".join(f"• {m}" for m in matches)

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    response = requests.post(url, json=payload)
    print(f"Отправлено: {text}")
    print(f"Статус: {response.status_code}")
else:
    print("Сегодня ничего нет.")
