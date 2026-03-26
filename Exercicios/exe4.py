entrada = input()

n = ""
s = 0

for c in entrada:
   if c == ",":
      s += int(n)
      n = ""
   else:
      n += c

s += int(n)
print("Soma =", s)
