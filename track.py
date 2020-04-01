from bs4 import BeautifulSoup
import requests
import smtplib

url = requests.get('https://www.flipkart.com/nikon-d5600-dslr-camera-body-dual-lens-af-p-dx-nikkor-18-55-mm-f-3-5-5-6g-vr-70-300-f-4-5-6-3g-ed-16-gb-sd-card/p/itmezvbdg2azkujh?pid=DLLEZVB8MDXDYTHG&lid=LSTDLLEZVB8MDXDYTHGCGYU2R&marketplace=FLIPKART&srno=s_1_1&otracker=search&fm=organic&iid=8096ecdf-7f03-45a2-a5b6-820bf7d3d7f2.DLLEZVB8MDXDYTHG.SEARCH&ppt=sp&ppn=sp&ssid=2pqk52pd9s0000001584272217479&qH=ac7edfe844c3c5f1').text
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

def check_price():
	soup = BeautifulSoup(url, 'lxml')

	find = soup.find(id='container')


	title = soup.find('div').h1.text
	print(title)
	print()
	price = soup.find('div', class_='_1vC4OE _3qQ9m1').text

	#print(price)
	new_price = price.split(',')
	price = new_price[0] + new_price[1]
	price = price.split('₹')[1]

	converted_price = float(price)
	print(converted_price)

	if(converted_price > 45000):
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('panchalutsav274@gmail.com', 'rpdwbzomffhxvwre')
	subject = "CHECKOUT HURRY! THE PRICE IS DOWN"
	body = "CHECK THE FLIPKART LINK  https://www.flipkart.com/nikon-d5600-dslr-camera-body-dual-lens-af-p-dx-nikkor-18-55-mm-f-3-5-5-6g-vr-70-300-f-4-5-6-3g-ed-16-gb-sd-card/p/itmezvbdg2azkujh?pid=DLLEZVB8MDXDYTHG&lid=LSTDLLEZVB8MDXDYTHGCGYU2R&marketplace=FLIPKART&srno=s_1_1&otracker=search&fm=organic&iid=8096ecdf-7f03-45a2-a5b6-820bf7d3d7f2.DLLEZVB8MDXDYTHG.SEARCH&ppt=sp&ppn=sp&ssid=2pqk52pd9s0000001584272217479&qH=ac7edfe844c3c5f1"
	

	msg = f'Subject: {subject} \n\n {body}'

	server.sendmail(
         'panchalutsav274@gmail.com', 
          'crazybanda793@gmail.com',
          msg,
          
		)
	print('HEY! EMAIL HAS BEEN SENT')

	server.quit()

check_price()







