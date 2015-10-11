import ftplib
import optparse

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] ' + str(hostname) +' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-] ' + str(hostname) +' FTP Anonymous Logon Failed.'
		return False

def main():
	parser = optparse.OptionParser("usage%prog "+"-H <direction>")
	parser.add_option('-H', dest='hname', type='string', help='specify host ip')
	(options, args) = parser.parse_args()
	if (options.hname == None):
		print parser.usage
		exit(0)
	else:
		anonLogin(options.hname)

if __name__ == '__main__':
	main()