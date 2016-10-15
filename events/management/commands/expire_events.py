from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):

    help = 'Expires event objects which are out-of-date'

    def handle_noargs(self):
        print (Event.objects.filter(date__lt=datetime.datetime.now()).delete())
