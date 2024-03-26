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


class Food:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


red_rabbit_menu_positions = {
    'rrПицца': [Food('Анти Гавайи', 390), Food('Груша-горгондзола', 390),
                Food('Мясной босс', 480), Food('Четыре сыра', 420),
                Food('Барбекю пицца', 390), Food('Пепперони', 390),
                Food('Маргарита', 290), Food('Манхеттен', 360), Food('Бекон, пепперони, 3 сыра', 420),
                Food('Цезарь-пицца', 390), Food('Фокачча с песто', 190), Food('Фокачча Маргаритта', 195)],
    'rrСалаты': [Food('Цыпленок с грушей в соусе дор блю', 380), Food('Цезарь', 420),
                 Food('С ростбифом', 450), Food('С креветками и авокадо', 420)],
    'rrЗакуски': [Food('Брускетта с ростбифом', 360), Food('Брускетта с гуакамоле', 260),
                  Food('Ростбиф', 490), Food('Строганина из красной рыбы', 360)],
    'rrСупы': [Food('Томатный с оливковым маслом и марграритой', 310), Food('Сырный с фокачча', 310)]
}

red_rabbit_random_variants = ['730р.\nСуп сырный с фокачча\nСалат цезарь 420р.',
                              '680р.\nПицца пепперони 22см\nЧизкейк манговый']

khan_buz_menu_positions = {
    # 'khСупы 200гр./400гр.': 'Борщ 95р./139р.\nЛагман 155р./229р.\nС говядиной 105р./159р.\n'
    #                         'С курицей 95р./139р.\nТом ям 290р.',
    # 'khВторое 200гр./400гр.': 'Лапша с говядиной в устричном соусе 205р./309р.\n'
    #                           'Лапша с курицей в сливочном соусе 185р./279р.\n'
    #                           'Плов с курицей 155р./209р.',
    # 'khСалаты': 'Свекольный 69р.\nМорковь по-корейски 59р.\nВитаминный 59р.\nКоул слоу 69 р.\nИз баклажанов 109р.',
    # 'khНапитки': 'Чай 45р.\nКофе55р.\nМорс85р.\nАлтай аква 89р.\nКола бочкари 109р.',
    # 'khДесерт': 'Боовы 89р.',
    # 'khБуузы': 'Буузы 65р.'
    'khСупы': [Food('Борщ', 95), Food('Лагман', 155)],
    'khВторое': [Food('Плов с курицей', 185)],
    'khСалаты': [Food('Морковь по-корейски', 59)],
    'khНапитки': [Food('Чай', 45)],
    'khДесерт': [Food('Боовы', 89)],
    'khБуузы': [Food('Буузы', 65)]
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


def process_food_data(category):
    answer_text = ''

    for food in category:
        answer_text += food.name + ' ' + str(food.price) + 'р.\n'

    return answer_text


game_numbers = {}


stickers = ["CAACAgIAAxkBAAELzGFmAv6Cmuf3eTLOrjA0y3GsAAEYOVYAAugzAAKE3shKDfMChELOzVQ0BA",
            "CAACAgIAAxkBAAELzGNmAv6S0WiEuvAak0I6AyYsVCXfdAACYkcAAqaByErr88hDy6wL6jQE",
            "CAACAgIAAxkBAAELzGVmAv6h_sFRvkrxzmn0dKOshpntZQACoz4AAjFC6EgFE8TH5IiMBjQE",
            "CAACAgIAAxkBAAELzGdmAv62Vl-9VR-r7xo7CdFBj4pkZgACmzgAAlBrwUuy7lEoMZ4wkTQE",
            "CAACAgIAAxkBAAELzGlmAv7SI64fMIVPh6IST-LxdD-JMgACzwADys3hF26Da_zo4wFDNAQ",
            "CAACAgIAAxkBAAELzGtmAv77rkn5a9E-CWU2YUcwKlD6fgACriUAAjSXoEs7eoAdUThGczQE",
            "CAACAgIAAxkBAAELzG9mAv92KBQ7KaMC0DbBdmvCkyTWQgACaQADMWfCNYjEs8VevoiQNAQ",
            "CAACAgIAAxkBAAELzHFmAv-jyLSuYKifRVVnW8f2Xm_RegACXx4AAnzKcEuSqgPA7RX3YTQE",
            "CAACAgIAAxkBAAELzHNmAv-56rnkvCggnM_VogZFxCQjKwACDR4AAiPqcUtYVUlSOLUU1TQE"]
