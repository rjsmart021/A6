from typing import List, Tuple

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keyword_highlighted_reviews = []
keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words_list = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words_list = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def get_review_sentiment_tally(reviews: List[str], positive_words_list: List[str],
                               negative_words_list: List[str]) -> List[Tuple[int, int]]:
    """

    :param reviews: list of review of a products of type string
    :param positive_words_list: List of positive keywords to check in a review
    :param negative_words_list: List of negative keywords to check in a review
    :return: return list of positive of negative keyword tally for each review. The first item in
    the tuple with in the list is the positive word count and the second item is the negative word count
    """
    sentiment_tally = []
    for review in reviews:
        positive_words = 0
        negative_words = 0
        for word in positive_words_list:
            if word.lower() in review.lower():
                positive_words += 1

        for word in negative_words_list:
            if word.lower() in review.lower():
                negative_words += 1

        sentiment_tally.append((positive_words, negative_words))

    return sentiment_tally


def create_summary(reviews: List[str]) -> List[str]:
    """

    :param reviews: list of review of a products of type string
    :return: List of reviews with high lighted keywords.
    """
    summary_reviews = []
    for review in reviews:
        if len(review) <= 30:
            return review
        else:
            summary = review[:30]
            last_space_index = summary.rfind(" ")
            if last_space_index != -1:
                summary = summary[:last_space_index]
            summary += "…"
            summary_reviews.append(summary)
    return  summary_reviews


def highlight_keywords(review: str, keywords: List[str]) -> str:
    """
    This method will highlight the keywords present in each review to upper case.
    :param review: review of a product of type string
    :param keywords: List of keywords
    :return: string
    """
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())

    return review


def get_keyword_highlighted_reviews():
    if len(keyword_highlighted_reviews) == 0:
        print("Reviews are empty.")
        return
    else:
        return keyword_highlighted_reviews


highlighted_reviews = []

for review in reviews:
    keyword_highlighted_reviews.append(highlight_keywords(review, keywords))

print(get_keyword_highlighted_reviews())
print(get_review_sentiment_tally(reviews, positive_words_list, negative_words_list))
print(create_summary(reviews))
