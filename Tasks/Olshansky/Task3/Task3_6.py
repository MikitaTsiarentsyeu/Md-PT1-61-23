# Subtask 3_6
# 6. Write a program that takes a string as input and returns the string with all vowels removed.

users_text = 'Римский император Константин I Великий по достоинству оценил выгодное местоположение приморского ' \
             'Византия, расположенного на стыке Европы и Азии. Кроме того, на решение Константина повлияла неспокойная ' \
             'обстановка в самом Риме: недовольство знати и постоянные распри в борьбе за трон. Император хотел ' \
             'увенчать свою реформаторскую деятельность созданием нового административного центра огромной державы. ' \
             'Закладка города состоялась осенью 324 года, и Константин лично решил обозначить его границы.'
users_text = users_text.lower()
users_text = users_text.replace('ы', '').replace('а', '').replace('о', '').replace('э', '').replace('ё', '').replace(
    'у', '').replace('е', '').replace('я', '').replace('и', '').replace('ю', '')
print(users_text)
