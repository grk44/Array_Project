def encoder():
	fn = input('Enter file name if in this folder or full path\n.txt file name:')
	file_name = open(fn)

	#fn = "test.txt"
	#file_name = open(fn)
	chars=[]
	for x in file_name:	
		chars.append(x)		

	nums=[]
	for y in chars:
		for q in y:		
			nums.append(ord(q))

	newf = open("unicoded.txt","w")
	newf.close()
	for z in nums:
		f=open("unicoded.txt","a")
		s=str(z)
		f.write(s+'$@$@')
		f.close()
	print("file saved as 'unicoded.txt'")

def decoder():
	fnd = input('Enter file name if in this folder or full path\n.txt file name:')
	file_name_d = open(fnd)
	#file_name_d = open("unicoded.txt")

	chars=""
	nums=[]
	ch=[]
	for x in file_name_d:	
		chars = (chars + x)	
	nums = chars.split("$@$@")
	nums.remove('')
	for y in nums:
		x=int(y)
		ch.append(chr(x))
	
	new_text=""
	for c in ch:
		new_text=(new_text + c)
	
	newf_dec = open("decoded.txt","w")
	newf_dec.write(new_text)
	newf_dec.close()
	print("file saved as 'decoded.txt'")


print("Welcome to this text obfuscation thing\nIt can convert a .txt file into unicode separated by $@$@")
print("It can also turn them back into plain text\n")
selectok=2
while selectok != 1:	
	select=input("1:Convert .txt into unicode mess\n2:Convert unicode mess into plain text\n[option 1 or 2]:")
	if select=="1":
		selectok=1
		encoder()
	elif select=="2":
		selectok=1
		decoder()
	else:
		selectok=2
		print("Try it again")