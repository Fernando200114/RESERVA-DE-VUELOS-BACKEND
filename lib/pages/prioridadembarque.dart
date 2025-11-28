import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    home: PrioridadEmbarquePage(),
    debugShowCheckedModeBanner: false,
  ));
}

class PrioridadEmbarquePage extends StatefulWidget {
  const PrioridadEmbarquePage({super.key});

  @override
  State<PrioridadEmbarquePage> createState() => _PrioridadEmbarquePageState();
}

class _PrioridadEmbarquePageState extends State<PrioridadEmbarquePage> {
  String? tipoPasajero;
  String? claseBoleto;
  String prioridad = "";

  final List<String> tiposPasajero = [
    "adulto ",
    "familia ",
    "pasajero regular"
  ];

  final List<String> clasesBoleto = [
    "economica",
    "ejecutiva",
  ];

  void calcularPrioridad() {
    String resultado = "baja"; 

    
    if (tipoPasajero == "adulto mayor" || claseBoleto == "ejecutiva") {
      resultado = "lta";
    } else if (tipoPasajero == "Familia con niños") {
      resultado = "Media";
    }

    setState(() {
      prioridad = resultado;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Prioridad de Embarque")),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text("Tipo de pasajero:"),
            DropdownButton<String>(
              value: tipoPasajero,
              hint: const Text("Seleccione tipo de pasajero"),
              items: tiposPasajero.map((String valor) {
                return DropdownMenuItem(
                  value: valor,
                  child: Text(valor),
                );
              }).toList(),
              onChanged: (val) {
                setState(() {
                  tipoPasajero = val;
                });
              },
            ),
            const SizedBox(height: 20),

            const Text("Clase de boleto:"),
            DropdownButton<String>(
              value: claseBoleto,
              hint: const Text("Seleccione clase"),
              items: clasesBoleto.map((String valor) {
                return DropdownMenuItem(
                  value: valor,
                  child: Text(valor),
                );
              }).toList(),
              onChanged: (val) {
                setState(() {
                  claseBoleto = val;
                });
              },
            ),

            const SizedBox(height: 30),

            ElevatedButton(
              onPressed: () {
                if (tipoPasajero != null && claseBoleto != null) {
                  calcularPrioridad();
                } else {
                  setState(() {
                    prioridad = "Por favor completa ambos campos.";
                  });
                }
              },
              child: const Text("Calcular prioridad"),
            ),

            const SizedBox(height: 30),

            Text(
              prioridad.isEmpty
                  ? "prioridad"
                  : "Prioridad asignada: $prioridad",
              style: const TextStyle(fontSize: 20),
            ),
          ],
        ),
      ),
    );
  }
}
