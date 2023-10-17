
# Teste Programador Data Scraping

import json
from dataclasses import dataclass

from bs4 import BeautifulSoup
from selenium import webdriver

# Definindo a class do dados

@dataclass
class Item:
    sport_league: str = ''
    event_date_utc: str = ''
    team1: str = ''
    team2: str = ''
    pitcher: str = ''
    period: str = ''
    line_type: str = ''
    price: str = ''
    side: str = ''
    team: str = ''
    spread: float = 0.0

# Criar uma instancia do Web Driver
driver = webdriver.Chrome()

# Carregar a pagina 
driver.get("https://www.veri.bet/sports")

#  Encontre e clique no Botão, Acesse o simulador de Aposta 
button = driver.find_element_by_xpath("//button[contains(text(), 'Access Betting Simulator')]")
button.click()

# Aguardando a pagina carregar
driver.implicitly_wait(10)

# Obtenha o codigo fonte da pagina 
page_source = driver.page_source

#  Analisando o codigo fonte 
soup = BeautifulSoup(page_source, 'html.parser')

# Encontre a tabela e analisa 
table = soup.find('table', {'class': 'table-casino'})
rows = table.find_all('tr')[1:]

items = []
for row in rows:
    cells = row.find_all('td')
    item = Item(
        sport_league=cells[0].get_text(),
        event_date_utc=cells[1].get_text(),
        team1=cells[2].get_text(),
        team2=cells[3].get_text(),
        pitcher=cells[4].get_text(),
        period=cells[5].get_text(),
        line_type=cells[6].get_text(),
        price=cells[7].get_text(),
        side=cells[8].get_text(),
        team=cells[9].get_text(),
        spread=float(cells[10].get_text())
    )
    items.append(item)

# Fechando Webdriver
driver.quit()

# Converte os dados para JSON
json_data = json.dumps([item.__dict__ for item in items], indent=2)

# Envie o Json para o console
print(json_data)








