# singleton.py
class Singleton:
    def __init__(self):
        pass

singleton = Singleton()


# using metaclass
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        pass


# using decorator
def singleton(cls):
    _instances = {}
    def getinstance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return getinstance

@singleton
class Singleton:
    def __init__(self):
        pass
