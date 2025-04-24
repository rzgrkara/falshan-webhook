from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/fal", methods=["POST"])
def fal_cevapla():
    data = request.get_json()
    user_input = data.get("message", "")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sen Falşan adında mistik, nazik ve sezgisel bir falcısın. Her zaman sembolleri yorumlayarak, sıcak ve destekleyici bir dille konuş."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=400
    )

    fal_mesajı = response.choices[0].message.content
    return jsonify({"reply": fal_mesajı})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
