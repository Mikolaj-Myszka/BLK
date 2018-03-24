import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'blk.settings')

import django
django.setup()
from teams.models import TeamClassic

i = 0
import csv
with open('TEAM-TEAM-CLASSIC-PERGAME.txt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        """
        p = TeamClassic.objects.get_or_create(
            team=row['Team']
            )[0]
        print(p)
        """

        i = i + 1
        print(i, row['Team'])

        ## https://amittbhardwj.wordpress.com/2015/10/15/django-queryset-update_or_create/
        
        # In this case, if the TeamClassic already exists, its name is updated
        p = TeamClassic.objects.update_or_create(
            team=row['Team'],
            defaults={
                'gp': row['GP'],
                'two_fgm': row['2FGM'],
                'two_fgms': row['2FGMS'],
                'two_prtg': row['2P%'],

                'three_fgm': row['3FGM'],
                'three_fgms': row['3FGMS'],
                'three_prtg': row['3P%'],

                'ftm': row['FTM'],
                'ftms': row['FTMS'],
                'ft_prtg': row['FT%'],

                'off_reb': row['OR'],
                'def_reb': row['DR'],
                'tot_reb': row['TR'],

                'ast': row['AST'],
                'stl': row['STL'],
                'blk': row['BLK'],
                'to': row['TO'],
                'fls': row['FLS'],
                
                'mi': row['MIN'],
                'pts': row['PTS'],
                }
            )
        print(p)

        
        #f = TeamClassic.objects.get(team=row['Team'])
        #print(f)

        #obj = TeamClassic.objects.get(team=row['Team'])

        """
        try:
            obj1 = TeamClassic.objects.get(team=row['Team'])
            print(obj1)
        except TeamClassic.DoesNotExist:
            obj = TeamClassic(team=row['Team'])
            #print(obj)
            obj.save()
        """
        


        """
        if f:
            print(f)
        """
        

        # was before
        #p = TeamClassic(team=row['Team'], gp=row['GP'])
        #p.save()



#https://stackoverflow.com/questions/14115318/create-django-model-or-update-if-exists/26286864#26286864
"""
# In this case, if the Person already exists, its name is updated
person, created = Person.objects.update_or_create(
        identifier=identifier, defaults={"name": name}
)

[('No', 'TOT'), ('Team', 'WRO'), ('GP', '4'), ('', ''), ('2FGM', '23.25'), ('2FGMS', '22.5'), ('2P%', '50.82'), ('3FGM', '5.25'),
('3FGMS', '11.5'), ('3P%', '31.34'), ('FTM', '13.5'), ('FTMS', '7.5'), ('FT%', '64.29'), ('OR', '10.25'), ('DR', '23.75'),
('TR', '34.0'), ('AST', '17.25'), ('STL', '6.5'), ('BLK', '1.75'), ('TO', '12.25'), ('FLS', '22.5'), ('SEC', '12000.0'),
('MIN', '200.0'), ('PTS', '75.75'), ('GS', '0'), ('TmREB', '8.25'), ('TmTO', '0.5'), ('TmFLS', '0.0')])
"""
















### taken from Tango with Django
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/"} ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
         "url":"http://flask.pocoo.org"} ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages} }

    # If you want to add more catergories or pages
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.


    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))



def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()




class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name



class Page(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.title
"""




