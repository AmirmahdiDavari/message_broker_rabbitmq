from send import send_message

queue = input(" queue name  : ")
while True:
    message = input(" message text : ")
    if message == 'siruse':
        break
    if queue:
        send_message(message, queue)
    else:
        send_message(message)
