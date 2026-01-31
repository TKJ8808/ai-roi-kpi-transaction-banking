import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train_sentiment_model(df: pd.DataFrame):
    """
    Train a simple sentiment classifier on operational feedback.
    """

    # Weak supervision for demo purposes
    labels = []
    for text in df["feedback_text"].str.lower():
        if any(word in text for word in ["reduced", "positive", "improved", "helpful", "saves"]):
            labels.append("positive")
        elif any(word in text for word in ["too many", "needs", "errors", "high"]):
            labels.append("negative")
        else:
            labels.append("neutral")

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(df["feedback_text"])

    model = LogisticRegression(max_iter=200)
    model.fit(X, labels)

    return model, vectorizer


def predict_sentiment(model, vectorizer, text: str) -> str:
    """
    Predict sentiment for new feedback text.
    """
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]


if __name__ == "__main__":
    df = pd.read_csv("data/feedback.csv")

    model, vectorizer = train_sentiment_model(df)

    print("=== FEEDBACK SENTIMENT ANALYSIS ===")
    for text in df["feedback_text"]:
        sentiment = predict_sentiment(model, vectorizer, text)
        print(f"[{sentiment.upper()}] {text}")
