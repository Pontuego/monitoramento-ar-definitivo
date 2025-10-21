import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://172.22.115.174:5000';

  static Future<Map<String, dynamic>> fetchSensorData(double lat, double lon) async {
    final url = Uri.parse('$baseUrl/sensor_data?lat=$lat&lon=$lon');
    final response = await http.get(url);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Erro ao buscar dados do sensor: ${response.statusCode}');
    }
  }
}
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://172.22.115.174:5000';

  static Future<Map<String, dynamic>> fetchSensorData(double lat, double lon) async {
    final url = Uri.parse('$baseUrl/sensor_data?lat=$lat&lon=$lon');
    final response = await http.get(url);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Erro ao buscar dados do sensor: ${response.statusCode}');
    }
  }
}