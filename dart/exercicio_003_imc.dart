import 'dart:io';

main() {
  calculoIMC();
}

calculoIMC() {
  print("Digite seu peso: ");
  var inputPeso = stdin.readLineSync();
  double peso = double.parse(inputPeso);

  print("Digite sua altura: ");
  String inputAltura = stdin.readLineSync();
  double altura = double.parse(inputAltura);

  double imc = calcIMC(peso, altura);

  imprimirResultado(imc);
}

double calcIMC(double peso, double altura) {
  return peso / (altura * altura);
}

imprimirResultado(double imc) {
  print('================');

  if (imc < 18.5) {
    print("Abaixo do Peso");
  } else if (imc > 18.5 && imc < 24.9) {
    print("Peso Normal");
  } else if (imc > 25 && imc < 29.9) {
    print("Sobrepeso");
  } else if (imc > 30 && imc < 34.9) {
    print("Obesidade Grai I");
  } else if (imc > 35 && imc < 39.9) {
    print("Obesidade Grau II");
  } else {
    print("Obesidade Grau III");
  }
}
