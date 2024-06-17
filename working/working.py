import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define the regular expression pattern to match the input formats
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$'
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid input format")

    # Extract components from the matched groups
    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_meridiem = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_meridiem = match.group(6)

    # Validate the times
    if not (0 <= start_hour <= 12) or not (0 <= end_hour <= 12):
        raise ValueError("Invalid hour in input")
    if not (0 <= start_minute <= 59) or not (0 <= end_minute <= 59):
        raise ValueError("Invalid minute in input")

    # Convert to 24-hour format
    if start_meridiem == "AM":
        if start_hour == 12:
            start_hour = 0  # Midnight edge case
    elif start_meridiem == "PM":
        if start_hour != 12:
            start_hour += 12

    if end_meridiem == "AM":
        if end_hour == 12:
            end_hour = 0  # Midnight edge case
    elif end_meridiem == "PM":
        if end_hour != 12:
            end_hour += 12

    # Format the output in 24-hour format
    start_time = f"{start_hour:02}:{start_minute:02}"
    end_time = f"{end_hour:02}:{end_minute:02}"

    return f"{start_time} to {end_time}"


if __name__ == "__main__":
    main()

