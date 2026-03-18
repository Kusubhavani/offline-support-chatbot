# Setup Guide

This document explains how to install the required tools and run the **Offline Customer Support Chatbot using Ollama and Llama 3.2**.

---

# 1. Install Ollama

Download and install Ollama from the official website:

https://ollama.com

After installation, verify it by running:

```
ollama --version
```

If Ollama is installed correctly, the version number will appear.

---

# 2. Download the Llama 3.2 Model

Pull the Llama 3.2 (3B) model using the following command:

```
ollama pull llama3.2:3b
```

The model size is approximately **2GB**, so downloading may take some time depending on your internet speed.

---

# 3. Test the Model (Optional)

You can test whether the model works correctly:

```
ollama run llama3.2:3b
```

Type any message to see the response.

Example:

```
Hello
```

To exit:

```
/bye
```

---

# 4. Clone or Create the Project Folder

Create the project directory with the following structure:

```
offline-support-chatbot/
│
├── chatbot.py
├── README.md
├── setup.md
├── report.md
│
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
│
└── eval/
    └── results.md
```

---

# 5. Create a Python Virtual Environment

Navigate to your project directory and run:

```
python -m venv venv
```

Activate the environment.

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

---

# 6. Install Required Python Libraries

Install the required dependencies:

```
pip install requests datasets
```

Libraries used:

* **requests** → for communicating with the Ollama API
* **datasets** → for accessing the Ubuntu Dialogue Corpus

---

# 7. Ensure Ollama Server is Running

The Ollama server usually runs automatically after installation.

To verify it is working, open your browser and visit:

```
http://localhost:11434
```

Or run a model command in the terminal.

---

# 8. Run the Chatbot Script

Execute the Python script:

```
python chatbot.py
```

The script will:

1. Load the prompt templates
2. Process 20 customer queries
3. Send prompts to the Ollama API
4. Receive model responses
5. Save the results

---

# 9. View the Output

After the script finishes, open the results file:

```
eval/results.md
```

This file will contain:

* Customer queries
* Zero-shot responses
* One-shot responses

You can manually evaluate the responses using the scoring rubric.

---

# 10. Troubleshooting

### Ollama not responding

Make sure the Ollama service is running and the endpoint is correct:

```
http://localhost:11434/api/generate
```

---

### Slow responses

Running LLMs locally on CPU may take several seconds per response. This is normal.

---

### Model not found

Run the command again:

```
ollama pull llama3.2:3b
```

---

# 11. Project Execution Summary

1. Install Ollama
2. Pull the Llama 3.2 model
3. Create Python environment
4. Install dependencies
5. Run `chatbot.py`
6. Check results in `eval/results.md`

---

Your chatbot is now running **completely offline using a local LLM**.
