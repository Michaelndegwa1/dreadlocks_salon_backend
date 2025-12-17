from .models import Notification
from .tasks import send_email_notification_task

class NotificationService:
    def send_notification(self, user, title, message, email=False):
        # Create in-app notification
        Notification.objects.create(user=user, title=title, message=message)
        
        if email and user.email:
            send_email_notification_task.delay(
                subject=title,
                message=message,
                recipient_list=[user.email]
            )
