from bs4 import BeautifulSoup
import cloudscraper, time, pandas as pd

def extractor(url):
    page = scraper.get(url)
    sp = BeautifulSoup(page.text, 'lxml')
    p = sp.find_all('p')
    text = ''
    for r in p:
        text += r.getText()
    return text

scraper = cloudscraper.create_scraper()
url = 'https://es.cointelegraph.com'
page = scraper.get(url+'/tags/bitcoin')


soup_page = BeautifulSoup(page.text, 'lxml')
_links = soup_page.find_all('a',{'class':['post-card-inline__title-link']})
_links = [url+x['href'] for x in _links]
categorias = soup_page.find_all('span', {'class':['post-card-inline__badge',' post-card-inline__badge_default']})
categorias = [x.getText() for x in categorias]
_fechas = soup_page.find_all('time', {'class':['post-card-inline__date']})
_fechas = [x['datetime'] for x in _fechas]


enlaces, contenido, fechas = [], [], []
for i in range(len(categorias)):
    if 'Noticias' in categorias[i]:
        time.sleep(3)
        try:
            enlaces.append(_links[i])
            contenido.append(extractor(_links[i]))
            fechas.append(_fechas[i])
        except Exception as e:
            if '404' in str(e):
                time.sleep(3)
                enlaces.append(_links[i])
                contenido.append(extractor(_links[i]))
                fechas.append(_fechas[i])
            else:
                print('{} \nEn enlace: {}'.format( str(e), _links[i] ) )


new_data = pd.DataFrame({
    'Enlace': enlaces,
    'Texto': contenido,
    'Fecha': fechas
})
data = pd.read_csv('datos.csv')

for enlace in new_data['Enlace']:
    if enlace not in data['Enlace']:
        data = data.append(new_data, ignore_index=True)
data.to_csv('datos.csv')