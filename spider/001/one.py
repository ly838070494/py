import requests
import pymysql
from datetime import datetime, timedelta
from pyquery import PyQuery as pq

url = 'http://wufazhuce.com/one/'
#数据库配置
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='111111', db='one', charset='utf8')
cursor = conn.cursor()

cursor.execute('select * from article order by id desc limit 1')
article = cursor.fetchone()
#print(article)
i = 0
date = '2012-10-15'
if article:
	i = article[0]
	date = article[-1]

j = 0
while True:
	i += 1
	response = requests.get(url+str(i))
	if response.status_code == 404:
		j += 1
		if j > 100:
			print('game over')
			break
		continue
	elif response.status_code == requests.codes.ok:
		cursor.execute('select id from article where id = %s', (str(i),))
		value = cursor.fetchone()
		if value:
			continue
		response.encoding = 'utf8'
		doc = pq(response.text)
		title = doc('.one-cita').text()
		image_path = doc('.one-imagen img').attr['src']
		image = requests.get(image_path)
		path = './images/img'+str(i)+'.png'
		#下载图片
		with open(path, 'wb') as f: 
			f.write(image.content)

		try:
			cursor.execute('insert into article (id, title, path, date) values (%s, %s, %s, %s)', [str(i), title, path, date])              
			conn.commit()
			print('数据插入成功：%d' % i)
		except Exception as e:
			print(e)

	#时间加一天
	date = datetime.strptime(date, '%Y-%m-%d')
	date += timedelta(days=1)
	date = date.strftime('%Y-%m-%d')
cursor.close()
conn.close()
	