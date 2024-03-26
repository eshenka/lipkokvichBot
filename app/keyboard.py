from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

import random

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
    'rrСупы': [Food('Томатный с оливковым маслом и марграритой', 310), Food('Сырный с фокачча', 310),
               Food('Том Ям с цыпленком', 400), Food('Том Ям с тигровыми креветками', 450),
               Food('Бульон с яйцом', 160)],
    'rrПаста': [Food('Карбонара с беконом и яйцом', 400), Food('Митболы в томатном соусе', 400),
                Food('Паста Том ям с цыпленком', 490), Food('Паста Том ям с креветками', 540),
                Food('Паста с песто', 360)],
    'rrДесерты': [Food('Морковный торт с гвоздичным кремом', 260),
                  Food('Чизкейк манговый', 290)]
}

red_rabbit_random_variants = ['730р.\nСуп сырный с фокачча\nСалат цезарь 420р.',
                              '680р.\nПицца пепперони 22см\nЧизкейк манговый']

khan_buz_menu_positions = {
    'khБуузы': [Food('Буузы', 65)],
    'khСупы': [Food('Борщ 200гр', 95), Food('Борщ 400гр', 139),
               Food('Лагман', 155), Food('С говядиной', 105),
               Food('С курицей', 95), Food('Том Ям', 290)],
    'khВторое': [Food('Плов с курицей', 185),
                 Food('Лапша с говядиной в устричном соусе', 205),
                 Food('лапша с курицей в сливочном соусе', 185)],
    'khСалаты': [Food('Свекольный', 69), Food('Морковь по-корейски', 59),
                 Food('Витаминный', 59), Food('Коул слоу', 69), Food('Из баклажанов', 109)],
    'khНапитки': [Food('Чай', 45), Food('Кофе', 55), Food('Морс', 85),
                  Food('Алтай Аква', 89), Food('Кола Бочкари', 109)],
    'khДесерт': [Food('Боовы', 89)]
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


def process_random(dishes):
    idea = ''
    cost = 0

    for i in range(0, 3):
        name, category = random.choice(list(dishes.items()))
        dish = category[random.randint(0, len(category) - 1)]
        idea += name[2:] + ' ' + dish.name + '\n'
        cost += dish.price

    return str(cost) + 'р' + '\n' + idea


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
