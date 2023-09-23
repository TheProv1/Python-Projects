import qrcode

site_url = input('Enter the url of the website: ')

img = qrcode.make(site_url)

img.save('qr.png')