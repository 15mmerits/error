import requests
import pandas as pd 
from bs4 import BeautifulSoup

# URL of Netflix Stock site
#url error below 
url = 'https://finance.yahoo.com/quote/NFLX/'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')
# print(soup.prettify)

# HTML Table into Pandas DataFrame

netflix_data = pd.DataFrame(columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
print(netflix_data)

# Isolating the body of table which contains all the information
# Then we loop through each row & find all colum values for each row

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    volume = col[6].text
    
# Then we append the data of each row to the table

netflix_data = netflix_data.append({'Date': date, 'Open': open, 'High': high, 'Low': low, 'Volume': volume}, ignore_index=True)


# netflix_data.head() # Print DataFrame
# # Pandas read_html
read_html = pd.read_html(url)
# #converting bs4 into string
bs4_str = pd.read_html(str(soup))

netflix_dataframe = bs4_str[0]
netflix_dataframe.head(5) 
