from tetris import Game


class App:
    """
    **Главный класс**\n
    имеет в себе один статический метод для запуска приложения\n
    да это c++/java ООП подходы в python)
    """

    @staticmethod
    def start() -> None:
        game = Game()
        game.run()


if __name__ == "__main__":
    App.start()
