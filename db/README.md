# 出身県当てるシステムDB

## 事前準備

- 過去データを取得

## Docker Build

```
$ docker build -t alcohol_suggest_db .
```

## docker compose

```
$ docker-compose up -d
```

### Port

- `5432` for postgresql

### log directory

- `/var/log/postgresql`

### log files

- `LOGDIR/postgresql-YYYYmmdd.log`

### config file

- `/etc/postgresql/postgresql.conf'

