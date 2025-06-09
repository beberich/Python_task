services:
  postgres:
    image: postgres:16
    restart: always
    container_name: postgres
    environment:
      POSTGRES_USER: test
      POSTGRES_PASSWORD: 1
      POSTGRES_DB: postgres
    ports:
      - "5433:5432"
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
      

  clickhouse:
    image: yandex/clickhouse-server:latest
    restart: always
    container_name: clickhouse
    ports:
      - "8123:8123"
      - "9000:9000"
    volumes:
      - ./clickhouse_data:/var/lib/clickhouse
      


volumes:
  postgres_data:
  clickhouse_data: