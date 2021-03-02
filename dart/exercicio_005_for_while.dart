main() {

  for (int x = 0; x < 10; x++) {
    print("Número $x");
  }

//..............

  bool condicao = true;
  int x = 0;

  while (condicao) {
    print("Número $x");
    x++;
    if (x > 9) {
      condicao = false;
    }    
  }
}
