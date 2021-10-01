try:
    raw_input_data = input("Kérlek adj meg egy időintervallumot másodpercekben")
    sum_of_second = int(raw_input_data)
    if sum_of_second < 0:
        print("Invalid input")
    elif sum_of_second == 0:
        print("now")
    else:
        second_in_minute = 60
        second_in_hour = 60 * second_in_minute # 3600
        second_in_day = 24 * second_in_hour # 86 400
        second_in_year = 356 * second_in_day # 31 536 000
        
        years = sum_of_second // second_in_year
        sum_of_second = sum_of_second - years * second_in_year
        
        days = sum_of_second // second_in_day
        sum_of_second = sum_of_second - days * second_in_day
        
        hours = sum_of_second // second_in_hour
        sum_of_second = sum_of_second - hours * second_in_hour
        
        minutes = sum_of_second // second_in_minute
        seconds = sum_of_second - minutes * second_in_minute
        
        number_of_units = 0
        if years > 0:
            number_of_units += 1
        if days > 0:
            number_of_units +=1
        if hours > 0:
            number_of_units +=1
        if minutes > 0:
            number_of_units +=1
        if seconds > 0:
            number_of_units +=1
        output = ""
        if years > 0:
            output += str(years) + " year"
            if year > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and"
            number_of_units -= 1
            
        output = ""
        if days > 0:
            output += str(days) + " day"
            if day > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and"
            number_of_units -= 1
            
        output = ""
        if hours > 0:
            output += str(hours) + " hour"
            if hour > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and"
            number_of_units -= 1   
        
        output = ""
        if minutes > 0:
            output += str(minutes) + " minute"
            if minutes > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and"
            number_of_units -= 1
            
        output = ""
        if seconds > 0:
            output += str(seconds) + " second"
            if seconds > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and"
            number_of_units -= 1
        print(output)
except ValueError:
    print("Invalid input")
    