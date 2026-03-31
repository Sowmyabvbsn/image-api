from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def generate_image():
    try:
        prompt = request.args.get("prompt")
        model = request.args.get("model", "default")
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400
        encoded_prompt = requests.utils.quote(prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        return redirect(image_url)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

application = app