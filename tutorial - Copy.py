import time

# What I can do: A Python tutorial that teaches how to input things on the command line, printing stuff,
# denoting variables, loops. If statements/arrays?

exp = input("Have you ever used Python before? \n")
exptest = False
annoyed = 0

while exptest == False:
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    for ele in exp:
        if ele in punc:
            exp = exp.replace(ele, "")
    exp = str.lower(exp)
    if exp == "yes" or exp == "y":
        print("Doesn't hurt to refresh yourself with the basics. \n")
        exptest = True
    elif exp == "no" or exp == "n":
        print("Well, here's your chance! \n")
        exptest = True
    elif annoyed >= 5:
        exp = print("Ugh, let's just skip to the tutorial. \n")
    elif annoyed >= 3:
        exp = input("Come on, we're wasting each other's time. Just respond with either \"yes\", \"y\", \"no\", or \"n\". \n")
        annoyed += 1
    else:
        exp = input("Sorry, this is a yes or no question. You can say \"yes\", \"y\", \"no\", or \"n\". \n" )
        annoyed+=1

annoyed = 0
time.sleep(2)
print("We'll be covering how to input stuff on the terminal line, how to write print statements, how to declare variables, and write loops. \n")
time.sleep(2)
input("You ready? \n")
print("Great! I can tell you already know how to input things on the terminal line, which is great. \n")
time.sleep(2)
print("Let's move onto writing print statements. \n")
time.sleep(2)
print("The way to write a print statement is to use the \"print()\" command. \n")
time.sleep(2)
print("For example, we can print \"Yes!\" with \"print(\"Yes!\")\". \n")
time.sleep(2)
printed = input("Let's try it out for ourselves! Let's print the famous \"Hello World!\" using the print() command. \n")

printtest = False

while printtest == False:
    if printed == "print(\"Hello World!\")":
        print("Congratulations! You got it! \n")
        printtest = True
    if printed[0:1] == "P":
        printed = input("Whoops, the \"P\" in the \"print\" is supposed to be in lowercase! \n")
        annoyed += 1
    if "(" not in printed and ")" not in printed:
        printed = input("You forgot the parentheses! \n")
        annoyed += 1
    if "(" not in printed:
        printed = input("You got the closing parenthesis, but not the opening one! \n")
        annoyed += 1
    if ")" not in printed:
        printed = input("You got the opening parenthesis, but not the closing one! \n")
        annoyed += 1
    if "\"" not in printed:
        printed = input("Don't forget to surround Hello World! in quotation marks! \n")
        annoyed += 1
    if printed.count("\"") != 2:
        printed = input("Don't forget - you need one quotation mark to open, and another to close! \n")
        annoyed += 1
    elif annoyed % 3 == 0 & annoyed != 0:
        printed = input("Don't forget - you want to print \"Hello World!\". \n")
        annoyed += 1
    else:
        printed = input("Sorry, that's not it. \n")
        annoyed+=1
annoyed = 0
time.sleep(1)

print("Congratulations! You printed your first print statement! \n")
time.sleep(2)
print("Some of you may know how to declare variables in other languages, like Java or C++. \n")
time.sleep(2)
print("You may remember having to do something like \"int x = 5;\". \n")
time.sleep(2)
print("Instead, Python uses something called dynamic typing, where you don't have to declare the type of the variable. So Python will automatically recognize if a variable is an integer, string, or Boolean value, to name a few. \n")
time.sleep(2)
print("For example, I can declare the variable \"num\" with \"num = 123\", \"str\" with \"str = \"Hello World!\"\", and \"lying\" with \"lying = True\". \n")
time.sleep(2)
print("So let's try to declare your own variable! We'll start by trying to declare an integer variable.\n")
time.sleep(2)
intvar = input("So just as I did before, declare an integer variable! \n")

inttest = False
while inttest == False:
    if intvar.count("=") < 1:
        intvar = input("You forgot the equals sign! \n")
    elif intvar.count("=") > 1:
        intvar = input("You have too many equals signs! \n")
    else:
        intvararr = intvar.split('=')
        intvararr[0] = intvararr[0].strip()
        intvararr[1] = intvararr[1].strip()
        if intvararr[0].isidentifier() == False:
            intvar = input("That's not a valid variable name, sorry. Make sure it doesn't start with a number and is not a reserved word in Python. \n")
        elif intvararr[1].isdigit() == False:
            intvar = input("That's not a valid integer! \n")
        else:
            print("Congratulations! You declared an integer variable! \n")
            inttest = True
time.sleep(2)
print("Now let's declare a string variable. \n")
time.sleep(2)
strvar = input("So just as I did before, declare a string variable! \n")
stringtest = False
while stringtest == False:
    if strvar.count("=") < 1:
        strvar = input("You forgot the equals sign! \n")
    elif strvar.count("=") > 1:
        strvar = input("You have too many equals signs! \n")
    else:
        strvararr = strvar.split('=')
        strvararr[0] = strvararr[0].strip()
        strvararr[1] = strvararr[1].strip()
        if strvararr[0].isidentifier() == False:
            strvar = input("That's not a valid variable name, sorry. Make sure it doesn't start with a number and is not a reserved word in Python. \n")
        elif strvararr[1][0] != "\"":
            if strvararr[1][-1] != "\"":
                strvar = input("Keep it consistent - make sure you start and end with a double inverted comma! \n")
            else:
                print("Great job! You declared a string variable! \n")
                stringtest = True
        elif strvararr[1][0] != "\'":
            if strvararr[1][-1] != "\'":
                strvar = input("Keep it consistent - make sure you start and end a single inverted comma! \n")
            else:
                print("Great job! You declared a string variable! \n")
                stringtest = True
        elif strvararr[1][0:2] != "\"\"\"":
            if strvararr[1][-3:-1] != "\"\"\"":
                strvar = input("Keep it consistent - make sure you start and end with three double inverted commas! \n")
            else:
                print("Great job! You declared a string variable! \n")
                stringtest = True
        elif strvararr[1][0:2] != "\'\'\'":
            if strvararr[1][-3:-1] != "\'\'\'":
                strvar = input("Keep it consistent - make sure you start and end with three single inverted commas! \n")
            else:
                print("Great job! You declared a string variable! \n")
                stringtest = True        
        else:
            print("Congratulations! You declared a string variable! \n")
            stringtest = True
time.sleep(2)
print("Last but not least, let's declare a Boolean variable. \n")
time.sleep(2)
boolvar = input("So declare a Boolean variable! \n")
booleantest = False
while booleantest == False:
    if boolvar.count("=") < 1:
        boolvar = input("You forgot the equals sign! \n")
    elif boolvar.count("=") > 1:
        boolvar = input("You have too many equals signs! \n")
    else:
        boolvararr = boolvar.split('=')
        boolvararr[0] = boolvararr[0].strip()
        boolvararr[1] = boolvararr[1].strip()
        if boolvararr[0].isidentifier() == False:
            boolvar = input("That's not a valid variable name, sorry. Make sure it doesn't start with a number and is not a reserved word in Python. \n")
        elif boolvararr[1] != "True" and boolvararr[1] != "False":
            boolvar = input("That's not a valid Boolean! \n")
        else:
            print("Congratulations! You declared a Boolean variable! \n")
            booleantest = True
print("Excellent! You can now declare variables of all sorts of types! \n")
time.sleep(2)
print("Now let's go over how loops work. \n")
time.sleep(2)
print("Loops are a way to repeat a block of code. \n")
time.sleep(2)
print("For example, let's say you want to print \"Hello World!\" five times. \n")
time.sleep(2)
print("You could do it like this: \n")
time.sleep(2)
print("print(\"Hello World!\") \n")
time.sleep(0.5)
print("print(\"Hello World!\") \n")
time.sleep(0.5)
print("print(\"Hello World!\") \n")
time.sleep(0.5)
print("print(\"Hello World!\") \n")
time.sleep(0.5)
print("print(\"Hello World!\") \n")
time.sleep(2)
print("But that's not very efficient. If you wanted to do it 10000 times, it would get time-consuming fast. We need a better way!\n")
time.sleep(2)
print("That's where loops come in! \n")
time.sleep(2)
print("There are two types of loops in Python: for loops and while loops. \n")
time.sleep(2)
print("For loops are used when you know how many times you want to run a block of code. \n")
time.sleep(2)
print("If you wanted to print \"Hello World!\" five times, you already know that you want to print it five times. \n")
time.sleep(2)
print("So you could do it like this: \n")
time.sleep(2)
print("for i in range(5): \n")
time.sleep(0.5)
print("    print(\"Hello World!\") \n")
time.sleep(2)
print("This is much better. Note that because we specify \"range(5)\", Python knows to repeat it exactly five times.\n")
time.sleep(2)
print("There is actually an indentation difference between the two. \n")
time.sleep(2)
print("For loops are indented four spaces, while while loops are indented two spaces. \n")
time.sleep(2)
print("This is because Python uses indentation to tell you what code is inside of what block. \n")
time.sleep(2)
print("Other coding languages use semicolons and curly brackets to tell you what code is inside of what block. You can do that in Python too, it is your choice. \n")
time.sleep(2)
print("But die-hard Python fans will destroy you if they see you use semicolons. \n")
time.sleep(2)
print("Let's make a for loop of our own! \n")
time.sleep(2)

fortest = False
print("I want you to print the phrase \"I bet you can't do this by hand!\" 9012345 times using a for loop. \n")
time.sleep(2)
print("Of course, there are many ways to do this, but I want you to use \"range\", just as I have, with the exact same spacing. \n")
time.sleep(2)
large = input("Let's just print the first line. If you have any doubts, just look at the example that was provided earlier. \n")
while fortest == False:
    if large == "for i in range(9012345)":
        large = input("Whoops, you got everything right, just forgot the colon at the end! \n")
    elif large == "for i in range(9012345):":
        print("That's right! \n")
        fortest = True
    else:
        large = input("Sorry, try again. Refer to the example if you need a refresher. \n")
time.sleep(2)
fortest = False
large = input("Now let's print the second line! Don't worry about indentation - just input the code contents of the line. \n")
while fortest == False:
    if large == "print(\"I bet you can't do this by hand!\")":
        large = input("Whoops, you got everything right, just forgot the colon at the end! \n")
    elif large == "print(\"I bet you can't do this by hand:\")":
        print("That's right! \n")
        fortest = True
    else:
        large = input("Sorry, try again. Refer to the example if you need a refresher. \n")
time.sleep(2)
print("Great! Let's look at while loops. \n")
time.sleep(2)
print("While loops are used when you don't know how many times you want to run a block of code. \n")
time.sleep(2)
print("So a while loop would exit only if a condition is met. You would have to state that condition. \n")
time.sleep(2)
print("In fact, this program is written mostly with while loops, which exit based on what you input! \n")
time.sleep(2)
print("You can also use while loops to do what you just did with the for loops. \n")
time.sleep(2)
print("So if you wanted to print \"Hello World!\" 5 times, you could do it like this: \n")
time.sleep(2)
print("i = 0 \n")
time.sleep(0.5)
print("while i < 5: \n")
time.sleep(0.5)
print("    print(\"Hello World!\") \n")
time.sleep(0.5)
print("    i = i + 1 \n")
time.sleep(2)
print("We still have the indentation, but we have this third line, which we didn't need before. \n")
time.sleep(2)
print("That's because without it, we would have an infinite loop! \n")
time.sleep(2)
print("Notice that we also have a condition in the while loop. \n")
time.sleep(2)
print("This is because we don't want to run the loop if the condition is not met. \n")
time.sleep(2)
print("We also have to declare a variable \"i\" before the while loop, and set it to 0. \n")
time.sleep(2)
print("Theoretically, we could start it at any number we want. But for simplicity, we start at 0 and end at 5. \n")
time.sleep(2)
print("So let's try to replicate what we had before, but with a while loop. \n")
time.sleep(2)
whiletest = False
print("I want you to print the phrase \"I bet you can't do this by hand!\" 9012345 times using a while loop, similar to the example. Use i as your incrementor variable. \n")
time.sleep(2)
large = input("Let's just print the first line. If you have any doubts, just look at the example that was provided earlier. \n")
while whiletest == False:
    nospace = large.replace(" ", "")
    if nospace == "i=0":
        large = input("Whoops, you got everything right, just forgot the colon at the end! \n")
    elif nospace == "i=0:":
        print("That's right! \n")
        whiletest = True
    else:
        large = input("Sorry, try again. Don't forget that this is the line that declares the incrementor variable. \n")
time.sleep(2)
whiletest = False
large = input("Now let's print the second line! This is the line that actually contains the word \"while\". Again, for the second through fourth lines, no need to indent. \n")
while whiletest == False:
    if large == "while i < 9012345":
        large = input("Whoops, you got everything right, just forgot the colon at the end! \n")
    elif large == "while i < 9012345:":
        print("That's right! \n")
        whiletest = True
    else:
        large = input("Sorry, try again. Remember that you want to repeat it 9012345 times! Refer to the example if you need a refresher. \n")
time.sleep(2)
whiletest = False
large = input("Let's print the third line. This is the line that prints the statement. \n")
while whiletest == False:
    large = large.strip()
    if large == "print(\"I bet you can't do this by hand!\")":
        large = input("Whoops, you got everything right, just forgot the colon at the end! \n")
    elif large == "print(\"I bet you can't do this by hand:\")":
        print("That's right! \n")
        whiletest = True
    else:
        large = input("Sorry, try again. Refer to the example if you need a refresher. \n")
time.sleep(2)
whiletest = False
large = input("Amazing! Now all we have is the last line, the line that increments the incrementor variable.")
while whiletest == False:
    nospace = large.replace(" ", "")
    if nospace == "i=i+1" or nospace == "i+=1":
        large = input("Whoops, you got everything right, just forgot the colon at the end! \n")
    elif nospace == "i=i+1:" or nospace == "i+=1:":
        print("That's right! \n")
        whiletest = True
    else:
        large = input("Sorry, try again. Don't forget that we want to increment the incrementor variable. \n")
time.sleep(2)
print("Congratulations! You made it through the basic tutorial!")
time.sleep(2)
print("You can now consider yourself a Python Apprentice.")