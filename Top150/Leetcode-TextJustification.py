from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        linesLen = [] 
        lineLength = 0
        currLine = []
        for i in range(len(words)):
            if lineLength + len(words[i]) <= maxWidth:
                currLine.append(words[i])
                lineLength += len(words[i]) + 1
            else:
                lines.append(currLine)
                linesLen.append(lineLength - len(currLine))
                currLine = [words[i]]
                lineLength = len(words[i]) + 1

        if lineLength != 0:
            lines.append(currLine)
            linesLen.append(lineLength- len(currLine))
        
        res = []
        for i in range(len(lines) - 1):
            currLine = ''
            line = lines[i]
            spaceCounter = maxWidth - linesLen[i]
            wordCount = len(lines[i])
            for j in range(len(line)):
                currLine += line[j]
                spaces = 0
                if wordCount > 1:
                    spaces = spaceCounter//(wordCount-1)
                    if spaceCounter % (wordCount - 1):
                        spaces += 1
                    spaceCounter -= spaces
                    wordCount -= 1
                elif wordCount == 1 and spaceCounter > 0:
                    spaces = spaceCounter
                currLine += ' ' * spaces
            
            res.append(currLine)
        
        currLine = ''
        line = lines[-1]
        spaceCounter = maxWidth - linesLen[-1]
        wordCount = len(lines[-1])
        for j in range(len(line)):
            currLine += line[j]
            spaces = 0
            if wordCount > 1:
                spaces = 1
                spaceCounter -= 1
            elif wordCount == 1 and spaceCounter > 0:
                spaces = spaceCounter
            wordCount -= 1
            currLine += ' ' * spaces
        res.append(currLine)
        return res

print(Solution.fullJustify(None,words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
print(Solution.fullJustify(None,words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))