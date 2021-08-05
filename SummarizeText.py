#This is the final version
import pyperclip
#Summarize Paragraph
#This program takes a long text and summarizes it, taking the first sentence of each paragraph

#Open file where text is located
#with open(r"C:\Users\jmonterr\Desktop\ToSummarize.txt") as file:
#    text = file.read()
text = pyperclip.paste()

#Assign text to paragraphs with split \n
paragraphs = text.split('\n')

#For each paragraph, get the first sentence and store in an array
sentences = []
for paragraph in paragraphs:
    sentences.append(paragraph.split('.')[0])

#Join first sencentes
summary = ''
for sentence in sentences:
    if sentence != "Open Transcript":
        summary += sentence + '\n'

#Output summary
pyperclip.copy(summary)
print('Summary created')