from imdb import IMDb
ia = IMDb()

class User:
    def __init__(self, name):
        self.name = name
        self.content = []
    def add_content(self, content):
        self.content.append(content)
    def add_content_list(self, content_list):
        for content in content_list:
            self.add_content(content)

# Example User
sam = User('Sam')
sam.add_content_list(['The West Wing', 'Arrested Development', 'True Blood', 'Game of Thrones', 'Dr Who'])

def cross_check(content, user):
    # returns list of intercepts for all User.content and content
    # [ToDo] address duplicates
    people = []
    for x in user.content:
        print('checking ' + x)
        i = intercepts(x, content)
        people = people + i
    return people

def intercepts(a,b):
    # returns a list of intercepts for A and B
    ids_a = IMDB(a)
    ids_b = IMDB(b)
    ids_a_and_b = ids_a.intersection(ids_b)
    people = [ia.get_person(x) for x in ids_a_and_b]
    return [person.get('name') for person in people]

def IMDB(content):
    # returns a set of actors and actresses in content
    search_results = ia.search_movie(content)
    guess = search_results[0] # [ADD FEATURE] ask user if this is correct
    movie = ia.get_movie(guess.getID())
    cast = movie.get('cast')
    ids = [person.getID() for person in cast]
    return set(ids)
