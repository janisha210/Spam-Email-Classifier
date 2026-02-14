"""
Script to create a sample spam classifier model for demonstration
This creates a TF-IDF + MultinomialNB pipeline as specified
"""
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample training data
spam_emails = [
    "Congratulations! You've won a free prize. Click here now!",
    "URGENT: Your account will be closed. Verify now!",
    "Get rich quick! Make $5000 per week from home!",
    "Free money! Click this link immediately!",
    "You have won the lottery! Claim your prize now!",
    "Limited time offer! Buy now and get 90% off!",
    "Lose weight fast with this one weird trick!",
    "Your package is waiting. Pay shipping fee to receive.",
    "Congratulations! You've been selected for a special offer!",
    "Act now! This offer expires in 24 hours!",
]

safe_emails = [
    "Hi, let's schedule a meeting for next Tuesday at 2pm.",
    "Thanks for your email. I'll review the document and get back to you.",
    "The project deadline has been moved to next Friday.",
    "Please find attached the report you requested.",
    "Can you send me the latest version of the presentation?",
    "I'll be out of office next week. Please contact my colleague.",
    "The team meeting is scheduled for tomorrow at 10am.",
    "Thank you for your purchase. Your order has been confirmed.",
    "Your subscription has been renewed successfully.",
    "Here are the meeting notes from yesterday's discussion.",
]

# Combine data
X_train = spam_emails + safe_emails
y_train = [1] * len(spam_emails) + [0] * len(safe_emails)  # 1 = spam, 0 = safe

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english')),
    ('classifier', MultinomialNB())
])

# Train the model
print("Training spam classifier...")
pipeline.fit(X_train, y_train)

# Test the model
test_spam = "Congratulations! You won a prize!"
test_safe = "Let's meet tomorrow for coffee."

print(f"\nTest predictions:")
print(f"'{test_spam}' -> {pipeline.predict([test_spam])[0]} (spam=1, safe=0)")
print(f"'{test_safe}' -> {pipeline.predict([test_safe])[0]} (spam=1, safe=0)")

# Save the model
model_path = "spam_model.pkl"
with open(model_path, 'wb') as f:
    pickle.dump(pipeline, f)

print(f"\nModel saved to {model_path}")
print("You can now run the FastAPI backend!")
