class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sent = sentence.split(" ")
        for i in range(len(sent)):
            temp=""
            for j in sent[i]:
                temp+=j
                if temp in dictionary:
                    sent[i]=temp
                    break
        return " ".join(sent)