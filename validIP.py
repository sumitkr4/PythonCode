'''
Inside this code, I am taking IP as string and checking either it is valid IPV4 Or not, same as IPV6 is valid or not.
'''

class Validation(object):
    def validIPAddress(self, IP):
        if ":" in IP:
            IP=IP.split(":")
            for i in IP:
                if len(i)>4 or not i.isalnum() or len(i)<0:return "Invalid IPV6" 
                for j in i:
                    if j.isalpha():
                        if j.isupper(): 
                            if ord(j)>ord("F"):return "Invalid IPV6" 
                        else:
                            if ord(j)>ord("f"):return "Invalid IPV6" 
            return "IPv6" 
        else:
            IP=IP.split(".")
            if len(IP)!=4:return "Invalid IPV4"
            for i in IP:
                if (len(i)>1 and i[0]=="0") or not i.isnumeric(): return "Invalid IPV4" 

                elif (int(i)>255 or int(i)<0):
                    return "Invalid IPV4"
            return "IPv4"
s=Validation()
print(s.validIPAddress("2.20.1.0"))
# print(s.validIPAddress("8003::1"))
