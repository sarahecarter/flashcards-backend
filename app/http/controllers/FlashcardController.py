""" A FlashcardController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Flashcard import Flashcard


class FlashcardController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", FlashcardController)
        """
        id = self.request.param("id")
        return Flashcard.where("id", id).get()

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", FlashcardController)
        """
        return Flashcard.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", FlashcardController)
        """
        topic = self.request.input("topic")
        term = self.request.input("term")
        definition = self.request.input("definition")
        flashcard = Flashcard.create({"topic": topic, "term": term, "definition": definition})
        return flashcard

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", FlashcardController)
        """
        id = self.request.param("id")
        topic = self.request.input("topic")
        term = self.request.input("term")
        definition = self.request.input("definition")
        Flashcard.where("id", id).update({"topic": topic, "term": term, "definition": definition})
        return Flashcard.where("id", id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", FlashcardController)
        """
        id = self.request.param("id")
        flashcard = Flashcard.where("id", id).get()
        Flashcard.where("id", id).delete()
        return flashcard