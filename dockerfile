FROM mongo:5.0.3

COPY ./conf/mongo.key /data/mongo.key
COPY ./loop /loop

RUN chmod 400 /data/mongo.key && \
    chmod 777 /loop

# ENTRYPOINT [ "/loop" ]
ENTRYPOINT [ "mongod" ]
CMD [ "--config", "/data/configdb/mongo.yml" ]
