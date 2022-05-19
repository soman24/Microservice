from mailjet_rest import Client

api_key = '9aa5c72ce9c248d0570aa1e6cabdc9ab'
api_secret = '9bed4b34d09b8e19017768cc8264479e'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')



def create_mail(to=[], subject='', text='', html=''):
    messages = []
    message = {
        'From': {
            'Email': 'khansom@oregonstate.edu',
            'Name': 'Soman Khan'
        },
        'To': to,
        'Subject': subject,
        'TextPart': text,
        'HTMLPart': html,
    }
    messages.append(message)
    data = {
        'Messages': messages
    }
    return data

def send_mail(to=[], subject='', text='', html=''):
    data = create_mail(to, subject, text, html)
    result = mailjet.send.create(data=data)
    return result.json()['Messages'][0]
