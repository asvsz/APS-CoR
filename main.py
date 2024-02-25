import hashlib

#Armazena informações do usuário
class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

#Classe abstrata para os manipuladores de autenticação
class AuthenticationHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def authenticate(self, username, password):
        if self.successor:
            return self.successor.authenticate(username, password)
        else:
            return None

#Implementa um manipulador de autenticação
class MemoryInAuthHandler(AuthenticationHandler):
    def __init__(self):
        super().__init__()
        self.users = {
            "aline": hashlib.md5("123456".encode()).hexdigest(),
            "marcia": hashlib.md5("091234".encode()).hexdigest()
        }

    def authenticate(self, username, password):
      
        if username in self.users and self.users[username] == hashlib.md5(password.encode()).hexdigest():
            return User(username, self.users[username])
        else:
            return super().authenticate(username, password)

if __name__ == "__main__":
    auth_handler = MemoryInAuthHandler()

    user1 = auth_handler.authenticate("aline", "123456")
    user2 = auth_handler.authenticate("amanda", "12345678")
    user3 = auth_handler.authenticate("marcia", "091234")

    if user1:
        print(f"Usuário {user1.username} autenticado com sucesso.")
    else:
        print("Autenticação falhou para o usuário aline.")

    if user2:
        print(f"Usuário {user2.username} autenticado com sucesso.")
    else:
        print("Autenticação falhou para o usuário amanda.")

    if user3:
        print(f"Usuário {user3.username} autenticado com sucesso.")
    else:
        print("Autenticação falhou para o usuário amanda.")
        
