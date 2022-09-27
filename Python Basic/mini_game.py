# Hangman mini game

# 기본 program
import time, csv, random, winsound

# 처음인사
name = input("What is your name?")

print("Hi, " + name, "Time to play hangman game!")
print()
time.sleep(1)

print("Start Loading..........")
print()
time.sleep(0.5)

# CSV 단어 리스트
words = []
# CSV 단어 리스트
with open('Python Basic\\resource\\word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)
q = random.choice(words)

# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심알고리즘코드!!! - while loop
# 기회 카운트가 남아 있을 경우
while turns > 0:
    # 실패횟수(단어 매치 수)
    failed = 0

    # 정답단어 반복
    for char in word:
        # 정답단어내에 추측문자가 있을경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
        else:
            # 틀린경우 underscore로 표시
            print("_", end=' ')
            failed += 1

    # 단어 추측 성공 경우
    if failed == 0:
        print()
        print()
        # 성공 사운드
        winsound.PlaySound('Python Basic\\sound\\good.wav', winsound.SND_FILENAME)
        print("Conguratulations! The Guesses is correct")
        break
    print()

    # 추측단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a character")

    # 단어 더하기
    guesses += guess

    # 정답단어에 추측한 문자 포함되 있지 않으면
    if guess not in word:
        turns -= 1
        # 오류 메시지
        print("Ooops! Wrong!")
        #남은 기회 출력
        print("You have", turns, "more guesses!")

    if turns == 0:
        # 실패 메시지
        winsound.PlaySound('Python Basic\\sound\\bad.wav', winsound.SND_FILENAME)
        print("You have failed! Good Bye!")


