FROM python:3.11-slim
RUN pip install mkdocs-material mkdocs==1.6.0 jinja2
WORKDIR /site
COPY mkdocs.yml /site/mkdocs.yml
COPY docs /site/docs
EXPOSE 8000
CMD ["mkdocs","serve","-a","0.0.0.0:8000"]
