# Предиктивная аналитика больших данных

Учебный проект для демонстрации основных этапов жизненного цикла проекта предиктивной аналитики.  

## Installation 

Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  

```sh
git clone https://github.com/kraoff/pabd24.git
cd pabd24

conda env create -f environment.yml
conda activate pabd24
```

## Usage

### 1. Сбор данных о ценах на недвижимость 
```sh
python src/parse_cian.py 
```  
Параметры для парсинга можно изменить в скрипте.  
Подробности см. в [репозитории](https://github.com/lenarsaitov/cianparser)  

### 2. Выгрузка данных в хранилище S3 
Для доступа к хранилищу скопируйте файл `.env` в корень проекта.  

```sh
python src/upload_to_s3.py -i data/raw/file.csv 
```  
### Демонстрация
gunicorn: http://95.174.93.205:8000

### Docker
```sh
docker run kraoff/pabd24:latest
```  