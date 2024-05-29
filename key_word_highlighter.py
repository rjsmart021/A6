from typing import List

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]


def high_light_keyword(review: str, keywords: List[str]) -> str:
    """

    :param review: review of a product of type string
    :param keywords: List of keywords
    :return: string
    """
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())

    return review


highlighted_reviews = []

for review in reviews:
    highlighted_reviews.append(high_light_keyword(review, keywords))

print(highlighted_reviews)
