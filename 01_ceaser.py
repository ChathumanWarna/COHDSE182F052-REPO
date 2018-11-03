plaintext=input('Enter Your Message:')
alphabet="abcdefghijklmnopqrstuwxyz"
key=1
cipher=''
for i in plaintext:
    if i in alphabet:
      cipher +=alphabet[(alphabet.index(i)+key)%(len(alphabet))]
print('Youe Encrypted Message Is :'+cipher)
