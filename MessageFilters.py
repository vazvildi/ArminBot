from aiogram import Bot, Dispatcher, executor, types  # Импортируем классы из библиотеки
from aiogram.dispatcher.filters import Filter
import emoji
API_TOKEN = '1765441335:AAEt2XDGK4iE5E1JLfIMpRmS0NNhzzsuZdU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class SunFilter(Filter):
    messages = ['тправь солн',
                'кинь солн',
                'то солн',
                'окажи солн',
                'де солн']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Bertrolt(Filter):
    messages = ['ото Бертрольда', 'ото Бертрольта', 'ото бертрольта', 'ото бертрольда']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Jan(Filter):
    messages = ['ото Жан', 'ото жан']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Zik(Filter):
    messages = ['ото Зик', 'ото зик']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Konni(Filter):
    messages = ['ото Конни', 'ото конни']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Levi(Filter):
    messages = ['ото Леви', 'ото леви']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Mikasa(Filter):
    messages = ['ото Микасы', 'ото микасы']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Rayner(Filter):
    messages = ['ото Райнера', 'ото райнера']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Sasha(Filter):
    messages = ['ото Саши', 'ото саши']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Hangi(Filter):
    messages = ['ото Ханджи', 'ото ханджи', 'ото Ханжи', 'ото ханжи']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Historiya(Filter):
    messages = ['ото Хистории', 'ото хистории']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Anni(Filter):
    messages = ['ото Энни', 'ото энни', 'ото Анни', 'ото анни']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Ervin(Filter):
    messages = ['ото Эрвин', 'ото эрвин', 'ото Эрвина Смит', 'ото эрвина смит']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Eren(Filter):
    messages = ['ото Эрен', 'ото эрен']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class Flok(Filter):
    messages = ['ото Флок', 'ото флок']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class WelcomeFilter(Filter):
    messages = ['ривет', 'хай', 'Хай', 'дравствуй', 'Охаё', 'охаё', 'оничива', 'оничиуа', 'обрый день', 'обрый вечер',
                'оброе утро']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class HowAreYouFilter(Filter):
    messages = ['ормально', 'орошо', 'еплохо', 'удесно', 'рекрасно']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False


class HowAreYouTwoFilter(Filter):
    messages = ['ойдёт', 'лохо', 'Так себе', 'так себе']

    async def check(self, message: types.Message):
        text = message.text
        for x in self.messages:
            if x in text:
                return True
        return False





