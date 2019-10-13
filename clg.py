import requests
adm=input("enter the admission number:") #input the admission number

url = "http://elive.sjcetpalai.ac.in/Uploads/Admission/"+adm+".jpg"
filename = url.split("/")[-1] #takes the url in the list hold the last position [-1]
save= requests.get(url)

if save.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(save.content)
        print(f"[+] successfully captured {filename}")
else:
	print("404 you doesn't belong here")
      

