import json

from pymangaj import pymangaj, Sources

def get_source(source):
    return {
        "manga_livre": Sources.MANGA_LIVRE,
        "muito_manga": Sources.MUITO_MANGA
    }[source]

def lambda_handler(event, context):
    title = event['queryStringParameters']['title']
    chapter_number = event['queryStringParameters']['chapter']
    source = event['queryStringParameters'].get('source', 'muito_manga')
    print(f"title:{title}, chapter_number:{chapter_number}, source: {source}")

    pages = pymangaj.search(title, chapter_number, sources=[get_source(source)])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "manga_title": title,
            "chapter_number": chapter_number,
            "source": source,
            "total_pages": len(pages),
            "pages": pages
        })
    }
