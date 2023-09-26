from APP.database import DatabaseConnection

class Chat:
    @staticmethod
    def find_user(username):
        query = "SELECT * FROM usuarios WHERE user = %s"
        #query0= "SELECT * FROM usuarios WHERE user ="
        #query1=query0+"'"+username+"'"
        result = DatabaseConnection.fetch_one(query, (username,))
        #result = DatabaseConnection.fetch_one(query1)
        if result is None:
            return None

        user = {
            'id': result[0],
            'user': result[6],
            'nombre': result[1],
            'apellido': result[2],
            'email': result[3],
            'password': result[4],
            'telefono': result[5]
        }

        return user
    

    @staticmethod
    def create_user(username, password, nombre, apellido, email, telefono):
        try:
            # Verificar si el usuario ya existe en la base de datos
            #existing_user = Chat.find_user(username)
            #if existing_user is not None:
             #   return {'success': False, 'message': 'El usuario ya existe'}
            
            query = """INSERT INTO usuarios (nombre, apellido, email, password, telefono, user) VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (nombre, apellido, email, password, telefono, username)
            user_id = DatabaseConnection.execute_query(query, values)
            
            return {'success': True, 'message': 'Usuario creado exitosamente', 'user_id': user_id}
        
        except Exception as e:
            return {'success': False, 'message': 'Error al crear el usuario: {}'.format(str(e))}