FROM mysql:latest

EXPOSE 3306

ENV MYSQL_ALLOW_EMPTY_PASSWORD yes


RUN mkdir /mysql
RUN mkdir /var/lib/mysql-files


COPY setup.sh /mysql
# COPY data.sql /mysql
COPY privileges.sql /mysql

RUN chown -R root /mysql
RUN chown -R root /var/lib/mysql-files

RUN sed -i 's/\r//' /mysql/setup.sh \
&& chmod +x /mysql/setup.sh \
&& chown root /mysql/setup.sh
#ENTRYPOINT ["/mysql/setup.sh"]
#CMD ["sh","/setup.sh"]
