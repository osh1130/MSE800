**Activity 1:**
- Create a NumPy array of the first 10 positive integers. np.arange(1, 11)
- Print the array, its size, and data type of each element. arr.dtype
- Multiply each element by 2 and print the result. arr * 2

**Activity 2:**
- Analyze a 2D array representing test scores of 5 students in 3 subjects.
- Calculate and print:
  - Average score for each student. np.mean(scores, axis=1)
  - Average score for each subject. np.mean(scores, axis=0)
  - The student with the highest total score. np.sum(scores, axis=1), np.argmax(total_scores)
  - Bonus: Add 5 points to the third subject for all students. scores[:, 2] += 5