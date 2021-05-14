import logging  # Импортируем модуль логгирования
import emoji  # Импортируем эмоджи
from aiogram import Bot, Dispatcher, executor, types  # Импортируем классы из библиотеки
from aiogram.dispatcher.filters import Filter # Импортируем класс фильтров
from MessageFilters import WelcomeFilter, SunFilter, Bertrolt, Jan, Zik, Konni, Levi, Mikasa, Rayner, Sasha, Hangi, \
    Historiya, Anni, Ervin, Eren, Flok, HowAreYouFilter, HowAreYouTwoFilter


API_TOKEN = '1765441335:AAEt2XDGK4iE5E1JLfIMpRmS0NNhzzsuZdU'
# Устанавливаем уровень логгирования
logging.basicConfig(level=logging.INFO)
# Инициализируем бота и диспатчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
# Диспатчер получает команду от пользователя
async def send_welcome(message: types.Message):
    # Создание асинхронной функции с параметром сообщения
    await message.answer("Охаё, меня зовут Армин Арлерт, я — солдат разведкорпуса, люблю любоваться морем и тобой")
    # Пишем в чат от лица бота реакцию в виде приветствия на данную команду


@dp.message_handler(commands=['help'])
# Диспатчер получает команду от пользователя
async def send_help(message: types.Message):
    # Создание асинхронной функции с параметром сообщения
    await message.answer("Тебе нужна помощь? Напиши /start, чтобы начать со мной диалог."
                         " Обещаю буду хорошим собеседником, буду писать и интересоваться как ты, "
                         "отравлять мои и друзей фото. Ещё могу рассказать что-нибудь или ответить на твой вопрос."
                         " Надеюсь мы поладим")
    # Пишем в чат от лица бота реакцию в виде справки на данную команду


@dp.message_handler(SunFilter())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/69/7a/ad/697aad4b7fd07f3bc3dc5a179169bca9.jpg'
    caption = "Вот моё солнышко! :heart: :sunny:"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Bertrolt())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/originals/40/90/b6/4090b649ecde9f93c5d19e41cdd8c288.jpg'
    caption = "Ну, Бертрольт тихий, замкнутый. Знаю, что он друг детства Райнера"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Jan())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/e7/04/93/e704930162208c4b953f294d90506448.jpg'
    caption = "Жан, мой хороший друг, всегда говорит то, что думает. Эрен называет его конём, но они хорошие друзья)"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Zik())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/b5/07/34/b5073437badfb4a75c2af3702f175048.jpg'
    caption = "Я знаю, что Зик - брат Эрена, ну он странно себя ведёт, ещё и обезьяна"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Konni())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/af/37/7c/af377ceaaff0849d6f0849fe08a1415a.jpg'
    caption = "Конни, он конечно глуповат, но добрый и всегда поможет. А ещё мне иногда кажется, они с Сашей - брат " \
              "и сестра "
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Levi())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/72/0b/1e/720b1ec806d7c7c2ffd57704936e25e0.jpg'
    caption = "Леви- вторая рука Эрвина. Сильнейший воин человечества. На самом деле, его боятся, ведь он очень " \
              "строгий! Но Леви всегда приходит на помощь, за что его и уважают. А еще жуткий чистюля..."
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Mikasa())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/0f/37/32/0f3732c36b5134342f5e915c0ddccca1.jpg'
    caption = "Сестрёнка Эрена, моя подруга детства и одна из лучших воинов в мире, любимая Микаса"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Rayner())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/0b/e3/be/0be3bee3254e5a751919bfc887d75f06.jpg'
    caption = "Райнер - сильный, странный, постоянно водится с Бертрольтом"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Sasha())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/20/ff/bd/20ffbd9a1676114d29e71fb2acadde09.jpg'
    caption = "Любительница поесть, необычная девушка и хороший воин. Ну конечно и хорошая подруга Конни"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Hangi())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/f0/17/40/f01740402178df8771cbf4aeb993e503.jpg'
    caption = "Я очень уважаю Ханджи! Она отличный лидер и воин! Но лучше не заводить с ней разговор на тему титанов..."
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Historiya())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/73/3e/a5/733ea5e5813bfcd51f77d18da6ecd4b8.jpg'
    caption = "Наша Королева, а совсем недавно сражалась с нами плечо к плечу. Я кстати при похощении переодевался в " \
              "Хисторию, мы довольно-таки похожи"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Anni())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/36/71/5f/36715fd7bc4a16f7c9593db8850be123.jpg'
    caption = "Энни - крайне сильная, необщительная, из одной местности с Бертрольтом и Райнером"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Ervin())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/29/11/e2/2911e25f18475849e6e5c13cc143a19a.jpg'
    caption = 'Эрвин - Командир развед отряда и лучший лидер. Он тот, на кого стоит ровняться. Очень рассудительный, ' \
              'честный и справедливый! Всегда советуется с Леви по любым вопросам '
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Eren())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/4a/7d/8a/4a7d8a41291aa69b748d7da289f12717.jpg'
    caption = "Мой лучший друг детства, ну ещё он титан и человек с непонятной никому волей"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(Flok())
async def sun_answer(message: types.Message):
    photo_url = 'https://i.pinimg.com/564x/64/be/7b/64be7b73ab1039eed89732e48961e322.jpg'
    caption = "Новенький, чем-то смахивает на Жана в кадетском корпусе"
    await bot.send_photo(message.from_user.id, photo_url,
                         caption=emoji.emojize(caption, use_aliases=True),
                         reply_to_message_id=None, allow_sending_without_reply=True)


@dp.message_handler(WelcomeFilter())
async def sun_answer(message: types.Message):
    await message.answer("Привет! Как у тебя дела?")


@dp.message_handler(HowAreYouFilter())
async def sun_answer(message: types.Message):
    await message.answer("Я рад, чем хочешь заняться?")


@dp.message_handler(HowAreYouTwoFilter())
async def sun_answer(message: types.Message):
    await message.answer("Я надеюсь, что скоро всё станет лучше, чем хочешь заняться?")


if __name__ == "__main__":
    dp.bind_filter(SunFilter)
    executor.start_polling(dp, skip_updates=True)
