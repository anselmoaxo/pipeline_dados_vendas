from sqlalchemy import create_engine
import yaml


# Carregar configuração do arquivo YAML
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)

class ConexaoPostgresql:
    
    def __init__(self,  database_config = config['database'],
                        dialect = config['database']['dialect'],
                        host = config['database']['host'],
                        port = config['database']['port'],
                        username = config['database']['username'],
                        password = config['database']['password'],
                        database_name = config['database']['database_name']):
        self._database_config = database_config
        self._dialect = dialect
        self._host = host
        self._port = port
        self._username = username
        self._password = password        
        self._database_name = database_name
        self.database_url = f'{dialect}+psycopg2://{username}:{password}@{host}:{port}/{database_name}'

    @staticmethod
    def create_connect():
        instance = ConexaoPostgresql()
        engine = create_engine(instance.database_url)
        try:
            # Tentativa de conectar ao banco de dados
            connection = engine.connect()
            print("Conexão bem-sucedida!")
            return engine
        except Exception as e:
            print(f"Erro ao conectar: {e}")
        finally:
            connection.close()