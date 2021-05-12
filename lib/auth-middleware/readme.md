# auth-middleware

## Environment variables needed to have setup on your instance to use this library.

They should match the ones that are set in the `authservice` flask app.

- `PHONE_VERIFY_SECRET`
- `PHONE_VERIFY_AUDIENCE`
- `SHIBBOLETH_HOST`
- `SHIBBOLETH_CLIENT_ID`
- `ROKWIRE_API_KEY`
- `AUTH_ISSUER` 
    - This is the issuer for the Auth Building Block. This should match the issuer environment variable in the Auth Building Block.
- `AUTH_PUBKEYS`
    - These are the public keys used to verify tokens signed by the Auth Building Block. This should be formatted as follows 
    ```
    [
        {
            "kty":  ,
            "e":  ,
            "kid":   ,
            "n":  
        }
    ]
    ``` 

SHIBBOLETH_CLIENT_ID can contain one or more client IDs that are separated by comma. 
For example, `SHIBBOLETH_CLIENT_ID=abc,def,ghi`