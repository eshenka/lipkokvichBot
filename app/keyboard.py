from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

food_courts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', callback_data='red-rabbit'),
     InlineKeyboardButton(text='Хан Буз♨️', callback_data='khan-buz')]
])

red_rabbit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', url='https://redrabbit-academ.ru/')],
    [InlineKeyboardButton(text='Меню', callback_data='red-rabbit-menu')],
    [InlineKeyboardButton(text='Не знаю, что заказать', callback_data='rr-random')]])

khan_buz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Хан Буз♨️', url='https://khan-buz.ru/')],
    [InlineKeyboardButton(text='Меню', callback_data='khan-buz-menu')],
    [InlineKeyboardButton(text='Не знаю, что заказать', callback_data='kh-random')]])

red_rabbit_menu_positions = {
    'rrПицца': 'Пицца 22см/32см\nАнти Гавайи 390р./590р. \nГруша-горгондзола 390р./590р. \nМясной босс\n'
               '480р./750р.\nЧетыре сыра 420р./640р.\nБарбекю пицца 390р./590р. \nПепперони 390р./590р.\n'
               'Маргарита 290р./480р.\nМанхеттен 360р./550р.\nБекон, пепперони, 3 сыра 420р./660р.\n'
               'Цезарь-пицца 390р./590р.\nФокачча с песто 190р.\nФокачча Маргаритта 195р.',
    'rrСалаты': "Цезарь 420р. \nС ростбифом 450р.",
    'rrСупы': 'Сырный с фокачча 310р. \nБульон с яйцом 160р. \nТоматный 310р.',
    'rrДесерты': 'Морковный торт с гвоздичным кремом 260р. \nЧизкейк манговый 290p.',
}

red_rabbit_random_variants = ['730р.\nСуп сырный с фокачча\nСалат цезарь 420р.',
                              '680р.\nПицца пепперони 22см\nЧизкейк манговый']

khan_buz_menu_positions = {
    'khСупы 200гр./400гр.': 'Борщ 95р./139р.\nЛагман 155р./229р.\nС говядиной 105р./159р.\n'
                            'С курицей 95р./139р.\nТом ям 290р.',
    'khВторое 200гр./400гр.': 'Лапша с говядиной в устричном соусе 205р./309р.\n'
                              'Лапша с курицей в сливочном соусе 185р./279р.\n'
                              'Плов с курицей 155р./209р.',
    'khСалаты': 'Свекольный 69р.\nМорковь по-корейски 59р.\nВитаминный 59р.\nКоул слоу 69 р.\nИз баклажанов 109р.',
    'khНапитки': 'Чай 45р.\nКофе55р.\nМорс85р.\nАлтай аква 89р.\nКола бочкари 109р.',
    'khДесерт': 'Боовы 89р.',
    'khБуузы': 'Буузы 65р.'
}

khan_buz_random_variants = ['319р.\nМорковь по-корейски\n4 буузы',
                            '485р.\nТом ям\n3 буузы',
                            '380р.\nЛапша с курицей в сливочном соусе 200гр\n3 буузы']


def inline_red_rabbit_menu():
    red_rabbit_menu_keyboard = InlineKeyboardBuilder()

    for position in red_rabbit_menu_positions.keys():
        red_rabbit_menu_keyboard.add(InlineKeyboardButton(text=position[2:], callback_data=position))

    red_rabbit_menu_keyboard.add(InlineKeyboardButton(text='Назад🔙', callback_data='rr-menu-back'))

    return red_rabbit_menu_keyboard.adjust(2).as_markup()


def inline_khan_buz_menu():
    khan_buz_menu_keyboard = InlineKeyboardBuilder()

    for position in khan_buz_menu_positions.keys():
        khan_buz_menu_keyboard.add(InlineKeyboardButton(text=position[2:], callback_data=position))

    khan_buz_menu_keyboard.add(InlineKeyboardButton(text='Назад🔙', callback_data='kh-menu-back'))

    return khan_buz_menu_keyboard.adjust(2).as_markup()
