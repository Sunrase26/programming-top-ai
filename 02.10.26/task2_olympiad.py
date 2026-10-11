def check_winners(scores, student_score):
    scores.sort(reverse=True)
    top_3 = scores[:3]
    if student_score in top_3:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

# Проверка
scores_list = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
check_winners(scores_list, 51)
check_winners(scores_list, 20)