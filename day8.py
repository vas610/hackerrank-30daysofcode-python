# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


if __name__ =='__main__':
    
    phone_book = {}
    
    n = int(input().strip())
    for l in range(n):
        l_split = str(input().strip()).split()
        phone_book[l_split[0]] = l_split[1]
        

    searches = sys.stdin.readlines()
    for search in searches:
        search = search.strip()                
        if search in phone_book:
            print(f'{search}={phone_book[search]}')
        else:
            print("Not found")
