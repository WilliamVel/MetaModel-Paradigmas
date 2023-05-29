from flask import Flask, render_template, url_for, flash, request, redirect
import pyodbc

app = Flask(__name__)

try:
    connection = pyodbc.connect('Driver={SQL Server}; SERVER=DESKTOP-OSMB394\SQLEXPRESS; DATABASE=Universidad; UID=test; PWD=1234')
    print("Conexion exitosa")
except Exception as e:
    print(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Asignatura')
def asignatura():
    if connection and connection.connected:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Asignatura")
        data = cursor.fetchall()
        cursor.close()
    else:
        # Código para manejar la situación en la que no se pudo establecer la conexión
        pass
    return render_template('CRUD Asignatura.html', Asignatura=data)

@app.route('/insert_Asignatura', methods=['POST'])
def insert_Asignatura():
    if request.method == "POST":
        flash ("Ingreso de datos exitoso")
        id_asignatura = request.form['id_asignatura']
        nombre = request.form['nombre']
        numero_creditos = request.form['numero_creditos']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO"+ 
                       "Asignatura (id_asignatura, nombre, numero_creditos) VALUES (?,?,?)", (id_asignatura, nombre, numero_creditos))
        connection.commit()
        return redirect(url_for('/Asignatura'))
    
@app.route('/delete_Asignatura/<string:id_asignatura>', methods = ['GET'])
def delete_Asignatura(id_asignatura):
    flash("Registro eliminado exitosamente")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Asignatura WHERE id_asignatura = {0}".format(id_asignatura))
    connection.commit()
    return redirect(url_for('Asignatura'))

@app.route('/update_Asignatura>', methods=['POST', 'GET'])
def update_Asignatura():
    if request.method == 'POST':
        id_asignatura = request.form['id_asignatura']
        nombre = request.form['nombre']
        numero_creditos = request.form['numero_creditos']
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE Asignatura
            SET nombre = ?,
                numero_creditos = ?
            WHERE id_asignatura = ?
        """, (nombre, numero_creditos, id_asignatura))
        flash("Registro actualizado exitosamente")
        connection.commit()
        return redirect(url_for('Asignatura'))

if __name__ == '__main__':
    app.run(debug=True)
