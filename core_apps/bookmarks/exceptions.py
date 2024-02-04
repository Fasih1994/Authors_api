from rest_framework.exceptions import APIException


class AlreadyBookmarkedArticle(APIException):
    status_code = 400
    default_detail = "You have already bookmarked this article"
    default_code = "bad_request"
