import requests

import lxml

from gtts import gTTS as GT

import os

import bs4

result = requests.get('https://en.wikipedia.org/wiki/Dog')

langunge = 'en'

soup = bs4.BeautifulSoup(result.text,'lxml')

title = soup.select('title')[0].getText()

site_p = soup.select('p')

toct = soup.select('.toctext')

def scrapping_to_mp3():

    texty = [title]

    for p in site_p:
      texty.append(p.getText())

    for t in toct:
      texty.append(t.getText())


    return " ".join(texty)

scrapping_text = scrapping_to_mp3()

print(scrapping_text)

obj = GT(text=scrapping_text, lang=langunge, slow=False)

file_name_obj = obj.save(f'{title}.mp3')

#os.system(f'{title}.mp3')


