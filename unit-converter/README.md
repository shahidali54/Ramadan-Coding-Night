Unit Converter
A simple unit converter built with Python, UV, and Streamlit.

Getting Started
1️⃣ Install UV
First, install UV (if not already installed):

curl -LsSf https://astral.sh/uv/install.sh | sh
For Windows:

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Verify installation:

uv --version
2️⃣ Create and Initialize the Project
uv init unit-converter
cd unit-converter
3️⃣ Install Sreamlit (Dependency)
uv add streamlit
4️⃣ Activate UV Virtual Environment (Windows)
.venv\Scripts\activate
For Linux/macOS:

source .venv/bin/activate
5️⃣ Run Unit Converter
streamlit run unit_converter.py
🎉 That’s it! Your Unit Converter is ready to use 🚀