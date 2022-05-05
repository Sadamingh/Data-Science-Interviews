# Find the course overlap of two students
# Sample Input:
#
# student_course_pairs_1 = [
#   ["58", "Software Design"],
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["17", "Software Design"],
#   ["58", "Mechanics"],
#   ["58", "Economics"],
#   ["17", "Linear Algebra"],
#   ["17", "Political Science"],
#   ["94", "Economics"],
#   ["25", "Economics"],
# ]
#
# Sample Output (pseudocode, in any order):
#
# find_pairs(student_course_pairs_1) =>
# {
#   [58, 17]: ["Software Design", "Linear Algebra"]
#   [58, 94]: ["Economics"]
#   [58, 25]: ["Economics"]
#   [94, 25]: ["Economics"]
#   [17, 94]: []
#   [17, 25]: []
# }
#
# Additional test cases:
#
# Sample Input:
#
# student_course_pairs_2 = [
#   ["42", "Software Design"],
#   ["0", "Advanced Mechanics"],
#   ["9", "Art History"],
# ]
#
# Sample output:
#
# find_pairs(student_course_pairs_2) =>
# {
#   [0, 42]: []
#   [0, 9]: []
#   [9, 42]: []
# }
