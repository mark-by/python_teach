email = ''
while email.find('@') == -1:
    email = input()
print(f"Вы вошли как {email.split('@')[0]}")