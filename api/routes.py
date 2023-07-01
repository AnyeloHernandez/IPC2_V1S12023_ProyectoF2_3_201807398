from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/getUsuarios', methods=['GET'])
def getUsuario():
    try:
        if request.method == 'GET':
            retorno = [
                            {
                                "rol": "cliente",
                                "nombre": "Juan",
                                "apellido": "Perez",
                                "telefono": "123456789",
                                "correo": "juan123@example.com",
                                "contrasenna": "123"
                            },
                            {
                                "rol": "cliente",
                                "nombre": "Luis",
                                "apellido": "Human",
                                "telefono": "987654321",
                                "correo": "HLuis@example.com",
                                "contrasenna": "contrasena"
                            },
                            {
                                "rol": "cliente",
                                "nombre": "Gordon",
                                "apellido": "Freeman",
                                "telefono": "321456986",
                                "correo": "gman@example.com",
                                "contrasenna": "hl3"
                            }
                        ]
        else:
             retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    

@app.route('/getSalas', methods=['GET'])
def getSalas():
    try:
        if request.method == 'GET':
            retorno ={
                    "cine": {
                        "nombre": "Cine ABC_2",
                        "salas": {
                            "sala": [
                                {
                                    "numero": "#USACIPC2_201807398_33",
                                    "asientos": "157"
                                },
                                {
                                    "numero": "#USACIPC2_201807398_27",
                                    "asientos": "85"
                                },
                                {
                                    "numero": "#USACIPC2_201807398_88",
                                    "asientos": "88"
                                }
                            ]
                        }
                    }
            }
        else:
             retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    


@app.route('/getPeliculas',methods=['GET'])
def getPeliculas():
    try:
        if request.method == 'GET':
            retorno ={
                "categoria": [
                {
                    "nombre": "Ciencia Ficción",
                    "peliculas": {
                        "pelicula": [
                            {
                                "titulo": "Interestellar",
                                "director": "Christopher Nolan",
                                "anio": "2014",
                                "fecha": "2023-04-06",
                                "hora": "20:45",
                                "imagen": "https://4.bp.blogspot.com/-G5t76cob4Fs/V0z3NQlmQDI/AAAAAAAAA28/qOKQebH3L1ErxWuwiKrMLKlrU-sX8cMXACKgB/s1600/interstellar-poster.jpg"
                            },
                            {
                                "titulo": "Volver al futuro",
                                "director": "Robert Zemeckis",
                                "anio": "1985",
                                "fecha": "2023-03-02",
                                "hora": "18:00",
                                "imagen": "https://elvortex.com/wp-content/uploads/2020/06/volverfuturovx.jpg"
                            },
                            {
                                "titulo": "Blade Runner",
                                "director": "Ridley Scott",
                                "anio": "1982",
                                "fecha": "2023-04-09",
                                "hora": "20:00",
                                "imagen": "http://4.bp.blogspot.com/-XrZK8uyAGtY/UsccMHg9fkI/AAAAAAAACvQ/eUI19Ylark4/s1600/bladerunner.jpg"
                            }
                        ]
                    }
                }
            ]}
        else:
             retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
@app.route('/getTarjetas',methods=['GET'])
def getTarjetas():
    try:
        if request.method == 'GET':
            retorno ={
                "tarjeta": [
                            {
                            "tipo": "Debito",
                            "numero": "0123456789",
                            "titular": "Pablito Clavito",
                            "fecha_expiracion": "07/26"
                            },
                            {
                            "tipo": "Debito",
                            "numero": "32153426745",
                            "titular": "Stanyel Parab",
                            "fecha_expiracion": "04/27"
                            },
                            {
                            "tipo": "Debito",
                            "numero": "5647839103",
                            "titular": "Jhon Titor",
                            "fecha_expiracion": "08/12"
                            }
                ]
            }
        else:
             retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)