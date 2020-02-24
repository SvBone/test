import hashlib
import json

mas = [1,3,4,3]
count = 0
has = ''
while True:
	has = str(hashlib.sha256(str(mas).encode()).hexdigest())
	if '000' in has[:3]:
		break
	else:
		mas.append(3)
		count += 1
mas = [{'has': has, 'count': count}]
with open('nh.json', 'w') as file:
	json.dump(mas,file, indent=4)
print(has, count)