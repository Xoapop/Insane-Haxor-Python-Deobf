import os, base64, codecs

# repalce these vars with the obf code
magic = 
love = 
god = 
destiny = 
joy = 
trust = 


# opens txt decodes it from base64 and writes to the txt
with open('decoded.txt', 'w') as f:
        thang = base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'
        print(thang, file=f)

with open('decoded.txt', 'r') as file:
    data = file.read()

os.remove("decoded.txt")

# removes the b" and reformats the code and writes to txt
decoded_data = data[3:-2]
decoded_data = decoded_data.replace('\\\\', '\\').replace('\\t', '\t').replace('\\n', '\n')

with open('formatted.txt', 'w') as file:
    file.write(decoded_data)

