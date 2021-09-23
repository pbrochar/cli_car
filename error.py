class CarNotFound(Exception):
    def __init__(self, id):
        self.id = id
    