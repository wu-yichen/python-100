import zlib

s = 'hello world!hello world!hello world!hello world!'

print(zlib.decompress(zlib.compress(s)))
