string = raw_input('Enter the sentence : ')
f=0
ls=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in ls:
    if not(i in string):
        f=1
        break
if f==1:
    print ' Not Pangram '
elif f==0:
    print ' Pangram '
