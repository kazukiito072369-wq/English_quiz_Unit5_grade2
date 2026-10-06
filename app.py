import streamlit as st
import random

questions = [
    {"question": "Also, you must check the location of the ( ) shelters in advance.", "answer": "evacuation"},
    {"question": "( ) we can’t stay home, we can stay at schools or community centers.", "answer": "when"},
    {"question": "There are different types of natural ( ) in Japan.", "answer": "disasters"},
    {"question": "Well, we have ( ) bags.", "answer": "emergency"},
    {"question": "We have them, ( ).", "answer": "too"},

    {"question": "Please ( ) this area.", "answer": "stay away from"},
    {"question": "Don’t ( ) the house. It’s haunted.", "answer": "get into"},
    {"question": "Although the teacher asked the students to give their opinions ( ), John was kicked out of the group.", "answer": "in a group"},
    {"question": "When you pet someone else’s dog, you should ask for the owner’s permission ( ).", "answer": "in advance"},

    {"question": "Japan has many ( ) of natural disasters.", "answer": "types"},
    {"question": "In some cases, you don’t have to ( ).", "answer": "evacuate"},
    {"question": "It ( ) on your situation and location.", "answer": "depends"},
    {"question": "These ( ) can save lives.", "answer": "actions"},
    {"question": "When a disaster hits, we have to ( ) ourselves.", "answer": "protect"},

    {"question": "He ( ) the book all day.", "answer": "kept reading"},
    {"question": "I always ( ) to the pole when I see a dog walking.", "answer": "hold on"},
    {"question": "How long people sleep on average ( ) countries.", "answer": "depends on"},
    {"question": "I will tell you her secret ( ).", "answer": "if necessary"},
    {"question": "Please ( ) my dog while I’m on vacation.", "answer": "take care of"},

    {"question": "Oh, and don’t ( ) cat food for Felix.", "answer": "forget"},
    {"question": "Here’s a ( ) about preparing for natural disasters.", "answer": "pamphlet"},
    {"question": "It’s ( ) to prepare well for emergencies.", "answer": "important"},
    {"question": "OK, but I don’t think you have to ( ) them all.", "answer": "bring"},
    {"question": "It ( ) a checklist of things for the emergency bag.", "answer": "has"},

    {"question": "( ) do your homework.", "answer": "remember to"}
]

all_answers = list(set(q["answer"] for q in questions))

st.title("2年生 Unit 5 まとめ")

if "question_list" not in st.session_state:
    st.session_state.question_list = random.sample(
        questions,
        min(10, len(questions))
    )
    st.session_state.number = 0
    st.session_state.results = []
    st.session_state.finished = False
    st.session_state.show_results = False
    st.session_state.choices = {}

if st.session_state.finished:

    st.success("10問終了！")

    score = 0

    for result in st.session_state.results:
        if result["answer"] == result["correct"]:
            score += 1

    st.write(
        "あなたの得点は",
        score,
        "/",
        len(st.session_state.results)
    )

    if st.button("今回の結果を見る"):
        st.session_state.show_results = True
        st.rerun()

    if st.session_state.show_results:

        st.write("### 今回の問題と結果")

        for i, result in enumerate(st.session_state.results):

            st.write("第", i + 1, "問")
            st.write("問題:", result["question"])
            st.write("あなたの答え:", result["answer"])
            st.write("正解:", result["correct"])

            if result["answer"] == result["correct"]:
                st.success("○ 正解")
            else:
                st.error("× 不正解")

    if st.button("もう一度挑戦"):

        st.session_state.question_list = random.sample(
            questions,
            min(10, len(questions))
        )

        st.session_state.number = 0
        st.session_state.results = []
        st.session_state.finished = False
        st.session_state.show_results = False
        st.session_state.choices = {}

        st.rerun()

else:

    question_data = st.session_state.question_list[
        st.session_state.number
    ]

    question = question_data["question"]
    correct = question_data["answer"]

    st.write(
        "第",
        st.session_state.number + 1,
        "問"
    )

    st.write(question)

    if st.session_state.number not in st.session_state.choices:

        choices = [correct]

        while len(choices) < 4:

            choice = random.choice(all_answers)

            if choice not in choices:
                choices.append(choice)

        random.shuffle(choices)

        st.session_state.choices[
            st.session_state.number
        ] = choices

    choices = st.session_state.choices[
        st.session_state.number
    ]

    answer = st.radio(
        "正しい答えを選んでください",
        choices,
        key="choice_" + str(st.session_state.number)
    )

    if st.button("回答"):

        if answer == correct:
            st.success("正解！")
        else:
            st.error(
                "不正解。正解は " + correct
            )

        st.session_state.results.append({
            "question": question,
            "answer": answer,
            "correct": correct
        })

        if st.session_state.number < 9:

            st.session_state.number += 1
            st.rerun()

        else:

            st.session_state.finished = True
            st.rerun()