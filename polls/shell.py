#
#
from polls.models import Choice, Question  # Import the model classes we just wrote.

questions = Question.objects.all()
print(questions) # No questions are in the system yet.

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q.save()

# Now it has an ID.
print(q.id)

# Access model field values via Python attributes.
print(q.question_text)

print(q.pub_date)

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database.
questions = Question.objects.all()
print(questions)








# Make sure our __str__() addition worked.
print(Question.objects.all())

# Django provides a rich database lookup API that's entirely driven by keyword arguments.
print(Question.objects.filter(id=1))
print(Question.objects.filter(question_text__startswith='What'))

# Get the question that was published this year.
current_year = timezone.now().year
print(Question.objects.get(pub_date__year=current_year))

# Request an ID that doesn't exist, this will raise an exception.
print(Question.objects.get(id=13))
#        Traceback (most recent call last):
#            ...
#        DoesNotExist: Question matching query does not exist.


# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
print(Question.objects.get(pk=1))

# Make sure our custom method worked.
q = Question.objects.get(pk=1)
print(q.was_published_recently())

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
print(q.choice_set.all())

# Create three choices.
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
print(c.question)

# And vice versa: Question objects get access to Choice objects.
q.choice_set.all()
print(q.choice_set.count())

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
print(Choice.objects.filter(question__pub_date__year=current_year))

# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()