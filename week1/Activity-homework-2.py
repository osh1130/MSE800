import numpy as np

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

student_avg = np.mean(scores, axis=1)
print("Average score for each student:", student_avg)


subject_avg = np.mean(scores, axis=0)
print("Average score for each subject:", subject_avg)

total_scores = np.sum(scores, axis=1)
top_student_index = np.argmax(total_scores)
print("Student (row index) with the highest total score:", top_student_index)


scores[:, 2] += 5
print("Add 5 bonus points to the third subject for all students:\n", scores)