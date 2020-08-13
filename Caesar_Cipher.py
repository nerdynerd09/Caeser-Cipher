import string,re
arr= []
converted = []
a = list(string.ascii_letters)
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
val = [47,48,49,50,51]

def Intro():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("     Welcome to Caeser Cipher Converter")
    print("         Instagram : hackersarena0")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("""[1] --> Convert to Caeser (from plaintext)\n[2] --> Convert from Caeser (to plaintext)\n""")
    user_choice = int(input("Choose an option: "))


    if user_choice == 1:
        to_Caeser()
    elif user_choice == 2:
        from_Caeser()
    else:
        print("Choose an option between 1 and 2")



def to_Caeser():
    change_to_caeser = input("Words to be converted into Caeser Cipher: ")
    for i in change_to_caeser:
        if i.isdigit():
            arr.append(int(i))
        else:
            arr.append(i)

    for j in arr:
        if str(j).isdigit():
            converted.append(str(j))
        elif regex.search(str(j)):
            converted.append(str(j))
        elif j.isupper():
            index_val = a.index(str(j))
            if index_val in val:
                j_upper = a[a.index(j) - 47]
                converted.append(j_upper.upper())
            else:
                j_upper = a[a.index(j) + 5]
                converted.append(j_upper.upper())
        elif j.islower():
            j_lower = a[a.index(j) + 5]
            converted.append(j_lower.lower())
    for k in converted:
        print(k,end='')

def from_Caeser():
    change_from_caeser = input("Words to be converted into Caeser Cipher: ")
    for i in change_from_caeser:
        if i.isdigit():
            arr.append(int(i))
        else:
            arr.append(i)
    for j in arr:
        if str(j).isdigit():
            converted.append(str(j))
        elif regex.search(str(j)):
            converted.append(str(j))
        else:
            converted.append(a[a.index(j)-5])
    for k in converted:
        print(k,end='')

Intro()

