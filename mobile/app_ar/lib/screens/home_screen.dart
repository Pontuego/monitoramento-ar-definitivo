import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/location_service.dart';
import '../widgets/sensor_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Map<String, dynamic>? sensorData;
  bool loading = true;
  String? errorMessage;

  @override
  void initState() {
    super.initState();
    loadData();
  }

  Future<void> loadData() async {
    setState(() {
      loading = true;
      errorMessage = null;
    });

    try {
      final position = await LocationService.getCurrentPosition();
      final data = await ApiService.fetchSensorData(position.latitude, position.longitude);

      setState(() {
        sensorData = data;
        loading = false;
      });
    } catch (e) {
      setState(() {
        loading = false;
        errorMessage = 'Erro ao carregar dados: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Monitoramento de Ar"),
        centerTitle: true,
        backgroundColor: Colors.teal,
      ),
      body: Center(
        child: loading
            ? const CircularProgressIndicator()
            : errorMessage != null
                ? Text(errorMessage!)
                : ListView(
                    padding: const EdgeInsets.all(16),
                    children: [
                      SensorCard(
                        title: 'Temperatura',
                        value: '${sensorData?['temperature'] ?? '--'} °C',
                        icon: Icons.thermostat,
                      ),
                      SensorCard(
                        title: 'Umidade',
                        value: '${sensorData?['humidity'] ?? '--'} %',
                        icon: Icons.water_drop,
                      ),
                      SensorCard(
                        title: 'Qualidade do Ar',
                        value: '${sensorData?['air_quality'] ?? '--'} AQI',
                        icon: Icons.air,
                      ),
                      const SizedBox(height: 20),
                      ElevatedButton.icon(
                        onPressed: loadData,
                        icon: const Icon(Icons.refresh),
                        label: const Text('Atualizar Dados'),
                      ),
                    ],
                  ),
      ),
    );
  }
}