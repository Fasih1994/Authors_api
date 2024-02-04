import re
from math import ceil


class ArticleReadTimeEngine:
    @staticmethod
    def word_count(text):
        words = re.findall(r"\w+", text)
        return len(words)

    @staticmethod
    def estimate_reading_time(
        article,
        words_per_minute: int = 250,
        seconds_per_image: int = 10,
        seconds_per_tag: int = 2,
    ):
        word_count_body = ArticleReadTimeEngine.word_count(article.body)
        word_count_title = ArticleReadTimeEngine.word_count(article.title)
        word_count_description = ArticleReadTimeEngine.word_count(article.description)

        total_word_count = word_count_body + word_count_title + word_count_description

        reading_time = total_word_count / words_per_minute

        if article.banner_image:
            reading_time += seconds_per_image / 60

        tag_count = article.tags.count()
        reading_time += (tag_count * seconds_per_tag) / 60

        reading_time = ceil(reading_time)

        return reading_time
