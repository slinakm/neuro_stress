import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:location/location.dart';
import 'package:http/http.dart';
import "dart:convert";

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Neuros',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double _lat = 0.0;
  double _lng = 0.0;
  double _spd = 0.0;
  int _time = 0;

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Column(
              children: [
                Text(
                  "It is now $_time"
                ),
                Text(
                  'You are at:',
                ),
                Text(
                  '$_lat, $_lng',
                  style: Theme.of(context).textTheme.display1,
                ),
                Text(
                  'You are moving at speed $_spd'
                )
              ]),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _getLocation,
        tooltip: 'Update Info',
        child: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  /**
   * This method sends an HTTP Request to report a user's self-reported "depression" score to
   * refine the model to the individual user.
   *
   */
  _reportScore() async {
    var score = 15; //TODO: CHANGE THIS to get input from a slider, TextView, etc.

    String url = 'http://localhost:5000/api/score/';
    Map<String, String> headers = {"Content-type": "application/json"};
    Map map = {"score": score};
    Response response = await post(url, headers: headers, body: json.encode(map));
  }

  _getLocation() async {
    var location = new Location();
    try {
      var currentLocation = await location.getLocation();

      setState(() {
        _lat = currentLocation.latitude;
        _lng = currentLocation.longitude; 
        _spd = currentLocation.speed;
        _time = currentLocation.time.toInt();
     });
           //send request
      String url = 'http://localhost:5000/api/score/';
      Map<String, String> headers = {"Content-type": "application/json"};
      Map map = {"lat": currentLocation.latitude, "lng": currentLocation.longitude, "time":currentLocation.time.toInt(), "spd":currentLocation.speed};
      Response response = await post(url, headers: headers, body: json.encode(map));
      print(response.body);
      
    } on PlatformException catch (e) {
      print(e);
    }
  }

  
}
