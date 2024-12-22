import csv
import string
import nltk
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import io

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Streamlit UI elements
st.image('https://infobeat.com/wp-content/uploads/2018/08/featured-image.png')
st.title("Plagiarism Checker")

# Text preprocessing function
def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    preprocessed_text = ' '.join(filtered_tokens)
    return preprocessed_text

@st.cache_data
def load_documents(file):
    documents = []
    try:
        # Handle file upload as a stream
        file_content = io.StringIO(file.getvalue().decode("utf-8"))
        for line in file_content:
            documents.append(preprocess_text(line.strip()))
    except Exception as e:
        st.error(f"Error while processing the file: {e}")
    return documents

# Upload file and process
uploaded_file = st.file_uploader("Upload your document for plagiarism check", type=["txt"])
if uploaded_file:
    documents = load_documents(uploaded_file)
    
    if documents:
        st.success("Documents loaded and preprocessed successfully!")
        
        # User input for plagiarism check
        user_text = st.text_area("Enter text for plagiarism check:")
        if user_text:
            preprocessed_user_text = preprocess_text(user_text)
            vectorizer = TfidfVectorizer()
            
            # Handle empty document list case
            if not documents:
                st.warning("No text to compare. Please upload a valid document.")
            else:
                tfidf_vectors = vectorizer.fit_transform(documents)
                user_tfidf_vector = vectorizer.transform([preprocessed_user_text])
                similarities = cosine_similarity(user_tfidf_vector, tfidf_vectors)
                
                # Calculate plagiarism percentage
                max_similarity = max(similarities[0])
                plagiarism_percentage = max_similarity * 100
                
                st.subheader("Similarity Results")
                st.write(f"Plagiarism Strength: {plagiarism_percentage:.2f}%")
                
                # Display plagiarism percentage in a slider
                plagiarism_slider = st.slider(
                    label="Plagiarism Strength",
                    min_value=0,
                    max_value=100,
                    value=int(plagiarism_percentage),
                    step=1,
                    disabled=True
                )
                

                
                # Decision based on similarity
                if max_similarity > 0.7:
                    st.write(f"The entered text is {plagiarism_percentage:.2f}% similar to the document, indicating potential plagiarism.")
                else:
                    uniqueness_percentage = (1 - max_similarity) * 100
                    st.write(f"The entered text is {uniqueness_percentage:.2f}% unique.")
    else:
        st.warning("The document is empty or not valid. Please upload a valid text file.")
else:
    st.warning("Please upload a document to check plagiarism.")
