from interestAPI import app
from interestAPI import selenium_handler
from datetime import datetime

def read_from_file():
    with open("DATA_FILE.txt", 'r') as file:
        for line in file.readlines():
            if line.startswith("INTEREST"):
                cur_interest = line.split('=')[1].strip().strip("'")
            elif line.startswith("NEXT_DATE"):
                next_date = line.split('=')[1].strip().strip("'")
    return {"Interest": cur_interest, 
            "NextDate": next_date}

def refresh_data():
    # Retrieving Data from Bank Of Israel 
    DATA = interest = selenium_handler.get_interest()
    INTEREST = DATA["Interest"]
    NEXT_DATE =DATA["Next Decision Date"]

    # Writing To File
    with open("DATA_FILE.txt", 'w') as file:
        # Write the variable values to the file
        file.write(f"INTEREST={INTEREST}\n")
        file.write(f"NEXT_DATE={NEXT_DATE}\n")

def validate_data(next_date):
    next_date = next_date
    date_format = "%d/%m/%Y"
    # Convert the given date string to a datetime object
    given_date = datetime.strptime(next_date, date_format)
    # Get the current date
    current_date = datetime.now()
    # Compare the dates
    if given_date.date() > current_date.date():
        print(f"Data is still valid, next decision date is {next_date}.")
        return True
    elif given_date.date() < current_date.date():
        print("Data if out of date.")
        return False
    else:
        print("Data if out of date.")
        return False



@app.route('/api/interest/', methods=['GET'])
def interest():
    data = read_from_file()
    next_date = data["NextDate"]
    
    if validate_data(next_date) == False:
        refresh_data()
        data = read_from_file()
    
    cur_interest = data["Interest"]
    next_date = data["NextDate"]

    return {"Interest": cur_interest,
            "NextDate": next_date}