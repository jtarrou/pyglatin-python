pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    (original)= original.lower()
    word = (original)
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print original
else:
    print 'empty'
