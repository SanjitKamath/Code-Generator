from vertexai import init
from vertexai.preview.generative_models import GenerativeModel

init(project="true-energy-464318-g4", location="us-central1")

model = GenerativeModel("gemini-2.0-flash-lite")
response = model.generate_content("Write a Python function to reverse a string.")
print(response.text)
