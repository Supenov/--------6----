from ipaddress import*

net = ip_network('115.198.0.0/255.254.0.0')

k = 0
for ip in net:
    n_ip = f'{ip:b}'
    if n_ip.count('1') % 5 == 0:
        k += 1
print(k)