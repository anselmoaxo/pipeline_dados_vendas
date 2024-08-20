```mermaid

graph TD
    A[Extração de Dados] --> B[Orquestração com Airflow]
    B --> C[Transformação com dbt]
    C --> D[Criar Dashboard com Power BI]
    
    subgraph Fonte
        A1[Base de Dados PostgreSQL "Novadrive"]
    end

    subgraph Orquestração
        B1[Data Warehouse PostgreSQL]
    end

    subgraph Transformação
        C1[Transformação de Dados]
    end

    subgraph Visualização
        D1[Dashboard no Power BI]
    end

    A --> A1
    B --> B1
    C --> C1
    D --> D1
