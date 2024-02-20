from database.connectDB import  get_connection_SQL_SERVER


class modelProject:
    @staticmethod
    def get_dataBank():
        connection = get_connection_SQL_SERVER()
        with connection.cursor() as cursor:
            try:
                query="SELECT IDBCO, DESCRIPCION FROM BANCOS"
                cursor.execute(query)
                result= cursor.fetchall()
                return  result

            except Exception as e:
                print(f"Error en la consulta { str(e)}")
                return []