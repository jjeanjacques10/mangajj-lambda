import json

from process import Process


def lambda_handler(event, context):
    title = event['queryStringParameters']['title']
    chapter_number = event['queryStringParameters']['chapter']

    pages = Process().execute(chapter_number, title)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "manga_title": title,
            "chapter_number": chapter_number,
            "total_pages": len(pages),
            "pages": pages
        }),
    }
