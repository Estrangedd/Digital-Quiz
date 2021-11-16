score = 0

question_list = [["what is the closest planet to the sun?","mercury"],

                ["what is the biggest planet in our solar system?","jupiter"],

                ["is it possible to inhabit a black hole?","yes"],

                ["what is the part of the black hole called that will be safe for us to inhabit and how far away?","the habitable zone 140 light years away from the event horizon"],

                ["what telescope was used to find dark matter?","chandra"],

                ["What is the oldest planet in our solar system called?","psr b12620-26 b"],

                ["what lays in the center of our galaxy?","a supermassive black hole"],

                ["What are the names of all planets in our solar system","earth, jupiter, saturn, mars, neptune and mercury?"],

                ["",""],

                ["what planet is missing in the 8th question?","uranus"]]


#main routine

for question in question_list:

   print(question[0])

   answer = (input("Answer").strip().lower())

   if answer == question[1]:

       print("Correct")

       score += 1

   else:

       print("Incorrect")


print("{}".format(score))

