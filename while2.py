#密碼重試程式
x = 1
y = 2
while x <= 3 :
	password = input('請輸入密碼:')
	if password == 'a123456' :
		print('登入成功')
		break		
	else:
		print('密碼錯誤!還有',y,'次機會')
		x += 1
		y -= 1


