from datetime import datetime, timedelta

def today_calculation():
    today = str(datetime.now().date())
    today = today.split("-")
    for i, item in enumerate(today):
        today[i] = int(today[i])
    return today

def age_calculation(day):
    today = today_calculation()
    age = today[0] - day[0]
    if(today[1]<day[1]):
        return age-1
    elif (today[1] == day[1]):
        if(today[2]<day[2]):
            return age-1
    return age

def ctrl_age(day):
    today = today_calculation()
    if(today[0]>day[0]):
        age = age_calculation(day)
        return age
    elif(today == day):
        print("Happy Bithday!!!")
        return 0

def birthday_calculation(day):
    return datetime.now() - day

Input = datetime(2006, 12, 8)
input = [2006, 122, 8]
print(f"Hai {age_calculation(input)} anni\n")
print(f"il tuo prossimo compleanno sarà fra: {birthday_calculation(Input)}") 