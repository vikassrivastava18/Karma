
from datetime import timedelta, timezone
from django.utils import timezone

from daily.models import *

def add_parayer_karma(date):
    karma = Karma(
        title  = "Daily Puja",
        karma = "<p><b>Mandatory</b> after bath.<br> Do with <b>bhava</b></p>",
        # daily = True,
        type = KarmaType.PRAYER,
        review = KarmaReview.PENDING,
        date = date
    )
    karma.save()

def add_study_karma(date):
    karma = Karma(
        title = "Daily Study",
        karma = "<p>Study for 2 hour.<br>Go <b>Deep</b></p>",
        # daily = True,
        type = KarmaType.STUDY,
        review = KarmaReview.PENDING,
        date = date
    )
    karma.save()

def add_work_karma(date):
    karma = Karma(
        title = "Daily Work",
        karma = "<p>Work with passion, sincerity. <br><b>Daily</b> </p>",
        # daily = True,
        type = KarmaType.WORK,
        review = KarmaReview.PENDING,
        date = date
    )
    karma.save()

def add_family_karma(date):
    karma = Karma(
        title = "Family Time",
        karma = "<p>Spend time with family.<br>Do with <b>love</b></p>",
        # daily = True,
        type = KarmaType.FAMILY,
        review = KarmaReview.PENDING,
        date = date
    )
    karma.save()

def add_play_karma(date):
    karma = Karma(
        title = "Play Time",
        karma = "<p>Play with friends/chess<br>Do with <b>focus</b></p>",
        # daily = True,
        type = KarmaType.PLAY,
        review = KarmaReview.PENDING,
        date = date
    )
    karma.save()

def add_public_karma(date):
    karma = Karma(
        title = "Public Life",
        karma = "<p><b>Interaction</b> and relationships.<br> Do with <b>love</b></p>",
        # daily = True,
        type = KarmaType.PUBLIC,
        review = KarmaReview.PENDING,
        date = date
    )
    karma.save()

def next_day_date(d):
    # Get the next date from now
    return timezone.now().date() + timedelta(days=d)

def add_data(days):
    for i in range(days):
        _date = next_day_date(i)
        add_parayer_karma(_date)
        add_public_karma(_date)
        add_play_karma(_date)
        add_family_karma(_date)
        add_work_karma(_date)
        add_study_karma(_date)


if __name__ == '__main__':
    add_data(100)

