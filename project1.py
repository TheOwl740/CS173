"""
This program takes 5 values, person 1 in and out, person 2 in and out, and the time the cat hops on the counter after midnight.
It adds each person's in and out times together, then performs a modulus operation with the hop time to get the location of the hop in the cycle.
Then it subtracts the in time, and compares against 0 to determine if the person was in during the hop.
After comparing with the and operator on the other person, it prints the success state.
"""
p1In = int(input()) #person 1 in time
p1Out = int(input()) #person 1 out time
p2In = int(input()) #person 2 in time
p2Out = int(input()) #person 2 out time
tHop = int(input()) #time of hop after midnight
if(((tHop % (p1In + p1Out)) - p1In >= 0) and ((tHop % (p2In + p2Out)) - p2In >= 0)): #large comparison
    print("SUCCESS")
else:
    print("CAUGHT")
