text = "X-DSPAM-Confidence:    0.8475";
pos=text.find(':')
value=text[pos+1:]
print(float(value))
