import json, os, base64, hashlib

def _short_code(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:7]

def lambda_handler(event, context):
    method = event.get('httpMethod', 'GET')
    if method == 'POST':
        body = json.loads(event.get('body') or '{}')
        url = body.get('url')
        if not url:
            return {"statusCode": 400, "body": json.dumps({"error": "url required"})}
        code = _short_code(url)
        # TODO: put in DynamoDB
        return {"statusCode": 201, "body": json.dumps({"code": code, "url": url})}
    else:
        params = event.get('pathParameters') or {}
        code = params.get('code')
        if not code:
            return {"statusCode": 400, "body": json.dumps({"error": "code required"})}
        # TODO: fetch from DynamoDB
        return {"statusCode": 302, "headers": {"Location": "https://example.com"}, "body": ""}
