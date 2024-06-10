# class Article:
#     all = []
#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
#         Article.all.append(self)

#     @property
#     def title (self):
#         return self._title
    
#     @title.setter
#     def title(self, new_title):
#         if hasattr (self, 'title'):
#             AttributeError("Title can't be changed")
#         elif isinstance(new_title,str) and (5<= len(new_title) <=50):
#                 self._title = new_title
#         raise ValueError ("Title must be between 5 and 50 characters")
    
#     @property
#     def author (self):
#         return self._author
    
#     @author.setter
#     def author (self, new_author):
#         if isinstance (new_author,Author):
#             self._author = new_author
#         else:
#             TypeError ("Author must be an instance of type Author")
    
#     @property
#     def magazine (self):
#         return self._magazine
    
#     @magazine.setter
#     def magazine (self, new_magazine):
#         if isinstance (new_magazine, Magazine):
#             self._magazine = new_magazine
#         else:
#             TypeError ("Magazine must be an instance of type Magazine")
        
# class Author:
#     pass
#     def __init__(self, name):
#         self._name = name
#         self._articles = []

#     @property
#     def name (self):
#         return self._name
    
#     @name.setter
#     def name (self, new_name):
#         if hasattr(self, 'name'):
#             raise AttributeError("Name can't be changed")
#         elif not isinstance(new_name,str) or len(new_name) ==0:
#             raise ValueError ("Name must be longer than 0 characters")
#         self._name = new_name

#     def articles(self):
#         pass
#         return [article for article in Article.all if self == article.author]

#     def magazines(self):
#         pass
#         return list ({article.magazine for article in self._articles()})

#     def add_article(self, magazine, title):
#         pass
#         article = Article(self, magazine, title)
#     #     self._articles.append(article)
#     #     magazine.add_article(article)
#         return article

#     def topic_areas(self):
#         pass
#         if list ({magazine.category for magazine in self.magazines()}):
#             return list ({magazine.category for magazine in self.magazines()})
#         return None

# class Magazine:
#     pass

#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     @property
#     def name (self):
#         return self._name
    
#     @name.setter
#     def name (self, name):
#         if not isinstance(name,str) or not (2<= len(name) <=16):
#             raise ValueError ("Name must be a string")
#         self._name = name

#     @property
#     def category (self):
#         return self._category
    
#     @category.setter
#     def category (self, category):
#         if not isinstance(category,str) or not len(category) ==0:
#             raise ValueError ("Category must be longer than 0 characters")
#         self._category = category

#     def articles(self):
#         pass
#         return [article for article in Article.all if self == article.magazine]

#     def contributors(self):
#         pass
#         return list ({article.author for article in self._articles()})

#     def article_titles(self):
#         pass
#         article_titles = [magazine.title for magazine in self.articles()]
#         if article_titles:
#             return article_titles
#         else:
#             return None

#     def contributing_authors(self):
#         authors = {}
#         list_of_authors = []
#         for article in self.articles():
#             if article.author in authors:
#                 authors[article.author] += 1
#             else:
#                 authors[article.author] = 1  
        
#         for author in authors:
#             if authors[author] >= 2:
#                 list_of_authors.append(author) 
                  
#         if (list_of_authors != []):
#             return list_of_authors
#         else:
#             return None