import requests

catalog = 'b1gtphdg2vndncqf33o7'
token = 'AQVNz0cWk7VBfTO-zTtEXUoRsPV-60QzH1ZJETqR'


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

def get_answer(question):

    prompt = {
        "modelUri": f'gpt://{catalog}/yandexgpt/latest',
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": 1000
        },
        "messages" : [
            {
                "role": "user",
                "text": f"{question}"
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {token}"
    }


    ans = requests.post(url=url, headers=headers, json=prompt)
    print(ans)

    ans = ans.json()['result']['alternatives'][0]['message']['text']
    return ans

