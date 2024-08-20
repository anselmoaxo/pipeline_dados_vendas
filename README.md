```mermaid

graph TD
    A[Extração de Dados] -->|Carregar Dados| B[Orquestração com Airflow]
    B -->|Mover Dados| C[Transformação com dbt]
    C -->|Transformar Dados| D[Criar Dashboard com Power BI]

    A1[Base de Dados PostgreSQL "Novadrive"] --> A
    B1[Data Warehouse PostgreSQL] --> B
    C1[Transformação de Dados] --> C
    D1[Dashboard no Power BI] --> D
