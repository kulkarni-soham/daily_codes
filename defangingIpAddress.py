def defangIPaddr(address) :
    return address.replace(".","[.]")

print(defangIPaddr("255.0.0.0"))