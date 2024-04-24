

# def AiGPT():
#     response = g4f.ChatCompletion.create(
#         model=g4f.models.gpt_4,
#         messages=[{"role": "user", "content": "Напиши стих о России"}],
#     )  # alternative model setting
#     print(response)

from g4f.client import Client

async  def AiGPT(promt: str):
    client = Client()
    print(promt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "director", "content":f'Расскажи об этом историческом событии {promt}'}]
    )
    return response.choices[0].message.content


# Изменить promthoices[0].message.content)