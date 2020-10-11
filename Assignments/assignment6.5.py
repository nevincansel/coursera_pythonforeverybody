text = "X-DSPAM-Confidence:    0.8475"
posz = text.find('0')
num = text[posz:]
print(float(num))
