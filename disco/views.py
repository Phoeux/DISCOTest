from datetime import timedelta

from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now

from core import settings


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
        model.objects.filter(pk__in=pks).delete()
    return did_work