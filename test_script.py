from FortiAPI import *

return_lists = []
with open('testfile.py', 'r') as f:
    return_lists = f.read().splitlines()

x = Fortigate(ip='192.168.1.99', vdom='root', user='admin', passwd='')
for i in return_lists:
    i = i.split(',')
    x.AddFwAddressIdempotent(name=+i[0]+,subnet=i[1])
