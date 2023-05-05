import openai
import os

openai.api_key = "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"


def context_summary(tweets):
    prompt = f"Generate an overall summary of these tweets ( what are they talking about 'context', etc..) \n\n "
    for tweet in tweets:
        prompt += f"Tweet: {tweet['tweet_text']} \n"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=200,
      temperature=0.7
    )

    response = response.choices[0].text
    return response
