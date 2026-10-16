import streamlit as st

# Page Configuration
st.set_page_config(page_title="AI Prompter Pro", page_icon="⚡", layout="centered")

# Custom CSS for UI styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%) !important;
        color: #f8fafc !important;
    }

    /* Gradient Title Styling */
    .title-text {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #60a5fa, #a855f7, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    .subtitle-text {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-bottom: 25px;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.85) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Customizing Inputs & Text Areas */
    .stTextArea textarea {
        background-color: rgba(30, 41, 59, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        color: #f8fafc !important;
        font-size: 1rem !important;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.65rem 1.25rem !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 14px 0 rgba(168, 85, 247, 0.39);
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(168, 85, 247, 0.55);
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<h1 class="title-text">⚡ AI Prompter Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Turn simple ideas into structured, high-converting master prompts instantly.</p>', unsafe_allow_html=True)

# Sidebar for Settings
st.sidebar.header("Configuration")
prompt_category = st.sidebar.selectbox(
    "Choose Category",
    ["Data Analysis / Python", "Software Engineering", "Business & Copywriting", "General Creative"]
)

prompt_style = st.sidebar.selectbox(
    "Prompt Depth",
    ["Comprehensive & Detailed", "Quick & Direct"]
)

# Main Input Area
raw_idea = st.text_area("Enter your rough idea or task:", placeholder="e.g., Clean a messy CSV file with missing sales data using Pandas", height=120)

if st.button("Generate Master Prompt 🚀"):
    if not raw_idea:
        st.warning("Please enter an idea first!")
    else:
        # Smart template generation based on selected category
        if prompt_category == "Data Analysis / Python":
            master_prompt = f"""You are an expert Data Scientist and Senior Python Developer.
Your task is to solve the following data problem with production-ready, clean, and well-commented code.

### Objective:
{raw_idea}

### Requirements:
1. Use modern Python libraries (e.g., Pandas, NumPy, Scikit-Learn where applicable).
2. Handle edge cases such as missing values, data type mismatches, and outliers.
3. Include clear comments explaining each step of the data transformation.
4. Provide clean code structure following PEP 8 standards.

### Output Format:
- Provide the complete Python code block.
- Briefly explain how the solution works."""

        elif prompt_category == "Software Engineering":
            master_prompt = f"""You are a Principal Software Architect and Full-Stack Engineer.
Write robust, scalable, and secure code following best software engineering practices.

### Task / Feature:
{raw_idea}

### Technical Guidelines:
1. Write clean, maintainable code with comprehensive error handling.
2. Include comments for complex logic.
3. Follow best practices for performance, readability, and security.

### Output Format:
- Code implementation.
- Brief explanation of the architecture or logic."""

        elif prompt_category == "Business & Copywriting":
            master_prompt = f"""You are a world-class Copywriter and Growth Marketing Expert.
Craft high-converting, engaging, and persuasive content based on the user's objective.

### Objective:
{raw_idea}

### Style Guidelines:
- Tone: Professional yet engaging, clear, and action-oriented.
- Structure: Strong hook, clear value proposition, and a compelling call to action (CTA).

### Output Format:
- Ready-to-use copy and structured content breakdown."""

        else:
            master_prompt = f"""You are an elite creative assistant and problem solver.
Your objective is to provide a comprehensive, creative, and structured response to the following prompt:

### Core Request:
{raw_idea}

### Guidelines:
- Think step-by-step.
- Provide deep insights, structured lists, and actionable takeaways.
- Tone: Helpful, intelligent, and creative."""

        st.success("Your Master Prompt is Ready!")
        st.code(master_prompt, language="markdown")
        st.info("💡 Copy this prompt and paste it into ChatGPT, Gemini, or Claude for top-tier results!")