from ldap3 import Server, Connection, ALL, SUBTREE, Tls

def ldapConnect(username, password):
    try:
        print(username,password)
        # Configuración para la conexión a Active Directory
        ldap_server = '192.168.1.50' 
        ldap_user = f'gepdc\\{username}'  
        ldap_password = password  

        # Establecer la conexión con Active Directory
        server = Server(ldap_server, get_info=ALL)
        conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)

        # Verificar si la conexión fue exitosa
        if conn.bound:
            print('Conexión exitosa a Active Directory')
            return 'Conexión exitosa a Active Directory'
        else:
            print('Falló la conexión a Active Directory')
            return 'Falló la conexión a Active Directory'

    except Exception as e:
        return f'Error en la conexión Active Directory: {str(e)}'