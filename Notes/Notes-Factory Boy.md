Using Factory Boy and Faker with Django

## factory.py

import factory
from django.contrib.auth.models import User
from factory.faker import faker

FAKE = faker.Faker		## Uses faker directly


class PostFactory(factory.django.DjangoModelFactory);
		class Meta:
			model = Post		## model you want to produce syn data for
			
		title = factory.Faker("sentence", nb_words=12)
		subtitle = factory.Faker("sentence", nb_words=12)
		slug = factory.Faker("slug")
		author = User.objects.get_or_create(username="admin")[0]
		
		@factory.lazy_attribute
		def content(self):
			x = ""
			for _ in range(0,5):
				x += "\n" + FAKE.paragraph(nb_sentences=30) = "\n"
			return x
		
		status = "published"


## end of Configuration

-- python3 manage.py shell
-- from <projectname>.<appname>.import PostFactory		## PostFactory is the class name of the factory.py class you want to use to produce data
-- x = PostFactory.create_batch(100)								## create_batch dictates how many items to create.


** Special Notes **
-- Look into Lazy Loading (Infinite Scrolling) data onto a page (like 10 to 20ish per load) that way you limit the load on server/page.
