from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Permission, User


# Create your models here.

## API Data model

class Contract(models.Model):
    name = models.CharField(max_length=250, default="<name>")
    vendor = models.CharField(max_length=250, default="<vendor>")
    service = models.CharField(max_length=500, default="<service>")
    API = models.CharField(max_length=100, default="<api address>")
    company_logo = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    is_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Node(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default="<name>")
    vendor = models.CharField(max_length=250, default="<vendor>")
    nodeos = models.CharField(max_length=250, default="<nodeos>")
    nodecpu = models.CharField(max_length=250, default="<nodecpu>")
    noderam = models.CharField(max_length=250, default="<noderam>")
    nodenic = models.CharField(max_length=250, default="<nodenic>")
    nodeservices = models.CharField(max_length=250, default="<nodeservices>")
    nodeports = models.CharField(max_length=250, default="<nodeports>")
    API = models.CharField(max_length=100, default="<api address>")
    company_logo = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    is_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class System(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default="<name>")
    vendor = models.CharField(max_length=250, default="<vendor>")
    systemservices = models.CharField(max_length=250, default="<systemservices>")
    systemports = models.CharField(max_length=250, default="<systemports>")
    service = models.CharField(max_length=500, default="<service>")
    API = models.CharField(max_length=100, default="<api address>")
    company_logo = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    contract = models.CharField(max_length=100, default="<contract>")
    is_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Event(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    srcip = models.CharField(max_length=100, default="<srcip>")
    dstip = models.CharField(max_length=100, default="<dstip>")
    srcport = models.CharField(max_length=100, default="<srcport>")
    dstport = models.CharField(max_length=100, default="<dstport>")
    md5hash = models.CharField(max_length=100, default="<md5hash>")
    virustotalscore = models.CharField(max_length=100, default="<virustotalscore>")
    internalthreatscore = models.CharField(max_length=100, default="<internalthreatscore>")
    ctiscore = models.CharField(max_length=100, default="<ctiscore>")
    dnsdisplayname = models.CharField(max_length=100, default="<dnsdisplayname>")
    dnsresolvedname = models.CharField(max_length=100, default="<dnsresolvedname>")
    payload = models.CharField(max_length=100, default="<payload>")
    score = models.CharField(max_length=100, default="<score>")
    link = models.CharField(max_length=100, default="<link>")
    contract = models.CharField(max_length=100, default="<contract>")
    def __str__(self):
#        return self.event_description + ' - ' + self.score
        return self.srcip + ' ' + self.dstip + ' ' + self.srcport + ' ' + self.dstport + ' ' + self.md5hash + ' ' + self.virustotalscore + ' ' + self.internalthreatscore + ' ' + self.ctiscore + ' ' + self.dnsresolvedname + ' ' + self.payload + ' ' + self.link + ' ' + self.contract + ' '

class Spread(models.Model):

    item1 = models.CharField(max_length=100, default = "<item>")
    item2 = models.CharField(max_length=100, default="<item>")
    item3 = models.CharField(max_length=100, default="<item>")
    item4 = models.CharField(max_length=100, default="<item>")
    item5 = models.CharField(max_length=100, default="<item>")
    x = models.CharField(max_length=1, default="")
    # x = models.BooleanField(True, default = False)

    def __str__(self):
#        return self.event_description + ' - ' + self.score
        return self.item1 + ' ' + self.item2 + ' ' + self.item3 + ' ' + self.item4 + ' ' + self.item5


class Case(models.Model):
    dockernumber = models.CharField(max_length=100, default="<docker #>")
    casemanager = models.CharField(max_length=100, default="<docker #>")
    casesupportmanager = models.CharField(max_length=100, default="<docker #>")
    issuedate = models.CharField(max_length=100, default="<docker #>")
    expirationdate = models.CharField(max_length=100, default="<docker #>")
    IMEIs = models.CharField(max_length=100, default="<docker #>")
    phonenumber = models.CharField(max_length=100, default="<docker #>")
    address = models.CharField(max_length=100, default="<docker #>")
    btp = models.BooleanField(default=False)
    br = models.BooleanField(default=False)
    both = models.BooleanField(default=False)