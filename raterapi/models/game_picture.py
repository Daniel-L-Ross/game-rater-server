from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.models import User


class GamePicture(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=DO_NOTHING, related_name='pictures')
    action_pic = models.ImageField(
        upload_to='actionimages', height_field=None,
        width_field=None, max_length=None, null=True)