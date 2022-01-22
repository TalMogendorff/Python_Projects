from gtts import gTTS as GT

import os

user_input_text = input('Write the text that you want to convert to Speech : ')

user_input_file_name = user_input_text.split(' ')[0]

languague = 'en'

obj = GT(text = user_input_text, lang = languague, slow = False)

file_name_obj = obj.save(f'{user_input_file_name}.mp3')

os.system(f'{user_input_file_name}.mp3')