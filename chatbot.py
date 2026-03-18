import requests
import json
import os
from datetime import datetime

# =========================
# Configuration
# =========================

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

PROMPT_DIR = "prompts"
RESULT_FILE = "eval/results.md"


# =========================
# Load Prompt Templates
# =========================

def load_template(file_name):
    path = os.path.join(PROMPT_DIR, file_name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# =========================
# Query Ollama API
# =========================

def query_ollama(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)

        response.raise_for_status()

        data = json.loads(response.text)

        return data.get("response", "").strip()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "ERROR: Could not retrieve response from Ollama."


# =========================
# Customer Queries (20)
# =========================

queries = [

"How can I track the shipping status of my order?",
"My discount code isn't working at checkout.",
"Can I change my delivery address after placing an order?",
"How do I return an item I purchased?",
"What payment methods do you accept?",
"I received the wrong product. What should I do?",
"My order hasn't arrived yet. Can you help?",
"How long does delivery usually take?",
"Can I cancel my order after placing it?",
"Do you offer international shipping?",
"How do I reset my account password?",
"Why was my payment declined?",
"Can I exchange a product instead of returning it?",
"Where can I download my invoice?",
"Is there a warranty on the products you sell?",
"How do I apply a gift card to my order?",
"What should I do if my package arrives damaged?",
"How do I contact customer support?",
"Can I update the quantity of items in my order?",
"Do you offer refunds for sale items?"

]


# =========================
# Write Results
# =========================

def write_results():

    zero_template = load_template("zero_shot_template.txt")
    one_template = load_template("one_shot_template.txt")

    os.makedirs("eval", exist_ok=True)

    with open(RESULT_FILE, "w", encoding="utf-8") as f:

        f.write("# Chatbot Evaluation Results\n\n")
        f.write(f"Generated on: {datetime.now()}\n\n")

        for i, query in enumerate(queries, start=1):

            print(f"Processing Query {i}/20")

            zero_prompt = zero_template.format(query=query)
            one_prompt = one_template.format(query=query)

            zero_response = query_ollama(zero_prompt)
            one_response = query_ollama(one_prompt)

            f.write(f"## Query {i}\n")
            f.write(f"**Customer Query:** {query}\n\n")

            f.write("### Zero-Shot Response\n")
            f.write(zero_response + "\n\n")

            f.write("### One-Shot Response\n")
            f.write(one_response + "\n\n")

            f.write("---\n\n")


# =========================
# Main
# =========================

if __name__ == "__main__":
    write_results()
    print("\nEvaluation complete. Results saved in eval/results.md")