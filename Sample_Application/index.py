def handler(event, context):
    import os
    import json

    environment = os.environ['ENVIRONMENT']

    with open("data.json", "r") as f:
        data = json.load(f)

    if event["rawPath"] == "/":
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps(data)
        }

    if event["rawPath"] == "/docs":
        # Create an HTML page with documentation
        docs_page = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>AAPI Documentation</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 0 auto;
                }
                h1, h2 {
                    color: #333;
                    border-bottom: 1px solid #ccc;
                }
                p {
                    margin-bottom: 16px;
                }
            </style>
        </head>
        <body>
            <h1>The Amazing API</h1>
            <h2>GET /</h2>
            <p>Returns all data in JSON format.</p>

            <h2>GET /{id}</h2>
            <p>Returns a specific item by its ID in JSON format.</p>
        </body>
        </html>
        """

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html",
            },
            "body": docs_page
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
                    "Content-Type": "application/json",
                },
                "body": json.dumps(item)
            }

    # Return a 404 if the id doesn't match any item
    else:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps({
                "message": f"id {id} not found",
                "event": event,
                "id": id
            })
        }

