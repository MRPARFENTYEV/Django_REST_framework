# syntax=docker/dockerfile:1

FROM python:3.9
WORKDIR /smart_home
COPY . /smart_home
RUN pip3 install --no-catche-dir --upgrade -r requierements.txt
# Эта команда устанавливает все пакеты, указанные в файле requirements.txt,
# с опцией --no-cache, которая предотвращает использование кэшированных зависимостей,
# и с опцией --upgrade, которая обновляет зависимости до самых последних версий.
ENV my_env =virtualenv
EXPOSE 3000
CMD ["python3","-u","main.py","--host","0.0.0.0","--port","6060"]
#прописываю какая команда должна быть выполнена

