# Movie Review Sentiment Analyzer

A Transformer-based NLP application that classifies movie reviews as **Positive** or **Negative** using a fine-tuned DistilBERT model.

## Overview

This project explores sentiment classification by comparing traditional machine learning, recurrent neural networks, and Transformer-based NLP approaches. The selected model is integrated into a web application through a FastAPI backend and Streamlit frontend.

## Models Compared

| Model | Accuracy | F1-score |
|---|---:|---:|
| TF-IDF + Logistic Regression | 89.28% | 89.46% |
| Bidirectional LSTM | 83.86% | 83.53% |
| Fine-tuned DistilBERT | 90.81% | 90.79% |

*Note: These are validation results from the project experiments, not a clean final test-set evaluation. The dataset overlap audit identified some overlap with the official IMDb test split, which is a limitation to address in future evaluation.*

## Features

- Positive and negative sentiment predictions
- Prediction confidence and class probabilities
- FastAPI inference API
- Interactive Streamlit interface
- Sample reviews for quick testing
- Comparison of three NLP approaches

## Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- DistilBERT
- FastAPI
- Streamlit
- IMDb movie review dataset

## Project Structure

```text
Sentiment Analysis/
├── backend/
│   ├── main.py
│   └── distilbert_model/  # Download separately; not stored in Git
├── frontend/
│   └── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally

1. Install the dependencies listed in `requirements.txt`.
2. Place the trained model and tokenizer files inside `backend/distilbert_model/`.
3. Start the API from the project root:

   ```bash
   python -m uvicorn backend.main:app --reload
   ```

4. In a second terminal, launch the frontend:

   ```bash
   python -m streamlit run frontend/app.py
   ```

5. Open `http://localhost:8501` to use the application.
6. Open `http://127.0.0.1:8000/docs` to explore the API.

## Limitations

- Sarcasm and mixed sentiment can lead to incorrect predictions.
- Confidence scores represent model probabilities and do not guarantee correctness.
- Long reviews are truncated to the model's configured input length.

## Future Improvements

- Evaluate on a clean, independent test set
- Improve handling of sarcasm and nuanced sentiment
- Deploy the application with publicly accessible endpoints
- Add further error analysis and model comparisons

## Author

Built as a hands-on project in Natural Language Processing, Deep Learning, and API-based ML deployment.