import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

LLM_SELECTOR_OLLAMA = "ollama"
LLM_SELECTOR_OPENAI = "openai"
LLM_SELECTOR_AWS_BEDROCK = "aws_bedrock"

OLLAMA_URI = os.environ.get("OLLAMA_URI", "http://0.0.0.0:11434")
LLM_MODEL = os.environ.get("COMMON_MODEL", "llama2:latest")
AWS_BEBROCK_MODEL_ID = os.environ.get("AWS_BEBROCK_MODEL_ID", "us.meta.llama3-2-11b-instruct-v1:0")

OPENAI_KEY = os.environ.get("OPENAI_KEY", "XXXX")
OPENAI_ML_MODEL = os.environ.get("OPENAI_ML_MODEL", "gpt-3.5-turbo")
AWS_BEDROCK_REGION = os.environ.get("AWS_BEDROCK_REGION", "us-east-1")
AWS_BEDROCK_ACCESS_KEY = os.environ.get("AWS_BEDROCK_ACCESS_KEY", "xxxx")
AWS_BEDROCK_SECRET_ACCESS_KEY = os.environ.get("AWS_BEDROCK_SECRET_ACCESS_KEY", "lxxxx")
