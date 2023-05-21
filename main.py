import play

play.set_backdrop("light blue")












@play.when_program_starts# функція для початку програми
def start():
    global player, speech
    text1 = play.new_text(words="г - гладити, с - спати, з - зіграти", x = 0, y = 270, font_size=40)
    text2 = play.new_text(words="к - кормити, п  - прибрати, пробіл - піти", x = 0, y = 240, font_size=40) 


    player = play.new_image(image="surikat.jpg", x=0, y=0, size=100)
    speech = play.new_text(words = "Привіт, мене звати Альфред", x=0, y=-250)



@play.repeat_forever# повторювати завжди(ігровий цикл)
async def do():
    if play.key_is_pressed("г") or play.key_is_pressed("Г"):
        player.size = 100
        player.image = "shiyapa.jpg"
        speech.words = "кайф"
        await play.timer(2.0)
    if play.key_is_pressed("з") or play.key_is_pressed("З"):
        player.size = 100
        player.image = "images.jpg"
        speech.words = "круто пограли"
        await play.timer(2.0)
    if play.key_is_pressed('с') or play.key_is_pressed('С'):
        player.size = 20
        player.image = "1575814835195130290.jpg"
        speech.words = "спить"
        await play.timer(2.0)


    if play.key_is_pressed("к") or play.key_is_pressed("К"):
        player.size = 100
        player.image = "surikat.jpg"
        speech.words = "ммм, як смачно"
        await play.timer(2.0)
    if play.key_is_pressed("п") or play.key_is_pressed("П"):
        player.size = 100
        player.image = "surikat 2.jpg"
        speech.words = "я поїв, прибери за мною"
        await play.timer(2.0)
    if play.key_is_pressed('space'):
        player.size = 100
        player.image = "kryket.jpg"
        speech.words = "ти вже йдеш? тоді бувай"
        await play.timer(2.0)



play.start_program()# запуск програми 