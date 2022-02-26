import math

def test(text, ws):
	compressed = compress(text,ws)
	decoded = decompress(compressed)
	assert(text == decoded)


# Test examples
text = input("Enter sample text: ")
ws = input("Enter a window size: ")
test(text, ws)

compressed = compress(text, ws)
decoded = decompress(compressed)
tuplesize = math.log2(int(ws))+math.log2(int(ws))+math.log2(256)

print("Output of LZ77 algorithm: ", compressed)
print("Size for each output tuple: {0:d} bits".format(round(tuplesize)))
print("Size for all tuples: {0:d} bits".format(round(tuplesize * len(compressed))))

print("Decoded: ", decoded)