import play

play.set_backdrop("light blue")












@play.when_program_starts# функція для початку програми
def start():
    text1 = play.new_text(words="г - гладити, с - спати, з - зіграти", x = 0, y = 270, font_size=40)
    text2 = play.new_text(words="к - кормити, п  - прибрати, пробіл - піти", x = 0, y = 240, font_size=40) 


    player = play.new_image(image="surikat.jpg", x=0, y=0, size=100)



@play.repeat_forever# повторювати завжди(ігровий цикл)
def do():
    pass


play.start_program()# запуск програми 