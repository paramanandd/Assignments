import collections

#-----------------INITIALIZATION-----------------------
# initializing string   
input_text = input ("Enter input string :")
#if input is to be hard coded use the below variable as input
#input_text= "test the input"

#------------------PART-I-----------------------------
#part 1 of the solution to print the input string size
print("number of character's in input: ", input_text+" :",len(input_text))

#-------------------PART-II----------------------------
# printing original string 
print ("The original string is : " +  input_text) 
  
# using split() to count words in string 
res = len(input_text.split(' ')) 

# printing result 
print ("The number of words in string are : " +  str(res)) 


#-------------------PART-III----------------------------
alpha_count=0
for i in range(len(input_text)):
	if(input_text[i].isalpha()):
		alpha_count = alpha_count + 1
#printing result
print("number of alphabets in sentence are :",alpha_count)

#-------------------PART-IV----------------------------
#Assuption if there are multiple values with same highest occurence then the first value found will be given as output and the string provided is not empty
try:
	most_commen = collections.Counter(input_text.lower()).most_common(1)[0]
	print("number of times the most commenly used character occurs :",most_commen)
except:
	print("not valid input String for getting maximum character ocurences")