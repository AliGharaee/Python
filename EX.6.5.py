text = "X-DSPAM-Confidence:    0.8475"
nu = text.find('0.8475')
en = text.find('5')
re = text[nu : en+1]
ref = float(re)
print(ref)
