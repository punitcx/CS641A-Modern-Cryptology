letterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
cipher= """omkf pi hdn cmgef icphsck .H krg vphqkc c,
fic mco kqgf ioqag eo qfcmckf oq ficpihdn
cm .Kg dcgeficu hfcm pi hdn cmklo uuncdgmc
oqfc mc kfoq afihqfiokgq c!Fi cpgy cvkc yeg 
mfio kdck kha cokh kodjuck vn k fofvfo
gqpojicmoqli opiyoa of kihsc nccqki oefc
ynr2 juhpck. Fi c jhkklgm yok oMxr9V1x ya
flofigvffic xvgfck. Fio kokfice"""

cipher=cipher.upper()
cipFreq={}
mapping={}
total=0
for let in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # Calculate total letters
	total+=cipher.count(let)
for let in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # Do Frequency Analysis
	cipFreq[let]=round(cipher.count(let)*100/total,2)

letterFreq=list(letterFreq.items())
cipFreq=list(cipFreq.items())
cipFreq.sort(key=lambda x: x[1], reverse = True)

for i in range(6): # Create the mapping dictionary
	mapping[cipFreq[i][0]]=letterFreq[i][0].lower()

print("CIPHERTEXT: {}".format(cipher))
plain=cipher
mapping['I'] = 'h'
mapping['K'] = 's'
mapping['O'] = 'i'
mapping['M'] = 'r'
mapping['E'] = 'f'
for key in mapping:
	plain=plain.replace(key,mapping[key]) # Replace the substituted characters from frequency analysis.
print("English Frequency: {}\nCipher Frequency Analysis: {}\nHalf Plaintext:{}".format(letterFreq,cipFreq,plain))

print("Plaintext using manual inspection :\n","IRST CH AMB EROFT HECAVES .A SYO UCANSE E, THE REI SNOT HINGO FI NTEREST IN THECHAMB ER .SO MEOFTHEL ATER CH AMB ERSWI LLBEMORE INTE RE STIN GTHANTHISON E!TH ECOD EUSE DFO RTHI SMES SAG EISA SIMPLES UB S TITUTI ONCIPHERINWH ICHDIG IT SHAVE BEENSH IFTE DBY2 PLACES. TH E PASSWOR DIS iRqy9U1q dg tWITHOUTTHE QUOTES. THI SISTHEF")

#USING FINAL SUBTITUTIONS as
#[ABCDEFGHIJKLMNOPQRSTUVWXYZ]
#[GKEMFTOAHPSWRBICNYVJLUXQDZ]

'''Final plaintext that we got after rearrangement of spaces is:
IRST CHAMBER OF THE CAVES. AS YOU CAN SEE, THERE IS NOTHING OF INTEREST IN THE CHAMBER. SOME OF THE LATER CHAMBERS WILL BE MORE INTERESTING THAN THIS ONE! CODE USED FOR THIS MESSAGE IS A SIMPLE SUBSTITUTION CIPHER IN WHICH DIGITS HAVE BEEN SHIFTED BY 2 PLACES. THE PASSWORD IS iRqy9U1qdgt WITHOUT THE QUOTES. THIS IS THE F
'''


#After Getting the password, try permutations of shifted numbers in circular way(mod 10) and attempt the password.
cipher=list("iRqy9U1qdgt")
print("Cipher={}".format(cipher))
for i in range(1,10):
	cip=list(cipher)
	cip[4]=str((int(cip[4])+i)%10)
	cip[6]=str((int(cip[6])+i)%10)
	print("Number Increment Shift {}".format(i),''.join(cip))
