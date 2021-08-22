def reno(t):
    s=""
    for j in t:
        for i in j:
            if i.isalpha():
                s=s+i
            else:
                pass
    return s
def reno1(t):
	s=''
	for j in t:
		for i in j:
			s+=i
	s=s.split(',')
	#removing null as its always present at the end
	if s[-1]=='None':
		s.pop(-1)
	return s
def w1(id1):
    f=open("idd1.txt",'w')
    f.write(id1)
    f.close()
def r1():
    f=open("idd1.txt",'r')
    d=f.read()
    f.close()
    return d

