__author__ = 'Dilan'
import hashlib
import os

numIterations = 100000
blocksize = 65536
def hash_normal(input):
    try:
        hasher = hashlib.sha256()
        salt = os.urandom(32).encode('hex')
        f = open(input, 'rb')
        buf = f.read(blocksize)
        buf += salt
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(blocksize)
        f.close()
        finaltupple = [hasher.hexdigest(), salt]
        #print finalTupple
        return finaltupple
    except NotImplementedError:
        print "Salting is not possible because no cryptographically secure way to generate random info was found"
        exit(1)


def check_normal_hash(hash, salt, input):
    hasher = hashlib.sha256()
    f = open(input, 'rb')
    buf = f.read(blocksize)
    buf += salt
    while len(buf) > 0:
        hasher.update(buf)
        buf = f.read(blocksize)
    f.close()
    print "testing hash {0:s} against {1:s}".format(hasher.hexdigest(), hash)
    if hasher.hexdigest() == hash:
        print "Matching hashes found."
        return True
    else:
        print "Hashes do not match."
        return False


def hash_kd(input):
    try:
        salt = os.urandom(32).encode('hex')
        h = hashlib.pbkdf2_hmac('sha256', input, salt, numIterations).encode('hex')
        finaltupple = [h, salt]
        #print finalTupple
        return finaltupple
    except NotImplementedError:
        print "Salting is not possible because no cryptographically secure way to generate random info was found," \
              " this program will exit now."
        exit(1)


def test_keyderived_hash(hash, salt, input):
    x = hashlib.pbkdf2_hmac('sha256', input, salt, numIterations).encode('hex')
    print "testing hash {0:s} against {1:s}".format(x, hash)
    if x == hash:
        print "Matching hashes found"
        return True
    else:
        print "Hashes do not match."
        return False
