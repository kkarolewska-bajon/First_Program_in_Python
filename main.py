input('Zapraszam Cię do porównania imienia i wieku z koleżanką :) ')
input('Jesteś gotowa? Zaczynamy!')
a=input('Twoje imię :')
c=input('Twój wiek :')
b=input('Imię koleżanki :')
d=input('Wiek koleżanki :')
input('Porównajmy najpierw wasze imiona:')
input('Podam teraz liczbę liter w waszych imioniach')
r='2020'
imie=[a,b]
for l in imie:
  print(l,'=', len(l))
input('Jeśli zastanawiałaś się czyje imię jest dłuższe teraz możesz się przekonać:')
if len(a)>len(b):
  print('Twoję imię',a, 'jest dłuższe =',len(a), 'liter')
elif len(b)>len(a):
  print('Imię Twojej koleżanki',b, 'jest dłuższe =',len(b), 'liter')
else:
  print('Wspólnie macie tą samą długość imienia')
ra=float(r)-float(c)
rb=float(r)-float(d)
razem=float(c)+float(d)
input('Pozwól, że obliczę Twój i koleżanki rok urodzenia:')
print(a,'urodziłaś się w roku :',int(ra))
print(b, 'urodziłaś się w roku :', int(rb))
input('W ilości siła, zobacz ile lat razem przeżyłyście:')
print('Razem macie ',int(razem),'lat')
print(a,'jesteś starsza czy młodsza od koleżanki?')
if float(c)>float(d):
  print('Jesteś starsza')
elif float(d)>float(c):
  print('Jesteś młodsza')
elif float(c)==float(d):
  print('Jesteście w tym samym wieku')
input('To już koniec na dziś, mam nadzieję, że się podobało.')
input('Do zobaczenia!')