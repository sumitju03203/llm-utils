
# 🧠 LangChain Multi-Provider LLM Router

This module allows you to switch between **OpenAI**, **Ollama (local)**, and **AWS Bedrock** LLM providers using a clean and configurable interface via feature/environment flags.

## ✅ Supported Providers

- 🧠 **Ollama** – Run models like `mixtral`, `llama2`, etc. locally
- ☁️ **OpenAI** – Use `gpt-3.5`, `gpt-4`, or any supported model
- 🛡️ **AWS Bedrock** – Use Amazon-hosted foundation models like `Claude`, `Mixtral`, or `Titan`

---

## 📁 Project Structure

```
.
├── constants.py            # Environment and config constants
├── llm_router.py           # Main LLM router logic
├── .env                    # Environment variables
├── README.md               # You're here!
```

---

## ⚙️ Setup Instructions

### 1. 📦 Install Required Dependencies

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### 2. 📄 Create `.env`

Copy .env.sample to .env

```env
ENV=DEV

# Ollama
OLLAMA_URI=http://localhost:11434
LLM_MODEL=mixtral

# OpenAI
OPENAI_KEY=your_openai_api_key
OPENAI_ML_MODEL=gpt-3.5-turbo

# AWS Bedrock
AWS_BEDROCK_ACCESS_KEY=your_aws_access_key
AWS_BEDROCK_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_BEDROCK_REGION=us-east-1
AWS_BEBROCK_MODEL_ID=amazon.titan-text-lite-v1
```

> 💡 You can switch environments using `ENV=DEV`, `QA`, or `PROD` depending on how you want to route traffic.

---

## 🧪 Example Usage

```python
from llm_router import get_llm
from constants import LLM_SELECTOR_OLLAMA, LLM_SELECTOR_OPENAI, LLM_SELECTOR_AWS_BEDROCK

# Choose your provider
llm = get_llm(LLM_SELECTOR_OLLAMA)  # or LLM_SELECTOR_OPENAI / LLM_SELECTOR_AWS_BEDROCK

# Send a prompt
response = llm.invoke("Explain what Mixture of Experts means in simple terms.")
print(response)
```

---

## 🔁 Switching Providers

Use one of the following selectors:
```python
LLM_SELECTOR_OPENAI       # "openai"
LLM_SELECTOR_OLLAMA       # "ollama"
LLM_SELECTOR_AWS_BEDROCK  # "aws_bedrock"
```

You can dynamically decide which one to use based on environment, user settings, tenant preferences, or feature flags.

---

## 📌 Notes

- Ensure Ollama is running locally and you have pulled the required model (e.g. `ollama pull mixtral`)
- AWS credentials should have permissions for Bedrock runtime
- OpenAI usage is billed, so keep your key secure
- Logs and errors will appear via `logging` if configured

