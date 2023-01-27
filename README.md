## mbtracklist

Seems we're all on a similar quest, by some intersections of space, time, music, etc. - Or maybe just me, hehe..

- mbtracklist - is my final portfolio project for the nucamp devops/python/backend online bookcamp certificate I'd begun persuing winter'22.

and is yet another simple music playlist manager clone in Python/Django, or in this case I would rather call it a "tracklists keeper" app with tracks seeded from MusicBrainz DB, so hence the "mbtrack" part of the project name.

mbtracklist consist of following app modules - Track & Tracklist and utilizes various features of the djangorestframework (via rest_framework)

Of various ways to handled the 3 SQL relations model via Django/ORM, I'd chosen to manage the many-to-many relations table between Tracks & Tracklists separately bypassing some other routes available to the ORM.
