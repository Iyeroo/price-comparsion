from bs4 import BeautifulSoup
import requests
import pdb
from my_fake_useragent import UserAgent

ua = UserAgent(family="chrome", os_family="windows")

def get_content(url: str) -> str:
    """Gets the contents of a remote url.
    Args:
        url
    Returns:
        The content fetched from remote url.
    """
    user_agent = ua.random()
    while True:
        content: str = requests.get(url, headers={"User-Agent": user_agent})
        if "api-services-support@amazon.com" in content.text:
            user_agent = ua.random()
            continue
        break

    return content

def flipkart_search(name):
    try:
        global flipkart
        # pdb.set_trace()
        name1 = name.replace(" ","+")
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')


        print("\nSearching in flipkart....")
        # print(res.text)
        soup = BeautifulSoup(res.text,'html.parser')
        
        if(soup.select('.KzDlHZ')):
            flipkart_name = soup.select('.KzDlHZ')[0].getText().strip().upper()
            flipkart_image = soup.select('.DByuf4')[0]['src']
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('.Nx9bqj')[0].getText().strip()
                flipkart_name = soup.select('.KzDlHZ')[0].getText().strip()
                print("Flipkart:")
                print(flipkart_name)
                print(flipkart_price)
                print("---------------------------------")
                
        elif(soup.select('.s1Q9rs')):
            flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
            flipkart_name = flipkart_name.upper()
            flipkart_image = soup.select('._396cs4')[0]['src']
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
                print("Flipkart:")
                print(flipkart_name)
                print(flipkart_price)
                print("---------------------------------")
        else:
            flipkart_price='0'
            
        return (flipkart_price, flipkart_image) 
    except E:
        print(E)
        print("Flipkart: No product found!")  
        print("---------------------------------")
        flipkart_price= '0'
    return (flipkart_price, '')

def amazon_search(name):
    try:
        global amazon
        # pdb.set_trace()
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/s?k={name2}&crid=3RLCCEAOBMMC7&sprefix={name2}%2Caps%2C286&ref=nb_sb_noss_1'
        # amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = get_content(amazon)
        print("\nSearching in amazon...")
        print(res.text)
        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            amazon_image = soup.select('.s-image')[i]['src']
            if name in amazon_name:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                print("Amazon:")
                print(amazon_name)
                print("₹"+amazon_price)
                print("---------------------------------")
                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:
                    amazon_price = '0'
                    print("amazon : No product found!")
                    print("-----------------------------")
                    break
                    
        return (amazon_price, amazon_image)
    except Exception as error:
        print(error)
        print("Amazon: No product found!")
        print("---------------------------------")
        amazon_price = '0'
    return (amazon_price, '')

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g

# if flipkart_price=='0':
#     print("Flipkart: No product found!")
#     flipkart_price = int(flipkart_price)
# else:
#     print("\nFlipkart Price:",flipkart_price)
#     flipkart_price=convert(flipkart_price)
# if amazon_price=='0':
#     print("Amazon: No product found!")
#     amazon_price = int(amazon_price)
# else:
#     print("\nAmazon price: ₹",amazon_price)
#     amazon_price=convert(amazon_price)
