import hashlib

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = hashlib.sha512('salt' + word).hexdigest()
		if (cryptWord == cryptPass):
			print "[+] Found Password: "+word+"\n"
			return
	print "[-] Password Not Found.\n"
	return

def main():
	passFile = open('passwords_sha512.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password For: "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()