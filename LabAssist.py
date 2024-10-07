import telebot
from telebot import types

bot = telebot.TeleBot('7283731812:AAGQPqBuZxQ6SuDPDSlvSuC2TYPU5jCpkws');
    
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1️⃣")
    btn2 = types.KeyboardButton("2️⃣")
    btn3 = types.KeyboardButton("3️⃣")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, text='Привет, я научный калькулятор, который поможет Вам в' 
                     'работе со световым излучением. \n \n Вот, что я могу: \n \n 1. Осуществление перевода частоты излучения или энергии фотона в длину волны света'
                     '\n \n 2. Вычисление флюенса лазерной системы по средней мощности'
                     '\n \n 3. Также вы можете оставить отзыв о научном ассистенте'.format(message.from_user), reply_markup=markup)
    




@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "1️⃣"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        frequency_btn = types.KeyboardButton("Частота излучения")
        energy_btn = types.KeyboardButton("Энергия фотона")
        exit_btn = types.KeyboardButton("Выйти в меню")
        markup.add(frequency_btn, energy_btn, exit_btn)
        bot.send_message(message.from_user.id, text= 'Что будем переводить в длину волны света?'.format(message.from_user), reply_markup=markup)
    
    if(message.text == "Частота излучения"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        frequency_btn = types.KeyboardButton("Частота излучения")
        energy_btn = types.KeyboardButton("Энергия фотона")
        exit_btn = types.KeyboardButton("Выйти в меню")
        markup.add(frequency_btn, energy_btn, exit_btn)
    
        
        bot.send_message(message.from_user.id, text= 'Введите частоту (в Гц)'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, convert_frequency_to_wavelength)
            
    if(message.text == "Энергия фотона"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        frequency_btn = types.KeyboardButton("Частота излучения")
        energy_btn = types.KeyboardButton("Энергия фотона")
        exit_btn = types.KeyboardButton("Выйти в меню")
        markup.add(frequency_btn, energy_btn, exit_btn)
        bot.send_message(message.from_user.id, text= 'Введите энергию (в эВ)'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, convert_energy_to_wavelength)
        
    if(message.text == "Выйти в меню"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣")
        btn2 = types.KeyboardButton("2️⃣")
        btn3 = types.KeyboardButton("3️⃣")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, text= 'Вот, что я могу: \n \n 1. Осуществление перевода частоты излучения или энергии фотона в длину волны света'
                     '\n \n 2. Вычисление флюенса лазерной системы по средней мощности'
                     '\n \n 3. Также вы можете оставить отзыв о научном ассистенте'.format(message.from_user), reply_markup=markup)
    
        
    if(message.text == "2️⃣"):
        compute_fluence(message)
        
    if(message.text == "3️⃣"):
        feedback(message)



def compute_fluence(message):
    bot.reply_to(message, "Введите среднюю мощность (Вт) и площадь в м², разделенные пробелом:")
    bot.register_next_step_handler(message, calculate_fluence)

def calculate_fluence(message):
    try:
        power, area = map(float, message.text.split())
        if area <= 0:
            bot.reply_to(message, "Вы и вправду думаете, что площадь может быть равна 0 или даже меньше? Введите среднюю мощность (Вт) и площадь в м², разделенные пробелом:")
            bot.register_next_step_handler(message, calculate_fluence)
        if area > 0:   
            fluence = power / area  #формула флюенса
            bot.reply_to(message, f"Флюенс: {fluence:.2f} Дж/м²")
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректные значения.")
        bot.register_next_step_handler(message, calculate_fluence)


def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {e}"
    
light_speed = 299792458 
#частота в длину волны 
def convert_frequency_to_wavelength(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣")
        btn2 = types.KeyboardButton("2️⃣")
        btn3 = types.KeyboardButton("3️⃣")
        markup.add(btn1, btn2, btn3)
        
        frequency = float(evaluate_expression(message.text))
        # длина волны  = скорость света  / частота 
        wavelength = light_speed / frequency
        bot.reply_to(message, f"Длина волны при частоте {frequency} Гц:  {wavelength} м \n \nТип излучения {radiation_type(wavelength)}".format(message.from_user), reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣")
        btn2 = types.KeyboardButton("2️⃣")
        btn3 = types.KeyboardButton("3️⃣")
        markup.add(btn1, btn2, btn3)   
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректное численное значение частоты (в Гц).".format(message.from_user), reply_markup=markup) 
        bot.register_next_step_handler(message, convert_frequency_to_wavelength)    

#энергия в длину волны 
def convert_energy_to_wavelength(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣")
        btn2 = types.KeyboardButton("2️⃣")
        btn3 = types.KeyboardButton("3️⃣")
        markup.add(btn1, btn2, btn3) 
        
        energy = float(evaluate_expression(message.text))
        # длина волны  = постоянная Планка * скорость света  / энергия фотона
        wavelength =  round(6.67 * light_speed / energy, 2)
        
        bot.reply_to(message, f"Длина волны при энергии фотона {energy} эВ:  {wavelength} * 10 в -34 степени м \n \nTип излучения {radiation_type(wavelength)}".format(message.from_user), reply_markup=markup)
    except ValueError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣")
        btn2 = types.KeyboardButton("2️⃣")
        btn3 = types.KeyboardButton("3️⃣")
        markup.add(btn1, btn2, btn3) 
        bot.reply_to(message, "Пожалуйста, введите корректное численное значение частоты (в эВ).".format(message.from_user), reply_markup=markup)   
        bot.register_next_step_handler(message, convert_energy_to_wavelength) 

#опрос 

def feedback(message):
    bot.reply_to(message, "Как вы оцениваете научного ассистента? Что можно улучшить?")
    bot.register_next_step_handler(message, handle_feedback)

def handle_feedback(message):
    with open("user_tips.txt", "a") as file:
        file.write('\n' + message.text)
    bot.reply_to(message, "Спасибо за ваш отзыв!")
    
#тип излучения 

def radiation_type(wavelength):
    if wavelength < 10 ** -11:
        return "гамма-излучение"
    elif 10 ** -11 <= wavelength < 4 * 10 ** -7:
        return "рентгеновское излучение"
    elif 4 * 10 ** -7 <= wavelength < 7 * 10 ** -7:
        return "ультрафиолетовое излучение"
    elif 7 * 10 ** -7 <= wavelength < 10 ** -3:
        return "видимый свет"
    elif 10 ** -3 <= wavelength < 10 ** -2:
        return "инфракрасное излучение"
    elif 10 ** -2 <= wavelength < 10:
        return "микроволны"
    elif wavelength > 10:
        return "радиоволны"
        
bot.polling(none_stop=True, interval=0)