class Session: ...


class SessionFactory:
    def session(self) -> Session:
        return Session()


# Пример наследования реализации.
# Классу Adapter для работы нужны некоторые сессии с другим компонентом
# (программной, модулем и т.д.), для их получения он наследует реализацию
# получения сессий от класса SessionFactory. Однако, Adapter не является
# частным случаем SessionFactory, ему нужны только сессии. Корректнее было
# бы заменить отношение наследования ассоциацией, так у класса Adapter
# было бы поле session_factory, в которое можно было бы передавать объекты
# SessionFactory и от них получать сессии.
class Adapter(SessionFactory):
    def do_something(self) -> None:
        print(self.session())


class Config:
    def __init__(self) -> None:
        self.param1 = 1
        self.param2 = "abc"


# Пример льготного наследования.
# Классу A для работы нужны значения param1 и param2,
# он наследуется от класса конфигурации Config,
# в котором описаны эти параметры. Но, логически,
# класс A не является частым случаем класса Config.
# Корректнее было бы заменить наследование композицией,
# чтобы у класса A было поле config, в которое можно было бы
# передавать объекты конфигураций.
class A(Config):
    def do_something(self) -> None:
        print(self.param1, self.param2)
