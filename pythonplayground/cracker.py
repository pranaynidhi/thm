hash="dxeedxebdwemdwesdxdtdweqdxefdxefdxdudueqduerdvdtdvdu"

def text_to_int_array(string_txt):
	arr=[]
	i=0
	while(i<len(string_txt)):
		temp=ord(string_txt[i])
		temp=temp-97
		arr.append(temp)
		print(arr[i])
		print(i)
		i+=1
	print(arr)
	print("\n")
	return arr

def int_array_to_string(my_array):
	i=0
	my_string=""
	while(i<len(my_array)):
		temp=int(my_array[i]*26)
		i+=1
		temp+=int(my_array[i])
		my_string+=chr(temp)
		i+=1

	return my_string

print(int_array_to_string(text_to_int_array(int_array_to_string(text_to_int_array(hash)))))
