import os
from twilio.rest import Client

APP_DIR = os.path.dirname(__file__)

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

if not account_sid or not auth_token or not TWILIO_PHONE_NUMBER:
    raise Exception("Missing Environmental variables for TWILIO authentication.")
client = Client(account_sid, auth_token)


def get_phone_list(file_path=os.path.join(APP_DIR, 'phone_list.txt')):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Please provide a valid path: {} is not found.".format(file_path))

    # TODO: Add phone number validation
    phone_list = []
    for line in open(file_path, 'r'):
        print(line)
        phone_list.append(line.replace('\n', '').strip())
    return phone_list


def main():
    phone_numbers = get_phone_list()
    for phone_number in phone_numbers:
        try:
            message = client.messages \
                            .create(body="Friendly reminder to practice your memory madness verse. You can do it!",
                                    from_=TWILIO_PHONE_NUMBER,
                                    to=phone_number
                                   )
            print(message.sid)
        except Exception as e:
            print("Phone number {} generated this error".format(phone_number))
            print(e)


if __name__ == '__main__':
    main()
