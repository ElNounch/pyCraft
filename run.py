from minecraft.networking.connection import Connection
import time, random, string, errno
from socket import error as socket_error

def main():
	username = "test" #''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
	connection = Connection("192.168.2.38", 25565, username=username)
	connection.connect()
	time.sleep(0.03) # use 0.3 in authentication mode, 0.03 if not.

if __name__ == "__main__":
	try:
		main()
        except socket_error as serr:
		if serr.errno == errno.ECONNREFUSED:
			open("stop.txt", 'a').close()
