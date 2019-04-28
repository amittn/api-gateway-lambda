import json

RESPONSE_SECURITY_HEADERS = {
    'Cache-control': 'no-store',
    'Pragma': 'no-cache',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
    'X-Content-Type-Options': 'nosniff',
    'X-XSS-Protection': '1'
}


def lambda_handler(event, context):
    try:
        print('---------------------event---------------------------------')
        print(event)
        print('---------------------context--------------------------------')
        print(context)
        print('------------------------------------------------------')
        return handle(event, context)
    except Exception as ex:
        print(ex)


def handle(event, context):
    response_body = {'search_result': 'success'}
    return generate_response(200, {}, response_body)


def generate_response(status_code, headers, response_body):
    """ This function generates a response containing a HTTP status code and response body.

        Args:
            status_code (int): the status code of the response
            headers (dict): extra headers as required
            response_body (dict): the response body

        Returns:
            dict: contains the status code and the response body
    """

    headers.update(RESPONSE_SECURITY_HEADERS)

    return {
        'statusCode': status_code,
        'headers': headers,
        'body': json.dumps(response_body)
    }