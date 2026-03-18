# Offline Customer Support Chatbot

---

##  Features

| Feature | Description |
|---------|-------------|
|  **100% Offline** | All processing on your local machine - no data sent to cloud |
|  **Llama 3.2 3B** | Meta's latest open-source model optimized for consumer hardware |
|  **20 E-commerce Queries** | Realistic customer support scenarios (shipping, returns, payments, etc.) |
|  **Prompt Comparison** | Compares Zero-shot vs One-shot prompting strategies |
|  **Auto-generated Reports** | Results automatically saved in Markdown format |
|  **Easy Setup** | Works on Windows, Mac, and Linux |

---

##  Project Structure

```
offline-support-chatbot/
│
├── chatbot.py              # Main Python script
├── README.md               # This file
├── setup.md                # Detailed setup instructions
├── report.md               # Complete analysis report
│
├── prompts/                # Prompt templates
│   ├── zero_shot_template.txt    # Instructions only
│   └── one_shot_template.txt     # Instructions + example
│
└── eval/                   # Evaluation results
    └── results.md          # Generated responses for all 20 queries
```

---

##  Quick Start (5 Minutes)
## watch the demo: https://drive.google.com/file/d/1EKaLvu8-yn9bxOccWz_unHvZ9jrAtmTV/view?usp=sharing
### Prerequisites
- Python 3.8 or higher
- 4GB RAM (8GB recommended)
- 2GB free disk space

### One-Line Setup

```bash
# 1. Install Ollama (download from https://ollama.com)

# 2. Download the model
ollama pull llama3.2:3b

# 3. Clone and setup
git clone https://github.com/Kusubhavani/offline-support-chatbot.git
cd offline-support-chatbot
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install requests datasets

# 4. Run the chatbot
python chatbot.py
```

**That's it!** Results will be saved in `eval/results.md` 🎉

---

## 🔧 Detailed Setup (If Needed)

### Windows
```powershell
# Open PowerShell as Administrator
cd C:\Users\YourName\Desktop
git clone https://github.com/Kusubhavani/offline-support-chatbot.git
cd offline-support-chatbot
python -m venv venv
venv\Scripts\activate
pip install requests datasets
python chatbot.py
```

## How It Works

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌─────────────┐
│             │     │              │     │             │     │             │
│ chatbot.py  │────▶│  Prompt      │────▶│  Ollama     │────▶│  Llama 3.2  │
│ (Client)    │     │  Templates   │     │  Server     │     │  (Model)    │
│             │◀────│              │◀────│             │◀────│             │
└─────────────┘     └──────────────┘     └─────────────┘     └─────────────┘
       │                                                              │
       │                      ┌──────────────┐                        │
       └─────────────────────▶│  eval/       │◀───────────────────────┘
                              │  results.md  │
                              └──────────────┘
```

1. **Reads** 20 customer queries from the script
2. **Formats** them using prompt templates
3. **Sends** to local Ollama API
4. **Gets** responses from Llama 3.2
5. **Saves** everything to `results.md`

---

##  Sample Queries

The chatbot handles 20 common customer questions:

| # | Category | Example Query |
|---|----------|---------------|
| 1 |  Shipping | "How can I track my order?" |
| 2 |  Payments | "My discount code isn't working" |
| 3 |  Address | "Can I change my delivery address?" |
| 4 |  Returns | "How do I return an item?" |
| 5 |  Payment | "What payment methods do you accept?" |
| 6 |  Wrong Item | "I received the wrong product" |
| 7 |  Delay | "My order hasn't arrived yet" |
| 8 |  Delivery | "How long does delivery take?" |
| 9 |  Cancellation | "Can I cancel my order?" |
| 10 |  Shipping | "Do you offer international shipping?" |
| 11 |  Password | "How do I reset my password?" |
| 12 |  Declined | "Why was my payment declined?" |
| 13 |  Exchange | "Can I exchange a product?" |
| 14 |  Invoice | "Where can I download my invoice?" |
| 15 |  Warranty | "Is there a warranty?" |
| 16 |  Gift Card | "How do I apply a gift card?" |
| 17 |  Damaged | "Package arrived damaged" |
| 18 |  Contact | "How do I contact support?" |
| 19 |  Quantity | "Can I update quantity?" |
| 20 |  Sale | "Refunds for sale items?" |

---

## Results Summary

After evaluating 40 responses (20 zero-shot + 20 one-shot):

| Method | Relevance | Coherence | Helpfulness | Overall |
|--------|-----------|-----------|-------------|---------|
| **Zero-Shot** | 4.5 | 5.0 | 4.3 | 4.6 |
| **One-Shot** | 4.2 | 5.0 | 4.0 | 4.4 |

**Key Finding:** Zero-shot prompting performed slightly better for this specific use case, providing more comprehensive answers.

*See [report.md](report.md) for detailed analysis*

---

##  Performance

| Metric | Value |
|--------|-------|
| **Response Time** | 5-30 seconds per query (CPU dependent) |
| **Memory Usage** | ~2.5GB RAM |
| **Model Size** | 2GB download, 2.5GB when loaded |
| **Total Runtime** | 5-10 minutes for all 20 queries |

---

##  Acknowledgments

- **Meta AI** for releasing Llama 3.2 open-source
- **Ollama Team** for making local LLMs accessible
- **Ubuntu Dialogue Corpus** for query inspiration
- **Partnr Network** for the project requirements

---

##  Contact

- GitHub: [@Kusubhavani](https://github.com/Kusubhavani)
- Project Link: [https://github.com/Kusubhavani/offline-support-chatbot]

---
