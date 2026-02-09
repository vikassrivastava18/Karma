from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from daily.models import *

def add_parayer_karma(date, user):
    karma = DailyKarma(
        title  = "Daily Puja",
        karma = "<p><b>Mandatory</b> after bath.<br> Do with <b>bhava</b></p>",
        # daily = True,
        type = DailyKarmaType.PRAYER,
        review = DailyKarmaReview.PENDING,
        date = date,
        user=user
    )
    karma.save()

def add_study_karma(date, user):
    karma = DailyKarma(
        title = "Daily Study",
        karma = "<p>Study for 2 hour.<br>Go <b>Deep</b></p>",
        # daily = True,
        type = DailyKarmaType.STUDY,
        review = DailyKarmaReview.PENDING,
        date = date,
        user=user
    )
    karma.save()

def add_work_karma(date, user):
    karma = DailyKarma(
        title = "Daily Work",
        karma = "<p>Work with passion, sincerity. <br><b>Daily</b> </p>",
        # daily = True,
        type = DailyKarmaType.WORK,
        review = DailyKarmaReview.PENDING,
        date = date,
        user=user
    )
    karma.save()

def add_family_karma(date, user):
    karma = DailyKarma(
        title = "Family Time",
        karma = "<p>Spend time with family.<br>Do with <b>love</b></p>",
        # daily = True,
        type = DailyKarmaType.FAMILY,
        review = DailyKarmaReview.PENDING,
        date = date,
        user=user
    )
    karma.save()

def add_play_karma(date, user):
    karma = DailyKarma(
        title = "Play Time",
        karma = "<p>Play with friends/chess<br>Do with <b>focus</b></p>",
        # daily = True,
        type = DailyKarmaType.PLAY,
        review = DailyKarmaReview.PENDING,
        date = date,
        user=user
    )
    karma.save()

def add_public_karma(date, user):
    karma = DailyKarma(
        title = "Public Life",
        karma = "<p><b>Interaction</b> and relationships.<br> Do with <b>love</b></p>",
        # daily = True,
        type = DailyKarmaType.PUBLIC,
        review = DailyKarmaReview.PENDING,
        date = date,
        user=user
    )
    karma.save()

def next_day_date(d):
    # Get the next date from now
    return timezone.now().date() + timedelta(days=d)

def add_data(days):
    user = User.objects.get(username='vikas')
    for i in range(days):
        _date = next_day_date(i)
        add_parayer_karma(_date, user)
        add_public_karma(_date, user)
        add_play_karma(_date, user)
        add_family_karma(_date, user)
        add_work_karma(_date, user)
        add_study_karma(_date, user)


if __name__ == '__main__':
    add_data(100)

