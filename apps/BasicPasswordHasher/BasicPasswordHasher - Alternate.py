desired_hash = 675 #Stored hash of password ciscoclass. User wants to match this hash with the one they enter.
final_hash = 1 #Starting final hash value used for password hashing algorithim computations.

def translater():
 global final_hash 
 translations = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 
 'x': 24, 'y': 25, 'z': 26}
 user_input = raw_input("Enter lowercase passphrase: ")
 for letter in str(user_input):
   if letter in translations:
    print("IH - " + str(translations.get(letter, "none")))
    if int(translations.get(letter, "none")) % 2 == 0:
       final_hash = final_hash * int(translations.get(letter, "none"))
    elif int(translations.get(letter, "none")) % 2 != 0:
       final_hash = final_hash + int(translations.get(letter, "none"))
   else:
    print("ERROR!")
 print("CH - " + str(final_hash))
 return final_hash
 hash_checker()
 
 
def hash_checker():
 global final_hash
 global desired_hash
 if final_hash == 1:
  print("Composite String Error!!!")
 else:
  if final_hash == desired_hash:
   print("Success! Logged-in!")
  else:
   print("Log-in Failed!")
 restart()
 
def restart():
 global final_hash 
 final_hash = 1
 translater()
 restart()
    
translater()

