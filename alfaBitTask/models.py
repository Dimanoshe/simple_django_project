from django.db import models


class LeadState(models.Model):
    # pk экземпляров модели
    STATE_NEW = 1  # Новый
    STATE_IN_PROGRESS = 2  # В работе
    STATE_POSTPONED = 3  # Приостановлен
    STATE_DONE = 4  # Завершен
    name = models.CharField(
        verbose_name=u"Название",
        db_index=True,
        max_length=50,
        unique=True,
    )
class Lead(models.Model):
    name = models.CharField(
        verbose_name=u"Имя",
        max_length=255,
        db_index=True,
        default=u"popo",
    )
    state = models.ForeignKey(
        LeadState,
        verbose_name=u"Состояние",
        on_delete=models.PROTECT,
        default=LeadState.STATE_NEW,
    )
    

    @classmethod
    def status_update(self, obj, new_status):
        '''
        Update status object method.
        self: Lead model
        obj: Lead model object
        new_status: New status for object
        '''
        valid_transition = {
            'STATE_NEW': ['STATE_IN_PROGRESS'],
            'STATE_IN_PROGRESS': ['STATE_POSTPONED', 'STATE_DONE'],
            'STATE_POSTPONED': ['STATE_IN_PROGRESS', 'STATE_DONE'],
            'STATE_DONE':[]
        }
        if new_status.name in valid_transition[obj.state.name]:
            obj.state = new_status
            obj.save()
            return True
        else:
            return False
