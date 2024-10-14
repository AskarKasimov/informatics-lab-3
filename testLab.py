import unittest
import unittest.mock as mock
from main import *


class TestLab(unittest.TestCase):
    # first task
    def test_first_task_1(self):
        with mock.patch("builtins.input", return_value="Сегодня отличный день 8-|, а погода просто чудесная! 8-| Мы решили пойти гулять в парк, где много деревьев 8-| и приятная атмосфера."):
            self.assertEqual(first_task(), 3)

    def test_first_task_2(self):
        with mock.patch("builtins.input", return_value=""):
            self.assertEqual(first_task(), 0)

    def test_first_task_3(self):
        with mock.patch("builtins.input", return_value="9-|8-||-8-8-|--|7--"):
            self.assertEqual(first_task(), 2)

    def test_first_task_4(self):
        with mock.patch("builtins.input", return_value="Привет, как дела? 8-| Я сегодня сделал много дел 8-|, но всё ещё чувствую, что не успел завершить всё, что планировал. 8-|"):
            self.assertEqual(first_task(), 3)

    def test_first_task_5(self):
        with mock.patch("builtins.input", return_value="М9-|ы приехали на дачу 8-|, и сразу8-| пошёл дождь. В8-|сё бы ничего, но я забыл зонт 8 -|, пришлось прятаться под деревом."):
            self.assertEqual(first_task(), 3)

    # second task
    def test_second_task_1(self):
        with mock.patch("builtins.input", return_value="Вечер за окном. / Еще один день прожит. / Жизнь скоротечна..."):
            self.assertEqual(second_task(), "Хайку!")

    def test_second_task_2(self):
        with mock.patch("builtins.input", return_value="Вечер за окном. / Еще один день прожит. / Жизнь скоротечна... / Зима на дворе..."):
            self.assertEqual(second_task(), "Не хайку. Должно быть 3 строки.")

    def test_second_task_3(self):
        with mock.patch("builtins.input", return_value="Вечер за окном. \\ Еще один день прожит. / Жизнь скоротечна..."):
            self.assertEqual(second_task(), "Не хайку. Должно быть 3 строки.")

    def test_second_task_4(self):
        with mock.patch("builtins.input", return_value="///"):
            self.assertEqual(second_task(), "Не хайку. Должно быть 3 строки.")

    def test_second_task_5(self):
        with mock.patch("builtins.input", return_value="Как сад похорошел! / И яблоки с дерев упали / Жаль, нет сегодня тебя рядом."):
            self.assertEqual(second_task(), "Не хайку.")

    # third task
    def test_third_task_1(self):
        with mock.patch("builtins.input", return_value="30 18 * * 1,4"):
            self.assertEqual(third_task(), True)

    def test_third_task_2(self):
        with mock.patch("builtins.input", return_value="30 9 * * 1"):
            self.assertEqual(third_task(), True)

    def test_third_task_3(self):
        with mock.patch("builtins.input", return_value="59 14 * * 1-5"):
            self.assertEqual(third_task(), True)

    def test_third_task_4(self):
        with mock.patch("builtins.input", return_value="*/10 9-17 * * 1-5"):
            self.assertEqual(third_task(), True)

    def test_third_task_5(self):
        with mock.patch("builtins.input", return_value="* 25 15 6 3"):
            self.assertEqual(third_task(), False)


if __name__ == "__main__":
    unittest.main()
