import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // URL do ngrok
  static const String baseUrl = 'https://0c3476319a2d.ngrok-free.app';

  static Future<Map<String, dynamic>> fetchSensorData(double lat, double lon) async {
    final url = Uri.parse('$baseUrl/qualidade-ar?lat=$lat&lon=$lon');
    final response = await http.get(url);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Erro ao buscar dados do sensor: ${response.statusCode}');
    }
  }
}