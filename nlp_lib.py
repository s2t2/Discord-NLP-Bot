from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def rank_score(score: float) -> str:
    s = abs(score)
    if s > 74:
        return 'Very '
    elif s < 51:
        return 'Sorta '
    else:
        return ''


def sentiment_score(sentence: str) -> str:
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    score = int(round(sentiment_dict['compound'] * 100))
    if score > 16:
        return f'{rank_score(score)}Positive'
    elif score < -16:
        return f'{rank_score(score)}Negative'
    else:
        return "Neutral"


if __name__ == '__main__':
    test_cases = (
        "positive",
        "negative",
        "i like it, but it's weird",
        "Yes, I love that idea, tell me more please!",
        "Hell no, I will not eat green eggs and ham, eww yuck gross bad!",
        "kinda like it",
        "kinda don't like it",
    )
    for case in test_cases:
        print(sentiment_score(case))
