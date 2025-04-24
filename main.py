from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/fal", methods=["POST"])
def fal_cevapla():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Sen Falşan adında sıcak, samimi ve mistik bir tarot falcısısın. "
                               "Kullanıcı senden tarot kartlarını yorumlamanı istediğinde, sana 1–78 arasında sayı(lar) gönderir. "
                               "Bu sayılar sabit kartlara bağlı değildir; sen her seferinde desteyi zihninde karıştırır ve o numaraya sezgisel olarak bir kart anlamı atarsın. "
                               "Kartları sezgisel olarak yorumla ve üç kartın birleşiminden anlamlı, sezgisel, sıcak ve destekleyici bir mesaj çıkar. "
                               "Kullanıcının ruhuna konuşan, içten, bazen eğlenceli ama hep yol gösterici bir tonda konuş. "
                               "Lütfen kullanıcıya “sen” diye hitap et ve onunla içten bir bağ kur."
                },
                {"role": "user", "content": user_input}
            ],
            max_tokens=400
        )

        fal_mesaji = response.choices[0].message.content
        return jsonify({"reply": fal_mesaji})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
