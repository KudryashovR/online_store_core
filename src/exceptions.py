class AddZeroQuantityException(Exception):
    """
    Класс исключения при попытке добавить товар в количестве 0 едениц.
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Товар с нулевым количеством не может быть добавлен'

    def __str__(self):
        return self.message
