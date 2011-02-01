from lettuce.django import django_url

def path_to(page_name):
    return django_url(
        {
          'the history page': '/history',
          'the projects page': '/projects',
        }[page_name])

