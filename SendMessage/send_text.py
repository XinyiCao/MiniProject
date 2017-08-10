from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC204564083e7d51aa06cd89ad43113e62"
# Your Auth Token from twilio.com/console
auth_token  = "5d07c80331d1e1261fdcceacbd6866bc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "+14703381649",        # Replace with your phone number
    from_ = "+12192096776",         # Replace with your Twilio number
    body = "Hi Cordia, HeLLo from Python!")

print(message.sid)