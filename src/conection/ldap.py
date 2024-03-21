import ssl
from ldap3 import Server, Connection, ALL, SUBTREE, Tls

def ldapConnect(username, password):
    try:
        print(username, password)
        # Configuración para la conexión a Active Directory
        ldap_server = '192.168.1.50'
        ldap_user = f'gepdc\\{username}'
        ldap_password = password

        # Configurar TLS
        tls_configuration = Tls(validate=ssl.CERT_NONE)

        # Establecer la conexión con Active Directory
        server = Server(ldap_server, use_ssl=True, tls=tls_configuration, get_info=ALL)
        conn = Connection(server, user=ldap_user, password=ldap_password)
        conn.open()  # Abre la conexión
        conn.bind()  # Intenta enlazar la conexión

        # Verificar si la conexión fue exitosa
        if conn.bound:
            print('Conexión exitosa a Active Directory')

            # Realizar una búsqueda LDAP para obtener los grupos del usuario
            conn.search(search_base='DC=gepdc,DC=local',
                        search_filter=f'(&(sAMAccountName={username})(objectCategory=person))',
                        search_scope=SUBTREE,
                        attributes=['memberOf'])

            # Extraer los grupos del resultado de la búsqueda
            if conn.entries:
                groups = [str(member_of) for entry in conn.entries for member_of in entry['memberOf']]
                print(f'Grupos de {username}: {groups}')
                return groups
            else:
                print(f'No se encontraron grupos para el usuario {username}')
                return []

        else:
            print('Falló la conexión a Active Directory')
            return 'Falló la conexión a Active Directory'

    except Exception as e:
        print(f'Error en la conexión Active Directory: {str(e)}')
        return f'Error en la conexión Active Directory: {str(e)}'

# Ejemplo de uso:
usuario = "administrador"
passs = "Adminwks66"
resultado = ldapConnect(usuario, passs)
print(resultado)
