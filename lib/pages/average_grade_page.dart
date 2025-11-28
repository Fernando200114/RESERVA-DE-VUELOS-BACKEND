import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class AverageGradePage extends StatefulWidget {
  const AverageGradePage({super.key});

  @override
  State<AverageGradePage> createState() => _AverageGradePageState();
}

class _AverageGradePageState extends State<AverageGradePage> {
  String n1Text = '';
  String n2Text = '';
 
  String resultText = '';

  void calculateAverage() {
  final total = double.tryParse(n1Text.replaceAll(',', '.')) ?? 0.0;
  final cantidad = double.tryParse(n2Text.replaceAll(',', '.')) ?? 0.0;

  final promedio = cantidad > 0 ? total / cantidad : 0.0;

  setState(() {
    resultText =
      'Total: ${total.toStringAsFixed(2)}\n'
      'Cantidad de vuelos: ${cantidad.toStringAsFixed(0)}\n'
      'Promedio: ${promedio.toStringAsFixed(2)}';
  });
}


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Promedio de vuelos'),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () => context.go('/'),
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Text(
                'Calcular promedio de vuelos',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 16),

              TextField(
                decoration: const InputDecoration(
                  labelText: 'total',
                  border: OutlineInputBorder(),
                ),
                keyboardType: TextInputType.number,
                onChanged: (value) {
                  n1Text = value;
                },
              ),

              const SizedBox(height: 16),

              TextField(
                decoration: const InputDecoration(
                  labelText: 'Cantidad de vuelos',
                  border: OutlineInputBorder(),
                ),
                keyboardType: TextInputType.number,
                onChanged: (value) {
                  n2Text = value;
                },
              ),

              const SizedBox(height: 16),

    

              const SizedBox(height: 16),
              ElevatedButton(
                onPressed: calculateAverage,
                child: const Text('Calcular'),
              ),

              const SizedBox(height: 16),
              Text(resultText),
            ],
          ),
        ),
      ),
    );
  }
}
