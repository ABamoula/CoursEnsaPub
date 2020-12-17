voe = 'aeiouy'
phrase = 'Le language du Python est super'
count = 0
for lign in phrase:
    if lign in voe:count+=1
print(count)