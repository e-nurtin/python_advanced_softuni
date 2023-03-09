from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
	def __init__(self):
		self.categories = []
		self.topics = []
		self.documents = []
	
	def add_category(self, category: Category):
		if category not in self.categories:
			self.categories.append(category)
	
	def add_topic(self, topic: Topic):
		if topic not in self.topics:
			self.topics.append(topic)
	
	def add_document(self, document: Document):
		if document not in self.documents:
			self.documents.append(document)
	
	def edit_category(self, category_id: int, new_name: str):
		[category.edit(new_name) for category in self.categories if category.id == category_id]
	
	def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
		[topic.edit(new_topic, new_storage_folder) for topic in self.topics if topic_id == topic.id]
	
	def edit_document(self, document_id: int, new_file_name: str):
		[doc.edit(new_file_name) for doc in self.documents if document_id == doc.id]
	
	def delete_category(self, category_id: int):
		[self.categories.remove(category) for category in self.categories if category_id == category.id]
	
	def delete_topic(self, topic_id: int):
		[self.topics.remove(topic) for topic in self.topics if topic_id == topic.id]
	
	def delete_document(self, document_id: int):
		[self.documents.remove(doc) for doc in self.documents if doc.id == document_id]
		
	def get_document(self, document_id: int):
		return [doc for doc in self.documents if doc.id == document_id][0]
	
	def __repr__(self):
		return '\n'.join([repr(doc) for doc in self.documents])
	
	