from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
from pandas import ExcelWriter


class ProductScrapper:

    def __init__(self ,urll,urll2):
        self.urll=urll
        self.urll2=urll2
        self.df=pd.DataFrame()

        self.list1=[]
        self.Book_name = []
        self.Book_price = []
        self.Book_org_price = []
        self.Book_ratings = []


    def weflip1(self):
        url1=urlopen(self.urll)
        page_soup = soup(url1, 'html.parser')
        for link in page_soup.findAll('a', {'class': '_2SvCnW'}):
            self.list1.append(link['href'])
        print(self.list1)
        return self.list1


    def weflip2(self):

          for i in range(0, len(self.list1)):
            url2 = urlopen(self.urll2+ self.list1[i])
            page_soup1 = soup(url2, 'html.parser')
            for l in page_soup1.findAll('a', {'class': '_2cLu-l'}):
                 self.Book_name.append(l['title'])

            for l in page_soup1.find_all('div', class_='_1vC4OE'):
                self.Book_price.append(l.text)

            for l in page_soup1.find_all('div', class_='_3auQ3N'):
                self.Book_org_price.append(l.text)

            for l in page_soup1.find_all('div', class_='hGSR34'):
                self.Book_ratings.append((l.text))

          Book_names=pd.Series(self.Book_name)
          Book_prices=pd.Series(self.Book_price)
          Book_org_prices=pd.Series(self.Book_org_price)
          Book_ratings=pd.Series(self.Book_ratings)

          self.df.insert(0,'Book Names',Book_names)
          self.df.insert(1,'Discounted Price',Book_prices)
          self.df.insert(2,'Original Price',Book_org_prices)
          self.df.insert(3,'Ratings',Book_ratings)
          print(self.df)

          writer=ExcelWriter('C:\\Users\\tejal\\Desktop\\VOIce\\wavBOOKSCRAPPER.xlsx')
          self.df.to_excel(writer)
          writer.save()


if __name__=='__main__':
    s1="https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    s2="https://www.flipkart.com"
    p1=ProductScrapper(s1,s2)
    p1.weflip1()
    p1.weflip2()