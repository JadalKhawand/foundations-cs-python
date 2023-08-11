from datetime import date


def getDate():
    today = str(
        date.today()
    )  # https://www.geeksforgeeks.org/get-current-date-using-python/
    today = today.replace("-", "")
    return today  # in the form YYYYMMDD


data = []

with open("ListTickets.txt", "r") as file:  # stackoverflow
    for line in file:
        data.append(
            line.strip().split(", ")
        )  # strips any whitespaces and split when seeing a comma
        # output: [['tick102', 'ev002', 'gio', '20230803', '2'],...]


# MERGE SORT wrt 2 indices at the same time
def mergeSort2(data, index1, index2):  # https://youtu.be/cVZMah9kEjI
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        # recursion
        mergeSort2(left_half, index1, index2)
        mergeSort2(right_half, index1, index2)
        # merge:
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if (
                left_half[i][index1] < right_half[j][index1]
            ):  # check if the element at index1 of the ith element of left side less than the right
                data[k] = left_half[i]
                i += 1
            elif (
                left_half[i][index1] == right_half[j][index1]
                and left_half[i][index2] < right_half[j][index2]
                # compares the index1 values of the i-th element in left_half and the
                # j-th element in right_half. If the index1 values are equal, it further compares
                # the index2 values to determine which element should come before the other in the merged data list.
            ):
                # if true the i-th element of left_half should be placed in the k-th position of the data list since
                # it is smaller in terms of both index1 and index2 values.
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(
            left_half
        ):  # copies the remaining element if there's any in the left half
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(
            right_half
        ):  # copies the remaining element if there's any in the right half
            data[k] = right_half[j]
            j += 1
            k += 1

    return data


# MERGE SORT for wrt 1 index
def mergeSort1(data, index):  # https://youtu.be/cVZMah9kEjI
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        # recursion
        mergeSort1(left_half, index)
        mergeSort1(right_half, index)
        # merge:
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][index] < right_half[j][index]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(
            left_half
        ):  # copies the remaining element if there's any in the left half
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(
            right_half
        ):  # copies the remaining element if there's any in the right half
            data[k] = right_half[j]
            j += 1
            k += 1

    return data


def login():
    username = input("Username: ")  # asks for username and password
    password = input("Password: ")
    if username == "admin":  # checks if the username is admin
        for i in range(4):
            if password == "admin123123":  # checks if the passwrod is admin123123
                break  # if it is it breaks out of the loop

            else:
                print("Incorrect Password please try again")
                print(
                    str(4 - i), "attempts left."
                )  # if the pass is wrong it prints how many attempts left
                username = input("Username: ")
                password = input("Password: ")  # then asks again for name and pass

        else:
            print(
                "Incorrect Username and/or Password, 0 attempts left"
            )  # if the user used the 5 attempts
            # it prints this
    else:
        print("\n")  # else means that the username is anything other than admin
        # we dont care about the password

    return username, password


def adminMenu():  # admin menu
    print(
        "\n1. Display Statistics\n"
        + "2. Book a Ticket\n"
        + "3. Display all Tickets\n"
        + "4. Change Ticket"
        + "'"
        + "s Priority\n"
        + "5. Disable Ticket\n"
        + "6. Run Events\n"
        + "7. Exit\n"
    )


def userMenu():  # user menu
    print("\n1. Book a Ticket\n" + "2. Exit\n")


def getAdminChoice():  # get the choice from the admin
    while True:
        choice = int(input("Please enter your choice here: "))
        if choice < 1 or choice > 7:  # choice can't be less than 1 or greater than 7
            print("Invalid input. Please enter a number between 1 and 7.")
        else:
            return choice


def getUserChoice():  # get the choice from the user
    while True:
        choice = int(input("Please enter your choice here: "))
        if choice < 1 or choice > 2:
            print("Invalid input. Please enter 1 or 2.")
        else:
            return choice


def displaystat():
    event_ids = [
        ticket[1] for ticket in data
    ]  # https://stackoverflow.com/questions/71115079/best-way-to-get-second-item-of-each-list-inside-of-a-2d-list
    # initialize max ticket count and event id to store the event id inside it
    max_ticket = 0
    event_id = ""  # to keep track of the max ticket and the corresponding id
    for i in event_ids:  # looping over all the events id
        count = event_ids.count(i)  # it counts the number of occurances of the event
        if count > max_ticket:  # if it's greater than the max ticket
            max_ticket = count  # it updates the max ticket with the new count
            event_id = i  # it assigns the current event id to the event id
    print("The event ID with the highest number of tickets is", event_id)


# it will only show the event with the max tickets of the first event in the data


def bookTicket(username, event, date, priority):
    if data:  # if data isnt empty:
        last_tick_num = int(
            data[-1][0].replace("tick", "")
        )  # replace tick by nothing and then
    # we take the value of the number next to tick and make it an integer
    else:  # data is empty and it starts from 0
        last_tick_num = 0

    new_tick = last_tick_num + 1  # we add 1 so it's now auto incremented
    new_ticket = [
        "tick" + str(new_tick),
        event,
        username,
        date,
        priority,
    ]  # then we put the new ticket
    # as a sublist
    data.append(new_ticket)  # add the sublist to the data
    with open("ListTickets.txt", "a") as file:
        line = ", ".join(
            str(item) for item in new_ticket
        )  # converts the new_ticket list into a single string
        # by joining its elements with a comma and space separator.
        file.write(line + "\n")  # finally we add it to the text file


def displayTickets():
    sorted_data = mergeSort2(data, 1, 3)  # sort data according to ev ids and date
    for ticket in sorted_data:
        if ticket[3] >= getDate():  # we check so we only print the newest dates
            print(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4])


def changePriority(ticket_id):
    index = -1
    for i in range(len(data)):
        if data[i][0] == ticket_id:  # we search for the ticket id in the data
            index = i
            break  # if its found we assing it to the index and then break out of the loop
    if index == -1:  # if it's still -1 so we couldn't find the ticket
        print("The ticket was not found.")
    else:
        new_priority = input("Please enter the new priority: ")
        data[index][4] = new_priority  # we change the ticket priority
        print("Ticket priority has been succefully changed")


def disableTicket(ticket_id):
    index = -1
    for i in range(len(data)):
        if data[i][0] == ticket_id:  # same as the last fn
            index = i
            break
    if index == -1:
        print("The ticket was not found.")
    else:
        del data[  #
            index
        ]  # https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
        print("Ticket has been succefully disabled.")


def runEvents():
    index = -1
    new_data = []
    event_dates = [tickets[3] for tickets in data]  # all the dates in the data
    # we get both the index i and the value of the date using enumerate function
    for i, date in enumerate(
        event_dates
    ):  # https://pythonbasics.org/enumerate/ get both the index i and the corresponding date from the list event_dates
        if date == getDate():  # we check if it matches the date of today
            index = i  # we assign it to the index
            new_data.append(data[index])  # we add it to the new list

    if index == -1:
        print("No tickets for Today's date.")
    else:
        new_data = mergeSort1(
            new_data, -1
        )  # sort the new data according to the priority
        del data[index]  # delete the data that have today's date
        for ticket in new_data:
            print(
                ticket[0], ticket[1], ticket[2], ticket[3], ticket[4]
            )  # print the new data for todays date


def bookUserTicket(name, event, date):
    if data:
        last_tick_num = int(data[-1][0].replace("tick", ""))
    else:
        last_tick_num = 0

    new_tick = last_tick_num + 1
    new_ticket = [
        "tick" + str(new_tick),
        event,
        name,
        date,
        "0",
    ]  # the same as the admin's but we set priority to 0
    data.append(new_ticket)
    with open("ListTickets.txt", "a") as file:
        line = ", ".join(
            str(item) for item in new_ticket
        )  # converts the new_ticket list into a single string
        # by joining its elements with a comma and space separator.
        file.write(line + "\n")  # write the line in the txt file and add a new line


def main():
    print(
        "HELLO and WElCOME aboard! Your one-stop destination for seamless ticketing and extraordinary experiences! \n"
        + "Kindly enter your username and password:"
    )
    user, password = login()
    while True:
        if user == "admin" and password == "admin123123":
            adminMenu()
            choice = getAdminChoice()
            if choice == 1:
                displaystat()
            elif choice == 2:
                date = ""
                print("Kindly enter these information to book a ticket:")
                username = input("Enter the username: ")
                event = input("Enter the event ID: ")
                while date < getDate():
                    date = input("Enter the date of the event (YYYYMMDD): ")
                    if date < getDate():
                        print("Enter today's date or after")
                priority = input("Enter the priority: ")
                bookTicket(username, event, date, priority)
            elif choice == 3:
                displayTickets()
            elif choice == 4:
                ticket_id = input("Please enter the ticket id [tickXX]: ")
                changePriority(ticket_id)
            elif choice == 5:
                ticket_id = input("Please enter the ticket id [tickXX]: ")
                disableTicket(ticket_id)
            elif choice == 6:
                runEvents()
            elif choice == 7:
                save = input(
                    "Do you want to save the changes? 'y' for yes, 'n' for no: "
                )
                print("Exiting...")
                break
        else:
            userMenu()
            choice = getUserChoice()
            if choice == 1:
                date = ""
                name = user
                event = input("Enter the event ID: ")
                while date < getDate():
                    date = input("Enter the date of the event (YYYYMMDD): ")
                    if date < getDate():
                        print("Enter today's date or after")
                bookUserTicket(name, event, date)
                print("The ticket has been succesfully booked!")
            elif choice == 2:
                print("Thank you for using my program!!")
                break


main()
