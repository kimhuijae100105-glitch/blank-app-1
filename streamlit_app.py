import random

# 이미지에서 추출한 단어 데이터 (N 01 ~ N 09 일부)
word_dict = {
    "속이 빈": "hollow",
    "강철": "steel",
    "가벼운": "light",
    "포함하다": "include",
    "무게": "weight",
    "튀다": "bounce",
    "적절히": "properly",
    "단단한 (고체)": "solid",
    "점토": "clay",
    "사고방식": "attitude",
    "나타나다": "emerge",
    "주장": "argument",
    "접근": "approach",
    "평범한": "ordinary",
    "세대": "generation",
    "단순함": "simplicity",
    "상호 작용하다": "interact",
    "분석하다": "analyze",
    "속이다": "fool",
    "맞서 싸우다": "combat",
    "위협": "threat",
    "진화": "evolution",
    "발생하다": "occur",
    "시력": "eyesight",
    "인과의": "causal",
    "관계": "relationship",
    "독립적인": "independent",
    "향상": "improvement",
    "의존적인": "dependent",
    "시도하다": "attempt",
    "배제하다": "rule out",
    "명백한": "apparent",
    "잡다": "grab",
    "반사하다": "reflect",
    "노출": "exposure",
    "환경": "environment",
    "~인 척하다": "pretend",
    "약속": "commitment",
    "요구 (요청)": "request",
    "놀라운": "astonishing",
    "승인하다": "approve",
    "존중": "respect",
    "재검토하다": "reexamine",
    "해석하다": "interpret",
    "방정식": "equation",
    "수소": "hydrogen",
    "원자": "atom",
    "산소": "oxygen",
    "화학": "chemistry",
}


def run_quiz():
    # 단어들을 무작위로 섞기 위해 리스트로 변환
    questions = list(word_dict.items())
    random.shuffle(questions)

    score = 0
    total = len(questions)

    print("====== 영단어 학습 퀴즈 프로그램을 시작합니다! ======")
    print("뜻을 보고 올바른 영단어를 입력하세요. (종료하려면 'q' 입력)\n")

    for i, (meaning, word) in enumerate(questions, 1):
        print(f"문제 {i}. [{meaning}]의 뜻을 가진 영단어는?")
        user_answer = input("정답 입력: ").strip().lower()

        if user_answer == 'q':
            print("\n퀴즈를 중도 종료합니다.")
            break

        if user_answer == word.lower():
            print("▶ 정답입니다! ✨\n")
            score += 1
        else:
            print(f"▶ 틀렸습니다. ❌ (정답: {word})\n")

    print("==================================================")
    print(f"퀴즈가 끝났습니다! 최종 점수: {score} / {i if user_answer == 'q' else total}")
    print("==================================================")


if __name__ == "__main__":
    run_quiz()
