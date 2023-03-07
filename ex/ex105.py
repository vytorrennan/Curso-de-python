def grades(*students_grades, sit=False):
    """
    -> Function to analyze grades and situations of many students.
    :param students_grades: one or more student grades (accept several grades)
    :param sit: optional value, shows whether or not to add the situation
    :return: dictionary with a lot of information about the class
    """
    class_dict = dict()
    class_dict['Number of Grades'] = len(students_grades)
    class_dict['Greatest grade'] = max(students_grades)
    class_dict['Smallest grade'] = min(students_grades)
    class_dict['Average'] = sum(students_grades) / len(students_grades)
    if sit:
        if class_dict['Average'] >= 7:
            class_dict['Situation'] = 'GOOD'
        elif 6 <= class_dict['Average'] < 7:
            class_dict['Situation'] = 'OK'
        else:
            class_dict['Situation'] = 'BAD'
    return class_dict


a = [5.5, 9.5, 10, 6.5]
print(*a, sep=', ')
answer = grades(5.5, 9.5, 10, 6.5, sit=True)
print(answer)
