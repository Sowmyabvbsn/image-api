from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)
client = Client()

@app.route("/", methods=["GET"])
def generate_image():
    try:
        prompt = request.args.get("prompt")
        model = request.args.get("model", "bing")

        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        response = client.images.generate(
            model=model,
            prompt=prompt,
            response_format="url"
        )

        image_url = response.data[0].url

        return jsonify({
            "prompt": prompt,
            "model": model,
            "image_url": image_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)