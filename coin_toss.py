# FILE NAME - coin_toss.py
# NAME: KEVIN LEE
# DATE: 10/3/2025
# BRIEF DESCRIPTION: This program simulates a coin toss by generating a random number and displaying either Heads or Tails 
# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience
########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!
import random

# Print the header
print("===== Coin Flipper =====")

# Generate random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)

# Determine Heads or Tails based on the specification
# 51 or greater = Tails, otherwise = Heads
if random_number >= 51:
    print("Tails")
else:
    print("Heads")








########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
This lab was relatively straightforward, but the main challenge was carefully reading 
the specifications to understand the exact logic required (51 or greater for Tails) 
rather than assuming a different threshold or using a different random range.






'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.
'''
