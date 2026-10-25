import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'calculadora_valproato'
}

def obter_conexao(usar_database=True):
    """Retorna uma conexão com o MySQL. Se usar_database=False, conecta sem especificar o banco (para criação)."""
    config = DB_CONFIG.copy()
    if not usar_database:
        config.pop('database', None)
    return mysql.connector.connect(**config)

def inicializar_banco():
    """Garante que o banco de dados e as tabelas necessárias existem."""
    try:
        # Conecta sem o banco para criá-lo se não existir
        conn = obter_conexao(usar_database=False)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        cursor.close()
        conn.close()

        # Conecta ao banco criado e cria as tabelas
        conn = obter_conexao(usar_database=True)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                documento VARCHAR(50) DEFAULT NULL,
                sus VARCHAR(50) DEFAULT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dispensacoes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                paciente_id INT NOT NULL,
                data_dispensacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                meses INT NOT NULL,
                cp_por_dia INT NOT NULL,
                sobra_inicial INT NOT NULL,
                total_caixas INT NOT NULL,
                sobra_final INT NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """)

        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Erro ao inicializar o banco de dados MySQL: {e}")
        return False

def buscar_paciente(termo):
    """Busca pacientes por Nome, CPF (documento) ou Cartão SUS."""
    try:
        conn = obter_conexao(usar_database=True)
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT id, nome, documento, sus
            FROM pacientes
            WHERE nome LIKE %s OR documento = %s OR sus = %s
        """
        termo_like = f"%{termo}%"
        cursor.execute(query, (termo_like, termo, termo))
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return resultados
    except Error as e:
        print(f"Erro ao buscar paciente: {e}")
        return []

def salvar_ou_atualizar_paciente(nome, documento=None, sus=None):
    """Salva um novo paciente ou atualiza se já existir (por documento ou SUS), retornando o ID."""
    try:
        conn = obter_conexao(usar_database=True)
        cursor = conn.cursor(dictionary=True)

        # Tenta encontrar por documento ou SUS se fornecidos
        paciente_id = None
        if documento or sus:
            query_busca = "SELECT id FROM pacientes WHERE (documento IS NOT NULL AND documento = %s) OR (sus IS NOT NULL AND sus = %s)"
            cursor.execute(query_busca, (documento or '', sus or ''))
            res = cursor.fetchone()
            if res:
                paciente_id = res['id']

        if paciente_id:
            # Atualiza dados existentes
            query_update = "UPDATE pacientes SET nome = %s, documento = %s, sus = %s WHERE id = %s"
            cursor.execute(query_update, (nome, documento or None, sus or None, paciente_id))
        else:
            # Insere novo paciente
            query_insert = "INSERT INTO pacientes (nome, documento, sus) VALUES (%s, %s, %s)"
            cursor.execute(query_insert, (nome, documento or None, sus or None))
            paciente_id = cursor.lastrowid

        conn.commit()
        cursor.close()
        conn.close()
        return paciente_id
    except Error as e:
        print(f"Erro ao salvar/atualizar paciente: {e}")
        return None

def obter_ultima_sobra(paciente_id):
    """Retorna a sobra_final da última dispensação do paciente (ou 0 se não houver)."""
    try:
        conn = obter_conexao(usar_database=True)
        cursor = conn.cursor()

        query = "SELECT sobra_final FROM dispensacoes WHERE paciente_id = %s ORDER BY data_dispensacao DESC LIMIT 1"
        cursor.execute(query, (paciente_id,))
        res = cursor.fetchone()

        cursor.close()
        conn.close()
        return res[0] if res else 0
    except Error as e:
        print(f"Erro ao obter última sobra: {e}")
        return 0

def salvar_dispensacao(paciente_id, meses, cp_por_dia, sobra_inicial, total_caixas, sobra_final):
    """Registra uma nova dispensação no banco de dados."""
    try:
        conn = obter_conexao(usar_database=True)
        cursor = conn.cursor()

        query = """
            INSERT INTO dispensacoes (paciente_id, meses, cp_por_dia, sobra_inicial, total_caixas, sobra_final)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (paciente_id, meses, cp_por_dia, sobra_inicial, total_caixas, sobra_final))

        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Erro ao salvar dispensação: {e}")
        return False
