# AWS Lambda MangaJJ

<p align="center">
    <a href="https://github.com/jjeanjacques10/mangajj-lambda/issues">Report Bug</a>
    ·
    <a href="https://github.com/jjeanjacques10/mangajj-lambda/issues">Request Feature</a>
</p>

<p align="center">
   <a href="https://www.linkedin.com/in/jjean-jacques10/">
      <img alt="Jean Jacques Barros" src="https://img.shields.io/badge/-JeanJacquesBarros-FFCC00?style=flat&logo=Linkedin&logoColor=white" />
   </a>
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jjeanjacques10/mangajj-lambda?color=FFCC00">

  <a href="https://github.com/jjeanjacques10/mangajj-lambda/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/jjeanjacques10/mangajj-lambda?color=FFCC00">
  </a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-FFCC00">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/jjeanjacques10/mangajj-lambda?color=FFCC00" />
  <a href="https://github.com/jjeanjacques10/mangajj-lambda/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/jjeanjacques10/mangajj-lambda?color=FFCC00&logo=github">
  </a>
</p>

AWS Function to extract manga chapters from websites to mangaJJ.

## Getting Started

### Use the SAM CLI to build and test locally

Running lambda function

``` bash
sam build --use-container
sam local invoke MangaJJFunction --event events/event.json
# or
sam local start-api
```

### Unit tests

Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests.

```bash
pip install pytest pytest-mock --user
python -m pytest tests/ -v
```

## API Contract

* GET /chapter?title=naruto&chapter=1&source=muito_manga

``` json
{
    "manga_title": "naruto",
    "chapter_number": "1",
    "source": "muito_manga",
    "total_pages": 49,
    "pages": [
        "https://cdn.statically.io/img/imgs.muitomanga.com/f=auto/imgs/naruto/1/1.jpg",
        "https://cdn.statically.io/img/imgs.muitomanga.com/f=auto/imgs/naruto/1/2.jpg",
        "https://cdn.statically.io/img/imgs.muitomanga.com/f=auto/imgs/naruto/1/3.jpg",
        "https://cdn.statically.io/img/imgs.muitomanga.com/f=auto/imgs/naruto/1/4.jpg",
        "https://cdn.statically.io/img/imgs.muitomanga.com/f=auto/imgs/naruto/1/5.jpg",
        <...>
    ]
}
```

---
Developed by [Jean Jacques Barros](https://github.com/jjeanjacques10/)
