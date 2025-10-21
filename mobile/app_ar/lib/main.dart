import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const AppAr());
}

class AppAr extends StatelessWidget {
  const AppAr({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Monitoramento de Ar',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal),
        useMaterial3: true,
      ),
      debugShowCheckedModeBanner: false,
      home: const HomeScreen(),
    );
  }
}