#imports and global variables
import time
import random
morals = 0
loop = 0
quotemark = raw_input("please enter the game code provided by the developer for testing purposes: ")
globname = raw_input("NAME: ")
html_escape_table = {
   "&": "&amp;",
   '"': "&quot;",
   "'": "&apos;",
   ">": "&gt;",
   "<": "&lt;",
}
#intro and redirect to name verification
def intro():
    global morals
    print "..."
    time.sleep(3)
    print "..."
    time.sleep(3)
    print "..."
    time.sleep(3)
    print "---THE---LIBRARY---"
    time.sleep(2)
    print "---BY---BRYNDAN---EIGL---"
    time.sleep(2)
    print "---ARTISTIC---ASSISTANCE---"
    time.sleep(2)
    print "---BY---NATASSJA---EIGL---"
    time.sleep(2)
    print "This game is a prototype and is not complete."
    time.sleep(1.5)
    print "please only use numerical digits, and lowercase type when neccesary."
    time.sleep(3)
    name = raw_input("NAME: ")
    if name.lower() == "bryn":
        print "you are the creator, and thus you automatically win!"
        end_credits()
    if name.lower() == "CANE HIM":
        print "There is no way i would challenge you!"
        print "you automatically win"
        end_credits()
    if name.lower() == "cane him":
        print "There is no way i would challenge you!"
        print "you automatically win"
        end_credits()
    else:
        print name + (". IS THAT YOUR NAME? (y/n)")
        name_verification()
#verifies name + takes you to part 1
def name_verification():
    global morals
    answer1 = raw_input("USER INPUT: ")
    if answer1 == "y":
        time.sleep(1)
        print "OH... THAT'S UNFORTUNATE."
        time.sleep(1)
        part1()
    if answer1 == "n":
        intro()
    else:
        intro()
#part one start menu
def part1():
    global morals
    print "PART ONE"
    start = raw_input("PLEASE TYPE start: ")
    if start == "start":
        library1()
    else:
        print "CAN'T EVEN SPELL PROPERLY, DEPRESSING."
        morals = morals - 1
        part1()
#lobby and decision on which branch user wants
def library1():
    global morals
    print "Welcome to the library."
    print "Hello! I am Bucket, I'll be helping with your orientation!"
    time.sleep(1)
    print "Before we begin, I have some tasks to complete."
    print "Please feel free to roam around and familiarize yourself with the area!"
    time.sleep(1)
    print "I shall notify you once I am prepared."
    print "Thank you, and once again, welcome to The Library."
    time.sleep(1)
    time.sleep(3)
    print "This library has 3 branches, to my left we have the books, and to my right we have the commons... The third branch is off limits at the moment."
    time.sleep(2)
    print "TYPE 1 FOR THE FIRST BRANCH, AND 2 FOR THE SECOND BRANCH, OR DO WHATEVER, YOU'RE THE BOSS AND I'M JUST A NARRATOR."
    branch_selection = raw_input("AWAITING INPUT: ")
    if branch_selection == "1":
        books_branch()
    if branch_selection == "2":
        commons_branch()
    if branch_selection == "3":
        time.sleep(0.5)
        print "IT IS OFF LIMITS. WHAT, ARE YOU ILLITERATE?"
    else:
        print "YOUR CHOICE WAS NOT RECOGNIZED, SORRY. YOU WILL NOW BE REDIRECTED TO THE LIBRARY LOBBY."
        morals = morals - 1
        time.sleep(1.5)
        library1()
#books branch redirects to lobby ATM
def books_branch():
    global morals
    time.sleep(1)
    print "Hi there!"
    time.sleep(3)
    print "Heeeellllooooo!!!"
    time.sleep(3)
    print "Yooooohooooo!!"
    time.sleep(2)
    print "AN OLD LIBRARIAN FACES YOU AND TRIES TO GAIN YOUR ATTENTION."
    print "YOU ATTEMPT TO AVOID EYE CONTACT BY SCANNING THE ROOM FOR MORE DETAILS."
    time.sleep(1.5)
    print "BOOKS LITTER THE ROOM NOT ONLY ON SHELVES, BUT ALSO ON THE FLOOR."
    time.sleep(1)
    print "AN OLD SIGN SAYS <Always remember: books are BAD, but CANE HIM is worse>;"
    time.sleep(1)
    print "what are you doing here?"
    print "THE OLD LIBRARIAN SEEMS INNOCENT, BUT INQUISETIVE."
    print "1. 'just browsing for books' 2. 'im trying to find CANE HIM' 3. RETURN TO LIBRARY LOBBY."
    books_doing = raw_input("WAITING: ")
    if books_doing == "1":
        print "well, okay..."
        morals = morals + 1
        time.sleep(1)
        books_browsing()
    if books_doing == "2":
        print "shhhhh!"
        print "w",
        time.sleep(0.5),
        print "e",
        time.sleep(0.5),
        print " ",
        time.sleep(0.5),
        print "d",
        time.sleep(0.5),
        print "o",
        time.sleep(0.5),
        print "n",
        time.sleep(0.5),
        print "t",
        time.sleep(0.5),
        print " ",
        time.sleep(0.5),
        print "s",
        time.sleep(0.5),
        print "p",
        time.sleep(0.5),
        print "e",
        time.sleep(0.5),
        print "a",
        time.sleep(0.5),
        print "k",
        time.sleep(0.5),
        print " ",
        time.sleep(0.5),
        print "o",
        time.sleep(0.5),
        print "f",
        time.sleep(0.5),
        print " ",
        time.sleep(0.5),
        print "h",
        time.sleep(0.5),
        print "i",
        time.sleep(0.5),
        print "m",
        time.sleep(0.5),
        print ".",
        time.sleep(0.5),
        print ".",
        time.sleep(0.5),
        print ".",
        time.sleep(0.5)
        morals = morals - 1
        books_browsing()
    else:
        library1()
#commons branch has three options --> 1. talk to person number one 2. talk to person number two 3. go back to lobby
def commons_branch():
    global morals
    time.sleep(1)
    print "Welcome to the commons " + globname + "."
    time.sleep(1)
    print "I am the HOST of the commons branch."
    print "The commons branch is for all users to interact."
    time.sleep(2)
    print "There are currently 2 people in the commons branch."
    print "Type 1 to speak to the first, 2 to speak to the second, and type 3 to return to the library lobby."
    talkto = raw_input("TYPE YOUR DECISION HERE: ")
    if talkto == "3":
        print "YOU WILL NOW BE REDIRECTED TO THE LIBRARY LOBBY."
        time.sleep(1.5)
        library1()
    if talkto == "2":
        print "YOU APROACH AN ATTRACTIVE WOMAN WHO YOU RECOGNIZE, BUT CAN NOT EXACTLY PLACE THE IDENTITY OF."
        print "SHE LOOKS UPSET"
        second_person1()
    if talkto == "1":
        print "YOU APROACH A YOUNG FIGURE WEARING A HOOD."
        first_person1()
    else:
        print "YOU WILL NOW BE REDIRECTED TO THE COMMONS BRANCH"
        commons_branch()
#talking to the first person currently just redirects to the commons branch.
def first_person1():
    global morals
    print "Woah didn't see you there!"
    time.sleep(1)
    print "THE HOODED FIGURE CONCEALS AN OBJECT INTO HIS POCKET AND TURNS TO FACE YOU."
    print "You need to get out, you are not supposed to be here."
    time.sleep(2.5)
    print "1: Ok ok, sorry. *RETURN TO COMMONS* 2: You dont even know me!"
    choice_person1 = raw_input("WAITING FOR NUMBER:")
    if choice_person1 == "1":
        print "RETURNING TO COMMONS BRANCH..."
        time.sleep(3)
        commons_branch()
    if choice_person1 == "2":
        print "... Ummm Okay..."
        time.sleep(2)
        print "Well... if you really want to talk..."
        time.sleep(1)
        print "Here is a coin, if it hits heads, then we talk... tails than you go back to the commons branch. Ok?"
        coin_flip = random.choice(["heads", "tails"])
        if coin_flip == "heads":
            print "IT HIT HEADS."
            morals = morals + 1
            time.sleep(3)
            first_person2()
        if coin_flip == "tails":
            print "IT HIT TAILS"
            morals = morals - 1
            time.sleep(3)
            print "YOU WILL NOW BE REDIRECTED TO THE COMMONS BRANCH"
            time.sleep(2)
            commons_branch()
#second person to talk to
def first_person2():
    global morals
    time.sleep(2)
    print "ummmm... I didn't think that you would get this far."
    print "THE YOUNG MAN LOOKS "
    print "A",
    time.sleep(0.5),
    print "N",
    time.sleep(0.5),
    print "G",
    time.sleep(0.5),
    print "E",
    time.sleep(0.5),
    print "R",
    time.sleep(0.5),
    print "E",
    time.sleep(0.5),
    print "Y",
    time.sleep(1)
    print "who are you? some sort of library inspector or something?"
    print "YES OR NO. (y/n)"
    inspector_answer = raw_input('INPUT: ')
    time.sleep(2)
    if inspector_answer == "y":
        morals = morals - 1
        insans_yes()
    if inspector_answer == "n":
        morals = morals + 1
        insans_no()
    else:
        first_person2()
#second person also just goes back to the commons branch.
def second_person1():
    global morals
    print "i know who you are and i want you to leave"
    print " "
    print " "
    print " "
    print "g",
    time.sleep(0.5),
    print "e",
    time.sleep(0.5),
    print "t",
    time.sleep(0.5),
    print " ",
    time.sleep(0.5),
    print "o",
    time.sleep(0.5),
    print "u",
    time.sleep(0.5),
    print "t",
    time.sleep(0.5),
    print " ",
    time.sleep(0.5),
    print "n",
    time.sleep(0.5),
    print "o",
    time.sleep(0.5),
    print "w",
    time.sleep(0.5),
    print ".",
    time.sleep(1.5)
    morals = morals - 1
    print "YOU WILL NOW BE REDIRECTED TO THE COMMONS BRANCH."
    commons_branch()
#they answer no to are you the library inspector
def insans_no():
    global morals
    time.sleep(2)
    print "well then... lEAvE mE aLOnE!"
    time.sleep(1)
    print "THE MAN PUSHES YOU AWAY FROM HIM AND THEN CLOSES A DOOR"
    print "YOU COULD SWEAR THAT THAT DOOR WASNT THERE WHEN YOU CAME INTO THE AREA..."
    door1()
#they answer yes to are you the library inspector
def insans_yes():
    global morals
    time.sleep(2)
    print "DESPITE BEING SUCH A HORRIBLE, HORRIBLE LIAR, THE MAN BELIEVES YOU!"
    time.sleep(2)
    print "..."
    time.sleep(1)
    print "SORRY TO BREAK MY ROLE AS" + quotemark + "THE NEUTRAL NARRATOR," + quotemark
    print "BUT I JUST THOUGHT I WOULD TELL YOU THAT YOU ARE A REALLY BAD LIAR..."
    time.sleep(2)
    print "oh, well then... come with me..."
    morals = morals - 1
    cellar1()
#browsing in books branch
def books_browsing():
    global morals
    print "null"
#cellar, for coming with the young man
def cellar1():
    global morals
    print "null"
    cellar1()
#grassy fiels, answering no to inspector question
def door1():
    global morals
    print "null"
    grassy_field1()
#end credits, infinite loop of end
def end_credits():
    global morals
    print "---A---GAME---BY---"
    print "------BRYNDAN---EIGL------"
    time.sleep(2)
    print "---MAIN---STORY---BY---"
    print "------BRYNDAN---EIGL------"
    time.sleep(2)
    print "---STORY---COLLABORATION---WITH---"
    print "------NATASSJA---EIGL------"
    while 2 == 2:
        print "---END---"
        time.sleep(0.1)
#starts the game
intro()
