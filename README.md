SmartChef Recipe Generator

SmartChef is a Flask-based web application that generates customized recipes (Vegetarian or Non-Vegetarian) using Google’s Gemini API. It features a modern, responsive dashboard interface and clearly structured output (Ingredients, Instructions, Notes, etc.). Below is a quick reference for each file in this repository.

Repository Structure
--------------------
smart-chef/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.txt

1. app.py
---------
Type: Python script (Flask application)
Purpose:
  - Bootstraps the Flask web server.
  - Loads your Gemini API key from the GEMINI_API_KEY environment variable.
  - Initializes the gemini-1.5-flash model.
  - Defines two routes:
    1. GET / → renders the dashboard (index.html).
    2. POST /generate_recipe → receives { ingredients, diet } as JSON, builds a prompt (strictly vegetarian or non-vegetarian), sends it to Gemini, and returns the raw recipe text as JSON.
  - Handles error cases (missing ingredients or API failures) and returns appropriate HTTP status codes.

2. templates/index.html
-----------------------
Type: HTML template (Jinja2)
Purpose:
  - Defines the dashboard layout (header, input panel, output panel).
  - Contains:
    - A <textarea> for entering ingredients.
    - Two “Diet Preference” buttons (Vegetarian / Non-Vegetarian) with a JavaScript click handler that visually highlights the selected option.
    - A “Generate Recipe” button that sends a JSON POST to /generate_recipe.
    - A <div id="recipe-output"> where the formatted recipe will appear (headings, bulleted lists, paragraphs).
  - Embeds a small <script> block that:
    1. Manages the selectedDiet variable.
    2. Sends the fetch request to /generate_recipe.
    3. Formats the returned text into structured HTML (recognizing lines ending in “:” as <h3>, lines starting with “- ” as <ul><li>, etc.).
  - Relies on url_for('static', filename='style.css') to load the CSS.

3. static/style.css
-------------------
Type: CSS stylesheet
Purpose:
  - Provides a professional, responsive dashboard look and feel.
  - Key sections:
    1. Reset & Base Styles: Zeroes out margins/padding and sets a clean font family.
    2. Dashboard Layout:
       - .dashboard flex container (column)
       - .dashboard-header (dark banner with white text)
       - .dashboard-main (flex: two side-by-side cards on desktop, stacked on mobile)
    3. Input & Output Cards (.input-section, .output-section): White backgrounds, rounded corners, drop shadows, vertical scrolling if content overflows.
    4. Textarea: Styled for readability, with padding and soft background.
    5. Diet Buttons (.diet-buttons button): Blue background by default, white text, toggles to a “selected” (white background, blue border/text) style. Hover states for better UX.
    6. Generate Button (#generate-btn): Green, with hover effect.
    7. Recipe Output Formatting (.recipe-output):
       - Headings (<h3>) get a green accent bar.
       - Unordered lists for lines prefixed with “- “.
       - Paragraphs for normal text.
    8. Loading & Error Messages: Italicized “Generating…” message and red error text.
    9. Responsive Breakpoints:
       - Below 768px, stack input + output vertically.
       - Below 480px, adjust font sizes, padding, and textarea height for small screens.

4. requirements.txt
-------------------
Type: Plain text (Python dependencies)
Purpose: Lists all Python packages needed to run SmartChef:
Flask
google-generativeai
python-dotenv

Quick Start Guide
-----------------
1. Clone this repository
   git clone https://github.com/your-username/smart-chef.git
   cd smart-chef

2. Install Python dependencies
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\Activate    # Windows PowerShell

   pip install -r requirements.txt

3. Set your Gemini API key
   Windows (PowerShell):
     $env:GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_KEY"
   macOS/Linux:
     export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_KEY"

4. Run the Flask server
   python app.py

5. Open your browser
   Navigate to http://127.0.0.1:5000 and you should see a two-panel dashboard:
   1. Enter ingredients (comma-separated).
   2. Click Vegetarian or Non-Vegetarian.
   3. Click Generate Recipe.

The generated recipe will appear on the right, neatly formatted into sections (e.g., “Ingredients:”, “Instructions:”, “Notes:”).
