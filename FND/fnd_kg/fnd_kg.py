import joblib
import pandas as pd
import re
import string

# Load the logistic regression model and vectorizer
def load_model():
    """
    Load the trained logistic regression model and vectorizer
    """
    model_file = 'C:\\develop\\code\\2_projects\\python\\FND\\fnd_kg\\logistic_regression_model.pkl'
    vectorizer_file = 'C:\\develop\\code\\2_projects\\python\\FND\\fnd_kg\\tfidf_vectorizer.pkl'
    
    try:
        model = joblib.load(model_file)
        vectorizer = joblib.load(vectorizer_file)
        print("***Model loaded successfully.")
        return model, vectorizer
    except FileNotFoundError:
        print("Model files not found. Make sure to save the models first.")
        return None, None

# Text preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]','',text)
    text = re.sub('[()]','',text)
    text = re.sub('\\W',' ',text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# function for prediction
def predict_news(news_text, model, vectorizer):
    """
    Predict if news is fake or real using logistic regression
    """
    processed_text = wordopt(news_text)                                   # Preprocess the news text
    test_data = pd.DataFrame({"text": [processed_text]})                  # Create DataFrame (same format as training)
    text_vectorized = vectorizer.transform(test_data["text"])             # Transform text to TF-IDF features
    prediction = model.predict(text_vectorized)[0]                        # Make prediction
    confidence = model.predict_proba(text_vectorized)[0]
    result = "Real News" if prediction == 1 else "Fake News"              # Format result
    confidence_score = confidence[1] if prediction == 1 else confidence[0]
    
    print(f"\nNews Analysis Result:")
    print(f"Prediction: {result}")
    print(f"Confidence: {confidence_score:.2%}")
    print("-" * 30)
    
    return result, confidence_score

# Main function for continuous news analysis
def run_fake_news_detector():
    """
    Run the fake news detector with continuous user input
    """
    print("-" * 30 +"\nUsing logistic regression for prediction.\n"+"-" * 30)
    
    # Load model once at startup
    model, vectorizer = load_model()
    if model is None:
        return
    
    print("\n*** Type 'quit' to exit. ***")
    while True:
        news_text = input("Enter news text or paragraph to analyze: ").strip()
        if news_text.lower() == 'quit':
            print("Program terminated...")
            break
        if news_text:
            predict_news(news_text, model, vectorizer)
        else:
            print("Invalid input, please enter some news text.")
# Start the application
if __name__ == "__main__":
    run_fake_news_detector()