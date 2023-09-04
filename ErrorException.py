class ErrorException(Exception):
    def __str__(self):
        return "허용되지 않습니다."