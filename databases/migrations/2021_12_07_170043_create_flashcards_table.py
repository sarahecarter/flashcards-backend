"""CreateFlashcardsTable Migration."""

from masoniteorm.migrations import Migration


class CreateFlashcardsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("flashcards") as table:
            table.increments("id")
            table.string("topic")
            table.string("term")
            table.string("definition")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("flashcards")
