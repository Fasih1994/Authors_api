from rest_framework.exceptions import APIException


class YouHaveAlreadyRatted(APIException):
    status_code = 400
    default_detail = "You have already ratted this article"
    default_code = "bad_request"
