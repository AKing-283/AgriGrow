**Agricultural Waste to Income Generator**

**Project Overview:**
This Python-based Streamlit application serves as a prototype for generating income ideas from various agricultural waste types. It utilizes a generative AI model to provide detailed insights, including potential earnings, pros and cons, and relevant statistics. Additionally, the application generates a downloadable PDF report containing the generated information and a visual representation of income trends.

**Key Features:**
User-friendly interface with dropdown menus for selecting waste categories and types.
Integration with a generative AI model (currently using Google's Gemini) to provide in-depth income generation ideas.
Dynamic PDF generation with embedded graphs, summarizing the generated information.
Downloadable PDF for future reference and sharing.

**Prerequisites:**
Python 3.6+
Required libraries (listed in requirements.txt):
streamlit
python-dotenv
google-cloud-aiplatform (or equivalent for your AI model)
fpdf
matplotlib
Installation:

**Clone the repository:**
git clone https://github.com/AKing-283/AgriGrow


**Create a virtual environment (recommended):**
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Use code with caution.

**Install dependencies:**
pip install -r requirements.txt


  
**Set up environment variables:**
Create a .env file in the project root.   
Add your Google Cloud API key (or equivalent for your AI model) as an environment variable.
Usage:

Run the application:
streamlit run app.py


Select the waste category and type from the dropdown menus.
Click the "Generate Income Ideas" button.
The generated income ideas will be displayed on the screen.
Download the generated PDF by clicking the "Download PDF" button.

**Limitations:**
1. This is a prototype and may have limitations in terms of data accuracy and comprehensiveness.
2. The generated income ideas are based on general information and might not be suitable for specific circumstances.

**Future Improvements:**
1. Incorporate user-specific data for more tailored recommendations.
2. Expand the database of waste types and income generation methods.
3. Enhance the PDF report with additional visualizations and data.
4. Explore different generative AI models for improved performance.
