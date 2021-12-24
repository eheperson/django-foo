
# Working with Serializers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# -----------------------------------------------------------------------------------------------------------------------
#  let's create a couple of code snippets to work with.
#
snippet = Snippet(code='foo = "bar"\n')
snippet.save()
snippet = Snippet(code='print("hello, world")\n')
snippet.save()
#
# -----------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------
# We've now got a few snippet instances to play with. 
# Let's take a look at serializing one of those instances.
#
serializer = SnippetSerializer(snippet)
print(serializer.data)
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
#
#At this point we've translated the model instance into Python native datatypes. 
# To finalize the serialization process we render the data into json.
content = JSONRenderer().render(serializer.data)
print(content)
# b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'
#
# -----------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------
# Deserialization is similar. 
# First we parse a stream into Python native datatypes...
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
#
# then we restore those native datatypes into a fully populated object instance.
serializer = SnippetSerializer(data=data)
print(serializer.is_valid())
# True
print(serializer.validated_data)
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>
#
# We can also serialize querysets instead of model instances. 
# To do so we simply add a 'many=True' flag to the serializer arguments.
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
print(serializer.data)
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
#
# -----------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------
# playing with model serializer
#
from snippets.serializers import SnippetModelSerializer
serializer = SnippetModelSerializer()
print(repr(serializer))
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...
#
# -----------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------
# testing via httpie
#
# $ http http://127.0.0.1:8000/snippets/
# $ http http://127.0.0.1:8000/snippets/2/
#
# -----------------------------------------------------------------------------------------------------------------------