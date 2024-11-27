"""
justify(25, “This is some sample text, really just enough to generate a few lines in the output
to show what the text justify function is supposed to do.”);

This is some sample text,
really   just  enough  to
generate  a  few lines in
the  output  to show what
the text justify function
is supposed to do.


Each line is 25 characters long, and both begins and ends with a non-whitespace character


Spaces are added as evenly as possible within lines to get the line to be the required length,
so no pair of adjacent words should have more than one more space between them than
any other pair in the line.

last line is left justified
atleast one word can be fit in the line



currLen = 5
[[(0,4, ),(5,6)], ...]
[22,5]

[6, 4, 6, 2]

diff/no. of words -1 =4
diff%no. of words -1 = 2
  
This is some sample text,
        |

currLen =21 , currLine = [[0,3], [5,6], [8,11], [13, 18]], lines = [], wordStartIdx = 20, totalWordsLength = [] , currWordsLength = 21
idx = 20

"""
import os

class TextFormatter:
	def extractWords(self, maxLineLength : int, text : str) -> tuple[list[list[tuple[int, int]]], list[int]]:
		currLen = 0
		currLine = []
		lines = []
		wordStartIdx = 0
		totalWordsLength = []
		currWordsLen = 0
		for idx in range(len(text)):
			char = text[idx]
			
			if char == os.linesep:
				continue
			
			if char == ' ' or idx == len(text)-1:
				if idx != wordStartIdx:
					currWordsLen += idx - wordStartIdx
					currLine.append((wordStartIdx, idx - int(idx != len(text)-1)))
				wordStartIdx = idx + 1
			
			elif char != ' ':
				currLen += 1
				if (currLen + (len(currLine)-1)) > maxLineLength:
					lines.append(currLine)
					totalWordsLength.append(currWordsLen)
					currWordsLen = 0
					currLine = []
					currLen = idx - wordStartIdx + 1 
		
		if len(currLine)>0:
			lines.append(currLine)
			totalWordsLength.append(currWordsLen)

		return (lines, totalWordsLength)

	def createEvenlySpacedString(self, maxLineLength : int, line : list[tuple[int, int]], wordsLength : int, text : str) -> str:
			noOfWords = len(line)
			spaceRequired = maxLineLength - wordsLength
			commonSpacing = spaceRequired // (noOfWords-1)
			remainingSpace = spaceRequired % (noOfWords-1)
			
			justifiedLine = []
			for wordIdx in range(len(line)):
				word = line[wordIdx]
				justifiedLine.append(text[word[0]:word[1]+1])
				if wordIdx == len(line)-1:
					break
				spaces = ' ' * (commonSpacing + int(remainingSpace > 0))
				remainingSpace -= 1
				justifiedLine.append(spaces)

			return ''.join(justifiedLine)		


	def justify(self, maxLineLength : int, text : str) -> str:
		(lines, totalWordsLength) = self.extractWords(maxLineLength, text)
		justifiedText = []
		for idx in range(len(lines) - 1):
			line = lines[idx]
			wordsLength = totalWordsLength[idx]
			spacedLine = self.createEvenlySpacedString(maxLineLength, line, wordsLength, text)
			justifiedText.append(spacedLine)

		justifiedText.append(' '.join([text[word[0]:(word[1]+1)] for word in lines[-1]]))

		return os.linesep.join(justifiedText)


a = TextFormatter()
op = a.justify(25, "This is some sample text, really just enough to generate a few lines in the output to show what the text justify function is supposed to do.")
#op = a.justify(25, "This is some sample text,")
print(op)




def justify(width, text):
    words = text.split()  # Split the text into words
    lines = []  # List to store justified lines
    current_line = []  # Temporary list to store words in the current line
    current_length = 0  # Current length of characters in the current line
    
    # Build lines
    for word in words:
        if current_length + len(word) + len(current_line) > width:
            # If adding this word would exceed the width, justify the current line
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)
        else:
            # Add the word to the current line
            current_line.append(word)
            current_length += len(word)

    # Add the last line
    lines.append(current_line)
    
    # Now, we need to justify each line
    justified_text = []
    for i, line in enumerate(lines):
        if len(line) == 1:  # For single word lines, no space needed
            justified_text.append(line[0].ljust(width))
        else:
            total_chars = sum(len(word) for word in line)  # Total length of words in the line
            total_spaces = width - total_chars  # Total spaces to distribute
            spaces_between_words = len(line) - 1  # Number of spaces to distribute
            if spaces_between_words > 0:
                even_space = total_spaces // spaces_between_words  # Even spaces
                extra_space = total_spaces % spaces_between_words  # Extra spaces to distribute
                
                # Join the words with appropriate spaces
                line_str = line[0]
                for j in range(1, len(line)):
                    space_to_add = even_space + (1 if j <= extra_space else 0)
                    line_str += ' ' * space_to_add + line[j]
                justified_text.append(line_str)
            else:
                # If only one word, just add the word with spaces at the end
                justified_text.append(line[0].ljust(width))

    # Join all the justified lines into the final text
    return '\n'.join(justified_text)

# Test the function with the provided text
text = "This is some sample text, really just enough to generate a few lines in the output to show what the text justify function is supposed to do."
justified_text = justify(25, text)
print(justified_text)

				
			
			
					
			
			
					














			