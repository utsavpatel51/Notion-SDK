from requests.models import HTTPError


class HTTP400Error(HTTPError):
    def __init__(self, response: dict) -> None:
        error_mes = "code:- %s\nmessage:-%s" % (
                     response.get('code'), response.get('message'))
        super().__init__(error_mes)
