from minecraft.networking.connection import Connection
import time

def main():
	username = "test"
	connection = Connection("127.0.0.1", 25565, username=username)
	connection.connect()
	
	time.sleep(0.015)

if __name__ == "__main__":
    main()
