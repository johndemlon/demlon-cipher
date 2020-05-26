def a(str):
	str = str + str
	str = str.replace("a","c")
	str = str.replace("b","m")
	str = str.replace("n","p")
	print(str)
def b(str,code):
    code1 = code
    code = code + code + code + code
    str = str + str
    str = str.replace("c","a")
    str = str.replace("m","b")
    str = str.replace("p","n")
    if(str == code):
        print(code1)
    else:
        print("wrong key!")
a(str(input("string to hash ")))
b(str(input("hashed string ")),str(input("key ")))
