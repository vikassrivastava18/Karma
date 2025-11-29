from rest_framework import serializers

from .models import DailyKarma

class DailyKarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyKarma
        fields = '__all__'

    def get_review_display(self, obj):
        return obj.get_review_display()