string='hello world good morning'
result=string.split(' ')
for word in result:
    length =len(word)
    if (length %2!=0):
         print('word : {} and length is : {}'.format(word,length))
         print('it is even length!!!!')
   
