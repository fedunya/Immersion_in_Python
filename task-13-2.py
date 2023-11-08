class InvalidError(Exception):
    pass

class InvalidTextError(InvalidError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid text: {self.text}. Text should be a non-empty string.'

class InvalidNumberError(InvalidError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid number: {self.number}. Number should be a positive integer or float.'

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text, number):
        if not isinstance(text, (str)) or len(text) == 0:
            raise InvalidTextError(text)
        else:
            self.text = text
        if not isinstance(number, (int, float)) or number < 0:
            raise InvalidNumberError(number)
        else:
            self.number = number

    def __str__(self) -> str:
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text}' \
            f' and {self.archive_number}'

    def __repr__(self) -> str:
        return f"Archive('{self.text}', {self.number})"

archive1 = Archive("Запись 1", 42)
print(archive1)
print(repr(archive1))
archive2 = Archive("Запись 2", 3.14)
print(archive1)
print(repr(archive1))