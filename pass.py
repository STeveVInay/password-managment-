import argparse, time
import string as st
import random as rd

def generatePwd(url,u,l,c):
	timecreated = time.asctime( time.localtime(time.time()) )
	f = open("User_Pass.txt","a+")
	pwd = ''
        if not (url):
		print"please enter url"
		exit()
	if u != None and l == None:
		pwd = pwd.join(rd.choice(c) for x in u)
		f.write("url= "+url+" user= "+u+" length= "+str(len(u))+" password= "+pwd+" createdOn= "+timecreated+"\n")
		return pwd
	elif u == None and l != None:
		l = int(l)
		pwd = pwd.join(rd.choice(c) for x in range(l))
		f.write("url= "+url+" user= "+u+" length="+str(l)+" password="+pwd+" timecreated="+timecreated+"\n")
		return pwd
	elif u != None and l != None:
		l = int(l)
		pwd = pwd.join(rd.choice(c) for x in range(l))
		f.write("url= "+url+" user= "+u+" length= "+str(l)+" password= "+pwd+" createdOn= "+timecreated+"\n")
		return pwd
	else:
		return "\nUse --help/-h option to view the usage of script\n"
		exit()
	f.close()

def main():
	if mode == "strong":
		chrr = st.letters + st.digits + st.punctuation
		print(generatePwd(url,username,length,chrr))
	if mode == "weak":
		chrr = st.letters
		print(generatePwd(url,username,length,chrr))
	if mode == "medium":
		chrr = st.letters + st.digits
		print(generatePwd(url,username,length,chrr))


if __name__ == '__main__':
	modes = ["strong","weak","medium"]
	m = "|".join(modes)
	parser = argparse.ArgumentParser(description="Random Password Generator", usage = "\npython pass.py -m <mode> --url <url>\npython pass.py -m <mode> -u <username>\npython pass.py -m <mode> -l <length>\npython pass.py -m <mode> -u <username> -l <length>")
	parser.add_argument('--url', help='Specify url')
	parser.add_argument('-m','--mode',help='Modes:%s' % (m), required=True)
	parser.add_argument('-u','--username', help='Specify Username')
	parser.add_argument('-l','--length',help='Specify Length')
	args = parser.parse_args()
	url = args.url
	username = args.username
	length = args.length
	# purpose = args.purpose
	mode = str(args.mode).strip()
	main()
