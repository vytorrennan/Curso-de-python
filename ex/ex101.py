def vote(birth):
    print('-' * 27)
    from datetime import datetime
    age = datetime.today().year - birth
    if 65 > age >= 18:
        return f'with {age} years old: MANDATORY VOTE'
    elif age >= 65 or 18 > age >= 16:
        return f'with {age} years old: OPTIONAL VOTE'
    elif age < 16:
        return f'with {age} years old: DON\'T VOTE'


birthYear = int(input('What year were you born? '))
print(vote(birthYear))
