import hashlib
from secrets import randbits



def generate_160bit():
    return randbits(160)

def sha1_digest(input_data: str) -> int:
    return int(hashlib.sha1(input_data.encode()).hexdigest(), 16)


# (2) Prime p and Generator g 


p = 178011905478542266528237562450159990145232156369120674273274450314442865788737020770612695252123463079567156784778466449970650770920727857050009668388144034129745221171818506047231150039301079959358067395348717066319802262019714966524135060945913707594956514672855690606794135837542707371727429551343320695239

g = 174068207532402095185811980123523436538604490794561350978495831040599953488455823147851597408940950725307797094915759492368300574252438761037084473467180148876118103083043754985190983472601550494691329488083395492313850000361646482644608492304078721818959999056496097769368017749273708962006689187956744210730


# (2) Compute y = g^x mod p, where x = SHA1(student ID)


student_id = "3894630"
x = sha1_digest(student_id)
y = pow(g, x, p)

print(" (2) Diffie-Hellman Step:")
print("x = SHA1(student ID) =", x)
print("y = g^x mod p =", y)


# (3) Diffie-Hellman



C = "Zhen"   # VPC (client side)
S = "Xiao"   # Data Centre (server side)

# Generate random 160-bit secrets a and b
a = generate_160bit()
b = generate_160bit()

# Compute A = SHA1(str(a) + C), B = SHA1(str(b) + S)
A = sha1_digest(str(a) + C)
B = sha1_digest(str(b) + S)

# Compute public keys g^A mod p and g^B mod p
gA = pow(g, A, p)
gB = pow(g, B, p)

# Compute shared secret keys
shared_key_vpc = pow(gB, A, p)  # VPC computes
shared_key_dc  = pow(gA, B, p)  # Data Centre computes

print("\n(3) Diffie-Hellman Key Exchange:")
print("Random a (VPC):", a)
print("Random b (Data Centre):", b)
print(f"A = SHA1(a + {C}) = {A}")
print(f"B = SHA1(b + {S}) = {B}")
print("g^A mod p:", gA)
print("g^B mod p:", gB)
print("Shared Key (computed by VPC):", shared_key_vpc)
print("Shared Key (computed by Data Centre):", shared_key_dc)

# Validate that both keys are equal
if shared_key_vpc == shared_key_dc:
    print("\nKeys Match: Secure Shared Key Established.")
else:
    print("\nKeys DO NOT Match: Something went wrong.")
