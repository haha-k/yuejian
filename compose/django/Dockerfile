FROM python


#RUN groupadd -r haha \
#$$ useradd -r -g haha haha

RUN mkdir /requirements
RUN mkdir -p /yuejian3

COPY ./requirements /requirements

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple 
RUN pip install --no-cache-dir -r /requirements/prod.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
&& rm -rf /requirements

COPY ./compose/django/gunicorn.py /
COPY ./compose/django/gunicorn.sh /

RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh \
    && chown root /gunicorn.sh

COPY . /yuejian3

RUN cat /gunicorn.sh

RUN chown -R root /yuejian3

USER root

#WORKDIR /Wendao/backend

#ENTRYPOINT ["/gunicorn.sh"]
#CMD ["sh","/gunicorn.sh"]


