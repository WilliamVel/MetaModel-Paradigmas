from flask import Flask, render_template, url_for, flash, request, redirect
import pyodbc

app = Flask(__name__)
app.secret_key = 'secreto'
driver = 'SQL Server'
server = 'DESKTOP-OSMB394\SQLEXPRESS'
database = 'Universidad'
uid = 'test'
pwd = '1234'
connection_string = f'Driver={driver}; SERVER={server}; DATABASE={database}; UID={uid}; PWD={pwd}'
try:
    connection = pyodbc.connect(connection_string)
    print("Conexión exitosa")
    cursor = connection.cursor()
except Exception as e:
    print("Error al conectar:", str(e))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Estudiante')
def Estudiante():
	cursor = connection.cursor()
	cursor.execute("SELECT TOP 0 * FROM Estudiante")
	columns = [column[0] for column in cursor.description]
	cursor.execute("SELECT * FROM Estudiante")
	data = cursor.fetchall()
	cursor.close()
	return render_template('CRUD Estudiante.html', Estudiante=data, columns=columns)

@app.route('/insert_Estudiante', methods=['POST'])
def insert_Estudiante(): 
	if request.method == "POST":
		flash ("Ingreso de datos exitoso")
		id_estudiante = request.form['id_estudiante']
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		direccion = request.form['direccion']

		column_names = eliminar_coma_final('id_estudiante,nombre,apellido,direccion,')

		value_placeholders = eliminar_coma_final('?,?,?,?,')
		
		sql_statement = "INSERT INTO Estudiante (" + column_names + ") VALUES (" + value_placeholders + ")"
		
		cursor.execute(sql_statement, (id_estudiante,nombre,apellido,direccion,))
		connection.commit()
		return redirect(url_for('/Estudiante'))

@app.route('/delete_Estudiante/<string:id_estudiante>', methods = ['GET'])
def delete_Estudiante(id_estudiante):
	flash("Registro eliminado exitosamente")
	cursor = connection.cursor()
	cursor.execute("DELETE FROM Estudiante WHERE id_estudiante = {0}".format(id_estudiante))
	connection.commit()
	return redirect(url_for('Estudiante'))	

@app.route('/update_Estudiante>', methods=['POST','GET'])
def update_Estudiante():
	if request.method == 'POST':
		id_estudiante = request.form['id_estudiante']
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		direccion = request.form['direccion']
		cursor = connection.cursor()
		sql_statement = eliminar_coma_before_where("""
            UPDATE Estudiante
            SET 
			nombre = ?,
			apellido = ?,
			direccion = ?,
			WHERE id_estudiante = ?
        """)
		cursor.execute(sql_statement, (nombre, apellido, direccion, id_estudiante))
		flash("Registro actualizado exitosamente")
		connection.commit()
		return redirect(url_for('Estudiante'))
@app.route('/Asignatura')
def Asignatura():
	cursor = connection.cursor()
	cursor.execute("SELECT TOP 0 * FROM Asignatura")
	columns = [column[0] for column in cursor.description]
	cursor.execute("SELECT * FROM Asignatura")
	data = cursor.fetchall()
	cursor.close()
	return render_template('CRUD Asignatura.html', Asignatura=data, columns=columns)

@app.route('/insert_Asignatura', methods=['POST'])
def insert_Asignatura(): 
	if request.method == "POST":
		flash ("Ingreso de datos exitoso")
		id_asignatura = request.form['id_asignatura']
		nombre = request.form['nombre']
		numero_creditos = request.form['numero_creditos']

		column_names = eliminar_coma_final('id_asignatura,nombre,numero_creditos,')

		value_placeholders = eliminar_coma_final('?,?,?,')
		
		sql_statement = "INSERT INTO Asignatura (" + column_names + ") VALUES (" + value_placeholders + ")"
		
		cursor.execute(sql_statement, (id_asignatura,nombre,numero_creditos,))
		connection.commit()
		return redirect(url_for('/Asignatura'))

@app.route('/delete_Asignatura/<string:id_asignatura>', methods = ['GET'])
def delete_Asignatura(id_asignatura):
	flash("Registro eliminado exitosamente")
	cursor = connection.cursor()
	cursor.execute("DELETE FROM Asignatura WHERE id_asignatura = {0}".format(id_asignatura))
	connection.commit()
	return redirect(url_for('Asignatura'))	

@app.route('/update_Asignatura>', methods=['POST','GET'])
def update_Asignatura():
	if request.method == 'POST':
		id_asignatura = request.form['id_asignatura']
		nombre = request.form['nombre']
		numero_creditos = request.form['numero_creditos']
		cursor = connection.cursor()
		sql_statement = eliminar_coma_before_where("""
            UPDATE Asignatura
            SET 
			nombre = ?,
			numero_creditos = ?,
			WHERE id_asignatura = ?
        """)
		cursor.execute(sql_statement, (nombre, numero_creditos, id_asignatura))
		flash("Registro actualizado exitosamente")
		connection.commit()
		return redirect(url_for('Asignatura'))
@app.route('/inscripcion')
def inscripcion():
	cursor = connection.cursor()
	cursor.execute("SELECT TOP 0 * FROM inscripcion")
	columns = [column[0] for column in cursor.description]
	cursor.execute("SELECT * FROM inscripcion")
	data = cursor.fetchall()
	cursor.close()
	return render_template('CRUD inscripcion.html', inscripcion=data, columns=columns)

@app.route('/insert_inscripcion', methods=['POST'])
def insert_inscripcion(): 
	if request.method == "POST":
		flash ("Ingreso de datos exitoso")
		id_inscripcion = request.form['id_inscripcion']
		Periodo = request.form['Periodo']

		column_names = eliminar_coma_final('id_inscripcion,Periodo,')

		value_placeholders = eliminar_coma_final('?,?,')
		
		sql_statement = "INSERT INTO inscripcion (" + column_names + ") VALUES (" + value_placeholders + ")"
		
		cursor.execute(sql_statement, (id_inscripcion,Periodo,))
		connection.commit()
		return redirect(url_for('/inscripcion'))

@app.route('/delete_inscripcion/<string:id_inscripcion>', methods = ['GET'])
def delete_inscripcion(id_inscripcion):
	flash("Registro eliminado exitosamente")
	cursor = connection.cursor()
	cursor.execute("DELETE FROM inscripcion WHERE id_inscripcion = {0}".format(id_inscripcion))
	connection.commit()
	return redirect(url_for('inscripcion'))	

@app.route('/update_inscripcion>', methods=['POST','GET'])
def update_inscripcion():
	if request.method == 'POST':
		id_inscripcion = request.form['id_inscripcion']
		Periodo = request.form['Periodo']
		cursor = connection.cursor()
		sql_statement = eliminar_coma_before_where("""
            UPDATE inscripcion
            SET 
			Periodo = ?,
			WHERE id_inscripcion = ?
        """)
		cursor.execute(sql_statement, (Periodo, id_inscripcion))
		flash("Registro actualizado exitosamente")
		connection.commit()
		return redirect(url_for('inscripcion'))

def eliminar_coma_final(cadena):
    if cadena.endswith(','):
        return cadena[:-1]
    else:
        return cadena

def eliminar_coma_before_where(sql_statement):
    index = sql_statement.rfind(",")
    if index != -1:
        sql_statement = sql_statement[:index] + sql_statement[index+1:]
    return sql_statement


if __name__ == '__main__':
    app.run(debug=True)
