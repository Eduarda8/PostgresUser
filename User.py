'''
Progama para selecionar e exibir na tela, os usuarios da Rede Social.
'''
import psycopg

def main():

    # Conectando a um banco de dados existente ;
    cnx = psycopg2.connect("dbname=mydb, user=myuser, password=secret")
    cur = cnx.cur()

    cur.execute("""
        SELECT * FROM tb_usuario;
    """)

    usuarios = cur.fetchall()

    for usuario in usuarios:
        print("Login:", usuario[0])
        print("Senha:", usuario[1])
        print("Nome:", usuario[2])
        print("Dia:", usuario[3])
        print("Mes:", usuario[4])
        print("Ano:", usuario[5])
        print("Data Nascimento:", usuario[6])
        print("Profissão:", usuario[7])
        print("Gênero:", usuario[8])

    # Fecha a comunicação com o banco;
    cnx.close()

if __name__ == '__main__':
    main()
