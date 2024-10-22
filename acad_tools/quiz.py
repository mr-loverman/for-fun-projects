import random

def readLine(subj, topic, quiz=False):
  if quiz is True:
    with open(f"C://Users//Jj//Documents//quiz questions//{subj}_{topic}.txt", "r") as f:
      quizDict = {}
      lines = f.readlines()
      index = 0

      for line in lines:
        question, answer = line.split(":")
        index+=1
        quizDict[index] = {question:answer}
        
    return quizDict, index
  else:
    with open(f"C://Users//Jj//Documents//quiz questions//{subj}_{topic}.txt", "r") as f:
      lines = f.readlines()
    
    return lines

def deleteLine(subj, topic, index):
  with open(f"C://Users//Jj//Documents//quiz questions//{subj}_{topic}.txt", "r+") as f:
    lines = f.readlines()
    del lines[index - 1]
    f.seek(0)
    f.writelines(lines)
    f.truncate()

def appendFile(subj, topic, question, answer):
  with open(f"C://Users//Jj//Documents//quiz questions//{subj}_{topic}.txt", "a") as f:
    f.write(f"{question}:{answer}\n")

def quiz():
  subj = input("What is the subject of the quiz: ")
  topic = input("What is the topic: ")

  while True:
    print("\nWhat do you want to do?\n1. Add questions\n2. Delete questions\n3. Take Quiz\n4. Quit")
    choice = input("Choice: ")
    print()

    match choice:
      case "1":
        question = input("Type the question: ")
        answer = input("Type the answer: ")

        appendFile(subj, topic, question, answer)
      case "2":
        lines = readLine(subj, topic) 
        i = 1

        for line in lines:
          print(f"{i}. {line}")
          i+=1

        index = int(input("\nWhat line do you want to delete: "))

        deleteLine(subj, topic, index)
        print()
        i = 0
      case "3":
        quizDict, index = readLine(subj, topic, quiz=True)
        order = random.sample(range(1, index + 1), index)
        wrong_counter = []
        score = 0
        index2 = 1

        for i in order:
          index_question = quizDict[i]
          
          for question, answer in index_question.items():
            answer = answer.strip("\n")
            print(f"{index2}. {question}")
            ans = input("Answer: ")
            print()
            
            if ans == answer:
              score+=1
              wrong_counter.append(f"{index2}. Correct")
            else:
              wrong_counter.append(f"{index2}. {answer}")

            index2 += 1

        print(f"\nscore: {score}\n")
        print("Correct answers: ")
        for i in wrong_counter:
          print(i)
        
        print()
        score = 0
        index2 = 0
      case "4":
        break
      case _: 
        print("Invalid choice")

if __name__=='__main__':
  quiz()

        



