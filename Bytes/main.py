message = b"Hello world hope you are doing good!!!"

data = bytearray(message)

print(f"Original Message : {message.decode('utf-8')}")

#encryption 

for i in range(len(data)):
    data[i] = (data[i] - 4) % 256

print(f"Encrypted data : {data.decode('utf-8')}")

#decryption
for i in range(len(data)):
    data[i] = (data[i] + 4) % 256

print(f"decrypted data : {data.decode('utf-8')}")