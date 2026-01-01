def access_vault(mfa_token):
    if mfa_token == "AUTH_TOKEN_99":
        return "SUCCESS: Access Granted. Sensitive Data: [Project_Alpha_Files]"
    else:
        return "FAILURE: Access Denied. Identity could not be verified."