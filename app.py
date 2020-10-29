print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling! Life is good.")
      counter -= 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("to find something fun to do.")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("to get some sleep. You deserve a good rest after all the hard work you did!")
      counter += 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("you'll do well!")
      counter += 1
    if each_word == "relieved":
      feelings_list.append ("relieved")
      encouragement_list.append ("I knew you would do fine!")  
      counter -= 1
    if each_word == "disappointed":
      feelings_list.append ("disappointed")
      encouragement_list.append ("that it's ok if you didn't do well this time! You can always try again and do better next year! Don't give up!") 
      counter += 1
    if each_word == "doubtful":
      feelings_list.append ("doubtful")
      encouragement_list.append ("don't think too much about it! You've worked hard and I'm sure you'll do fine!") 
      counter += 1
    if each_word == "sad":
      feelings_list.append ("sad")
      encouragement_list.append ("to cheer up and you can always work harder next time!") 
      counter += 1
    if each_word == "okay":
      feelings_list.append ("okay")
      encouragement_list.append ("to continue to stay this way.") 
      counter -= 1
    if each_word == "lonely":
      feelings_list.append ("lonely")
      encouragement_list.append ("you are never alone in this world cuz you have me and all your loved ones to back you up!") 
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember "+ encouragement_list[0] + " Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "" + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "" + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + " Hope you feel better :)"

  print()
  print(output)
  print()
