import requests

catalog = 'b1gtphdg2vndncqf33o7'
token = 'AQVNylyLM4wMzwA1QlLZ-ogkTM5Zcn1wqKhPjHZE'


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

while True:

    user = input('введи вопрос: ')


    prompt = {
        "modelUri": f'gpt://{catalog}/yandexgpt/latest',
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": 200
        },
        "messages" : [
            {
                "role": "user",
                "text": f"{user}"
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {token}"
    }


    ans = requests.post(url=url, headers=headers, json=prompt)

    ans = ans.json()['result']['alternatives'][0]['message']['text']
    print(ans)
