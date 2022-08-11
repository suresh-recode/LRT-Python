from twilio.rest import Client


def call_by_twilio(user_input: str):
    """
    user_input : ACCOUNT_SID#AUTH_TOKEN#TWIML#TO_NUMBER#FROM_NUMBER
    Example: 112#6556565657687#<Response><Say>Hello, World!</Say></Response>#+14155551212#+15017122661
    :return: call ID
    """
    twilio_account_sid, twilio_auth_token, twiml, to_number, from_number = user_input.split('#')

    client = Client(twilio_account_sid, twilio_auth_token)

    call = client.calls.create(
                            twiml=twiml,
                            to=to_number,
                            from_=from_number
                        )

    return call.sid