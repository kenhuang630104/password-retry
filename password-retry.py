i = 3
password = 'a123456'
while i > 0:
	i = i - 1
	pwd = input('please input password')
	if pwd == password:
		print('login success!')
		break
	else:
		print('invalid password!', end = " ")
		if i > 0:
			print('You have', i, 'chance')