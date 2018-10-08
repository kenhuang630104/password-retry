i = 3
password = 'a123456'
while i > 0:
	pwd = input('please input password')
	if pwd == password:
		print('login success!')
		break
	else:
		i = i - 1
		print('you have', i,'chance!')