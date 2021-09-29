class CarError(Exception):
    pass


class OutOfGazError(CarError):
    def __init__(self, message: str, move_time: float):
        super().__init__(message)
        self.move_time = move_time


class CarNotFound(Exception):
    def __init__(self, id: int):
        self.id = id


class BadCarName(Exception):
    pass


class BadTokenError(Exception):
    pass


class BadTokenFormatError(BadTokenError):
    pass
