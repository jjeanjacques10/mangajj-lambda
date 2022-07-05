import requests


class MuitoMangaService:

    def __init__(self) -> None:
        pass

    def get_chapter(self, chapter_number, anime):
        pages = []

        for i in range(1, 50):
            url = f"https://cdn.statically.io/img/imgs.muitomanga.com/f=auto/imgs/{anime}/{chapter_number}/{i}.jpg"
            response = requests.get(url)
            if response.status_code == 200:
                pages.append(url)
            else:
                print(f"final page {i}|{anime}|{chapter_number}")
                break

        return pages
