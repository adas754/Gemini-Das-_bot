from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
app = Flask(__name__)
genai.configure(api_key=" ") 
model = genai.GenerativeModel("models/gemini-pro")

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message") 
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        ai_response = generate_content(user_input)
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
