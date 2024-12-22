# Plagiarism Checker

A simple plagiarism checker built using Python, Streamlit, and NLP techniques. This app checks the similarity between a user-provided text and a document uploaded by the user, giving a percentage that indicates how much of the text is similar to the document, helping users identify potential plagiarism.

## Features
- Upload a `.txt` document for comparison.
- Enter custom text for plagiarism check.
- Displays the plagiarism percentage based on the similarity to the uploaded document.
- Text is preprocessed with tokenization, stopword removal, and lemmatization.
- Provides a visual slider to show plagiarism strength.

## Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/plagiarism-checker.git
    cd plagiarism-checker
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download necessary NLTK datasets**:
    Run the following Python code to download required NLTK datasets:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')
    ```

5. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## How to Use

1. Upload a `.txt` document for comparison.
2. Enter the text you want to check for plagiarism.
3. The app will display the plagiarism percentage and similarity strength.

## Project Structure

