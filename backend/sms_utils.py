from twilio.rest import Client

# --- Twilio Config ---
TWILIO_SID = "USd74d3ab8f40e686a6a55813da93d3584"
TWILIO_AUTH = "AC3193a9187b53c7b58716e5c848696a17:e487db6481163283c50893afac464f3f"
TWILIO_PHONE = "+16067555896"    # Twilio trial number
ALERT_PHONE = "+918409323793"   # Your verified number

client_sms = Client(TWILIO_SID, TWILIO_AUTH)

def send_alert_sms(message: str):
    """Send SMS alert using Twilio"""
    try:
        client_sms.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=ALERT_PHONE
        )
        print("[SMS SENT]", message)
    except Exception as e:
        print("[SMS FAILED]", e)
