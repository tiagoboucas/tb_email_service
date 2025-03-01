# tb_email_service
Mail server that allows you to send emails via a REST API


## Curl

### Get emails
curl -X GET {{url}}/emails -H "X-API-KEY: {{api_key_here}}"

### Send an email (HTML)
curl -X POST {{url}}/send -H "Content-Type: application/json" \
-H "X-API-KEY: {{api_key_here}}" \
-d '{
    "to": "test@mail.com",
    "subject": "Test HTML Email",
    "content": "<h1>This is an HTML email</h1><p>Sent from my Flask mail server.</p>",
    "content_type": "html"
}'

### Send an email (text)
curl -X POST {{url}}/send -H "Content-Type: application/json" \
-H "X-API-KEY: {{api_key_here}}" \
-d '{
    "to": "test@mail.com",
    "subject": "Test HTML Email",
    "content": "Sent from my Flask mail server....",
    "content_type": "plain"
}'
