from smtplib import SMTP
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, email_to, message):
        self.email_sender = #### HERE GOES YOUR EMAIL ####
        self.password =  #### HERE GOES YOUR PASSWORD ####
        self.email_receiver = email_to
        self.message = message
        self.send_mail()

    def send_mail(self):
        with SMTP("smtp.gmail.com") as conexion:
            conexion.starttls()
            conexion.login(user=self.email_sender, password=self.password)
            conexion.sendmail(from_addr=self.email_sender, to_addrs=self.email_receiver,
                              msg=f"Subject:Alerta de rebajas en vuelos!!\n\n{self.message}")


