import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "Trial Pack expiring",
        message = "Your Trial Period for Amazon Prime seems to be expiring in 5days. Considering to purchase?",
        app_icon = "C:\\Users\\Vivek hotti\\desktop\\Notifier\\icon.ico",
        timeout = 10
    )