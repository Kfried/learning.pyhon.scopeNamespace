apples = 1
'''This is the BAD way of doing it, not that you should be using globals '''
def add_apple():
     global apples
     apples+=1
     print(apples)

add_apple()

'''the following shows a great example of how the globas are and are not accessed
and note it breaks the new_fruit at the end'''

def add_apple():
    return apples+1

print(apples)
add_apple()
print(apples)
apples = add_apple()
print(apples)

fruit = ['banana', 'cocnut']
if apples < 3:
    new_fruit = fruit[0]

print(new_fruit)