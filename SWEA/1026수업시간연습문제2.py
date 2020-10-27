num = 0x11D06079861D79F99F
binay_num = bin(num)[2:]
print(binay_num)
for i in range(0, len(binay_num), 7):
    print(int(binay_num[i:i+7], 2))