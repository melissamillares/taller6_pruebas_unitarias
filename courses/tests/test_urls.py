from django.urls import reverse, resolve
from courses.urls import urlpatterns

class TestUrls:
	#Test para la url detail
	def test_details_url(self):
		#construimos la url a partir de su definicion
		path = reverse('courses:detail', args=[1])
		#ejecutamos la url
		resolver = resolve(path)
		#verificamos que el nombre de la url es el correcto
		assert resolver.url_name == 'detail'
		#verificamos los argumentos que se pasaran a la vista
		assert resolver.kwargs == {'pk': '1'}

	#Test para la url new
	def test_new_url(self):
		#construimos la url a partir de su definicion
		path = reverse('courses:new')
		#ejecutamos la url
		resolver = resolve(path)
		#verificamos que el nombre de la url es el correcto
		assert resolver.url_name == 'new'

	#Test para la url list
	def test_list_url(self):
		#construimos la url a partir de su definicion
		path = reverse('courses:list')
		#ejecutamos la url
		resolver = resolve(path)
		#verificamos que el nombre de la url es el correcto
		assert resolver.url_name == 'list'

	#Test para la url edit
	def test_edit_url(self):
		#construimos la url a partir de su definicion
		path = reverse('courses:edit', args=[1])
		#ejecutamos la url
		resolver = resolve(path)
		#verificamos que el nombre de la url es el correcto
		assert resolver.url_name == 'edit'
		#verificamos los argumentos que se pasaran a la vista
		assert resolver.kwargs == {'pk': '1'}	

	#Test para la url delete
	def test_delete_url(self):
		#construimos la url a partir de su definicion
		path = reverse('courses:delete', args=[1])
		#ejecutamos la url
		resolver = resolve(path)
		#verificamos que el nombre de la url es el correcto
		assert resolver.url_name == 'delete'
		#verificamos los argumentos que se pasaran a la vista
		assert resolver.kwargs == {'pk': '1'}