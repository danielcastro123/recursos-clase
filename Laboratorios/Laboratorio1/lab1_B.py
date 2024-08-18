# Nombre:Daniel Esteban Castro Calderin
# Grupo: 302
# Cod Estudiante: 202310422

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Cree un algoritmo que encuentre si un número es par o impar.
# Calcula el contador de frecuencias y orden de magnitud

# INICIO SOLUCIÓN
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

using namespace std;

int main() {

int ordenMagnitud(int N) {
    return to_string(abs(N)).length();
}
 unordered_map<int, int> frecuencias;
    vector<int> N;

  int N;
cout << "ingrese un numero: ";
cin >> N;

if (N % 2 == 0) {
  cout << "el numero" << N << " es par";
} 
else { 
  cout << "el numero" << N << "es impar";
}

# FIN SOLUCIÓN
    while (cin >> N) {
        numeros.push_back(N);
        frecuencias[N]++;
    }

    cout << "Frecuencias de los números:";
    for (const auto& par : frecuencias) {
        int num = par.first;
        int freq = par.second;
        cout << "El número " << num << " aparece " << freq << " vez/veces.";
    }

    cout << "Orden de magnitud de los números:";
    for (const auto& num : numeros) {
        cout << "El número " << num << " tiene un orden de magnitud de " << ordenMagnitud(num) << " (cantidad de dígitos).";
    }
######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# Cree un algoritmo que encuentre el factorial de un número
# Calcula el contador de frecuencias y orden de magnitud

# INICIO SOLUCIÓN
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

using namespace std;

int main() {

  int ordenMagnitud(int numero) {
    return to_string(abs(numero)).length();
}
    unordered_map<int, int> frecuencias;
    vector<int> numero;
    int numero;

    cout << "Ingrese un número entero no negativo: ";
    cin >> numero;

    if (numero < 0) {
        cout << "El factorial no está definido para números negativos.";
    } else {
        unsigned long long resultado = factorial(numero);
        cout << "El factorial de " << numero << " es " << resultado <<;
    }
# FIN SOLUCIÓN
    while (cin >> numero) {
        numeros.push_back(numero);
        frecuencias[numero]++;
    }

    cout << "Frecuencias de los números:";
    for (const auto& par : frecuencias) {
        int num = par.first;
        int freq = par.second;
        cout << "El número " << num << " aparece " << freq << " vez/veces.";
    }

    cout << "Orden de magnitud de los números:";
    for (const auto& num : numeros) {
        cout << "El número " << num << " tiene un orden de magnitud de " << ordenMagnitud(num) << " (cantidad de dígitos).";
    }
######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Cree un algoritmo que encuentre si una matriz es identidad.
# Calcula el contador de frecuencias y orden de magnitud

# INICIO SOLUCIÓN
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

using namespace std;

const int TM = 100;

bool esMatrizIdentidad(int matriz[TM][TM], int tamaño) {
    for (int i = 0; i < tamaño; ++i) {
        for (int j = 0; j < tamaño; ++j) {
            if (i == j) {
                if (matriz[i][j] != 1) {
                    return false;
                }
            } else {
                // Elementos fuera de la diagonal principal deben ser 0
                if (matriz[i][j] != 0) {
                    return false;
                }
            }
        }
    }
    return true;
}
int ordenMagnitud(int T) {
    return to_string(abs(T)).length();
}

int main() {
    unordered_map<int, int> frecuencias;
    vector<int> T;
    int T;
    int matriz[TM][TM];

    cout << "Ingrese el tamaño de la matriz cuadrada: ";
    cin >> T;

    cout << "Ingrese los elementos de la matriz:";
    for (int i = 0; i < T; ++i) {
        for (int j = 0; j < T; ++j) {
            cin >> matriz[i][j];
        }
    }

    if (esMatrizIdentidad(matriz, T)) {
        cout << "La matriz es una matriz identidad.";
    } else {
        cout << "La matriz no es una matriz identidad.";
    }
# FIN SOLUCIÓN
    while (cin >> T) {
        numeros.push_back(T);
        frecuencias[T]++;
    }

    cout << "Frecuencias de los números:";
    for (const auto& par : frecuencias) {
        int num = par.first;
        int freq = par.second;
        cout << "El número " << num << " aparece " << freq << " vez/veces.";
    }

    cout << "Orden de magnitud de los números:";
    for (const auto& num : numeros) {
        cout << "El número " << num << " tiene un orden de magnitud de " << ordenMagnitud(num) << " (cantidad de dígitos).";
    }
######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Cree un algoritmo que divida un número entre otro haciendo restas sucesivas.
# Calcula el contador de frecuencias y orden de magnitud

#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

using namespace std;

int ordenMagnitud(int numero) {
    return to_string(abs(numero)).length();
}

int main() {
    unordered_map<int, int> frecuencias;
    vector<int> numeros;

    int dividendo, divisor;
    int cociente = 0;
    int residuo;

    cout << "Ingrese el dividendo: ";
    cin >> dividendo;

    cout << "Ingrese el divisor: ";
    cin >> divisor;

    if (divisor == 0) {
        cout << "Error: División por cero no permitida.";
        return 1;
    }

    residuo = dividendo;

# FIN SOLUCIÓN
     while (residuo >= divisor) {
        residuo -= divisor;
        ++cociente;
    }

    numeros.push_back(cociente);
    numeros.push_back(residuo);

    frecuencias[cociente]++;
    frecuencias[residuo]++;

    cout << "Cociente: " << cociente <<;
    cout << "Residuo: " << residuo <<;

    cout << "Frecuencias y orden de magnitud de los números:";
    for (const auto& numero : numeros) {
        cout << "Número: " << numero 
             << ", Frecuencia: " << frecuencias[numero] 
             << ", Orden de magnitud: " << ordenMagnitud(numero);
    }

######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Cree un algoritmo que determine si una cadena de texto es palindroma.
# Calcula el contador de frecuencias y orden de magnitud

# INICIO SOLUCIÓN
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <string>
#include <cctype>

using namespace std;

int ordenMagnitud(int n) {
    return to_string(abs(n)).length();

}
bool esPalindromo(const string& cadena) {
    int inicio = 0;
    int fin = cadena.length() - 1;

    while (inicio < fin) {
        while (inicio < fin && !isalnum(cadena[inicio])) {
            ++inicio;
        }
        while (inicio < fin && !isalnum(cadena[fin])) {
            --fin;
        }

        if (tolower(cadena[inicio]) != tolower(cadena[fin])) {
            return false;
        }

        ++inicio;
        --fin;
    }
    return true;
}

int main() {
    string cadena;

    cout << "Ingrese una cadena de texto: ";
    getline(cin, cadena);

    if (esPalindromo(cadena)) {
        cout << "La cadena es un palíndromo.";
    } else {
        cout << "La cadena no es un palíndromo.";
    }
# FIN SOLUCIÓN
void extraerNumeros(const string& cadena, unordered_map<int, int>& frecuencias) {
    string numeroStr;
    for (char c : cadena) {
        if (isdigit(c)) {
            numeroStr += c;
        } else if (!numeroStr.empty()) {
            int numero = stoi(numeroStr);
            frecuencias[numero]++;
            numeroStr.clear();
        }
    }
    if (!numeroStr.empty()) {
        int numero = stoi(numeroStr);
        frecuencias[numero]++;
    }
}

int main() {
    string cadena;
    unordered_map<int, int> frecuencias;

    cout << "Ingrese una cadena de texto: ";
    getline(cin, cadena);

    extraerNumeros(cadena, frecuencias);

    cout << "Frecuencias de los números:";
    for (const auto& par : frecuencias) {
        int numero = par.first;
        int freq = par.second;
        cout << "El número " << numero << " aparece " << freq << " vez/veces. Tiene un orden de magnitud de " << ordenMagnitud(numero) << " (cantidad de dígitos).";
    }
######################################
#                                    #
#             Punto #6               #
#                                    #
######################################

# Cree un algoritmo que encuentre los valores máximo y mínimo de un arreglo.
# Calcula el contador de frecuencias y orden de magnitud

# INICIO SOLUCIÓN

#include <iostream>
#include <climits>
#include <unordered_map>
#include <cmath>
#include <vector>
using namespace std;

int ordenMagnitud(int numero) {
    return to_string(abs(numero)).length();
}

int main() {
    const int TAMANIO = 10;
    int arreglo[TAMANIO];
    unordered_map<int, int> frecuencias;
    vector<int> numeros;
    int maximo = INT_MIN;
    int minimo = INT_MAX;

    cout << "Ingrese " << TAMANIO << " números enteros:";
    for (int i = 0; i < TAMANIO; ++i) {
        cin >> arreglo[i];
    }

    for (int i = 0; i < TAMANIO; ++i) {
        if (arreglo[i] > maximo) {
            maximo = arreglo[i];
        }
        if (arreglo[i] < minimo) {
            minimo = arreglo[i];
        }
    }

    cout << "Valor máximo: " << maximo;
    cout << "Valor mínimo: " << minimo;

# FIN SOLUCIÓN
for (int i = 0; i < TAMANIO; ++i) {
        frecuencias[arreglo[i]]++;
        if (find(numeros.begin(), numeros.end(), arreglo[i]) == numeros.end()) {
            numeros.push_back(arreglo[i]);
        }
    }

    cout << "Frecuencias y orden de magnitud de los números:";
    for (int numero : numeros) {
        cout << "Número: " << numero 
             << ", Frecuencia: " << frecuencias[numero] 
             << ", Orden de magnitud: " << ordenMagnitud(numero);
    }
######################################
#                                    #
#             Punto #7               #
#                                    #
######################################

# Cree un algoritmo que encuentre la potencia de un número haciendo multiplicaciones sucesivas.
# Calcula el contador de frecuencias y orden de magnitud

# INICIO SOLUCIÓN
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int ordenMagnitud(int numero) {
    return to_string(abs(numero)).length();
}

int potencia(int base, int exponente) {
    int resultado = 1;

    for (int i = 0; i < exponente; ++i) {
        resultado *= base;
    }

    return resultado;
}

int main() {
    int base, exponente;

    cout << "Ingrese la base: ";
    cin >> base;

    cout << "Ingrese el exponente: ";
    cin >> exponente;

    if (exponente < 0) {
        cout << "El exponente no puede ser negativo.";
        return 1;
    }

    int resultado = potencia(base, exponente);

    cout << "El resultado de " << base << " elevado a la " << exponente << " es: " << resultado;
# FIN SOLUCIÓN
unordered_map<int, int> frecuencias;
    frecuencias[resultado]++;

    int magnitud = ordenMagnitud(resultado);

    cout << "Resultado de " << base << " elevado a la " << exponente << " es: " << resultado;
    cout << "Frecuencia del resultado: " << frecuencias[resultado];
    cout << "Orden de magnitud del resultado: " << magnitud;
