def send_sms(to_number, body, account_sid, auth_token, from_number='+12762779105'):
    from twilio.rest import Client

    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        to=to_number,
        from_=from_number,  # Twilio phone number
        body=body
    )
    return 'Message sent!'