from plyer import notification

def notify(title, message, icon):
    notification.notify(
        title = title,
        message = message,
        app_icon= icon,



        timeout = 15,
        app_name='PostureApp'

    )