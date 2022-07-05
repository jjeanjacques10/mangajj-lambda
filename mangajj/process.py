from src.muito_manga_service import MuitoMangaService


class Process:

    def __init__(self):
        self.muito_manga = MuitoMangaService()

    def execute(self, chapter_number, title):
        return self.muito_manga.get_chapter(chapter_number, title)
