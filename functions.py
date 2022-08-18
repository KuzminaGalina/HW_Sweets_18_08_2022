from random import randint

global game
game = False
global sweet
sweet = 0
global round_sweet
round_sweet = 0
global turn

def start (update, context):
    global game
    game = False
    global sweet
    sweet = 0
    global round_sweet
    round_sweet = 0
    global turn
    turn = 0
    context.bot.send_message(update.effective_chat.id, "Привет, хочешь поиграть в конфетки?")

def main (update, context):
    text = update.message.text
    global game
    global sweet
    global round_sweet
    global turn
    if game == False and text == 'да':
        game = True
        context.bot.send_message(update.effective_chat.id, "Супер, тогда введи общее количество конфет (цифру больше единицы)")
        return game
    elif game == False and text != 'да':
       context.bot.send_message(update.effective_chat.id, "Тогда в другой раз") 
    if game == True and sweet == 0:
        if text.isdigit() and int(text) > 0:
            sweet = text
            context.bot.send_message(update.effective_chat.id, "Теперь введи количество конфет за один ход")
            return int(sweet)
        else:
            context.bot.send_message(update.effective_chat.id, "Некорректный ввод")   
    if game == True and round_sweet == 0:
        if text.isdigit() and int(text) > 0:
            round_sweet = text
            turn = randint(0,1)
            if turn == 0:
                context.bot.send_message(update.effective_chat.id, "Ты ходишь первым")
            else:
                context.bot.send_message(update.effective_chat.id, "Первым ходит твой друг")
            return int(round_sweet)
        else:
            context.bot.send_message(update.effective_chat.id, "Некорректный ввод")   
    if game == True and int(round_sweet) > 0:
        if text.isdigit() and int(text) > 0:
            sweet = int(sweet)
            sweet -= int(text)
            if int(text) < 1 or int(text) > int(round_sweet):
                context.bot.send_message(update.effective_chat.id, "Перебор")
            else:
                if sweet > 0:
                    if turn == 0:
                        context.bot.send_message(update.effective_chat.id, "Ходит твой друг")
                        turn = 1
                    else:
                        context.bot.send_message(update.effective_chat.id, "Твой ход")
                        turn = 0
                    context.bot.send_message(update.effective_chat.id, f"Осталось {sweet} конфет")
                    return turn
                elif sweet <= 0:
                    if turn == 0:
                        context.bot.send_message(update.effective_chat.id, "Ты проиграл") 
                    else:                  
                        context.bot.send_message(update.effective_chat.id, "Ты выиграл") 
                    return start(update, context)
        else:
            context.bot.send_message(update.effective_chat.id, "Некорректный ввод")    









