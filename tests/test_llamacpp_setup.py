# tests/test_llama_cpp.py
import pytest
from langchain import LlamaCpp  # Import the LlamaCpp module


@pytest.fixture
def model_path() -> str:
    return "models/ggml-model-codellama-13B-q4_0.gguf"


@pytest.fixture
def llama_cpp_model(model_path: str):
    # Initialize the LlamaCpp model (adjust the path as needed)
    return LlamaCpp(model_path=model_path)


def test_llama_cpp_with_langchain(llama_cpp_model: LlamaCpp):
    # Example: Generate a code completion using LlamaCpp and Langchain
    input_code = """
    def greet(name):
    """

    # Use LlamaCpp to generate the code
    code = llama_cpp_model.predict(input_code)

    # Assert that the code summary is not empty or None
    assert code is not None and code.strip() != ""
