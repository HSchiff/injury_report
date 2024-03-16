from bs4 import BeautifulSoup
import requests

class Player:
    def __init__(self, name, injury, participation, status):
        self.name = name
        self.injury = injury
        self.participation = participation
        self.status = status

# fixes status if the bills dont update their injury report
def isPlaying(data_list):
    p = ''
    for status in data_list:
        if status == '':
            break
        else:
            p = status
    return p

# format the list so it's readable
def format(players_list):
    content = f"{'-' * 81}\n"
    content += f"| {'Player' : <20}| {'Injury' : <20}| {'Practice Status' : <20}| {'Game Status' : <11} |\n"
    content += f"{'-' * 81}\n"
    for player in players_list:
        content += f"| {player.name : <20}| {player.injury : <20}| {player.participation : <20}| {player.status : <11} |\n"
    content += f"{'-' * 81}"
    return content

# parses website
def parse():
    html_text = requests.get("https://www.buffalobills.com/team/injury-report/").text

    soup = BeautifulSoup(html_text, 'lxml')

    table = soup.find('table', class_ = 'd3-o-table d3-o-table--row-striping')

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')


    # creates instance for each player in the injury report
    players_list = []
    for i in rows:
        table_data = i.find_all('td')
        data = [j.text.strip() for j in table_data]
        player = Player(data[0], data[2], isPlaying(data[3:5]), data[6])
        players_list.append(player)

    content = format(players_list)
    print(content)
    f = open("log.txt", "w")
    f.write(content)

parse()