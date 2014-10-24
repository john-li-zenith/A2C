from apps.models import App, AppUpdate
from plans.validators import ModelCountValidator


class MaxAppsValidator(ModelCountValidator):
    code = 'MAX_APP_COUNT'
    model = App

    def get_queryset(self, user):
        return super(MaxAppsValidator, self).get_queryset(user).filter(user=user)

max_apps_validator = MaxAppsValidator()

class MaxAppUpdatesValidator(ModelCountValidator):
    code = 'MAX_APPUPDATE_COUNT'
    model = AppUpdate

    def get_queryset(self, user):
        return super(MaxAppUpdatesValidator, self).get_queryset(user).filter(user=user)

max_appupdates_validator = MaxAppUpdatesValidator()