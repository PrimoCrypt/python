def find_anagram(word, anagram):

    if(sorted(word)== sorted(anagram)):
        answer=True
    else:
        answer=False
    return answer
word=input("Enter first word: ")
anagram=input("Enter Second word: ")
answer=find_anagram(word,anagram)
print(answer)
print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))