from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import Counter
import string

# Make sure to download NLTK resources
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def preprocess_review(review):
    """Removes stopwords, punctuation, and converts to lowercase."""
    stop_words = set(stopwords.words('english'))
    # Lowercase
    review = review.lower()
    # Remove punctuation
    review = review.translate(str.maketrans('', '', string.punctuation))
    # Tokenize and remove stopwords
    tokens = word_tokenize(review)
    preprocessed_review = [word for word in tokens if word not in stop_words]
    return preprocessed_review

def analyze_sentiment(preprocessed_review):
    """Calculates polarity and subjectivity using TextBlob."""
    text = " ".join(preprocessed_review)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity       # -1 (negative) to 1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
    return polarity, subjectivity

def extract_keywords(preprocessed_review, top_n=5):
    """Identifies the most frequent nouns and adjectives."""
    tagged_words = pos_tag(preprocessed_review)
    # Keep only nouns (NN, NNS) and adjectives (JJ, JJR, JJS)
    filtered_words = [word for word, pos in tagged_words if pos.startswith('NN') or pos.startswith('JJ')]
    # Count frequency
    word_counts = Counter(filtered_words)
    keywords = [word for word, count in word_counts.most_common(top_n)]
    return keywords

def categorize_review(polarity, subjectivity, keywords):
    """Classifies reviews based on polarity, subjectivity, and keywords."""
    if polarity > 0.2:
        category = "Positive"
    elif polarity < -0.2:
        category = "Negative"
    else:
        category = "Neutral"

    # Optionally, refine using subjectivity
    if subjectivity > 0.6:
        category += " & Subjective"
    else:
        category += " & Objective"

    # You could also use keywords for custom classification rules if needed
    return category
