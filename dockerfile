# define a imagem
FROM python:3.9

# define diretorio 
WORKDIR /app

#copia o arquivo para o diretorio do conteiner "/app"
COPY requirements.txt .

# executa o comando sem armazenar cache
RUN pip install --no-cache-dir -r requirements.txt

#copia todos os arquivos do Dockerfile para o conteiner
COPY . .

# porta que o conteiner vai usar
EXPOSE 8000

#define o que vai ser executado
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


