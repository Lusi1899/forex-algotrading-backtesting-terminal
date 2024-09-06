from bs4 import BeautifulSoup
import cloudscraper

def get_article(card):
    if card is not None:
        return dict(
                headline=card.get_text(),
                link='https://reuters.com'+ card.get('href')

        )
def bloomberg_com():
    s=cloudscraper.create_scraper()

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"}

    resp=s.get("https://www.reuters.com/business/finance/",headers=headers)
    soup=BeautifulSoup(resp.content,"html.parser")
    links=[]
    cards=soup.select('[class^="media-story-card__body"]')

    for card in cards:
        ca=card.find('a',{'data-testid':'Heading'})
        links.append(get_article(ca))
        links1=links[1:]
    return links1