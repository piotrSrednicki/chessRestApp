# REST Chess solver

Projekt polega na utworzeniu prostej aplikacji REST wspomagającej grę w szachy.

## Informacje wstępne

* Python 3.6 - 3.8
* Black (formatowanie)
* Flake8 (linter)
* Pytest (testy)
* Flask 1.0+
* SQLAlchemy (jeśli potrzeba)
* Dozwolone jest używanie zewnętrznych bibliotek

## Opis zadania

W pierwszej kolejności utwórz klasę abstrakcyjną `Figure`, która posiada:

- konstruktor, przyjmujący jako pierwszy parametr, pole na którym znajduje się figura
- metodę publiczną `list_available_moves()`, wypisującą dozwolone ruchy
- metodę publiczną `validate_move(dest_field)`, informującą, czy możliwy jest ruch na wskazane pole.

Następnie utwórz 6 klas reprezentujących dane figury szachowe ( lista figur: https://en.wikipedia.org/wiki/Chess_piece ). 

Następnym krokiem jest implementacja algorytmów poruszania się po polu szachowym przez dane figury. Możliwe kombinacje ruchów dostępne są tutaj: https://www.ichess.net/blog/chess-pieces-moves/. 

> **WAŻNE**: W obu metodach uwzględniamy tylko sekwencje poruszania, bez sekwencji bicia. Wynikiem metody `list_available_moves` powinna być lista pól, na które określona figura znajdująca się na wskazanym polu szachownicy może się poruszyć, zgodnie z zasadami gry. 

Szachownicę należy stworzyć zgodnie z zasadami, zachowując wszystkie pola ( https://pl.wikipedia.org/wiki/Szachownica ).

Kolejnym krokiem jest stworzenie warstwy API wystawiającej poniżej podane url (w nawiasach kwadratowych zostały podane metody wywołania):

#### [GET] `/api/v1/{chess-figure}/{current-field}` (wyświetla listę możliwych ruchów)

Na wybranym obiekcie jednej z 6 klas wywoływana jest metoda `list_available_moves`, która bazując na podanym polu np. h5 zwraca listę możliwych pozycji, na które można przesunąć figurę.

Przykładowe zapytanie:
`curl http://localhost:8000/api/v1/rook/h2`

Przykładowa odpowiedź:

```json
{
   "availableMoves":[
      "H3"
   ],
   "error": null,
   "figure":"rook",
   "currentField":"H2"
}
```

Przykładowe zapytanie:
`curl http://localhost:8000/api/v1/rook/h15`

Przykładowa odpowiedź:

```json
{
   "availableMoves":[],
   "error": "Field does not exist.",
   "figure":"rook",
   "currentField":"H15"
}
```

####  [GET] `/api/v1/{chess-figure}/{current-field}/{dest-field}` (waliduje czy ruch na wskazane pole jest poprawny)

Na wybranym obiekcie jednej z 6 klas wywoływana jest metoda `validate_move`, która bazując na podanym polu bieżącym, sprawdza czy możemy przesunąć figurę na wskazane w dest-field pole.

Przykładowe zapytanie:
`curl http://localhost:8000/api/v1/rook/h2/h3`

Przykładowa odpowiedź:

```json
{
   "move":"valid",
   "figure":"rook",
   "error": null,
   "currentField":"H2",
   "destField":"H3"
}
```

Przykładowe zapytanie:
`curl http://localhost:8000/api/v1/rook/h2/h1`

Przykładowa odpowiedź:

```json
{
   "move":"invalid",
   "figure":"rook",
   "error": "Current move is not permitted.",
   "currentField":"H2",
   "destField":"H3"
}
```

### Na co zwracać uwagę:
- kod powinien posiadać README.md z prostą instrukcją umożwiającą uruchomienie aplikacji
- każda odpowiedź serwera musi mieć poprawny response code:
    - 200 (jeśli wszystko jest ok)
    - 409 (w przypadku złego pola)
    - 404 (jeśli odpytamy o nieistniejącą figurę)
    - 500 (w przypadku błędu serwera)
- aplikacja powinna posiadać podstawowe testy jednostkowe
- kod powinien być sformatowany z wykorzystaniem Black
- kod powinien być sprawdzony linterem flake8
- kod powinien zostać stworzony zgodnie z dobrymi praktykami, w szczególności dotyczącymi bezpieczeństwa, niezawodności i czytelności

## Jak oddać zadanie

1. Gotowe repozytorium pakujemy komendą: `git bundle create IMIĘ_NAZWISKO.bundle --all`. Proszę pamiętać aby wszelkie zmiany były za-commitowane (!)
2. Paczkę .bundle wysyłamy jako załącznik na mój email.

## Przydatne linki

1. https://httpstatuses.com/
2. https://flask.palletsprojects.com/en/1.1.x/testing/
3. https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

Plusem będzie zastosowanie Static Typing oraz Dockera.

W razie pytań, proszę o kontakt.