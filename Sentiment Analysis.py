from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

while True:
  # Get user input
  user_input = input("Enter a sentence to analyze (or 'q' to quit): ")

  # Check for quit command
  if user_input.lower() == "q":
    break

  # Analyze sentiment using pipeline
  sentiment_analysis = sentiment_pipeline([user_input])

  # Print the analysis result
  print(f"Sentiment: {sentiment_analysis[0]['label']} | Score: {sentiment_analysis[0]['score']}")

print("Thank you for using the sentiment analysis tool!")
