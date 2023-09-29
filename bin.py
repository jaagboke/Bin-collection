from datetime import datetime
from twilio.rest import Client

def send_notification():
    try:
        # Twilio credentials
        twilio_account_sid = "AC1a0d427679ca26e64a343bdeb2dc3b33"
        twilio_auth_token = "1a735816a0e44980a489298ae8edccf0"
        twilio_phone_number = "+447449883569"
        recipient_phone_number = "+447404908838"

        # Initialize twilio client
        client = Client(twilio_account_sid, twilio_auth_token)

        # Determine the current date
        current_date = datetime.now().date()

        # Define bin collection schedules
        black_bin_schedule = ["2023-09-29", "2023-10-05", "2023-10-12", "2023-10-19", "2023-10-26", "2023-11-02"]
        brown_bin_schedule = ["2023-09-29", "2023-10-12", "2023-10-26", "2023-11-09", "2023-11-23", "2023-12-07"]
        blue_bin_schedule = ["2023-10-05", "2023-10-19", "2023-11-02", "2023-11-16", "2023-11-30", "2023-12-14"]

        # Initialize a message string
        message = "Today, the following bins are collected: "

        # Check which bins need to be collected today and add them to the message
        if current_date.isoformat() in black_bin_schedule:
            message += "Black Bin, "

        if current_date.isoformat() in brown_bin_schedule:
            message += "Brown Bin, "

        if current_date.isoformat() in blue_bin_schedule:
            message += "Blue Bin, "

        # Remove the trailing comma and space
        message = message.rstrip(", ")

        # Send SMS
        if message != "Today, the following bins are collected: ":
            client.messages.create(
                to=recipient_phone_number,
                from_=twilio_phone_number,
                body=message
            )
            print(f"Notification sent: {message}")
        else:
            print("No bin collection today.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    send_notification()
