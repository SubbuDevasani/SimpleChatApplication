import jwt
class Token:
    # Request the request from the accounts views to create a token 
    # By passing the below arguments
    def encode(payload,key,algorithm):
        # By using the jwt and passing the arguments to the encode functon in jwt ande creating a token and returning the token
        token = jwt.encode(payload=payload, key=key, algorithm=algorithm).decode('utf-8')
        return token
    #  Request the request from the accounts views to decode a token 
    def decode(token,key,algorithm):
        payload= jwt.decode(token,key,algorithms=[algorithm])
        # returning the payload varible
        return payload
