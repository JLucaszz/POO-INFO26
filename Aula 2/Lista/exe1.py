sdp = 0
sdi = 0
for i in range(4):
    x = int(input())
    if x%2 == 0: sdp += x
    else: sdi += x
print('soma dos pares: ', sdp)
print('soma dos ímpares: ', sdi)