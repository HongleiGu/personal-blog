import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

# Configuration from the HTML
passphrase = "hg1523:Raymond#1234"  # Combined username:password
keystore_entry = "gvR3NW27K8CeO4jkQXfrOg==;uZD2QNCfhYExTaI0qVeuUs2ZRxJYY/WrKUgRQOuzscgzZvS7qaOR52iqFqBcZaBXb2u4Qj/E1vW4HNEms2KrD6E4MtJPzHtw0XmOrd64bPQ0ervp6VY0iKzeLmqtvAN7;R7dHU9Z+y47oSuPO7w+NDw=="
encrypted_content = "nJFwyLV76uTDxlCUc2CM6w==;MKQrILQf8g7XUxQzLblSLc91OjkH86u9Xu/8LXo9+ToGB7WMMTmUOwNJUaIbs7/aBGU9Je12WS0KRZGjOnONtFAAK9lcCFTyJNNx2Pm4y9uPyQaMUx/iCLTG4DgWrxl+07K8BO/JmC82mR4I7vTZNHnefT2bxgE6XQYN+Wm2ZDu9EvGia923LLWdKXTqTbExk1hPqMZoQQLsZESAq4QHcc7fhfqO5fQDARGSpb5nXlzRGd+4U+Ukus+mrjeQSscaj9LQy/sBl3dCpEl3H64kVRSZuTTXpa/7iN6kGRrUAmDFBOvgsX4+NIBIZmAxR5K9Mmvw6YB4jzUuWaQGcf2zNj7rATBqTqKRP9sFw+tzfRrVHgeH+z5kn5RlvGjuI5k3hzfhArWmWcVTY4HyOnV0j3OeHBFvDl8HqDnTmVyKwfYvr20Q76To2NbzbXxZCaSEyNMh4zzhgb95BCh4pj6N684m4azNKmalyWbNLFap46+kAGogv1itfN3kL9rn37+C+CchVTFnx+Oqn7yp9z+1PQaDIJGCGHRtoQ7yhZz9UwX+d2HdfNjrikOF/o1P7tf27vdI4m5zTnDoEjixotp6KCGVLq5RSraaNmNe8U7cWNKPbrMDQlNoJKNbYavPPjjLbBXN+VqbtQB2tGxxljeWYQekg0DpYoMx/ZhrCDaCgWPSQzYHf1KjopSYVqtPmHqAWVzete5ebyF5yMybeWmw0G3AOA1aF5/rjzBGVoQ/xDGlEzAH6RPCTIS3PmoXkZnAyu6FBPQPfjr3jHWBIW/zzVZZE6gZRTiCuRea/5+jNM2ZqVfaD/PmfDiy43DdSxX2YcJa/aRLp5ZIn2rM6rpoCLDKi5R8ytmyb4uXdIbsmvLtECvJ6ESmPZvIQMLjj8ftIvkJw5n+mRr0ad23y6wHq1GceSjKZ46aunWJ0hZPhIMV7j7GZbS5WBhxI2dJL4oOJGmsV5NJz+dcKqeECZRqxH4p1K0NTVjAJEu/l5AcUVHBzLlAeiFxOQp+0U8aPjF88WY1qWIDsrqARoGFk3N/qxx3BXBm+AKmhrSEirwmgnoPLnu3p64N8kRTYM5f41cZ+EJlngojKA6x3LRuH8w7irNvoYTTcYjvflKGwCY7VX0aG6qH03Q7vuTZ3kUGLnRk/65drfjKdeM54Ydi89YgC2lBHXTMWbAcZfOhhsQXfURmrqN7mtSlm2d39BLRpCSJO4eA09DspoFaMj59nnXfXfZeuMMr9UG6JKDtaKjrTRI8PipBARlfV7hBAsExd5oQ+vNPY/Vlow9FVEy17vNtDqIU3Fqxs2J5E8ce9FAG6pHojX5ieBtUvAWGZWMdUoBmn5pwamroXRQ+BZ19U3LzRJAQgBeuJt6hMQxYrvasUQ0GSQvKJXxUyRjF5KOQBz9WWqj3g/KkCCs3zyM/poCSR09ttgeA7SVYsPTwWeQfgIxaq4qlJPFDCpH82GORr19uGNABJi5ylDUTkjINv7ffaJwZMCmbUS2SsqdOd4KbNjXiuKnIG8YixucVkPM4RXCKXcHOrwriD8ZgdpDnlWr3H4MFOHNMl4mRR6GhRRsP/es/11G7gyq/EyrmUvCsmOorW1AjJ9vgUqHPZRmTGnS+Wi8d6QZnKiJtkHKZyIsdTBTXSJgWewAcEc9Fr25KswTg6Y/5jEuqIjOfXxofm8YIEagSDXM6TzUN7tlpVULM+LZj2wJD6TSL51QXQTQv2/xg7Oq2PZ6fczNDluPq9N6ZGwG08oZzBYQ4RZE3P3xA2TxEO2hbTyXw/4s1KxRxxQR63ks11prqnzgp1Q8SghHMAOGlsa3MZuHFdWTZC2cMzwMM+nVfeEUvtBZpD29U+UvxfiiUcVCA6yKyG3lMsijRkHaGJnhAII5yKtwACbt+b6AMNGoxZQsBr2FFCXNSRjzVicKiscVtiw6nvdi5/2WKvw2Oe8arIvbAAOF6PBrPz1TYf4AU7FgoLOZpQk7+2jbqsl2ordD642OcL4FPDcPfMUtlyW1yL1nlcEcTkrCiWqExRuLO8ZDPhulImeGb6wYEw4Xo9fcaxZpwCN3q06S8XlShsWHAsI9JPS1g+AnloOPIGhjaUk/cNPBlrQ1O8Tn/oIHFJcb5pMv3u0oSyeKVWjF+NMJsCSSIgpkyKByYvW0g8c5TVSVip2TqiXGIjLEX"

# Split keystore entry
salt_b64, encrypted_key_b64, _ = keystore_entry.split(';', 2)
salt = base64.b64decode(salt_b64)
encrypted_key = base64.b64decode(encrypted_key_b64)

# Derive key using PBKDF2
dk = PBKDF2(
    passphrase,
    salt,
    dkLen=48,       # 32-byte key + 16-byte IV
    count=100000,
    hmac_hash_module=SHA256
)
key = dk[:32]
iv = dk[32:48]

# Decrypt the content key
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
content_key = cipher.decrypt(encrypted_key)

# Remove PKCS#7 padding
padding_length = content_key[-1]
content_key = content_key[:-padding_length]

# Split encrypted content
iv_b64, ciphertext_b64 = encrypted_content.split(';', 1)
iv_content = base64.b64decode(iv_b64)
ciphertext = base64.b64decode(ciphertext_b64)

# Decrypt the content
cipher = AES.new(content_key, AES.MODE_CBC, iv=iv_content)
decrypted_data = cipher.decrypt(ciphertext)

# Remove PKCS#7 padding
padding_length = decrypted_data[-1]
decrypted_content = decrypted_data[:-padding_length].decode('utf-8')

print(decrypted_content)