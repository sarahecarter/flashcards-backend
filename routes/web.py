"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
      Get("/", "FlashcardController@index").name("index"),
      Get("/@id", "FlashcardController@show").name("show"),
      Post("/", "FlashcardController@create").name("create"),
      Put("/@id", "FlashcardController@update").name("update"),
      Delete("/@id", "FlashcardController@destroy").name("destroy")
    ], prefix="/flashcards", name="flashcards")
]
