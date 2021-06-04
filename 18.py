words = ["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]

variants = {}
varCount = 0

for var in range(97, 123):
    variants[chr(var)] = 0

for word in words:
    for var in word:
        variants[var] += 1
        varCount += 1

word = input("Введите стоп слово: ")

chance = 1
for var in word:
    chance *= variants[var] / varCount

print(chance)