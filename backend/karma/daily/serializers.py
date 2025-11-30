from rest_framework import serializers

from .models import DailyKarma, Reflection

class DailyKarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyKarma
        fields = '__all__'

    def get_review_display(self, obj):
        return obj.get_review_display()



class ReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflection
        fields = '__all__'