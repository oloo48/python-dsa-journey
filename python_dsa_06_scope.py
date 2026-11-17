print("=" *60)
print("     🌍PART 1:GLOBAL VS LOCAL VARIABLES")
print("=" *60)
print("n\ ---1.  GLOBAL VARIABLES---")
school_name ="Nakuru Institute of technology"
def print_school():
    print(f"school: {school_name}")
    print_school()
    print(f"Outside Too: {school_name}")
    print("✅Global Variables work everywhere!\n")
    print("---2. Local Variables---")
    def my_function():
        student_name="Oloo48"
        print(f"Inside function:Hello {student_name}")
        my_function()
        print("❌ Student_name only exists inside my_function _outside,it's gone!\n")
        print("---3.WHEN NAMES CONFLICT;LOCAL WINS!---")
        message="I am a Global"
        def show_message():
            message="I am a local"
            print(f"Inside function: {message}")
            show_message()
            print(f"outside function: {message}")
            print(f"✅ Python uses closest Variable.Thus local variable wins in this case\n ")
            #--------------------------------------------------------------------------------
            print("----4. Changing A global__Use 'global' keyword----")
            score=0
            def update_score():
                global score
                score +=10
                print(f"inside score now:{score}")
                print("⚠️ Tip:Avoid global variables when you can use return values instead!\n")
                print("----5. ✅Best practice: Return The Value")
                total=0
                def add_points(current_total,points):
                    new_total=current_total+points
                    return new_total
                total= add_points(total,10)
                print(f"After +10: {total}")
                total=add_points(total,25) 
                print(f"After +25: {total}")
                print("This is how professiuonal code works! \n")

                print("----6. Nested Functions----")
                def outer():
                    outer_message="I'm from the outer function"

                    def inner():
                        print(f"Inner sees:{outer_message}")
                        inner()
                        outer()
                        print("✅Inner functions can see variables from their outer funtions too!\n")
                        print("=" *60)
                        print("scope Basics Mastered!")
                        print("=" *60)
