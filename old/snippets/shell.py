#
#
# $ ./manage.py shell < shell.py
# it is same with drop into the Django shell : $python manage.py shell


# Okay, once we've got a few imports out of the way, let's create a couple of code snippets to work with.
import io
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, SnippetModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#
snippet = Snippet(code='foo = "bar"\n')
snippet.save()
#
snippet = Snippet(code='print("hello, world")\n')
snippet.save()


# We've now got a few snippet instances to play with. Let's take a look at serializing one of those instances.
serializer = SnippetSerializer(snippet)
print(serializer.data)
# output should be like :
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

# At this point we've translated the model instance into Python native datatypes.
# To finalize the serialization process we render the data into json.
content = JSONRenderer().render(serializer.data)
print(content)
# output should be like :
# b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'


# Deserialization is similar. First we parse a stream into Python native datatypes...
#
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
#
# then we restore those native datatypes into a fully populated object instance:
serializer = SnippetSerializer(data=data)
print(serializer.is_valid())
# output should be like :
# True
print(serializer.validated_data)
# output should be like :
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>


# We can also serialize querysets instead of model instances. To do so we simply add a many=True flag to the serializer arguments.
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
print(serializer.data)
# output should be like :
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]


from snippets.serializers import SnippetSerializer
serializer = SnippetModelSerializer()
print(repr(serializer))
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = 
# im not sure but it seems like mean of the repr is 'representation'