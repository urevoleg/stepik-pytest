

class ExternalLogger():
    @staticmethod
    def send(self, message: str):
        print(message)

external_logger = ExternalLogger()

def log_message(message):
    # Эта функция ничего не возвращает, только вызывает другую
    external_logger.send(message)