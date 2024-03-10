from django.db import models
import db_users_app.models as user_models


class Place(models.Model):
    '''
    The table's place 
    '''
    number = models.IntegerField() # Table's number
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number}"


class Booking(models.Model):
    '''
    Model for booking table in restaurant
    '''
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)    # User who booking table
    number = models.ForeignKey(Place, on_delete=models.CASCADE)             # Table's number
    count_of_people = models.IntegerField()                                 # People's number
    booking_data = models.DateTimeField()                                   # Data & time booking table 
    valid_until = models.DateTimeField()                                    # Data & time booking table end

    def __str__(self):
        return f"Користувач: {self.user}, Номер столу:{self.number}, На кількість людей: {self.count_of_people} Заброньовано з: {self.booking_data} ,Діє до: {self.valid_until}"
    

    class Meta:
        unique_together = (('user', 'number', 'count_of_people', 'booking_data', 'valid_until'),)

