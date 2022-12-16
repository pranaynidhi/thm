from PIL import Image

print("[!] Note Add extention also.")

pic1_name=input("[-] Enter First Image: " )
pic2_name=input("[-] Enter Second Image: ")
out_name=input("[-] Enter Name of The output image:")


pic1=Image.open(pic1_name)
print("[+] Reading pic1")  #finding the size of picture1 
pic2=Image.open(pic2_name)
print("[+] Reading pic2") #finding the size of picture2

#pic2=pic1.resize(pic1.size) #resizing the pic2 according to pic1
#print("[+] pic2 resized Successfully.")

'''
so that we can xor each and every coordinate of both the pictures
'''

print(pic2) #After Resizing

x_cord_pic1=pic1.size[0]
y_cord_pic1=pic1.size[1]

newpic = Image.new('RGB',pic1.size) # Creating NEW image

for y in range(y_cord_pic1):
    for x in range(x_cord_pic1):
        pixel_1=pic1.getpixel((x,y))
        pixel_2=pic2.getpixel((x,y))
        newpixel =[]
        for p in range(len(pixel_1[:3])): #for all three values

            newpixel.append(pixel_1[p] ^ pixel_2[p]) # ^ --> use to xor two Values
        newpixel=tuple(newpixel)
        #print(newpixel)
        newpic.putpixel((x,y),newpixel)
print("[+] Xored successfully")
print("[+]  Successfully saved as "+out_name)
newpic.save(out_name)

