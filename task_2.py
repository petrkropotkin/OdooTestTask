# Ваша програма має видати безперервну послідовність латинських літер в нижньому регістрі
#  довжиною 1 000 000 символів. Послідовність має відповідати вимогам:
# •	Кожна літера з'являється не частіше 40 000 раз в послідовності; 
from string import ascii_lowercase
letters = ascii_lowercase
end_letters = 1000000-len(letters*(1000000//26))
print(letters*(1000000//26)+ letters[:end_letters])

# •	Кожна можлива послідовність з двох букв зявляється не частіше 2 000; ???
# •	Кожна можлива послідовність з трьох букв з'являється не частіше 100; ???
