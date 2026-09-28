text="hello, DSA world!"
print("original :", text)
print("\nFirst character:", text [0])
print("second character:", text [1])
print("last character:", text [-1])
#
# slicing
#
print("\nFirst five characters:", text[:5])
print("From index 7 onwards" , text[7:])
print("charcters 0 to 4" , text[0:5]) 
print("Every second character" ,text[::2])
print("Reversed:", text[::-1])
#
#immutability
#
print("\n----- IMMUTABILITY -----")
new_text="H" + text[1:]
print("fixed version:", new_text)
# -----------
#useful methods
print("\n -------STRING METHODS -----")
s = " python dsa is aweome! "
print("original: [",s, " ]" )
print(".strip(): [", s.strip(), "]")
print(".upper(): [", s.upper(), "]")
print(".lower(): [", s.lower(), "]")
print(".title(): [", s.title(), "]")
print("length:", len(s))
print("'.find('dsa'):", s.find("dsa"))
print("'.count('s'):", s.count("s"))
print("starts 'Py'?",s.startswith("Py"))
print("ends 'me'?",s.strip().endswith("me"))
print("\n----- SPLIT & JOIN -----")
sentence= "I love learning DSA"
words = sentence.split()
print("split into list:", words)
print("first word:", words[0])
print("last word:", words[-1])
print("split():", words)
joined = "-".join(words)
print("join():", joined)
csv_data="oloo48,20,Kenya,Python"
parts=csv_data.split(",")
print("split csv by comma:", parts)
print("Username:", parts[0])
print("Age:", parts[1])
print("Country:", parts[2])
print("Language:", parts[3])
print("\n----- PALINDROME CHECK -----")
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))
test_words = ["racecar", "Python", "madam", "hello", "abba",]
for word in test_words:
    if is_palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")