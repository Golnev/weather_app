class CantGetIPAddress(Exception):
    """Program can`t get current IP Address"""

    def __init__(self):
        super().__init__()
        print(f'Program can`t get current IP Address')


class CantGetCoordinates(Exception):
    """Program can`t get current GPS coordinates"""

    def __init__(self):
        super().__init__()
        print(f'Program can`t get current GPS coordinates')


class ApiServiceError(Exception):
    def __init__(self):
        super().__init__()
        print('Api Error')
