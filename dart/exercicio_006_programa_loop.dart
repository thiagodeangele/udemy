import 'dart:io';
main() {
  bool condicao = true;

  while (condicao) {
    print("Escreva um texto ======");
    var text = stdin.readLineSync();
    if (text == 'sair') {
      condicao = false;
      print("=== Finalizado ===");
    } else {
      print("Você digitou $text");
    }
  }
}
