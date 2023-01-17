users_id_count    = 1
bookings_id_count = 1

credentials       = {}

users_database    = {}
bookings_database = {}
cars_database     = [

    {"id": "1", "car_brand": "Volvo", "stars": "4.7", "price": "$140/day", "available": True},
    {"id": "2", "car_brand": "Volvo", "stars": "4.5", "price": "$110/day", "available": True},
    {"id": "3", "car_brand": "Benz", "stars": "4.9", "price": "$200/day", "available": True},
    {"id": "4", "car_brand": "Porcshe", "stars": "4.9", "price": "$190/day", "available": True}
]

def login():

    phone_number = input("Please enter your Phone Number: ")
    password     = input("Please a valid Password: ")

    record       = users_database.get(phone_number)

    if not record:
        print("Record Not found, please signup first!")
        display()

    if record["password"] != password:
        print("Wrong Password!")
        login()

    print("Login Successfull!")

    credentials["phone_number"] = phone_number
    credentials["password"] = password
    credentials["logged"] = True

    display()

def signup():

    global users_id_count

    fullname     = input("Please enter your fullname: ")
    phone_number = input("Please enter your phone number: ")
    password     = input("Please enter your password: ")
    confirm      = input("Please re-enter your password: ")

    if password != confirm:
        print("Passwords not matched!")
        signup()

    if not fullname or not phone_number or not password or not confirm:
        print("Invalid data!")
        signup()

    users_database[phone_number] = {"id": users_id_count, "fullname": fullname, "password": password}

    users_id_count += 1

    print("Signup Successfull! Please login to the system.")
    display()

def search():
    
    search_word = input("Please type a car brand: ")
    result      = False

    print("ID\t\tCar Brand\tstars\t\tprice")

    for car in cars_database:
        if car["available"] and car["car_brand"] == search_word:
            print(car["id"]+"\t\t"+car["car_brand"]+"\t\t"+car["stars"]+"\t\t"+car["price"]+"\t\t")
            result = True

    if not result:
        print("No cars found!")
    
    display()

def confirmBooking():

    if not credentials.get("logged"):
        print("Please Login before you confirm!")
        display()
    else:
        car_id     = input("Please enter the ID of the desired car: ")
        start_date = input("Please Enter the start date: ")
        end_date   = input("Please Enter the end date: ")

        record     = {"car_id": car_id, "start_date": start_date, "end_date": end_date}
        checkoutBooking(record)

def checkoutBooking(record):
    
    global bookings_id_count

    payment_menu = "1- Bank Card"
    print(payment_menu)
    option = input("Please Choose the desired payment method: ")

    if int(option) == 1:

        card_number = input("Please Enter Your Visa/master card number: ")

        if not card_number:
            print("Please enter a valid card number!")
            checkoutBooking(record)

        record["payment"]  = True
        record["id"]       = bookings_id_count
        bookings_id_count += 1

        book_record = bookings_database.get(credentials["phone_number"])

        if book_record:
            book_record.append(record)
        else:
            bookings_database[credentials["phone_number"]] = [record]

        print(f'Booking Successfull! Your Booking ID is {record["id"]}')
        display()
    else:
        print("Please choose from the menu!")
        checkoutBooking(record)

def myBookings():

    if not credentials.get("logged"):
        print("Please Login before you confirm!")
        display()

    for booking in bookings_database[credentials["phone_number"]]:
        print(booking)

    display()

def logout():
    return print("You're logged out!")

menu = " 1- Login To System\n 2- Signup To system\n 3- Search for cars\n 4- Confirm Car booking\n 5- MyBookings\n 6- Logout"

func_dict = {

    1: login,
    2: signup,
    3: search,
    4: confirmBooking,
    5: myBookings,
    6: logout
}

def display():

    print("#"*7+ "    Welcome to the Car Rental System    " +  7*"#")
    print(menu)
    option = int(input("Please select an option from the above menu: "))

    if option in range(1, 7):
        func_dict[option]()
    else:
        print("Wrong Selection")
        display()

print(display())
