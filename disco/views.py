from datetime import timedelta, datetime

from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now

from core import settings
from disco.models import Track, Playlist, PlaylistVersion, TrackComment


def empty_trash(self, last_run, interval):
    cutoff = now() - timedelta(days=settings.TRASH_DAYS)
    models = (
        Track, Playlist, PlaylistVersion, TrackComment,
    )
    did_work = False
    for model in models:
        pks = model.objects\
            .filter(deleted__isnull=False)\
            .filter(hard_deleted__isnull=True)\
            .filter(deleted__lt=cutoff)\
            .values_list('pk',flat=True)[:settings.TRASH_BATCH_SIZE]
        did_work |= (pks.count() > 0)
        date = datetime.now()
        model.objects.filter(pk__in=pks).update(hard_deleted=date)
    return did_work
