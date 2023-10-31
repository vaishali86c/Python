n = input("Whats your name ? ")

print("hello,",n)

# remove whitespaces  
n = n.strip()
# capital first letter
n = n.capitalize()
# capital all the first letter 
n = n.title()
# split users name in first and last name
n = n.split(" ")
print(f"hello, {n}")
