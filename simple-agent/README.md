# Simple Agent

A simple Agent built with Python, UV, OpenAI Agents SDK, and Gemini API.

## Getting Started

### 1️⃣ Install UV

First, install **UV** (if not already installed):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```sh
uv --version
```

---

### 2️⃣ Create and Initialize the Project

```sh
uv init simple-agent
cd simple-agent
```

---

### 3️⃣ Install Dependencies

```sh
uv add openai-agents python-dotenv
```

---

### 4️⃣ Activate UV Virtual Environment (Windows)

```sh
.venv\Scripts\activate
```

For Linux/macOS:

```sh
source .venv/bin/activate
```
---

### 5️⃣ Create .env file

Create a `.env` file in the root directory of the project and add the following:

```sh
GEMINI_API_KEY=your_gemini_api_key
```

Get Google Gemini API key from [here](https://aistudio.google.com/app/apikey)

---

### 6️⃣ Run Simple Agent

```sh
uv run main.py
```

Enter your message like `hi` or `bye` in the terminal and see the result.

🎉 That’s it! Your Simple Agent is ready to use 🚀
