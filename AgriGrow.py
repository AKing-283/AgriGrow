import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from fpdf import FPDF
import io
import matplotlib.pyplot as plt
import tempfile

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input_text, prompt])
    return response.text

def generate_income_ideas(waste_type):
    prompt = (f"You are an expert in agricultural waste management. Provide detailed information on how to generate income "
              f"from the given {waste_type}. Include estimated earnings, pros and cons of the suggested methods, and provide "
              f"historical statistics and trends for the last few years. Exclude any asterisks or unnecessary comments. "
              f"Include suggestions for potential graphs and charts that can be used to illustrate the data.")
    response = get_gemini_response("", prompt)
    return response

def generate_graph():
    # Example data
    years = ['2021', '2022', '2023']
    values = [1000, 1500, 1200]
    
    plt.figure(figsize=(8, 6))
    plt.plot(years, values, marker='o', linestyle='-', color='b')
    plt.title('Income Trends Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Income ($)')
    plt.grid(True)
    
    # Save the plot to a BytesIO object
    graph_buffer = io.BytesIO()
    plt.savefig(graph_buffer, format='png')
    graph_buffer.seek(0)
    return graph_buffer

def generate_pdf(waste_type, income_ideas):
    pdf_buffer = io.BytesIO()
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    # Title
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Income Generation from {waste_type}", ln=True, align='L')

    # Income Ideas
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 10, income_ideas)

    # Generate and add graph
    graph_buffer = generate_graph()
    
    # Save graph to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        temp_file.write(graph_buffer.getvalue())
        temp_filename = temp_file.name
    
    # Add the image to PDF
    pdf.image(temp_filename, x=10, y=pdf.get_y() + 10, w=180)
    
    # Clean up the temporary file
    os.remove(temp_filename)

    pdf_output = pdf.output(dest='S')  # Output PDF as bytes
    if isinstance(pdf_output, str):
        pdf_output = pdf_output.encode('latin1')  # Convert to bytes if necessary
    
    pdf_buffer.write(pdf_output)
    pdf_buffer.seek(0)  # Reset buffer position to the beginning
    return pdf_buffer

st.title("Agricultural Waste to Income Generator")

waste_category = st.selectbox("Waste Category", [
        "Crop Residues",
        "Animal Wastes",
        "Food Processing Wastes",
        "Agriculture chemicals",
        "Other"
    ])

if waste_category == "Crop Residues":
    waste_type = st.selectbox("Crop Residue Type", ["Stubble", "Straw", "Husks", "Leaves", "Shells", "Roots"])
elif waste_category == "Animal Wastes":
    waste_type = st.selectbox("Animal Waste Type", ["Manure", "Litter", "Poultry Litter", "Slaughterhouse Waste"])
elif waste_category == "Food Processing Wastes":
    waste_type = st.selectbox("Food Processing Waste Type", ["Fruit/Veg Wastes", "Dairy Processing Wastes", "Sugarcane Processing Wastes", "Grain Processing Wastes", "Meat Processing Wastes"])
elif waste_category == "Agriculture chemicals":
    waste_type = st.selectbox("Agriculture Chemicals", ["Pesticides", "Fertilizers", "Container Wastes"])
else:
    waste_type = st.selectbox("Other Waste Type", ["Irrigation Return Flow", "Silage Effluents", "Plastic Mulch"])

generate_button = st.button("Generate Income Ideas")

if generate_button:
    if waste_type:
        income_ideas = generate_income_ideas(waste_type)
        st.write(income_ideas)
        
        pdf_buffer = generate_pdf(waste_type, income_ideas)
        
        pdf_data = pdf_buffer.getvalue()
        
        st.download_button(
            label="Download PDF",
            data=pdf_data,
            file_name=f"{waste_type}_income_ideas.pdf",
            mime='application/pdf'
        )
    else:
        st.write("Please select a waste type first")
