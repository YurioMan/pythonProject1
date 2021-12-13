#from sys import argv
#from os.path import exists

#script, cast.txt, linux1.txt = argv
#print ("Copy from %s to %s") % (cast.txt, linux1.txt)

f1 = open('cast.txt')
f11 = f1.read()

#print ("Simvolov v faile %d") % len(f11)
#print ("Sootvetstvuet li file? %r") % exists()

#raw_input()

f2 = open('linux1.txt', 'a')
f2.write(f11)


print("Proverte file")
 
f2.close()
f1.close()


