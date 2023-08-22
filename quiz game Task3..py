#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
QUIZ GAME
"""
print("WELCOME TO THE QUIZ GAME\n"
      
      "\nRules:-"
      "\n1.Give an answer in the integer form (1 to 4)"
      "")


A = input("\nDo you want to play a quiz:")
if (A.lower() == "yes"):
    score = 0
    Answer1 = int(input("\nWho developed Python Programming language?\n"
                        "1.Wick van Rossum.\n"
                        "2.Rasmus lendorf.\n"
                        "3.Guido van Rassum.\n"
                        "4.Niene stom.\n"
                        "\nUser answer="))

    if (Answer1 == 3):
        print("Your answer is correct.")
        score += 1
        print(f"Your score is {score}")
    else:
        print("Your answer is incorrect. 'Guido van Rassum' is correct answer.")

    Answer2 = int(input("\nWhich type of Programming does Python support?\n"
                        "1.object-oriented programming.\n"
                        "2.structured programming.\n"
                        "3.functional Programming.\n"
                        "4.all of the above.\n"
                        "\nUser answer="))
    if (Answer2 == 4):
        print("Your answer is correct.")
        score += 1
        print(f"Your score is {score}")
    else:
        print("Your answer is incorrect.'object-oriented programming' is correct answer.")

    Answer3 = int(input("\nWhich ofthe following is the correct extension of the python fill?"
                        "\n1.python\n"
                        "2.pl\n"
                        "3.py\n"
                        "4.ps\n"
                        "\nUser answer ="))
    if (Answer3 == 3):
        print("Your answer is correct.")
        score += 1
        print(f"Your score is {score}")
    else:
        print("your answer is incorrect.'.py' is correct answer.")

    Answer4 = int(input("\nWhich keyword is used for function in python language?\n"
                        "1.Function.\n"
                        "2.def.\n"
                        "3.Fun.\n"
                        "4.Define.\n"
                        "User answer="))
    if (Answer4 == 2):
        print("Your answer is correct.")
        score += 1
        print(f"Your score is {score}")
    else:
        print("Your answer is incorrect.'def' is correct answer.")
    print("\nYour total score is", (score), "in these question!!")
    print("You got " + str((score / 4) * 100) + "%")





# In[ ]:


# In[ ]:





# In[ ]:




