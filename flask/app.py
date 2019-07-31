import random
import requests
from bs4 import BeautifulSoup
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/lotto')
def lotto():
    numbers = random.sample(range(1, 46), 6)
    return render_template('lotto.html', numbers=numbers)

@app.route('/lunch')
def lunch():
    lst = {
        '짜장면': 'http://static.hubzum.zumst.com/hubzum/2019/07/01/10/967a67742c244ebe9ac7c85048c591c3.jpg',
        '짬뽕': 'https://i.ytimg.com/vi/M04aOUyPIDg/maxresdefault.jpg',
        '스테이크': 'https://fresheasy.speedgabia.com/contents/p.images/S1932390/750x750.jpg',
        '칼국수': 'https://homecuisine.co.kr/files/attach/images/140/824/012/7ece1535875d6ce18990de309b9dbcfb.JPG',
        '나주곰탕': 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1201/IE002061721_STD.JPG'
    }
    menu, img = random.choice(list(lst.items()))
    return render_template('lunch.html', menu=menu, img=img)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/search')
def search():
    opgg_url = 'https://www.op.gg/summoner/userName='
    summoner = request.args.get('summoner')
    url = opgg_url + summoner

    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    tier = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank').text
    return render_template('search.html', tier=tier, summoner=summoner)

if __name__== '__main__':
    app.run(debug=True)