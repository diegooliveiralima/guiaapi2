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
from google_trans_new import google_translator
import urllib3



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
    #CRIAÇÃO DE CICLOS DE TIMEOUT ######################################################################################
    banco = mysql.connector.connect (
    host="us-cdbr-east-02.cleardb.com",
    user="b64ccbb6c5e3c0",
    passwd="1569cc14",
    database="heroku_3d387bc54c19158"
    )
        
    cursor = banco.cursor()
    cursor.execute('SELECT ciclo from controle where titulo="letterbox"')
    ciclo = cursor.fetchall()
    ciclo = ciclo[0][0]
    ciclo = int(ciclo)
    print(ciclo)
    if ciclo  == 0:
        print("ciclo 0")
        users = ("kurstboy","austinburke")
    elif ciclo == 1:
        users = ("adrianbalboa", "max_delgado")
        print("Ciclo 1")
    elif ciclo == 2:
        print("Ciclo 2")
        users = ("joelollo", "twillis04")
    elif ciclo == 3:
        print("Ciclo 3")
        users = ( "justmiaslife",  "cervantes3")
    elif ciclo == 4:
        print("Ciclo 4")
        users = ( "mesh509",  "xene")
    elif ciclo == 5:
        users = ("jslk", "swaghili123")
        ciclo = -1
        print("Ultimo ciclo")
        
    ciclo = ciclo + 1
    ciclo = str(ciclo)
    letterbox = "letterbox"
    cursor = banco.cursor()
    comando = 'UPDATE controle  SET ciclo="' + ciclo + '" where titulo="letterbox"' 
    cursor.execute(comando)
    banco.commit() 
    
    try:
       
    
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
                linkFilme = re.sub('/1/', '', linkFilme)
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
                query = re.sub("&", "and", query)
            
                try:
                    req = requests.get(letterboxlink)
                    soup = BeautifulSoup(req.content, 'html.parser')
                    Detalhes = soup.find('p', class_='text-link text-footer')

                    a = Detalhes.find('a')
                    linkIMDBInteiro = a['href']
                    print(linkIMDBInteiro)
                    n = re.search('http://www.imdb.com/title/tt', linkIMDBInteiro, re.IGNORECASE)
                    if n:
                        print("é um link IMDB")
                    else:
                        continue
                except: 
                    continue
                
        
                cursor = banco.cursor()
                cursor.execute("select * from filmes where fonte = '" + linkIMDBInteiro +  "'")
                results = cursor.fetchall()
                row_count = cursor.rowcount
                print ("number of affected rows: {}".format(row_count))

                if row_count <= 0:

                    #PEGA DADOS IMDB  ######################################################################################
                    #PEGA NUMERO DE CRITICAS ######################################################################################
                    try:
                        url = linkIMDBInteiro
                        req = requests.get(url)
                        soup = BeautifulSoup(req.content, 'html.parser')
                        criticas = soup.find('div', class_='user-comments') #encontra todas as classes h2 do blog
                        critica = criticas.findAll('a')
                        print(critica[4].text)
                        numeroCriticas = critica[4].text
                    except:
                        numeroCriticas = "0"
                        print("erro ao pegar as criticas")
                    numeroCriticas = re.sub(',', "", numeroCriticas)

                    j = re.search('\d',numeroCriticas)
                    if j:
                        numeroCriticas = re.search(r'\d+',numeroCriticas).group()
        
                    else:
                        numeroCriticas = '0'
                    
                    
                    
                    
                    #PEGA NOTAS E TITULO ######################################################################################

                    
                    linkIMDB = linkIMDBInteiro.replace("http://www.imdb.com/title/tt", "")
                    
                    linkIMDB = linkIMDB.replace("/", "")
                    linkIMDB = linkIMDB.replace("maindetails", "")
                    linkIMDB = linkIMDB.replace("releaseinfo", "")
                    linkIMDBInteiro = linkIMDBInteiro.replace("releaseinfo", "")
                    print(linkIMDB)
                    #linkFilmow = linkFilmow.replace("ficha-tecnica/", "")

                    
                    req = requests.get('http://www.omdbapi.com/?apikey=73634e02&type=movie&i=tt' + linkIMDB)
                    dicionario = json.loads(req.text)
                    tituloIMDB = dicionario['Title']
                    NotaIMDB = dicionario['imdbRating']
                    year = dicionario['Year']
                    generoIngles = dicionario['Genre']
                    imagemUrl = dicionario['Poster']
                    Semcurta = re.search('Short', generoIngles, re.IGNORECASE)
                            
                    try:
                        NotaTomate = dicionario['Ratings'][1]
                        NotaTomate = NotaTomate['Value']
                    except:
                        NotaTomate = "N/A"

                    try:
                       votosQuantidade = dicionario['imdbVotes']
                    except:
                        votosQuantidade = "N/A"
                    votosQuantidade = re.sub(',', "", votosQuantidade)
                    


                    print("O titulo no imdb é: " + tituloIMDB + " A nota é: " + NotaIMDB + " notatomate: " + NotaTomate + " Votos: " + votosQuantidade + " numcriticas: " + numeroCriticas + " ano: " + year + " genero: " + generoIngles)
                   
                    
                    banco = mysql.connector.connect (
                    host="us-cdbr-east-02.cleardb.com",
                    user="b64ccbb6c5e3c0",
                    passwd="1569cc14",
                    database="heroku_3d387bc54c19158"
                            )
                    print("Não encontrou nenhum titulo")
                    #filme não existe, cadastra no banco para na proxima vez nao procurar mais por ele


                    #PEGAR DADOS NO FILMOW ######################################################################################

                    page = 1
                    start = (page - 1) * 1 + 1
                    API_KEY = "AIzaSyC_ylJR_jjPf9h3JXWaOMj1pZ1shPzxPS4"
                    SEARCH_ENGINE_ID = "006935070929965711800:7vjhbn7medw"
                    
                    urlFilmow = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}+filmow&start={start}"
                    dataFilmow = requests.get(urlFilmow).json()
                    linkFilmow = dataFilmow.get("items")[0]["link"] 
                    print(linkFilmow)
                    f = -1
                    for item in range(len(dataFilmow)):
                        f = f + 1
                        print("procurando links do filmow... " + dataFilmow.get("items")[f]["link"])
                        m = re.search(r'filmow.com', dataFilmow.get("items")[f]["link"])
                        if m:
                            linkFilmow = dataFilmow.get("items")[f]["link"]
                            print("achou esse link do filmow: " + linkFilmow)
                            break
                        else:
                            querySemEspaco = re.sub(r' ', '%20', query)
                            querySemEspaco = re.sub(r'&', '', querySemEspaco) 
                            linkFilmow = "www.google.com/search?q=filmow%20" + querySemEspaco
        
                    
                            querySemEspaco = re.sub(r' ', '%20', query)
                            querySemEspaco = re.sub(r'&', '', querySemEspaco) 
                            linkFilmow = "www.google.com/search?q=filmow%20" + querySemEspaco
                            print(linkFilmow)

                    
                    #pegar sinopse do filme para exibição formata ######################################################################################
                    try:
                        url = linkFilmow
                        req = requests.get(url)
                        soup = BeautifulSoup(req.content, 'html.parser')
                        Sinopse = soup.find('div', class_='description text-truncate') 
                        Sinopse =  str(Sinopse.text) #passa para string
                        Sinopse = BeautifulSoup(Sinopse, 'html.parser').text
                        print(Sinopse)
                    except:
                        try:
                            urlAdoro = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}+adorocinema&start={start}"
                            dataAdoro = requests.get(urlAdoro).json()
                            linkAdoro = dataAdoro.get("items")[0]["link"] 
                            f = -1
                            for item in range(len(dataAdoro)):
                                f = f + 1
                                print("procurando links do filmow... " + dataAdoro.get("items")[f]["link"])
                                m = re.search(r'adorocinema.com/filmes', dataAdoro.get("items")[f]["link"])
                                if m:
                                    linkAdoro = dataAdoro.get("items")[f]["link"]
                                    break
                            print("achou esse link do filmow: " + linkAdoro)
                            url = linkAdoro
                            req = requests.get(url)
                            soup = BeautifulSoup(req.content, 'html.parser')
                            Sinopse = soup.find('div', class_='content-txt') 
                            Sinopse =  str(Sinopse.text) #passa para string
                            Sinopse = BeautifulSoup(Sinopse, 'html.parser').text
                            print(Sinopse)
                        except:
                            Sinopse = dicionario['Plot']
            
                    
    #-------------------------------- Pegar os generos no filmow ou no imdb ######################################################################################
        
                    try:
                        url = linkFilmow
                        req = requests.get(url)
                        soup = BeautifulSoup(req.content, 'html.parser')
                        generos = soup.find('div', class_="btn-tags-list") #encontra todas as classes h2 do blog
                        generos = generos.findAll('a')
                        a = 0
                        genero = ""
                        for tag in range(len(generos)):
                            genero = genero + " " + generos[a].text
                            a = a + 1
                        print(genero)
                    except:
                        try:
                            genero = dicionario['Genre']
                        except:
                            genero = "erro"

                        #pega a nota no imdb se vier invalida
                    try:
                        if NotaIMDB == "N/A":      
                            url = linkIMDBInteiro
                            req = requests.get(url)
                            soup = BeautifulSoup(req.content, 'html.parser')
                            span = soup.find('span', itemprop='ratingValue') #encontra todas as classes h2 do blog
                            NotaIMDB = span.text
                        linkFilmow = re.sub(r'/ficha-tecnica/', "", linkFilmow)
                    except:
                        print("erro pegar nota IMDB")
                    try:
                        url = linkFilmow
                        req = requests.get(url)
                    except:
                        print("erro no link do filmow")
        
                #pegar nome do filme para exibição formata
                    nomeFormatado = " "
                    nomeFormatadoSemTraco = " "
                    nomeIngles = " "
                    try:
                        soup = BeautifulSoup(req.content, 'html.parser')
                        nomeFormatado = soup.find('h1', itemprop='name')
                        nomeFormatado =  str(nomeFormatado.text) #passa para string
                        nomeFormatado = BeautifulSoup(nomeFormatado, 'html.parser').text
                        nomeIngles = dicionario['Title']
                        nomeFormatadoSemTraco = nomeFormatado
                        if nomeIngles == nomeFormatado:
                            nomeFormatado = ""
                        else:
                            nomeFormatadoSemTraco = nomeFormatado
                            nomeFormatado = nomeFormatado + " - "
                            print("Titulo em portuges:")
                            print(nomeFormatado)
                    except:
                        print("Erro na busca do nome em português, apenas título inglês")
                        nomeIngles = dicionario['Title']
                        nomeFormatado = "■ "
                    
                    api_youtube = "AIzaSyCXE2iZJGfDhJ2s5OHjUsjA_ojtXFxV6l0"
                    search_url = 'https://www.googleapis.com/youtube/v3/search'

                    # ------------------------------------- Procurar o trailer no youtube ###############################################################################
                    try:
                        youtube = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyCXE2iZJGfDhJ2s5OHjUsjA_ojtXFxV6l0&q=' + nomeFormatadoSemTraco + '+trailer+legendado&part=snippet&maxResults=8&type=video'

                        r = requests.get(youtube)
                        print(r)
                        h = 0
                        for resultado in range(8):
                            idTrailer = r.json()['items'][h]['id']['videoId']

                            idTrailer = r.json()['items'][h]['id']['videoId']

                            linkTrailer = "https://www.youtube.com/watch?v=" + idTrailer

                            video_url = linkTrailer

                            response = requests.get(video_url).text

                            title = re.findall(r'"title":"[^>]*",',response)[0].split(',')[0][9:-1]

                            tituloYoutube = "{}".format(title)

                            m = re.search('trailer', tituloYoutube, re.IGNORECASE)
                            p = re.search('legendado', tituloYoutube, re.IGNORECASE)

                            b = re.search('TRAILER', tituloYoutube, re.IGNORECASE)
                            v = re.search('LEGENDADO', tituloYoutube, re.IGNORECASE)
           
                            x = re.search(nomeIngles, tituloYoutube, re.IGNORECASE)
            
                            if m and p and x or (x and b and v):
                                print("Ok, é um trailer legendado perfeito!")
                                break
                            if h == 7:
                                j = 0
                                youtube = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyCXE2iZJGfDhJ2s5OHjUsjA_ojtXFxV6l0&q=' + nomeIngles + '+trailer+legendado&part=snippet&maxResults=8'
                                r = requests.get(youtube)
                                for resultado in range(8):
                                    idTrailer = r.json()['items'][j]['id']['videoId']
                                    idTrailer = r.json()['items'][j]['id']['videoId']
                                    linkTrailer = "https://www.youtube.com/watch?v=" + idTrailer
                                    z = re.search(nomeIngles, tituloYoutube, re.IGNORECASE)
                                    d = re.search('trailer', tituloYoutube, re.IGNORECASE)
                                    u = re.search('Trailer', tituloYoutube, re.IGNORECASE)
                                    if z and d or (z and u):
                                        print("Achou um trailer com nome em ingles mesmo")
                                        break
                                    else:
                                        nomeInglessemEspaco = re.sub(r' ', '%20', nomeIngles)    
                                        linkTrailer =  "https://www.youtube.com/results?search_query=" + nomeInglessemEspaco
                            h = h + 1
                    except:
                        print("Não foi possível obter o trailer")
                        nomeInglessemEspaco = re.sub(r' ', '%20', nomeIngles)
                        nomeInglessemEspaco = re.sub(r'&', '', nomeInglessemEspaco)    
                        linkTrailer =  "https://www.youtube.com/results?search_query=" + nomeInglessemEspaco
                    print(linkTrailer)

                    numeroCriticas = int(numeroCriticas)
                    if votosQuantidade == 'N/A':
                        print("Sem votos")
                        votosQuantidade = 0
                    else:
                        votosQuantidade = int(votosQuantidade)
                    try:
                       
                        year = int(year)
                    except:
                        year = 0
                    votosQuantidade = int(votosQuantidade)
                    # VERIFICA OS CRITÉRIOS E ENVIA PARA O TELEGRAM ######################################################################################
                    
                    if NotaIMDB <= '5.0' or Semcurta or (numeroCriticas < 15 and votosQuantidade < 700 and NotaIMDB <= '6.0' ) or (numeroCriticas < 10 and votosQuantidade < 700) or year == 0  or year < 2019:
                        print("Filme não passou nos critérios")
                        
                        votosQuantidade = str(votosQuantidade)
                        year = str(year)
                        NotaIMDB = str(NotaIMDB)
                        NotaTomate = str(NotaTomate)
                        numeroCriticas = str(numeroCriticas)

                        cursor = banco.cursor()
                        cursor.execute('SELECT ciclo from controle where titulo="movies_alert_negados"')
                        ciclo = cursor.fetchall()
                        ciclo = ciclo[0][0]
                        ciclo = int(ciclo)
                        
                        _bot_token = "1335874302:AAGHfCU4hKFhp_LRQctCL3gYCtNDtntnN0Q"
                        bot = telegram.Bot(_bot_token)
                        print("Bot do telegram conectado!")
                        _bot_chatID = "@negados_alert"
                        txt = '[​​​​​​​​​​​](' + imagemUrl + ')' + '*' + nomeFormatado + nomeIngles + ' ' + year + '*  \n' + 'Gênero: ' + genero + '  \n' +  'Sinopse: ' +  Sinopse   + '  \n' +  'Notas: IMDB ' + NotaIMDB + ' / RottenTomatoes ' +  NotaTomate  + '  \n' +  'Links: ' +  '[IMDB](' + linkIMDBInteiro + ')'  +  ' / '  +  '[Filmow](' + linkFilmow + ')'  + ' / ' + '[Trailer](' + linkTrailer + ')'  +  '  \n' +  'Fonte: ' + "Letterbox"
                        bot.send_message(_bot_chatID, txt, parse_mode='markdown')

                        pontos = 1
                        pontos = str(pontos)
                        fonte = "Letterbox"
                        datetime.datetime.now()
                        datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

                        
                        query = re.sub('[^a-zA-Z0-9 \n\.]', '', query)
                    
        
                        hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        estado = "negado"
                        cursor = banco.cursor()
                        comando = "INSERT INTO filmes (filme, fonte, hora, estado, votosQuantidade, pontos, numCriticas) values ('" + query + "', '" + linkIMDBInteiro + "', '" + hora + "' , '"  + estado +  "' , '" + votosQuantidade + "' ,  '" + pontos  + "' ,  '" + numeroCriticas +  "')"
                        cursor.execute(comando)
                        banco.commit() 











                        ciclo = ciclo + 1 
                        ciclo = str(ciclo)
             
                        cursor = banco.cursor()
                        comando = 'UPDATE controle  SET ciclo="' + ciclo + '" where titulo="movies_alert_negados"' 
                        cursor.execute(comando)
                        banco.commit() 

                        
                        try:
                            ciclo = int(ciclo)
                            ciclo = ciclo + 1
                            ciclo = str(ciclo)
                            delete_text = 'https://api.telegram.org/bot' + _bot_token + '/deleteMessage?chat_id=' + _bot_chatID + '&message_id=' + ciclo
                            response = requests.get(delete_text)
                            print(response)
                            if response.status_code == 400: 
                                print("Nao houve erro")
                            else:
                                print("houve erro chato")
                                cursor = banco.cursor()
                                comando = 'UPDATE controle  SET ciclo="' + ciclo + '" where titulo="movies_alert_negados"' 
                                cursor.execute(comando)
                                banco.commit() 
                        except:
                            print("Não havia mensagens para excluir")
                    else:
                        print("Enviando filme")
                        votosQuantidade = str(votosQuantidade)
                        year = str(year)
                        NotaIMDB = str(NotaIMDB)
                        NotaTomate = str(NotaTomate)
                        numeroCriticas = str(numeroCriticas)

                        cursor = banco.cursor()
                        cursor.execute('SELECT ciclo from controle where titulo="movies_alert"')
                        ciclo = cursor.fetchall()
                        ciclo = ciclo[0][0]
                        ciclo = int(ciclo)
                        
                        _bot_token = "1335874302:AAGHfCU4hKFhp_LRQctCL3gYCtNDtntnN0Q"
                        bot = telegram.Bot(_bot_token)
                        print("Bot do telegram conectado!")
                        _bot_chatID = "@movies_alert"
                        txt = '[​​​​​​​​​​​](' + imagemUrl + ')' + '*' + nomeFormatado + nomeIngles + ' ' + year + '*  \n' + 'Gênero: ' + genero + '  \n' +  'Sinopse: ' +  Sinopse   + '  \n' +  'Notas: IMDB ' + NotaIMDB + ' / RottenTomatoes ' +  NotaTomate  + '  \n' +  'Links: ' +  '[IMDB](' + linkIMDBInteiro + ')'  +  ' / '  +  '[Filmow](' + linkFilmow + ')'  + ' / ' + '[Trailer](' + linkTrailer + ')'  +  '  \n' +  'Fonte: ' + "Letterbox"
                        bot.send_message(_bot_chatID, txt, parse_mode='markdown')

                        ciclo = ciclo + 1 
                        ciclo = str(ciclo)
             
                        cursor = banco.cursor()
                        comando = 'UPDATE controle  SET ciclo="' + ciclo + '" where titulo="movies_alert"' 
                        cursor.execute(comando)
                        banco.commit() 

                        try:
                           ciclo = int(ciclo)
                           ciclo = ciclo + 1
                           ciclo = str(ciclo)
                           delete_text = 'https://api.telegram.org/bot' + _bot_token + '/deleteMessage?chat_id=' + _bot_chatID + '&message_id=' + ciclo
                           response = requests.get(delete_text)
                           print(response)
                           if response.status_code == 400: 
                               print("Nao houve erro")
                           else:
                               print("houve erro chato")
                               cursor = banco.cursor()
                               comando = 'UPDATE controle  SET ciclo="' + ciclo + '" where titulo="movies_alert"' 
                               cursor.execute(comando)
                               banco.commit() 
                        except:
                           print("Não havia mensagens para excluir")








                        pontos = 1
                        pontos = str(pontos)
                        fonte = "Letterbox"
                        datetime.datetime.now()
                        datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
                    
        
                        hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        estado = "Alerta"
                        cursor = banco.cursor()
                        comando = "INSERT INTO filmes (filme, fonte, hora, estado, votosQuantidade, pontos) values ('" + query + "', '" + linkIMDBInteiro + "', '" + hora + "' , '"  + estado +  "' , '" + votosQuantidade + "' ,  '" + pontos  +   "')"
                        cursor.execute(comando)
                        banco.commit() 








                    
            
                else:
                    print("Filme já cadastrado")

        
           
            
            
        


                

            g = g + 1





    except Exception as e: 
        print(e)









            
        
   
   
    
    
    return jsonify({"message": "Não entre em pânico!"})



    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

 
    