import mysql.connector


def connect_to_database():
    # Conexão com o banco de dados
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123abc@",
        database="bdpython"
    )
    return conn


def create_table(conn):
    cursor = conn.cursor()

    # Criação de uma tabela
    table_create = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
    cursor.execute(table_create)


def insert_data(conn):
    cursor = conn.cursor()

    # Inserção de dados
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = ("Ronaldo Pereira", "ronaldopereira@example.com")
    cursor.execute(sql, val)
    conn.commit()


def read_data(conn):
    cursor = conn.cursor()

    # Leitura de dados
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)


def update_data(conn):
    cursor = conn.cursor()

    # Atualização de dados
    sql = "UPDATE users SET email=%s WHERE name=%s"
    val = ("ronaldopereira2@example.com", "Ronaldo Pereira")
    cursor.execute(sql, val)
    conn.commit()


def delete_data(conn):
    cursor = conn.cursor()

    # Deletar dados
    sql = "DELETE FROM users WHERE name=%s"
    val = ("Ronaldo Pereira",)
    cursor.execute(sql, val)
    conn.commit()


def close_connection(conn):
    # Fechando a conexão
    conn.close()


connection = connect_to_database()

while True:
    print("O que você deseja fazer?")
    print("C - Criar tabela")
    print("R - Ler dados")
    print("U - Atualizar dados")
    print("D - Deletar dados")
    print("I - Inserir dados")
    print("S - Sair")
    choice = input("Escolha uma opção: ")

    if choice == "C":
        create_table(connection)
        print("Comando Criar tabela Executado")
    elif choice == "R":
        print("Comando Ler dados Executado")
        read_data(connection)
    elif choice == "U":
        print("Comando Atualizar dados Executado")
        update_data(connection)
    elif choice == "D":
        print("Comando Deletar dados Executado")
        delete_data(connection)
    elif choice == "I":
        print("Comando Inserir dados Executado")
        insert_data(connection)
    elif choice == "S":
        print("Comando Sair Executado \n")
        print("Programa Finalizdo! \n")
        break
    else:
        print("Opção inválida.")

close_connection(connection)
