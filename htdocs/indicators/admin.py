from django.contrib import admin
from indicators.models import IndicatorType,Sector,ActivityData,PeriodType,Program,Indicator,TargetsAndActuals,DissaggregationType

admin.site.register(IndicatorType)
admin.site.register(Sector)
admin.site.register(DissaggregationType)
admin.site.register(TargetsAndActuals)
admin.site.register(ActivityData)
admin.site.register(PeriodType)
admin.site.register(Program)
admin.site.register(Indicator)
