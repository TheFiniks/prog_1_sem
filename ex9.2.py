with open('input.txt', 'r') as f:
    sentencens = f.read()
print(sum(sentencens.count(i) for i in '.!?') - sentencens.count('!?') - sentencens.count('?!') - 2*sentencens.count('...'))
