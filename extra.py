@app.route("/agenda", methods=["POST"])
def handlerAgenda():
    text = request.get_data()
    
    print(text)
    
    '''
    TOKEN = "1335874302:AAGfJS-I6j8QJL1vpU_oryvlX0_4ZvnJSms"
    bot = telegram.Bot(TOKEN)
    print("Bot do telegram conectado!")
    chat_id = "-394502097"
    print(text)
    lista = json.loads(text)
    txt = lista['titulo'] + "\n" + lista['inicio']
    print(txt)
    bot.send_message(chat_id, txt, parse_mode='html')   


    '''

    return ""
    
@app.route("/livro", methods=["POST"])
def handlerLivro(): 


    EntryContent = request.get_data(as_text=True)    
    print(EntryContent)

    s = re.findall(r'more', EntryContent)
    if s:
        y = 1
        myurl = "https://diegooli.s3.us-east-2.amazonaws.com/Pap%C3%A9is+Avulsos+by+Assis+Machado+de+(z-lib.org).epub"
        for envio in range(1):
            sleep(10); enviarLivro(myurl, "4", y)
            y = y + 1
    
    k = re.findall(r'mais', EntryContent)
    if k:
        y = 1
       
        for envio in range(2):
            enviarLivroPDF("5", y)
            y = y + 1
    
    b = re.findall(r'2', EntryContent)
    if b:
        y = 1
        myurl = "https://diegooli.s3.us-east-2.amazonaws.com/Voc%C3%AA+N%C3%A3o+Merece+Ser+Feliz+-+Como+Conseguir+Mesmo+Assim+by+Craque+Daniel+%5BDaniel%2C+Craque%5D+(z-lib.org).epub"
        for envio in range(2):
            sleep(10); enviarLivro(myurl, "2", y)
            y = y + 1

    
    currentTime = datetime.datetime.now()
    currentTime.hour
    t = re.findall(r'null', EntryContent)
    if t:
        if currentTime.hour < 12:
            pass       
            
        if 12 <= currentTime.hour < 18:
            print("de tarde")
            '''
            y = 1
           
            for envio in range(2):
                enviarLivroPDF("5", y)
                y = y + 1
            '''
            y = 1
            myurl = "https://diegooli.s3.us-east-2.amazonaws.com/Pap%C3%A9is+Avulsos+by+Assis+Machado+de+(z-lib.org).epub"
            for envio in range(1):
                sleep(10); enviarLivro(myurl, "4", y)
                y = y + 1
            
            y = 1
            myurl = "https://diegooli.s3.us-east-2.amazonaws.com/Critica+da+Razao+Pura+-+Immanuel+Kant.epub"
            for envio in range(1):
                sleep(10); enviarLivro(myurl, "1", y)
                y = y + 1
            
            y = 1
            myurl = "https://diegooli.s3.us-east-2.amazonaws.com/Voc%C3%AA+N%C3%A3o+Merece+Ser+Feliz+-+Como+Conseguir+Mesmo+Assim+by+Craque+Daniel+%5BDaniel%2C+Craque%5D+(z-lib.org).epub"
            for envio in range(1):
                sleep(10); enviarLivro(myurl, "2", y)
                y = y + 1
            
        else:
            print("saindo...")
            
           
            
            
            

        
       
    else:
        print("Não é null, não será enviado o disparo diário")
        

    

    
    

    
    return "a string"

def enviarLivroPDF(id, repeticao):

    banco = mysql.connector.connect (
        host="us-cdbr-east-02.cleardb.com",
        user="b64ccbb6c5e3c0",
        passwd="1569cc14",
        database="heroku_3d387bc54c19158"
        )



    cursor = banco.cursor()
    cursor.execute('SELECT progresso from livros where id="' + id + '"')
    progresso = cursor.fetchall()
    progresso = progresso[0][0]
    progresso = int(progresso)
    

    TOKEN = "1335874302:AAGfJS-I6j8QJL1vpU_oryvlX0_4ZvnJSms"
    bot = telegram.Bot(TOKEN)
    
    data = date.today().strftime('%d/%m/%Y')
    chat_id = "-403146097"
    proximo = progresso + 1
    
    porcentagem = "{0:.0%}".format(proximo/194)   
    porcentagem = str(porcentagem)
    data = date.today().strftime('%d/%m/%Y')

    hoje = date.today().weekday()
    hoje = str(hoje)
    cursor = banco.cursor()
    cursor.execute('SELECT semana from livros where id="' + id + '"')
    semana = cursor.fetchall()
    semana = semana[0][0]
    semana = str(semana)
    if hoje == semana:
        txt = ""
    else:
        txt = "Leitura do dia " + data + "/" + "Progresso: " +  porcentagem

    proximo = str(proximo)
    cursor = banco.cursor()
    comando = 'UPDATE livros SET progresso = "' + proximo + '", envios = envios+1 WHERE ID=' + id
    cursor.execute(comando)
    banco.commit() 
    progresso = str(progresso)
    bot.send_photo(chat_id=chat_id, photo='https://diegooli.s3.us-east-2.amazonaws.com/terapia/terapia+(' + progresso + ').jpg', caption= txt)

    hoje = str(hoje)
    cursor = banco.cursor()
    comando = 'UPDATE livros SET semana = "' + hoje + '" WHERE ID=' + id
    cursor.execute(comando)
    banco.commit() 

    return ""

def enviarLivro(myurl, id, repeticao): 
    with urllib.request.urlopen(myurl) as url:
        s = url.read()
            
    with open(r"c:\tmp\test.epub", "wb") as f:
        f.write(s)

    epub_path = r"c:\tmp\test.epub"

    def epub2thtml(epub_path):
        book = epub.read_epub(epub_path)
        chapters = []
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item.get_content())
        return chapters

    blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script' ]

    def chap2text(chapters):
        output = ''
        soup = BeautifulSoup(chapters, 'html.parser')
        
        soup = str(soup)
        '''
        soup = re.sub(r'(index-.*?_\d)', r"/>\1", soup)
        soup = re.sub(r'<img class="calibre2" src=', '', soup)
        soup = re.sub(r'<img class="calibre1" src=', '', soup)
        soup = re.sub(r'(\-)(</p>)', r'\1', soup)
        soup = re.sub(r'(p\.)( </p>)', r'\1', soup)
        soup = re.sub(r'(/d/d)(  |)', r'Página \1', soup)
               
        soup = re.sub(r'"/>', '', soup)
        '''
        soup = re.sub("', '", "", soup)
        soup = re.sub(r"\xa0", "", soup)
        soup = re.sub("\xa0", "", soup)
        soup = re.sub(r"\\xa0", "", soup)
        #soup = re.sub(r'index-.*?_', r'\1', soup)
        soup = re.sub("</?p[^>]*>", r"/n", soup)
        
        soup = re.sub('<[^<]+?>', '', soup)
            
        
            
        #for t in text:
            #if t.parent.name not in blacklist:
                #output += '{} '.format(t)
            
        return soup


    def thtml2ttext(thtml):
        Output = []
        for html in thtml:
            text =  chap2text(html)
            Output.append(text)
        return Output


    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    ttext = str(ttext)

    #lines =  ttext.split(r'\n')

    #linha = ttext.splitlines(True)

    texto = []

    n = 4000
    mensagem = 0

    banco = mysql.connector.connect (
            host="us-cdbr-east-02.cleardb.com",
            user="b64ccbb6c5e3c0",
            passwd="1569cc14",
            database="heroku_3d387bc54c19158"
        )



    cursor = banco.cursor()
    cursor.execute('SELECT progresso from livros where id="' + id + '"')
    progresso = cursor.fetchall()
    progresso = progresso[0][0]
    progresso = int(progresso)

    for letra in range(5000):
        ultimaLetra = (progresso + n) - 1
        if progresso + n > len(ttext):
            break
        if ttext[ultimaLetra] == ".":
            if ttext[ultimaLetra + 1] == ")":
                print("Procurando letras anteriores...")
                print(ttext[ultimaLetra + 1])
            else:
                print(ttext[ultimaLetra + 1])
                break
        else:
            n = n - 1
    proximo = progresso + n
    print(n)
    print(len(ttext))
    split = [ttext[i:i+n] for i in range(progresso, len(ttext), n)]

    #print(len(ttext))
    #print(split[0])
    resultado = split[0]
    print("------")
        
    resultado.strip(" ")
    resultado  =  resultado.split(r'/n')
    resultado  = '\n'.join(resultado) 
    resultado  =  resultado.split(r'\n')
    resultado  = ''.join(resultado) 
    resultado = re.sub(r"\\n", "", resultado)
    resultado = re.sub("', '", "", resultado)
    resultado = re.sub("', '", "", resultado)
     

        
    print(resultado) 
    '''
    for line in range(10):
            
        if (lines[i] == "") or (lines[i] == " "):
            pass
        else:
            if sum(len(i) for i in texto) > 2500:
                break
            else:
                texto.append(lines[i])
                print(texto)
                print(sum(len(i) for i in texto))
                print("-----------------")
        i = i + 1



    resultado  = '\n'.join(texto)   
    '''
    porcentagem = "{0:.0%}".format(proximo/len(ttext))   
    porcentagem = str(porcentagem)
    TOKEN = "1335874302:AAGfJS-I6j8QJL1vpU_oryvlX0_4ZvnJSms"
    bot = telegram.Bot(TOKEN)
    print("Bot do telegram conectado!")
    data = date.today().strftime('%d/%m/%Y')

    hoje = date.today().weekday()
    hoje = str(hoje)
    cursor = banco.cursor()
    cursor.execute('SELECT semana from livros where id="' + id + '"')
    semana = cursor.fetchall()
    semana = semana[0][0]
    semana = str(semana)
    if hoje == semana:
        cursor = banco.cursor()
        comando = 'UPDATE livros SET ofensiva= ofensiva + 1 where id=' + id
        cursor.execute(comando)
        banco.commit() 


        txt = "\n"  +  resultado    
    else:
        
        cursor = banco.cursor()
        comando = 'UPDATE livros SET ofensiva= ofensiva - 2 where id=' + id
        cursor.execute(comando)
        banco.commit() 

        cursor = banco.cursor()
        cursor.execute('SELECT ofensiva from livros where id="' + id + '"')
        ofensiva = cursor.fetchall()
        ofensiva = ofensiva[0][0]
        ofensiva = str(ofensiva)
        
        
        txt = "Leitura do dia " + data + "\n" + "Progresso: " +  porcentagem + "\n" + "Ofensiva: " +  ofensiva + "\n\n"  +  resultado 

    hoje = str(hoje)
    cursor = banco.cursor()
    comando = 'UPDATE livros SET semana = "' + hoje + '" WHERE ID=' + id
    cursor.execute(comando)
    banco.commit() 


    print("id: ")
    print(id)
    if id == "1":
        chat_id = "-466512231"
        #chat_id = "608446615"
    if id == "4":
        chat_id = "-429509381"
    if id == "3":
        chat_id = "-403146097"
    if id == "2":
        print("se nao nao deu")
        chat_id = "@leituradodia"
        #chat_id = "608446615"
    
    bot.send_message(chat_id, txt, parse_mode='html')
    

    #bot.send_photo(chat_id, photo=open('path', 'rb'))

    print(proximo)
    proximo = str(proximo)
    cursor = banco.cursor()
    comando = 'UPDATE livros SET progresso = "' + proximo + '", envios = envios+1 WHERE ID=' + id
    cursor.execute(comando)
    banco.commit() 

        





'''
url = "https://letterboxd.com/bratpitt/films/diary/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
notasLetterbox = soup.findAll('div', class_='hide-for-owner')

y = 0
for each in range(3):
    nota = notasLetterbox[y]
    y = y + 1
    nota = str(nota)
    nota = re.sub('<div class="hide-for-owner" data-owner="' + "bratpitt" + '"> <span class="rating rated-', '', nota)
    nota =  re.sub('[^0-9]', '', nota)
    
    print(nota)
'''


            
        

   
#---------------------------------------------- Disparo com o IFFT - TELEGRAM -------------------   
@app.route("/ifttt", methods=["GET"])
def handler(): 
    
    datetime.datetime.now()
    datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
    print("Hora do disparo:")
    print(datetime.datetime.now())

    print(EntryContent)

    


    
 




    banco = mysql.connector.connect (
        host="us-cdbr-east-02.cleardb.com",
        user="b64ccbb6c5e3c0",
        passwd="1569cc14",
        database="heroku_3d387bc54c19158"
    )
    #---------------------------------------------- Verificar ofensiva dos livros ------------------- 
    '''
    idTemporario = "4"
    cursor = banco.cursor()
    cursor.execute('SELECT ofensiva from livros where id="' + idTemporario +  '"')
    ofensiva = cursor.fetchall()
    ofensiva = ofensiva[0][0]
    ofensiva = int(ofensiva)
    print(ofensiva)
    if ofensiva < 0:
        f = 1
        for numero in range(10):
            ler = ofensiva + f
            
            
            if ler == 1:
                ofensiva = str(ofensiva)
                f = str(f)
                TOKEN = "1335874302:AAGfJS-I6j8QJL1vpU_oryvlX0_4ZvnJSms"
                bot = telegram.Bot(TOKEN)
                if idTemporario == "4":
                    chat_id = "-429509381"
                txt = "Sua ofensiva está " + ofensiva + ". Você preicsa ler mais " + f + " bloco(s) para ficar com a leitura em dia"
                bot.send_message(chat_id, txt, parse_mode='html')
                print("ALERTA! Sua ofensiva está " + ofensiva + ". Você preicsa ler mais " + f + " bloco(s) para ficar com a leitura em dia")
                break
            f = f + 1
    '''
    
    users = ("deathproof", "austinburke", "silentdawn", "kurstboy", "justmiaslife", "adrianbalboa", "max_delgado", "cervantes3", "joelollo", "twillis04", "xene", "jslk", "swaghili123")
    
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
    
            f = f + 1
            titulos =  str(titulos.text) #passa para string
            anos = str(anos.text)
            titulos = re.sub('<h3 class="headline-3 prettify"><a href="/deathproof/film/', '', titulos)
            titulos = re.sub(r'\/\"\>+.</a></h3>', '', titulos)  
            titulos = re.sub('<h3 class="headline-3 prettify"><a href="/deathproof/film/', '', titulos)
            anos = re.sub('<td class="td-released center<span>', '', anos)  
            anos = re.sub('<span></td>', '', anos)      
            tituloAno = titulos + " " + anos
            testador = titulos
            testador = re.sub('’', '', testador)
            testador = re.sub("'", "", testador)
            
            testador = re.sub("&", "", testador)
            testador = re.sub("-", "", testador)
            testador = re.sub(":", "", testador)
            
            testador = re.sub("é", "e", testador)
            testador = re.sub("´", "", testador)
           
            cursor = banco.cursor()
            cursor.execute("SELECT filme FROM filmes WHERE filme like '%" + testador +  "%'")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            print ("number of affected rows: {}".format(row_count))
            
        
            if row_count <= 0:
                t2 = re.findall(r'Euphoria', testador)
                f2 = re.findall(r'Beyon', testador)
                p2 = re.findall(r'Last Always', testador)
                n2 = re.findall(r'A Voz Suprema do Blues', testador)
                u2 = re.findall(r'Black Bottom', testador)
                
                
                if t2 or f2 or p2 or u2:
                   print("não enviar esse")
                else:
                   sleep(20); enviarFilme(tituloAno, "", "Usuários do Letterbox") #após verificar se há nova postagem, envia o filme para a função do telegram
            else:
                print("### LOG ### - " + users[g] + "  ### - O filme " +  testador + " já está cadastrado")
                if row_count > 1:
                    print("Encontrou varios filmes com esse titulo: " + testador + ", portanto não foram adicionados pontos")
                else:
                    cursor = banco.cursor()
                    comando = "UPDATE filmes SET pontos = pontos + 1 WHERE filme like '%" + testador +  "%'"
                    cursor.execute(comando)
                    banco.commit() 


                

        g = g + 1
    


    return 'a string'
    

#-------------------------------------Enviar os filmes para o telegram --------------------------
def enviarFilme(x, y, z):
    API_KEY = "AIzaSyC_ylJR_jjPf9h3JXWaOMj1pZ1shPzxPS4"
    SEARCH_ENGINE_ID = "006935070929965711800:7vjhbn7medw"
    titulo = x
    fonte = z
    ano = ""
    #titulo = request.get_data(as_text=True)
    m = re.search(r'\d\d\d\d', titulo)
    print("O titulo enviado foi " + titulo)
    if m:
        titulo = titulo.replace("1080", "")
        #titulo = re.search(r'[A-Za-z0-9-.& ,+!@#$%\^*();\/|<>"\'?=:\t_\n[\]{}~`]*.\d\d\d\d', titulo)
        #print(titulo.group())
        #titulo = titulo.group()
    else:
        print("Filme está sem ano")

    
    titulo = titulo.replace('"', '')
    titulo = titulo.replace('#', '')
    titulo = re.sub('&', "", titulo)
    query = titulo
    print("quero é igual a: " + query)
    page = 1
    start = (page - 1) * 1 + 1
    print(query)

    if y: #se o fime está sem o ano, ele precisar pegar o ano no IMDB
        print("foi enviado o y: " + y)
        linkIMDBInteiro = y
        url = linkIMDBInteiro
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        span = soup.find(id='titleYear') #encontra todas as classes h2 do blog
        year = span.text
        titulo = titulo + " " + year
        titulo = re.sub(r'&', "", titulo)
        query = titulo
        print(query)
        

    else:
        #pesquisa no google o filme e IMDB já com o ano
        urlIMDB = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}+imdb&start={start}"
        dataIMDB = requests.get(urlIMDB).json()
        linkIMDBInteiro = dataIMDB.get("items")[0]["link"] 
        i = -1
        for item in range(len(dataIMDB)):
            i = i + 1
            print("procurando links do imdb... " + dataIMDB.get("items")[i]["link"])
            m = re.search(r'https://www.imdb.com/title/', dataIMDB.get("items")[i]["link"])
            if m:
                linkIMDBInteiro = dataIMDB.get("items")[i]["link"]
                break
        print("achou esse link do imdb: " + linkIMDBInteiro)
    
    m = re.search(r'\d\d\d\d', titulo)
    if m:
        print("filme já tem ano")
    else:  #mais um para pegar ano de filmes sem ano do reddit
        url = linkIMDBInteiro
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        span = soup.find(id='titleYear') #encontra todas as classes h2 do blog
        ano = span.text
    

    try:
        urlFilmow = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}+filmow&start={start}"
        dataFilmow = requests.get(urlFilmow).json()
        linkFilmow = dataFilmow.get("items")[0]["link"] 
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
        
    except:
        querySemEspaco = re.sub(r' ', '%20', query)
        querySemEspaco = re.sub(r'&', '', querySemEspaco) 
        linkFilmow = "www.google.com/search?q=filmow%20" + querySemEspaco

    

    #lista_filmes =  str(lista_filmes.text) #passa para string
    #BeautifulSoup(lista_filmes, 'html.parser').text #retira as tags
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
    
    
   
    linkIMDB = linkIMDBInteiro.replace("https://www.imdb.com/title/tt", "")
    linkIMDB = linkIMDB.replace("/", "")
    linkIMDB = linkIMDB.replace("releaseinfo", "")
    linkIMDBInteiro = linkIMDBInteiro.replace("releaseinfo", "")
    #linkFilmow = linkFilmow.replace("ficha-tecnica/", "")

    try:
        req = requests.get('http://www.omdbapi.com/?apikey=73634e02&type=movie&i=' + linkIMDB)
        dicionario = json.loads(req.text)
        tituloIMDB = dicionario['Title']
        NotaIMDB = dicionario['imdbRating']
    except:
        try:
            req = requests.get('http://www.omdbapi.com/?apikey=73634e02&type=movie&i=tt' + linkIMDB)
            dicionario = json.loads(req.text)
            tituloIMDB = dicionario['Title']
            NotaIMDB = dicionario['imdbRating']
        except:
            banco = mysql.connector.connect (
            host="us-cdbr-east-02.cleardb.com",
            user="b64ccbb6c5e3c0",
            passwd="1569cc14",
            database="heroku_3d387bc54c19158"
            )
            print("Não encontrou nenhum titulo")
            #filme não existe, cadastra no banco para na proxima vez nao procurar mais por ele
            

            datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
        
            hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            estado = "negado"
            cursor = banco.cursor()
            comando = "INSERT INTO filmes (filme, fonte, hora, estado) values ('" + query + "', '" + fonte + "', '" + hora + "' , '" + estado + "')"
            cursor.execute(comando)
            banco.commit() 


    try:
        NotaTomate = dicionario['Ratings'][1]
        NotaTomate = NotaTomate['Value']
    except:
        NotaTomate = "N/A"

    try:
        votosQuantidade = dicionario['imdbVotes']
    except:
        votosQuantidade = "N/A"

    
        

    #-------------------------------- Pegar os generos no filmow ou no imdb
        
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

    # ------------------------------------- Procurar o trailer no youtube
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
        


    try:
        #pegar o ano do filme para exibição formatada
        url = linkIMDBInteiro
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        span = soup.find(id='titleYear') #encontra todas as classes h2 do blog
        anoFormatado = span.text
    except:
        print("Não deu o ano imdb")
        anoFormatado = ""

    #pegar sinopse do filme para exibição formata
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

    try:
        year = dicionario['Year']
        year = int(year)
    except:
        year = 0
    j = re.search('\d',numeroCriticas)
    if j:
        numeroCriticas = re.search(r'\d+',numeroCriticas).group()
        
    else:
        numeroCriticas = '0'
    votosQuantidade = re.sub(',', "", votosQuantidade)
    if votosQuantidade == 'N/A':
        print("Sem votos")
        votosQuantidade = 0
    else:
        votosQuantidade = int(votosQuantidade)
    numeroCriticas = int(numeroCriticas)
    # -------------------------------------------- Negar um filme com base em critérios    
    
    generoIngles = dicionario['Genre']
    n = re.search('Short', generoIngles, re.IGNORECASE)
    '''if n:
        a = re.search('curta', genero, re.IGNORECASE)
        if a:
            prtint("O curta já esta catalogado como curta")
        else:
            genero = genero + " Curta"
    '''
    
    if NotaIMDB <= '5.0' or n or (fonte == 'Top 10 do site torrentfreak' and NotaIMDB <= '6.0') or (fonte == 'Usuários do Letterbox' and year < 2019)  or (fonte == 'LegendasTv' and year < 2019) or (numeroCriticas < 15 and votosQuantidade < 700 and NotaIMDB <= '6.0' ) or (numeroCriticas < 10 and votosQuantidade < 700) or year == 0 or year < 2019:
        print("filme não passou no critério, um dos requisitos abaixos não foi suprido:")
        print("Nota é " + NotaIMDB)
        print("Genero é ")
        print("Fonte é " + fonte)
        print(votosQuantidade)
        print(numeroCriticas)


        banco = mysql.connector.connect (
            host="us-cdbr-east-02.cleardb.com",
            user="b64ccbb6c5e3c0",
            passwd="1569cc14",
            database="heroku_3d387bc54c19158"
        )

        testador = nomeIngles.replace("\t", "")
        testador = testador.replace("'", "")
        testador = re.sub("'", "", testador)
        testador = re.sub("&", "", testador)
        testador = re.sub("-", "", testador)
        testador = re.sub(":", "", testador)
        
        testador = re.sub("´", "", testador)
        query = re.sub("'", "", query)
        query = re.sub("&", "", query)
        query = re.sub("-", "", query)
        query = re.sub(":", "", query)
        

        datetime.datetime.now()
        datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
        
        hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estado = "negado"

        cursor = banco.cursor()
        cursor.execute("SELECT filme FROM filmes WHERE filme like '%" + testador +  "%'")
        results = cursor.fetchall()
        row_count = cursor.rowcount
        print ("number of affected rows: {}".format(row_count))
        if row_count <= 0:
            cursor = banco.cursor()
            votosQuantidade = str(votosQuantidade)
            pontos = 1
            pontos = str(pontos)
            comando = "INSERT INTO filmes (filme, fonte, hora, estado, votosQuantidade, pontos) values ('" + testador + " - " + query + "', '" + fonte + "', '" + hora + "' , '"  + estado +  "' , '" + votosQuantidade + "' ,  '" + pontos  +   "')"
            cursor.execute(comando)
            banco.commit() 
            imagemUrl = dicionario['Poster']

            if (fonte == "Usuários do Letterbox" and NotaIMDB < '6.0'):
                print("Não enviar")
            else:
                TOKEN = "1335874302:AAGfJS-I6j8QJL1vpU_oryvlX0_4ZvnJSms"
                bot = telegram.Bot(TOKEN)
                print("Bot do telegram conectado!")
                chat_id = "@negados_alert"
                txt = '[​​​​​​​​​​​](' + imagemUrl + ')' + '*' + nomeFormatado + nomeIngles + ' ' + anoFormatado + '*  \n' + 'Gênero: ' + genero + '  \n' +  'Sinopse: ' +  Sinopse   + '  \n' +  'Notas: IMDB ' + NotaIMDB + ' / RottenTomatoes ' +  NotaTomate  + '  \n' +  'Links: ' +  '[IMDB](' + linkIMDBInteiro + ')'  +  ' / '  +  '[Filmow](' + linkFilmow + ')'  + ' / ' + '[Trailer](' + linkTrailer + ')'  +  '  \n' +  'Fonte: ' + fonte
                bot.send_message(chat_id, txt, parse_mode='markdown')
        else:
            print("### LOG ### - Blog Top10filmes ### - O filme "  + testador + " já está cadastrado")

       

        
        
        
        return ""
    # ---------------------------------------- Enviar filme para o telegram
    else: 
        print("o texto digitado eh {}".format(titulo))
        imagemUrl = dicionario['Poster']
        TOKEN = "1335874302:AAGfJS-I6j8QJL1vpU_oryvlX0_4ZvnJSms"
        bot = telegram.Bot(TOKEN)
        print("Bot do telegram conectado!")
        chat_id = "@movies_alert"
        txt = '[​​​​​​​​​​​](' + imagemUrl + ')' + '*' + nomeFormatado + nomeIngles + ' ' + anoFormatado + '*  \n' + 'Gênero: ' + genero + '  \n' +  'Sinopse: ' +  Sinopse   + '  \n' +  'Notas: IMDB ' + NotaIMDB + ' / RottenTomatoes ' +  NotaTomate  + '  \n' +  'Links: ' +  '[IMDB](' + linkIMDBInteiro + ')'  +  ' / '  +  '[Filmow](' + linkFilmow + ')'  + ' / ' + '[Trailer](' + linkTrailer + ')'  +  '  \n' +  'Fonte: ' + fonte
        bot.send_message(chat_id, txt, parse_mode='markdown')


        banco = mysql.connector.connect (
            host="us-cdbr-east-02.cleardb.com",
            user="b64ccbb6c5e3c0",
            passwd="1569cc14",
            database="heroku_3d387bc54c19158"
        )

        testador = nomeIngles.replace("\t", "")
        testador = testador.replace("'", "")
        testador = re.sub("'", "", testador)
        query = re.sub("'", "", query)
        

        datetime.datetime.now()
        datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
        hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estado = "enviado"



        cursor = banco.cursor()
        votosQuantidade = str(votosQuantidade)
        pontos = 1
        pontos = str(pontos)
        comando = "INSERT INTO filmes (filme, fonte, hora, estado, votosQuantidade, pontos) values ('" + testador + " - " + query +  "', '" + fonte + "', '" + hora + "' , '" + estado + "' , '" + votosQuantidade +   "' ,  '" +  pontos   +  "')"
        cursor.execute(comando)
        banco.commit() 

    EntryContent = request.get_data(as_text=True)
    datetime.datetime.now()
    datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
    print("Hora do disparo:")
    print(datetime.datetime.now())

    print(EntryContent)

    return 'a string'

            