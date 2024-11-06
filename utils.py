from file_manager import *


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
            log_exception(str(e))
    return wrapper


