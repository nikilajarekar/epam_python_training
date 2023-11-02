import re

str1 = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

#mormalize the cases
normal_case = str1.capitalize()
print(normal_case)
#pattern to match the last word of each sentence by finding the letters and dot at the end
pattern = '[a-z]+\.'
last_words = re.findall(pattern,normal_case)
print(last_words)
sentence = ' '.join(last_words)
#remove the dots
new_sentence = sentence.replace(".","",6)
print(sentence)
print(new_sentence)

#find the pos to insert
insert_pos = normal_case.index('paragraph') + len('paragraph') + 1
#insert the sentence at the specidifed position
added_string = normal_case[:insert_pos] + new_sentence + normal_case[insert_pos:]
#print(added_string)

#pattern to find the "Iz" only as a full word and replace it with is
pat = r'\biz\b'
correct_str = re.sub(pat,'is',added_string)
print(correct_str)

#pattern to fins \n \t spaces \r \f
pat1 = '\s'
res = re.findall(pat1,correct_str)
print(len(res)) #count
