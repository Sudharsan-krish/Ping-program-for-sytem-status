import subprocess

lt = []

with open('iplist.txt','r') as f:
    lt = f.readlines()

unreachable_ip = []

if unreachable_ip != []:
    unreachable_ip.clear()


for ip in lt:
    p1 = subprocess.run('ping '+ ip ,shell=True,text=True,capture_output=True)
    result = p1.stdout
    print(result)
    print('\n')
    if 'Destination host unreachable' in result:
        unreachable_ip.append(ip)
    if 'Request timed out' in result:
        unreachable_ip.append(ip)

print(f'{unreachable_ip} -- unreachable IP list')