import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  static const platform = const MethodChannel('es.kungfusoftware.tfg/battery');
  String _batteryLevel = 'Pulse el boton de abajo para obtener el porcentage de batería.';

  Future<void> _getBatteryLevel() async {
    String batteryLevel;
    try {
      final int result = await platform.invokeMethod('getBatteryLevel');
      batteryLevel = 'El porcentage de la bateria es $result % .';
    } on PlatformException catch (e) {
      batteryLevel =
          "Fallo la obtención de el porcentaje de batería: '${e.message}'.";
    } on MissingPluginException catch (e) {
      batteryLevel =
          "El canal ${platform.name} no esta conectado: '${e.message}'.";
    }
    setState(() {
      _batteryLevel = batteryLevel;
    });
  }

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Demo canales de plataforma',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        body: SafeArea(
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(_batteryLevel),
                RaisedButton(
                  child: Text('Obtener nivel de batería'),
                  onPressed: _getBatteryLevel,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
