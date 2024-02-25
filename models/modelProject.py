from database.connectDB import get_connection_SQL_SERVER


class modelProject:
    @staticmethod
    def get_dataBank():
        connection = get_connection_SQL_SERVER()
        with connection.cursor() as cursor:
            try:
                query = "SELECT IDBCO, DESCRIPCION FROM BANCOS"
                cursor.execute(query)
                result = cursor.fetchall()
                return result

            except Exception as e:
                print(f"Error en la consulta {str(e)}")
                return []

    # Insert
    @staticmethod
    def insert_bank(description):
        connection = get_connection_SQL_SERVER()
        mycursor = connection.cursor()
        SQLINSERT = "INSERT INTO Bancos (DESCRIPCION) VALUES(?)"
        try:
            mycursor.execute(SQLINSERT, description)
        except:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.close()
            return True

    @staticmethod
    def update_bank(idbank, description):
        connection = get_connection_SQL_SERVER()
        mycursor = connection.cursor()
        SQLUPDATE = "UPDATE Bancos SET DESCRIPCION=? WHERE  IDBCO=?"
        try:
            mycursor.execute(SQLUPDATE, description, idbank)
        except:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.close()
            return True

    @staticmethod
    def delete_bank(idbank):
        connection = get_connection_SQL_SERVER()
        mycursor = connection.cursor()
        SQLDELETE = "DELETE FROM Bancos WHERE IDBCO=?"
        try:
            mycursor.execute(SQLDELETE, idbank)
        except:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.close()
            return True
