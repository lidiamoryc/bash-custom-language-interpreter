M Myrta/Moryc/Misiaczyńska \
A Again \
S \
H Shell 

# Opis programu
Program ten jest interpreterem języka mash, napisanego przy użyciu narzędzia ANTLR (Another Tool for Language Recognition). Język mash jest prostym językiem skryptowym, który pozwala na wykonywanie podstawowych operacji arytmetycznych, logicznych oraz manipulację zmiennymi. Dodatkowo, język ten wspiera struktury kontrolne, takie jak pętle (while, for) oraz instrukcje warunkowe (if, elif, else).

# Technologie
Program wykorzystuje następujące technologie i narzędzia:

- ANTLR (Another Tool for Language Recognition): Narzędzie do tworzenia parserów dla różnych języków programowania.
- Python: Główny język programowania używany do implementacji interpretera.
- ANTLR4 Runtime for Python: Biblioteka potrzebna do uruchomienia parsera wygenerowanego przez ANTLR w Pythonie.

# Pliki projektu
- mash.g4: Plik gramatyki dla języka mash w formacie ANTLR.
- mashLexer.py, mashParser.py, mashVisitor.py: Pliki wygenerowane przez ANTLR na podstawie pliku gramatyki mash.g4.
- mashVisitorCustom.py: Niestandardowy visitor, który implementuje logikę wykonywania kodu w języku mash.
- main.py: Główny plik uruchamiający interpreter.

# Struktura gramatyki
Gramatyka języka mash definiuje następujące elementy:

### Program
- **Opis**: Sekwencja instrukcji zakończona końcem pliku (EOF).
- **Definicja w gramatyce**: 
  ```antlr
  program : statement* EOF;
  ```
  
### Instrukcje
- **Opis**: Mogą być wywołaniami funkcji echo, deklaracjami zmiennych, przypisaniami wartości do zmiennych, oraz strukturami kontrolnymi (if, while, for).
- **Definicja w gramatyce**: 
  ```antlr
  statement : echo_function | var_declar | assignment | if_statement | while_statement | for_statement;
  ```

  ### Funkcja echo
- **Opis**: Wypisuje na standardowe wyjście wartość wyrażenia lub zmiennej.
- **Definicja w gramatyce**: 
  ```antlr
  echo_function : 'echo' (expression | IDENTIFIER);
  ```
- **Przykład użycia**:
  ```mash
  echo "Hello, World"
  ```

  ### Wyrażenia
- **Opis**: Arytmetyczne, logiczne, porównania, oraz identyfikatory.
- **Definicja w gramatyce**: 
  ```antlr
  expression : arithmetic_expression | string_expression | logical_expression | int_expression | IDENTIFIER;
  ```
- **Przykład użycia**:
  ```mash
  5 + 3
  "Hello" + " " + "World"
  ```

    ### Deklaracje zmiennych
- **Opis**:  Deklaracja zmiennych typu string_var lub int_var z opcjonalnym przypisaniem wartości.
- **Definicja w gramatyce**: 
  ```antlr
  var_declar : type IDENTIFIER ('=' (expression | IDENTIFIER))?;
  type : 'string_var' | 'int_var';
  ```
- **Przykład użycia**:
  ```mash
  int_var x = 5
  string_var name = "Mash"
  ```

### Przypisania
- **Opis**:  Przypisuje wartości do wcześniej zadeklarowanych zmiennych.
- **Definicja w gramatyce**: 
  ```antlr
  assignment : IDENTIFIER '=' (expression | IDENTIFIER);
  ```
- **Przykład użycia**:
  ```mash
  x = 10
  ```

### Pętle while
- **Opis**:  Wykonuje pętlę while.
- **Definicja w gramatyce**: 
  ```antlr
  while_statement : 'while' '(' logical_expression ')' '{' statement* '}';
  ```
- **Przykład użycia**:
  ```mash
  while (x > 0) { echo x x = x - 1 }
  ```

  ### Pętle for
- **Opis**:  Wykonuje pętlę for.
- **Definicja w gramatyce**: 
  ```antlr
  for_statement : 'for' '(' assignment ';' logical_expression ';' assignment ')' '{' statement* '}';
  ```
- **Przykład użycia**:
  ```mash
  for (int_var i = 0; i < 10; i = i + 1) { echo i }
  ```

    ### Intrukcje warunkowe
- **Opis**:  Instrukcje warunkowe if, elif, else.
- **Definicja w gramatyce**: 
  ```antlr
  if_statement : 'if' '(' logical_expression ')' '{' statement* '}' elif_block* else_block?;
  elif_block : 'elif' '(' logical_expression ')' '{' statement* '}';
  else_block : 'else' '{' statement* '}';
  ```
- **Przykład użycia**:
  ```mash
  if (x > 5) { echo "x is greater than 5" } 
  elif (x == 5) { echo "x is equal to 5" } 
  else { echo "x is less than 5" }
  ```

# Implementacja mashVisitorCustom
Klasa mashVisitorCustom jest implementacją visitora, który odwiedza węzły drzewa parsowania i wykonuje odpowiednie działania. Poniżej opisano niektóre z głównych metod:

- visitProgram: Przetwarza wszystkie instrukcje programu.
- visitEcho_function: Wykonuje funkcję echo, wypisując na standardowe wyjście wartość wyrażenia lub zmiennej.
- visitVar_declar: Deklaruje zmienne i przypisuje im wartości.
- visitAssignment: Przypisuje wartości do wcześniej zadeklarowanych zmiennych.
- visitIf_statement: Wykonuje instrukcję warunkową if-elif-else.
- visitWhile_statement: Wykonuje pętlę while.
- visitFor_statement: Wykonuje pętlę for.

# Przykładowe użycie
Poniżej przedstawiono przykładowy kod w języku mash oraz sposób jego przetworzenia przez interpreter.

Przykładowy kod w języku mash (zapisany w pliku test.mash):

'''
# Deklaracja i inicjalizacja zmiennych
int_var x = 10
int_var y = 5
string_var greeting = "Hello, Mash!"

# Wypisanie wartości zmiennych
echo "Initial values:"
echo x
echo y
echo greeting

# Instrukcja warunkowa
if (x > y) { 
  echo "x is greater than y" 
} 
elif (x == y) { 
  echo "x is equal to y" 
} 
else { 
  echo "x is less than y" 
}

# Pętla while
echo "Countdown from x to 0:"
while (x > 0) { 
  echo x 
  x = x - 1 
}

# Pętla for
echo "Counting from 0 to y:"
for (int_var i = 0; i < y; i = i + 1) { 
  echo i 
}

# Final message
echo "Script execution completed."
'''

# Instalacja i uruchomienie
Aby uruchomić interpreter, wykonaj poniższe kroki:

1. Zainstaluj ANTLR4:
'''
pip install antlr4-python3-runtime

2. Wygeneruj pliki parsera za pomocą ANTLR4:
'''
antlr4 -Dlanguage=Python3 mash.g4
'''

3. Uruchom interpreter:
'''
python main.py
'''

# Podsumowanie
Interpreter języka mash jest prostym narzędziem, które ilustruje użycie ANTLR do tworzenia parserów i interpreterów. Program obsługuje podstawowe operacje na zmiennych, wyrażenia arytmetyczne i logiczne, oraz struktury kontrolne, co pozwala na wykonywanie prostych skryptów.
