from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# ─── Configure the Gemini API key ─────────────────────────────────────────────
# Make sure you have set GEMINI_API_KEY in your environment before running:
#   For Windows PowerShell:
#     $env:GEMINI_API_KEY = "YOUR_ACTUAL_KEY_HERE"
#   For macOS/Linux:
#     export GEMINI_API_KEY="YOUR_ACTUAL_KEY_HERE"
genai.configure(api_key=os.getenv("your api key"))

# ─── Initialize the Gemini model (use 'gemini-1.5-flash' for higher free-tier limits) ───
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.get_json()
    ingredients = data.get('ingredients', '').strip()
    diet = data.get('diet', '')

    if not ingredients:
        return jsonify({'error': 'No ingredients provided.'}), 400

    # Build the prompt based on diet
    prompt = f"Generate a detailed recipe using only these ingredients: {ingredients}."
    if diet == 'Vegetarian':
        prompt += " The recipe must be strictly vegetarian (no meat, poultry, or seafood)."
    elif diet == 'Non-Vegetarian':
        prompt += " The recipe may include meat, poultry, or seafood."

    try:
        response = model.generate_content(prompt)
        recipe_text = response.text
        return jsonify({'recipe': recipe_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
