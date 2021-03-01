# WebServer
Django based backend for the next big thing **Mai - Health Tracker and Detection**

### Endpoints (Accounts)

### 1. `/accounts/register/`
#### Request Type: 
`POST`
#### Request Format:
```
{
    'name': <Name>,
    'email_id': <Email-id>,
    'gender': <Gender>,
    'device_token': <Device Token>
}
```
#### Response Format:
```
{
    'message': <Message>
    'success': bool
}
```

### 2. `/accounts/login/`
#### Request Type: 
`POST`
#### Request Format:
```
{
    'email': <Email-id>,
    'password':<Password>
}
```
#### Response Format:
```
{
    'message': <Message>
    'success': bool
    'user': <request.user.username> (Only for successfull login)
}
```
### 3. `/accounts/logout/`
#### Request: 
`GET/POST`
#### Response Format:
```
{
    'message': <Message>
    'success': bool
}
```
### 4. `/accounts/getAccount/`
#### Request: 
`GET`
#### Response Format (On Logged in):
```
{
    'id': <userid>,
    'name': <username>,
    'email': <Email-id>,
    'success': True
}
```
#### Response Format (Anonymous User):
```
{
    'message': "No Account Logged in"
    'success': False
}
```
