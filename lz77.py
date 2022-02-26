import math

def compress(text, ws):
	'''
	Parameters:
		text
		ws: window size
	Returns:
		ouput: tuple list the compression
	'''
	ws = int(ws)
	matches = 0
	output = []
	for i in range(0,len(text)):
		# Skip many iterations as matches
		if matches > 0:
			matches = matches - 1
			continue

		# Search window
		if len(text[:i]) > ws:
			window = text[i-ws:i]
		else:
			window = text[:i]

		# Largest prefix
		prefix = text[i]
		while True:
			if prefix in window:
				matches = matches + 1				
				aux = prefix
				# check next prefix
				prefix = text[i:i+matches+1] 
				
				# special case last char
				if aux == prefix:
					prefix = prefix + '_'
					break
			else: break

		# Output
		if matches == 0:
			offset = 0
			length = 0
			symbol = prefix
		else:
			length = len(prefix)-1  # prefix is ​​the last checked that didn't match
			symbol = prefix[length]
			prefix = prefix[:-1] # correct prefix
			offset = i - window.rfind(prefix) - (i - len(window))

		output.append((offset,length,symbol))
	return output

def decompress(tuples):
	'''
	Parameters:
		tuples: compress output
	Returns:
		decoded: original text
	'''
	decoded = ""
	for i in range(0,len(tuples)):
		if tuples[i][0] == 0:
			# Add new patterns
			decoded += tuples[i][2]
		else:
			offset = tuples[i][0]
			length = tuples[i][1]
			symbol = tuples[i][2]
			j = len(decoded)
			# Add repeated patterns
			rep = decoded[j-offset:j-offset+length]
			decoded += rep
			# Final text special case
			if symbol != "_":
				decoded += symbol
	return decoded

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
		



								