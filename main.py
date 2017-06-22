#from the Python file "spy_details" we imported some variables in use
from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime

STATUS_MESSAGES = ['You can always be my Son :B', 'Whole world is working hard.. And i am just having a Beer.. :D ', 'Nothing much to Say.. :(']



#Function to update your Status
def add_status():

    updated_status_message = None
#checking status of cuurent status. If present then show status else print no status.
    if spy.current_status_message != None:

        print '\n\nYour current status message is : %s \n' % (spy.current_status_message)
    else:
        print "\n\n~~~~~~\ Currently you have not uploaded any Status /~~~~~~"
#asking if we want to select an older status
    default = raw_input("\nDo you want to select a Status that you have earlier uploaded (y/n): ")
#if no then asking for asking for new status
    if default.upper() == "N":
        new_status_message = raw_input("What status message would you like to upload on Spychat: ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
#if yes then show list of all status and ask user to select one
    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages:  "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is ~~~~~\ %s /~~~~~' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

#function for adding new friends on spychat and counting no. of friends
def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("\nPlease add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("We would like to know their Age: ")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("What is there Spy Rating: ")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.age<55 and new_friend.rating>= Spy.rating:
        friends.append(new_friend)
        print '~~~~~~~~****Your Friend is Added****~~~~~~~~\n'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)



#User is shown a list of friends.. and asked to select a friend to whom you want send the Message..
def select_a_friend():
    item_number = 0
#Displaying details of all friends with a serial no.
    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose a friend from your friends: ")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#We are using this function to send msg to selected friend using select_a_friend() funtion.
def send_message():
    if (len(friends)>0):

       friend_choice = select_a_friend()
       original_image = raw_input("*What is the name of the image:  ")
       output_path ="Image.jpg"
       text = raw_input("*What secret message do you want to send in that image:  ")
       if len(text)<=100:
           #encoding msg into the image.
           Steganography.encode(original_image, output_path, text)

           new_chat = ChatMessage(text,True)

           friends[friend_choice].chats.append(new_chat)

           print "\n-----***Your secret Message Image is sent to your online Friend***-----\n"
       else:
           print "You cannot send a message bigger than length 100...!! Try Again..!!\n"
           send_message()

    else:
        print "\nPlease add some Friends on Spychat....!!\n\n"
        yes_no = raw_input("So do you want to add Friends..(Y/N): ")
        if (yes_no.upper() == 'Y'):
            add_friend()
        else:
            print "-----@@@@Its totally Your Wish@@@@-----"



def read_message():
    #checking whether friends are added or not..
    if(len(friends)>0):
        sender = select_a_friend()

        output_path = raw_input("What is the name of the file? \n")
        #decoding message from the image
        secret_text = Steganography.decode(output_path)

        new_chat = ChatMessage(secret_text,False)

        friends[sender].chats.append(new_chat)

        print "\n-----***Your secret message has been saved in chat***-----\n\n"

    else:
        print "Buddy you dont even have any friends... Whom the hell do you want to read the message from...!!!\n\n"


def read_chat_history():
    if (len(friends) > 0):
        read_for = select_a_friend()
        if len(friends[read_for].chats)>0:
            print '\n6'

            for chat in friends[read_for].chats:
                if chat.sent_by_me:
                    print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
                else:
                    print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

        else:
            print"\n\n-----***There is no conversation between you and your Friend***-----\n\n"
    else:
        print "Buddy you dont even have any friends... Whom the hell do you want to read the message from...!!!\n\n"


def start_chat(Spy):
    Spy.current_status_message = None

    Spy.name = Spy.salutation + " " + Spy.name

    if Spy.age > 12 and Spy.age < 50:

        print "Authentication complete. Welcome " + Spy.name + " age: " + str(Spy.age) + " and rating of: " + str(Spy.rating) + " You are on board..."

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n \n Please enter your Choice "+ Spy.name+" :"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    print 'You chose to update the status'
                    # calling add_status() function to update status
                    Spy.current_status_message = add_status()#(Spy.current_status_message)

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    #calling add_friends() function to add new friends
                    print 'You have %d friends' % (number_of_friends)

                elif menu_choice == 3:
                    #calling send_message() funtion to send a message
                    send_message()

                elif menu_choice == 4:
                    #calling read_message() function to read a message
                    read_message()

                elif menu_choice == 5:
                    #calling read_chat_history() funtion to read chat history of selected user
                    read_chat_history()

                elif menu_choice == 6:
                    show_menu = False

                else:
                    print "You Entered a wrong Value.. Please Re-enter the choice..!!"
    else:
        print 'Sorry you are not of the correct age to be a spy'


if len(Spy.name)>0:
    print "*****~~~~~Its time to Start working on Spychat~~~~~*****"
    question = "Do you want to continue as "  + Spy.name + " (Y/N): "
    existing = raw_input(question)

    if existing.upper() == "Y":
        start_chat(Spy)
    else:
        Spy.name = ''
        Spy.salutation = ''
        Spy.age = 0
        Spy.rating = 0.0
        Spy.is_online = False

        spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

        if len(Spy.name) > 0:
            Spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

            Spy.age = raw_input("What is your age?")
            Spy.age = int(Spy.age)

            Spy.rating = raw_input("What is your spy rating?")
            Spy.rating = float(Spy.rating)

            Spy.is_online = True

            start_chat(Spy.name, Spy.age, Spy.rating)
        else:
            print 'Please add a valid spy name'

else:
    print "Sorry.. You need to start the application again as you didn't entered any name ...!!"