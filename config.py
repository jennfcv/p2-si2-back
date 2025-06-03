import psycopg2

def conectar_db():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port="5432",
            database="aulainteligente",
            user="postgres",
            password="5328"
        )
        return conexion
    except Exception as e:
        print("❌ Error al conectar con la base de datos:", e)
        return None
