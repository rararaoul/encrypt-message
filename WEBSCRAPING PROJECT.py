#!/usr/bin/env python
# coding: utf-8

# In[4]:


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url="https://www.hemnet.se/bostader?location_ids%5B%5D=898472"
# Gör så att request kommer från en browser (i det här fallet från Mozilla version 5.0)
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

# Läs info från url 
webpage = urlopen(req).read()

# skapa en BeatifulSoup
soup = soup(webpage, "html.parser")

css_key="li.normal-results__hit.js-normal-list-item"

container= [i for i in soup.select(css_key)]


css_key_m2 ="div.listing-card__attribute.listing-card__attribute--primary"


# In[5]:


url = "https://www.hemnet.se/bostader?location_ids%5B%5D=898472&page=3"


# In[6]:


lst_adress=[]
lst_room=[]
lst_price=[]
lst_squaremeter=[]
    
for listing in container:
    # no. of rooms
    rooms = [i.text for i in listing.select(css_key_m2)][2]
    lst_room.append(rooms)
    
    # price
    price = [i.text for i in listing.select(css_key_m2)][0]
    lst_price.append(price)
    
    # sqm
    squaremeter = [i.text for i in listing.select(css_key_m2)][1]
    lst_squaremeter.append(squaremeter)
    
    # address
    adress = [i.text for i in listing.select("h2")][0]   
    
    #vi gjorde om lista till string i adresser genom att plocka ut det första elementet. 
    lst_adress.append(adress)
    


# In[7]:


lst_adress


# In[8]:


len(lst_room)


# In[9]:


lst_adress


# In[10]:


#regex för att ta bort vissa värden
#hämta url länkar från varje rum, sqm, lägenhet och pris
#loop för att uppatera för varje sida (150 träffar, 4 sidor)
-> skapa en kod som loopar genom url:en


# In[ ]:


lst_price


# In[ ]:


# css keys

css_key_container = "li.normal-results__hit.js-normal-list-item"

css_key_m2_price_rooms ="div.listing-card__attribute.listing-card__attribute--primary"


# In[ ]:


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

lst_adress=[]
lst_room=[]
lst_price=[]
lst_squaremeter=[]

for x in range(1,5):
    url=f"https://www.hemnet.se/bostader?location_ids%5B%5D=898472&page={x}" 
    print(x)
    print(url)
    
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

    # Läs info från url . request och webpage funktionerna använder samma data igen
    webpage = urlopen(req).read()
    
    page_soup = soup(webpage, "html.parser")
    
    container = [i for i in page_soup.select(css_key_container)]

    for listing in container:
   
        rooms = [i.text for i in listing.select(css_key_m2_price_rooms)][2]
        lst_room.append(rooms)

        # price
        price = [i.text for i in listing.select(css_key_m2_price_rooms)][0]
        lst_price.append(price)

        # sqm
        squaremeter = [i.text for i in listing.select(css_key_m2_price_rooms)][1]
        lst_squaremeter.append(squaremeter)

        # address
        adress = [i.text for i in listing.select("h2")][0]
        lst_adress.append(adress)
    


# In[11]:


import pandas as pd


# In[52]:


hemnet = pd.DataFrame({"adress":lst_adress, "room":lst_room, "price":lst_price, "squaremeter":lst_squaremeter})


# In[53]:


hemnet.to_csv("hemnet_unclean.csv")


# In[54]:


hemnet


# # cleaning

# ## adress

# In[55]:


type(hemnet.adress)


# In[56]:


hemnet.adress[0]


# In[57]:


hemnet.adress=hemnet.adress.str.replace("\n" , "")


# In[58]:


hemnet.room=hemnet.room.str.replace("\n" , "")


# In[59]:


hemnet.room=hemnet.room.str.replace("rum" , "")


# In[60]:


hemnet.price=hemnet.price.str.replace("\n" , "")


# In[61]:


hemnet.price=hemnet.price.str.replace("kr" , "")


# In[62]:


hemnet.squaremeter=hemnet.squaremeter.str.replace("\n" , "")


# In[63]:


hemnet.squaremeter=hemnet.squaremeter.str.replace("m²" , "")


# In[64]:


hemnet.squaremeter


# In[29]:


hemnet.room


# In[ ]:





# In[65]:


hemnet.adress.value_counts(dropna=False)


# In[41]:


import numpy as np


# In[42]:


hemnet


# In[66]:


# fundera på descr eller loc funktioner för prisintervaller du vill ta fram.
#fortsätt rensa dataframe på "kr" och "rum" tex


# In[67]:


hemnet.info()


# In[70]:


hemnet.price


# In[80]:


hemnet.price.str.replace(" ", "").str.replace(" ", "")


# In[76]:


hemnet.price = hemnet.price.str.replace(" ", "").astype("int")


# In[46]:


hemnet.set_index("price", inplace=True)


# In[51]:


hemnet.sort_index(ascending=False)


# In[ ]:





# In[47]:


hemnet.columns


# In[37]:


hemnet.loc[0]


# In[38]:


hemnet.loc[hemnet.price ]


# In[89]:


hemnet.price.agg("mean")


# In[32]:


hemnet.describe()


# In[36]:


hemnet.sort()


# In[34]:


import seaborn as sns


# In[35]:


sns.boxplot(hemnet["price"])


# In[37]:


hemnet.adress.replace(to_replace = [“\n”], value = [""], inplace= True)


# In[ ]:




