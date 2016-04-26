import uuid
import hashlib
import time
import math
import base64
import M2Crypto

# timing dependent only on length of b
def secure_string_equal(a, b):
	equal = True
	c0 = None
	for i in xrange(0, len(b)):
		c1 = b[i]
		if i < len(a):
			c0 = a[i]
		else:
			c0 = None

		if c0 != c1:
			equal = False

	return equal
 
def hash_password(password):
	# uuid is used to generate a random number
	salt = uuid.uuid4().hex
	return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
	
def check_password(hashed_password, user_password):
	password, salt = hashed_password.split(':')
	return secure_string_equal(password, hashlib.sha256(salt.encode() + user_password.encode()).hexdigest())

def get_session(num_bytes=16):
	return base64.b64encode(M2Crypto.m2.rand_bytes(16))
