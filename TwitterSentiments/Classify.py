import cohere
from cohere.responses.classify import Example
co = cohere.Client('qGwbbyFxTCk86PNl53kcvzzvGSpAfzSC9cVvCrCz')
import json
import math

examples = [
    Example("I love spending time with my family ❤️", "Positive"),
    Example("This is the worst day ever! 😡", "Negative"),
    Example("Just finished a great workout 💪", "Positive"),
    Example("I hate it when my flight gets delayed 🙄", "Negative"),
    Example("So excited for the concert tonight! 🎤", "Positive"),
    Example("This traffic is making me late for my appointment 😩", "Negative"),
    Example("Enjoying a relaxing day at the beach 🏖️", "Positive"),
    Example("I can't believe how terrible this movie is 🤮", "Negative"),
    Example("Had a delicious meal at my favorite restaurant 🍽️", "Positive"),
    Example("I can't stand this rainy weather ☔", "Negative"),
    Example("Just got a promotion at work! 🎉", "Positive"),
    Example("I'm so sick of being stuck in quarantine 🤒", "Negative"),
    Example("What a beautiful sunset 🌅", "Positive"),
    Example("I can't believe I lost my phone again 😔", "Negative"),
    Example("Had a great time with friends at the game last night 🏀", "Positive"),
    Example("I'm so over this pandemic 😷", "Negative"),
    Example("Just got back from an amazing vacation! 🌴", "Positive"),
    Example("Why does everything always go wrong for me? 😞", "Negative"),
    Example("I love my new job, it's so fulfilling! 😊", "Positive"),
    Example("The weather is nice today ☀️", "Neutral"),
    Example("I need to buy groceries later 🛒", "Neutral"),
    Example("I'm feeling a little tired today 😴", "Neutral"),
    Example("I'm learning a new programming language 🤓", "Neutral"),
    Example("I'm not sure what to have for dinner tonight 🤔", "Neutral"),
]


def classify_tweets(tweets):
    inputs = [tweet['tweet_text'] for tweet in tweets]
    response = co.classify(
      model='large',
      inputs=inputs,
      examples=examples,
    )
    classified_tweets = []
    for i, classification in enumerate(response.classifications):

      predictions = classification.labels
      label = classification.prediction
      confidence = predictions[label].confidence
      confidence = math.floor(confidence * 100) / 100
      # add the sentiment and confidence to the tweet
      tweets[i]['sentiment'] = label
      tweets[i]['confidence'] = confidence
      classified_tweets.append(tweets[i])
      
    return classified_tweets
    