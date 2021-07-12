import re

str1 = "My name is Rohit Mondal and my email id is example@gmail.com, I am pursuing B.Tech from KIIT University, Bhubaneshwar and I also have a college email, which is example2@gmail.com."

list1 = re.findall(r'\w+@\S+\w', str1)
Write = open("email_extract.txt", 'a')
j = 1
for i in list1:
    Write.write(f"Email{j}: {i}\n")
    j = j+1
Write.close()

print(f"Email list is as followed:\n{list1}\n")
print(f"Total number of emails are: {j-1}")