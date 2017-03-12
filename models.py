#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    number = models.IntegerField(default=0)
    english_name = models.CharField(max_length=200)
    spanish_name = models.CharField(max_length=200)


class Language(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    code2 = models.CharField(max_length=2, null=True, unique=True)
    english_name = models.CharField(max_length=45)
    french_name = models.CharField(max_length=45, null=True)
    spanish_name = models.CharField(max_length=45, null=True)


class Country(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=45)
    internet_domain = models.CharField(max_length=3, null=True)
    phone_prefix = models.PositiveSmallIntegerField(null=True)
    language1 = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='country')
    language2 = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, related_name='country2')


class State(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default='usa')
    name = models.CharField(max_length=45)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, default="eng")
    zip_from = models.CharField(max_length=3, null=True)
    zip_to = models.CharField(max_length=3, null=True)
    

class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default='usa')
    state = models.ForeignKey(State, on_delete=models.PROTECT, default='ca')
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=45, null=True)
    zip_code = models.CharField(max_length=8, null=True)
    geox = models.FloatField(null=True)
    geoy = models.FloatField(null=True)


class Person(models.Model):
    CHURCH_ROLE_GUEST = "GU"
    CHURCH_ROLE_MEMBER = "ME"
    CHURCH_ROLE_PASTOR = "PA"
    CHURCH_ROLE_ELDER = "EL"
    CHURCH_ROLE_DEACON = "DE"
    CHURCH_ROLE_CHOICES = (
	(CHURCH_ROLE_GUEST, "Guest"),
	(CHURCH_ROLE_MEMBER, "Member"),
        (CHURCH_ROLE_PASTOR, "Pastor"),
        (CHURCH_ROLE_ELDER, "Elder"),
        (CHURCH_ROLE_DEACON, "Deacon")
    )

    RIGHTS_NONE = "N"
    RIGHTS_USER = "U"
    RIGHTS_ADMIN = "A"
    RIGHTS_CHOICES = (
	(RIGHTS_NONE, "None"),
	(RIGHTS_USER, "User"),
	(RIGHTS_ADMIN, "Admin")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45)
    website = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default='usa')
    state = models.ForeignKey(State, on_delete=models.PROTECT, default='ca')
    church = models.ForeignKey("Church", on_delete=models.SET_NULL, null=True, related_name='member')
    church_role = models.CharField(max_length=2, choices=CHURCH_ROLE_CHOICES, default=CHURCH_ROLE_GUEST)
    subscriptions = models.ManyToManyField("Church", through='Subscription')
    password_hash = models.CharField(max_length=255)
    rights = models.CharField(max_length=1, choices=RIGHTS_CHOICES, default=RIGHTS_USER)
    last_login = models.DateTimeField(null=True) 
    can_login = models.BooleanField(default=True)


class Church(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default='usa')
    state = models.ForeignKey(State, on_delete=models.PROTECT, default='ca')
    conference = models.ForeignKey("Church", on_delete=models.SET_NULL, null=True, related_name='conference_member')
    union = models.ForeignKey("Church", on_delete=models.SET_NULL, null=True, related_name='union_member')
    division = models.ForeignKey("Church", on_delete=models.SET_NULL, null=True, related_name='division_member')
    members = models.PositiveSmallIntegerField(null=True)
    contact1 = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='contact1_church')
    contact2 = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='contact2_church')
    contact3 = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='contact3_church')
    phone = models.CharField(max_length=45, null=True)
    fax = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null=True)
    website = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    language1 = models.ForeignKey(Language, on_delete=models.PROTECT, default="eng", related_name='church')
    language2 = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, related_name='church2')


class Resource(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=4096, null=True)
    url = models.CharField(max_length=255)
    date_posted = models.DateField()
    church = models.ForeignKey(Church, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, default="eng")


class Event(models.Model):
    EVENT_WORSHIP = "WO"
    EVENT_SABBATHSCHOOL = "SS"
    EVENT_SERMON = "SE"
    EVENT_POTLUCK = "PO"
    EVENT_RETREAT = "RE"
    EVENT_CONFERENCE = "CO"
    EVENT_OTHER = "OT"
    EVENT_CHOICES = (
	(EVENT_WORSHIP, "Worship"), 
	(EVENT_SABBATHSCHOOL, "Sabbath School"), 
	(EVENT_SERMON, "Sermon"), 
	(EVENT_POTLUCK, "Potluck"), 
	(EVENT_RETREAT, "Retreat"), 
	(EVENT_CONFERENCE, "Conference"), 
	(EVENT_OTHER, "Other") 
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=4096, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True)
    date_from = models.DateTimeField(null=True)
    date_to = models.DateTimeField(null=True)
    contact = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='contact')
    organizer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='organizer')
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=2, choices=EVENT_CHOICES, default=EVENT_WORSHIP)
    language1 = models.ForeignKey(Language, on_delete=models.PROTECT, default="eng", related_name='event1')
    language2 = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, related_name='event2')


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=4096)
    announcer = models.ForeignKey(Person, on_delete=models.CASCADE)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    date_posted = models.DateField()
    language = models.ForeignKey(Language, on_delete=models.PROTECT, default="eng")


class Bulletin(models.Model):
    date = models.DateField()
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    notes = models.TextField(max_length=4096, null=True)
    resources = models.ManyToManyField(Resource)
    events = models.ManyToManyField(Event)
    announcements = models.ManyToManyField(Announcement)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, default="eng")

class Subscription(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    email = models.BooleanField(default=False)
    email_count = models.PositiveIntegerField(default=0)
    sms = models.BooleanField(default=False)
    sms_count = models.PositiveIntegerField(default=0)
    newsletter = models.BooleanField(default=False)
    newsletter_count = models.PositiveIntegerField(default=0)
