from openai import OpenAI
import os

from .key import KEY

client = OpenAI(api_key=KEY, base_url="https://api.deepseek.com")



def split_grade(text):
    """
    Функція шукає оцінку на початку тексту у форматі 'Оцінка X/Y' і повертає її окремо від решти тексту.
    """
    import re

    # Шукаємо шаблон 'Оцінка цифри/цифри'
    match = re.match(r'Grade\s+(\d+)/\d+\.?\s*(.*)', text, re.DOTALL)

    if match:
        grade = match.group(1)      # тільки число
        content = match.group(2)    # решта тексту
    else:
        grade = "Grade ?/10"
        content = text

    return [grade, content]

def checking(card_title, answear):
    print("Generating spans with translations...")
    prompt = f"""
    You MUST answer in this format:

    Grade X/10
    Explanation: ...

    Task: {card_title}

    User idea:
    {answear}
    """
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        # {"role": "system", "content": "You are a translator that formats every word as span with onmouseover."},
        {"role": "user", "content": prompt}
    ],
    stream=False
    )
    print(response.choices[0].message.content)

    grade = split_grade(response.choices[0].message.content)[0]
    content = split_grade(response.choices[0].message.content)[1]

    answear = {
        "content": content,
        "grade": grade,
        }

    return answear
