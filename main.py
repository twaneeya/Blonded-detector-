# A fun little program to ask the user who their favourite artist is and respond  accordingly 

name=input("What is your name?")
artist=input(f"Nice to meet you,{name}! Who is your favourite artist?")
print(artist)
if artist.lower()=="frank ocean":
  print("OMG! He is magical! I lobby for you to listen to channel orange right now!")

else:
print(artist.title()+"is cool too! but we all know that Frank ocean is the GOAT!")
