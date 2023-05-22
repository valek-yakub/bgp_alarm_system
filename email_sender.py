#!/usr/bin/env python
import smtplib

"""
    NAME
        email_sender
        
    DESCRIPTION
        The script receives data and send ones to specified recipients.
   
   :import smtplib: uses as smtp client
   
    
"""


def notification_sender(notification_msg: str, recipients_list: list,
                        smtp_server_settings: dict, sender_email="BGP_ALARM_SYSTEM"):
    """Send the notification message to the recipients from the list of recipients"""
    server = smtplib.SMTP(smtp_server_settings["server_ip"], smtp_server_settings["port"])
    try:
        for recipient in recipients_list:
            server.sendmail(sender_email, recipient, notification_msg)
    except Exception as e:
        print(e)

    finally:
        server.quit()


def main():
    # notification_sender()
    pass


if __name__ == "__main__":
    main()
