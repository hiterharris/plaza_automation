from datetime import datetime

def isAvailable():
    day = datetime.now().strftime('%A')
    hour = datetime.now().hour
    ampm = datetime.now().strftime("%I:%M %p")[-2:]

    if (day == 'Saturday' or 'Sunday') and (hour <= 8 or hour >= 11):
        availability = False
    else:
        availability = True

    print("isAvailable, availability: ", availability)
    return availability
