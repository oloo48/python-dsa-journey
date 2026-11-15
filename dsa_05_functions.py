print("=" * 60)
print("        #️⃣ PART1: BASIC FUNCTIONS ")
print("=" * 60)
print("\n----1. FUNCTION DEFINITION AND CALLING----")
#Defining a function
def greet():
    print("hello there!")
    print("Welcome to the world of functions.")
#Calling a function
print("\nCalling the function greet()")
greet()
print("Function finished!\n")
print("----2.PARAMETERS :GIVE INFORMATION TO A FUNCTION----")
def greet_person(name):
    print(f"Hello, {name}!👋")
    print(f"Nice to meet you, {name}!\n")
    print("Calling with 'Oloo48':")
    greet_person("Oloo48")
    print("Calling with 'Alice':")
    greet_person("Alice")
    #-----------------------------------------------------------------
    # MULTIPLE PARAMETERS: A function can accept multiple parameters separated by commas.
    print("----3. MULTIPLE PARAMETERS----")
    def introduce(name,age,country):
        print(f"Hi,I'm {name}.")
        print(f"I'm {age} years old.")
        print(f"originally from {country}.\n")
        introduce("Oloo48",21,"Kenya")
        introduce("Alice",30,"USA")
        print("----4. RETURNING VALUES FROM FUNCTIONS:SENDING RESULTS BACK----")
        def add(a,b):
            result=a+b
            return result
        sum1=add(5,3)
        print(f"5+3={sum1}")
        sum2=add(100,250)
        print(f"100+250={sum2}")
        # use directly in another expression
        total=add(10,5)*2
        print(f"(10+5)*2={total}")
        print("\n"+"="*60)
        print("          ⚙️ PART2: ADVANCED FUNCTIONS ")
        print("="*60)
        print("\n-----5. Default parameters------:")
        def greet_message(name,message="Hope you're having a great day!"):
            print(f"hello,{name}! {message}")
        greet_message("Oloo48")
        #overriding the default message with own message
        greet_message("Oloo48","Keep coding every day!💪")
        # practical examples
        print("\n-----6. Practical example ------")
        # Example A: Calculate area of a circle with default radius
        import math
        def circle_area(radius):
            """Calculate and return the area of a circle given it's radius."""
            return math.pi*radius**2
        r=5
        area=circle_area(r)
        print(f"Circle radius{r}  Area={area:.2f}")

        def is_even(number):
            """Return true if number is even,False if odd."""
            if number % 2==0:
                return True
            else:
                return False
            nums=[2,3,10,15,8]
            for n in nums:
                status="Even ✅" if is_even(n) else "ODD ❌"
                print(f"  {n}: {status}")
                def count_vowels(text):
                    """"count how many vowels are there in a given string."""
                    vowels="aeiouAEIOU"
                    count=0
                    for letter in text:
                        if letter in vowels:
                         count += 1
                        return count
                    sentence= "Functions make code cleaner and easier to reuse!"
                    v_count= count_vowels(sentence)
                    print(f"\nSentence: {sentence}")
                    print(f"Total vowels:{v_count}")
                    print("\n" + "=" * 60)
                    print("✅ Funtion basics ready")
                    print("= *60")
                    