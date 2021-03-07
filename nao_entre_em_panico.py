import os
from flask import Flask, jsonify

import requests
import json
import re
import mysql.connector
from bs4 import BeautifulSoup
from time import sleep
import datetime
from datetime import date

from apiclient.discovery import build
#rom google_auth_oauthlib.flow import InstalledAppFlow
#scopes = ['https://www.googleapis.com/auth/calendar']
#flow = InstalledAppFlow.from_client_secrets_file
import telegram
import sys

import urllib.request
import PyPDF2
import io

import ebooklib




'''
url = "https://www.google.com.br/alerts/feeds/06114678530526052316/7725213029379595095"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('entry')

item = items[0]

print(item.title.text)
print(item.link.get('href'))
'''


'''
response = {"value1":"jantar", "value2":"08/15 17:00", "value3":"08/15 17:00"}
requests.post("https://hooks.zapier.com/hooks/catch/8251891/ofm655u", data=response)
'''

'''

url = "http://www.unilab.edu.br/restauranteuniversitario/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

links = soup.find_all('a', href=re.compile(r'(\.pdf)'))
links = links[0]['href']
links = str(links)
links = re.sub('Ç', r'%C3%87', links)

myurl = links

with urllib.request.urlopen(myurl) as url:
    s = url.read()
    
with open(r"c:\tmp\test.pdf", "wb") as f:
    f.write(s)

pdf_path = r"c:\tmp\test.pdf"


tables = camelot.read_pdf(pdf_path)


tables.export('foo.csv', f='csv', compress=True) # json, excel, html, sqlite
tabela = tables[0]

tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}

#print(tables[0].df) # get a pandas DataFrame!

tables[0].to_json('foo.json')

with open('foo.json') as f:
    l = json.load(f)
    print(l)
diaColuna = date.today().weekday() + 1  #Dia da semana + 1 é a formula
diaColuna = str(diaColuna)
coluna = diaColuna 
if coluna == "7":
    pass
else:


    princpal1   =  l[2][coluna]
    princpal2   =  l[3][coluna]   
    vegetariano =  l[4][coluna]  
    salada1     =  l[5][coluna]  
    salada2     =  l[6][coluna]  
    guarnicao   =  l[7][coluna] 
    acompanha1  =  l[8][coluna]
    acompanha2  =  l[9][coluna] 
    acompanha3  =  l[10][coluna]
    suco        =  l[11][coluna]
    sobremesa1  =  l[12][coluna]
    sobremesa2  =  l[13][coluna]

    nprincpal1   =  l[15][coluna]
    nprincpal2   =  l[16][coluna]   
    nvegetariano =  l[17][coluna]  
    nsalada1     =  l[18][coluna]  
    nsalada2     =  l[19][coluna]  
    nguarnicao   =  l[20][coluna] 
    nacompanha1  =  l[21][coluna]
    nacompanha2  =  l[22][coluna] 
    nacompanha3  =  l[23][coluna]
    sopa         =  l[24][coluna]
    acompSopa    =  l[25][coluna]
    nsuco        =  l[26][coluna]
    nsobremesa1  =  l[27][coluna]
    nsobremesa2  =  l[28][coluna]

    inicio  =  l[0]["1"]
    termino  = l[0]["6"]


    cardapioManha = "<b>Principal:</b> " + princpal1 + ", "  + princpal2 + "\n" + "Vegetariano: " + vegetariano + "\n" + "Saladas: " + salada1 + ", " + salada2 +  "\n" + "Guarnição: " + guarnicao  + "\n" + "Acompanhamentos: " + acompanha1 + ", " + acompanha2 + ", " + acompanha3 + "\n" + "Suco: " + suco + "\n" + "Sobremesas: " + sobremesa1 + ", " + sobremesa2
    print(cardapioManha)

    cardapioNoite =  "<b>Principal:</b> " + nprincpal1 + ", "  + nprincpal2 + "\n" + "Vegetariano: " + nvegetariano + "\n" + "Saladas: " + nsalada1 + ", " + nsalada2 +  "\n" + "Guarnição: " + nguarnicao  + "\n" + "Acompanhamentos: " + nacompanha1 + ", " + nacompanha2 + ", " + nacompanha3 + "\n" + "Sopa: " + sopa + "\n" + "Acompanhamento da sopa: " + acompSopa + "\n" +  "Suco: " + nsuco + "\n" + "Sobremesas: " + nsobremesa1 + ", " + nsobremesa2

    TOKEN = "1335874302:AAGfJS-I6j8QJL1vpU_oryvlX0_4ZvnJSms"
    bot = telegram.Bot(TOKEN)
    print("Bot do telegram conectado!")
    chat_id = "608446615"
               
    txt = "CARDÁPIO - SEMANA - " + inicio + " até " + termino + "\n" + "\n" + "Manhã: " + "\n" + cardapioManha + "\n" + "\n" +  "Noite: " + "\n" + cardapioNoite
    bot.send_message(chat_id, txt, parse_mode='html')   
'''




app = Flask(__name__)

@app.route('/', methods=["POST"])
def nao_entre_em_panico():



    
    users = ("kurstboy","austinburke" )
    
    g = 0
    for number in users:
        url = "https://letterboxd.com/" +  users[g]  + "/films/diary/"
        
        print("prcourando filmes na lista... " + url)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        titulosLetterbox = soup.findAll('h3', class_='headline-3 prettify')
        anosLetterbox = soup.findAll('td', class_='td-released center')
        f = 0

        for item in range(3):
            titulos = titulosLetterbox[f]
            anos = anosLetterbox[f]
            a = titulos.find('a')
            linkFilme = a['href']
            linkFilme = re.sub('/' + users[g] + '/film/', '', linkFilme)
            print(linkFilme)


            letterboxlink = "https://letterboxd.com/film/" + linkFilme
            print(letterboxlink)

            f = f + 1
            titulos =  str(titulos.text) #passa para string
            anos = str(anos.text)
            titulos = re.sub('<h3 class="headline-3 prettify"><a href="/deathproof/film/', '', titulos)
            titulos = re.sub(r'\/\"\>+.</a></h3>', '', titulos)  
            titulos = re.sub('<h3 class="headline-3 prettify"><a href="/deathproof/film/', '', titulos)
            anos = re.sub('<td class="td-released center<span>', '', anos)  
            anos = re.sub('<span></td>', '', anos)      
            tituloAno = titulos + " " + anos
            print(tituloAno)
            query = tituloAno

            
            
            req = requests.get(letterboxlink)
            soup = BeautifulSoup(req.content, 'html.parser')
            Detalhes = soup.find('p', class_='text-link text-footer')

            a = Detalhes.find('a')
            linkIMDBInteiro = a['href']
            print(linkIMDBInteiro)

            banco = mysql.connector.connect (
            host="us-cdbr-east-02.cleardb.com",
            user="b64ccbb6c5e3c0",
            passwd="1569cc14",
            database="heroku_3d387bc54c19158"
            )
        
            cursor = banco.cursor()
            cursor.execute("select * from filmes where fonte = '" + linkIMDBInteiro +  "'")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            print ("number of affected rows: {}".format(row_count))

            if row_count <= 0:
                print("Cadastrar filme")
                cursor = banco.cursor()
                votosQuantidade = 0
                votosQuantidade = str(votosQuantidade)
                pontos = 1
                pontos = str(pontos)
                fonte = "Letterbox"
                estado = "ativo"
                datetime.datetime.now()
                datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
                hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                comando = "INSERT INTO filmes (filme, fonte, hora, estado, votosQuantidade, pontos) values ('" + query + "', '" + linkIMDBInteiro + "', '" + hora + "' , '"  + estado +  "' , '" + votosQuantidade + "' ,  '" + pontos  +   "')"
                cursor.execute(comando)
                banco.commit() 
            
            else:
                print("Filme já cadastrado")

        
           
            
            
        


                

        g = g + 1



























    try:

        url2 = "http://unilab.edu.br/noticias/category/noticias/feed/"


  
        resp = requests.get(url2)

        soup = BeautifulSoup(resp.content, features="xml")

        items = soup.findAll('item')
        k = 4
        for item in range(5):
            item = items[k]

            print(item.title.text)
            print(item.link.text)

            titulo = item.title.text
            link = item.link.text

            banco = mysql.connector.connect (
            host="us-cdbr-east-02.cleardb.com",
            user="b64ccbb6c5e3c0",
            passwd="1569cc14",
            database="heroku_3d387bc54c19158"
            )
            cursor = banco.cursor()
            cursor.execute("SELECT titulo FROM feed WHERE titulo like '%" + titulo +  "%'")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            print ("number of affected rows: {}".format(row_count))
            if row_count > 0:
               print("noticia já foi enviada anteriormente")
            else:

                cursor = banco.cursor()
                comando = "INSERT INTO feed (titulo, link) values ('" + titulo + "' , '" + link + "')"
                cursor.execute(comando)
                banco.commit() 

            
                _bot_token = "1564169676:AAHUwrOqqiIytaRi7NDhnet0dSYAYsbSJ5A"
                _bot_chatID = "@unilabNoticias"

                bot_message = '[' + item.title.text + '](' + link + ') \n \n' '[' + 'Link alternativo' + '](' + 'https://outline.com/' + link + ')' 
                send_text = 'https://api.telegram.org/bot' + _bot_token + '/sendMessage?chat_id=' + _bot_chatID + '&parse_mode=Markdown&disable_web_page_preview=True&text=' + bot_message


                response = requests.get(send_text)
         
               
            k = k - 1

    except:
        print("error")
            
        
   
   
    return jsonify({"message": "Não entre em pânico!"})




    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

 
    