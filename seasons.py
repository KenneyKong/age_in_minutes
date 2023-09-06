from datetime import date, datetime
import sys

def main():
    user_input = input("Date of Birth: ")
    
    try:
        birth_date = datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)
    
    today = date.today()
    
    age_in_minutes = calculate_age_in_minutes(birth_date, today)
    age_in_words = convert_minutes_to_words(age_in_minutes)
    
    print(f"{age_in_words} minutes")

def calculate_age_in_minutes(birth_date, today):
    age = today - birth_date
    age_in_minutes = age.days * 24 * 60  # 24 hours per day, 60 minutes per hour
    return age_in_minutes

def convert_minutes_to_words(minutes):
    # Use the inflect library to convert minutes to English words
    try:
        import inflect
        p = inflect.engine()
        age_in_words = p.number_to_words(minutes, andword="")
        return age_in_words.replace(",", "")  # Remove commas from large numbers
    except ImportError:
        print("Install the 'inflect' library to display age in words.")
        sys.exit(1)

if __name__ == "__main__":
    main()
