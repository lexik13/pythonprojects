"""
Password generator
Requirements:
-generates 10 passwords
-use different hashing algorithms
-use online password cracking site to see if they can be cracked
"""
import hashlib

def prompts():
    print('     Hello...')
    print('     Want to encode a secret?')
    password_generator()

def password_generator():
    max_passwords = 10

    secrets_utf = None
    secret_sha = None
    secrets_md = None
    secret_sha512 = None

    for i in range(max_passwords):
        secret_utf = input('Enter a secret: ') # UTF
        secrets_utf = secret_utf.encode('utf-8')
        print('encoded string: ', secrets_utf)

        secrets_md = hashlib.md5(secrets_utf).hexdigest() # MD 5
        print('MD5: ', secrets_md)

        md_bytes = secrets_md.encode('utf-8')
        secret_sha = hashlib.sha256(md_bytes).hexdigest() # SHA 256
        print('SHA256: ', secret_sha)

        secret_sha512 = hashlib.sha512(secrets_utf).hexdigest()
        print('SHA512: ', secret_sha512)

    return secrets_md, secrets_utf, secret_sha, secret_sha512

def main():
    prompts()
main()



