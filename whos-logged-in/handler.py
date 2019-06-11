import json, boto3, datetime


def whos_logged_in(event, context):

    client = boto3.client('cloudtrail')
    cloudwatch_events = boto3.client('events')

    response = client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'EventName',
                'AttributeValue': 'ConsoleLogin'
            },
        ],
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(minutes=105),
        EndTime=datetime.datetime.utcnow(),
        MaxResults=100
    )

    for entry in response['Events']:
        entry['EventTime'] = entry['EventTime'].strftime("%Y-%m-%d %H:%M:%S")
        cwResponse = cloudwatch_events.put_events(
            Entries=[
                {
                    'Time': datetime.datetime.utcnow(),
                    'Source': 'ConsoleLogin',
                    'DetailType': 'ConsoleLogin',
                    'Detail': "{\"username\":" + "\"" + entry['Username'] + "\"}"
                },
            ]
        )

    return response

