```mermaid
graph TD
    A[Extrair Dados] --> B[Transformar Dados]
    B --> C[Cargar Dados]
    A1[Fonte de Dados 1] --> A
    A2[Fonte de Dados 2] --> A
    B1[Limpando Dados] --> B
    B2[Enriquecendo Dados] --> B
    C1[Data Warehouse] --> C
    C2[Data Lake] --> C
    C3[Banco de Dados de Destino] --> C
    A1 -->|Extração| A
    A2 -->|Extração| A
    B1 -->|Transformação| B
    B2 -->|Transformação| B
    C1 -->|Carga| C
    C2 -->|Carga| C
    C3 -->|Carga| C

