import email
from email import policy

def parse_eml(file_obj):
    msg = email.message_from_binary_file(file_obj, policy=policy.default)

    subject = msg.get('subject', '')
    from_addr = msg.get('from', '')
    to_addr = msg.get('to', '')

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode(errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode(errors='ignore')

    return {
        "subject": subject,
        "from": from_addr,
        "to": to_addr,
        "body": body
    }
