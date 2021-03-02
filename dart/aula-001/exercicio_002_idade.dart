import 'dart:io';

// Pergunta a idade da pessoa
// Se a pessoa for maior ou igual a 18
//    ele é maior de idade
// Se a pessoa for menor que 18
//    ele não é maior de idade

main() {
  print("Digite sua idade ---------");

  var input = stdin.readLineSync();
  var idade = int.parse(input);

  if (idade >= 65) {
    print("Uma pessoa com ${idade} anos é idoso");
  } else if (idade >= 18) {
    print("Uma pessoa com ${idade} anos é adulta");
  } else if (idade >= 12) {
    print("Uma pessoa com ${idade} anos é adolescente");
  } else {
    print("Com ${idade} anos ainda é uma criança");
  }
}
