import logging
import os
from .constants import (OLLAMA_URI, LLM_MODEL, AWS_BEBROCK_MODEL_ID,
                         LLM_SELECTOR_OLLAMA, LLM_SELECTOR_OPENAI, LLM_SELECTOR_AWS_BEDROCK,
                         OPENAI_KEY,
                         OPENAI_ML_MODEL,
                         AWS_BEDROCK_REGION,
                         AWS_BEDROCK_ACCESS_KEY,
                         AWS_BEDROCK_SECRET_ACCESS_KEY)
from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock

logger = logging.getLogger(__name__)

# AWS Bedrock LLM
def get_aws_bedrock_llm():
    llm = ChatBedrock(
        model_id=AWS_BEBROCK_MODEL_ID,
        region_name=AWS_BEDROCK_REGION,
        aws_access_key_id=AWS_BEDROCK_ACCESS_KEY,
        aws_secret_access_key=AWS_BEDROCK_SECRET_ACCESS_KEY,
        model_kwargs={'max_gen_len': 1024, 'temperature': 0.0001}
    )
    return llm

# OpenAI ChatGPT
def get_openai_llm():
    return ChatOpenAI(
        api_key=OPENAI_KEY,
        temperature=0.0001,
        model=OPENAI_ML_MODEL
    )

# Ollama (Locally Hosted) LLM

def get_ollama_llm(base_url=OLLAMA_URI, repeat_penalty=1.2, temperature=0.0001):
    from langchain.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    from langchain.llms import Ollama

    if not hasattr(get_ollama_llm, "ollama_feedback_common"):
        get_ollama_llm.ollama_feedback_common = Ollama(
            model=LLM_MODEL,
            base_url=base_url,
            repeat_penalty=repeat_penalty,
            temperature=temperature,
            repeat_last_n=-1,
            callback_manager=CallbackManager(
                [StreamingStdOutCallbackHandler()]
            ),
        )
    return get_ollama_llm.ollama_feedback_common


def get_llm(llm_provider):

    print("LLM Provider: ", llm_provider)

    # Add Bedrock to the selector map
    llm_selector = {
        LLM_SELECTOR_OPENAI: lambda: get_openai_llm(),
        LLM_SELECTOR_OLLAMA: get_ollama_llm,
        LLM_SELECTOR_AWS_BEDROCK: lambda: get_aws_bedrock_llm()
    }

    # Return the appropriate LLM or raise an error if the value is invalid
    try:
        return llm_selector[llm_provider.lower()]()
    except KeyError:
        raise ValueError(
            f"""Invalid value for llm_provider: {
                llm_provider}. "
            "Must be 'openai', 'ollama', or 'aws_bedrock'."""
        )
