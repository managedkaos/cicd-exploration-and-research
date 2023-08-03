def handler(event, context):
    import json

    with open("data.json", "r") as f:
        data = json.load(f)

    if event["rawPath"] == "/":
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/json",
            },
            "body": json.dumps(data)
        }

    # Get the id from the path
    id = event["rawPath"][1:]

    # Check the id against each item in the data
    for item in data:

        # Return the item if the id matches
        if item["id"] == id:
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "text/json",
                },
                "body": json.dumps(item)
            }

    # Return a 404 if the id doesn't match any item
    else:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "text/json",
            },
            "body": json.dumps({
                "message": f"id {id} not found",
                "event": event,
                "id": id
            })
        }

