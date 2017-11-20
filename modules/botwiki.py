#botwiki.py
import wikipedia
wikipedia.set_lang("pt")
class botWiki(object):

    def __init__(self, a):
        text = a
        
    def page(text):
    	pagina = wikipedia.page(text) 
    	return pagina

    def title(text):
    	title = wikipedia.title(text)
    	return title

    def url(text):
    	url = wikipedia.url(text)
    	return url

    def content(text):
    	content = wikipedia.content(text)

        return self.a + self.b