from socket import*
host = "51.158.165.206"
port = 9091
obj = socket(AF_INET, SOCK_STREAM)
obj.connect((host, port))
while True:
	data = str(obj.recv(1024))
	try:
	    print(data)
	    answer = data.split('\\r\\n')[-2].upper()
	    print(f'answer = {answer}')
	    obj.sendall(answer.encode() + b'\r\n')
	    flag = answer.split()[-1]
	except:
		print("END!")
		break
print(f'flag = {flag}')
