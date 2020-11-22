import socket
import passdecode
import sys
import threading
import time
import hashlib

name = 'SCANNER'
print("-"*50)
print(name.center(50," "))
print("-"*50)

def result():
	global enter
	print("-"*50)
	print("Choose Your Option:")
	a = '1. PORT SCANNING'
	b = '2 .MD5 HASHING(ENCRYPT AND DECRYPT)'
	c = '3. PYTHON BCRYPT(ENCRYPT & DECRYPT)'
	q = '4. \'q\' or \'Q\' For Exit'
	print(a.center(50, " "))
	print(b.center(50, " "))
	print(c.center(50, " "))
	print(q.center(50, " "))
	print("-" * 50)
	take = input("Enter Your Chooice: ")
	print("-"*50)
	try:
		enter = int(take)
	except 	ValueError:
		if(take == 'q' or take == 'Q'):
			sys.exit()
		else:
			print("-"*50)
			result()
			main_work()

result()


def main_work():
	if (enter > 4 or enter < 1):
		print("Enter Correct Option.")
		result()
		main_work()
	if (enter == 1):
		c = '1. PORT SCANNING'
		print(c.center(50, " "))
		host = input("Enter Your Target Ip:")
		start_port = int(input("Enter Start Port:"))
		end_port = int(input("Enter End Port:"))
		print("-" * 50)
		#x = '.'
		#length = len(host)
		if start_port >= 1 and end_port <= 65535:
			try:
				ip = socket.gethostbyname(host)
				print("Target Ip ------------>%s" % ip)
				print("*"*50)
			except socket.gaierror:
				print("Host Not Found or Enter A Valid IP")


			def scan(port):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(2)
				conn = s.connect_ex((ip, port))
				if not conn:
					print(f"Port {port} Is Open")
				s.close()
				if port == " ":
					print("*"*50)
					result()
					main_work()

			for port in range(start_port, end_port + 1):
				thread = threading.Thread(target=scan, args=(port,))
				thread.start()
		else:
			print("Port Must Be Under {1-65535}")	
            

	if (enter == 2):
		print("-" * 50)
		d = '2. MD5 HASHING'
		print(d.center(50, " "))
		print("-" * 50)
		e = '1. MD5 ENCRYPT'
		f = '2. MD5 DECRYPT'
		g = '3. Back'
		print(e.center(50, " "))
		print(f.center(50, " "))
		print(g.center(50, " "))
		print("-" * 50)
		put = input("Enter Your Choise:")
		print("-"*50)
		def verify():
			try:
				taken = int(put)
				if (taken > 3 or taken < 1):
					print("Enter Correct Chooice")
					sys.exit()
				if (taken == 1):
					text = input("Enter Your Text:")
					has_obj = hashlib.md5(text.encode("utf8")).hexdigest()
					print("Your Hash:", has_obj.center(50, " "))
					print("-" * 50)
					result()
					main_work()
				if (taken == 2):
					passdecode.md5_hash()
					result()
					main_work()
				if(taken == 3):
					result()
					main_work()
			except ValueError:
				print("Enter Correct Chooice")
				result()
				main_work()
		verify()
	if(enter == 3):
		print("-"*50)
		bc = 'PYTHON BCRYPT'
		print(bc.center(50, " "))
		print("-"*50)
		e = '1. BCRYPT ENCRYPT'
		f = '2. BCRYPT DECRYPT'
		g = '3. Back'
		print(e.center(50, " "))
		print(f.center(50, " "))
		print(g.center(50, " "))
		print("-" * 50)
		put = input("Enter Your Choise:")
		print("-"*50)
		try:
			ta = int(put)
			if (ta > 3 or ta < 1):
				print("Enter Correct Chooice")
				sys.exit()
			if (ta == 1):
				passdecode.bc_encrypt()
				result()
				main_work()
			if (ta == 2):
				passdecode.bc_decrypt()
				result()
				main_work()
			if (ta == 3):
				result()
				main_work()
		except ValueError:
			print("Enter Correct Chooice")
			result()
			main_work()
	if enter == 4:
		quit()
	sys.exit()
main_work()