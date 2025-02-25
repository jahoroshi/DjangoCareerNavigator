

**Recruitment Assistant - система поиска кандидатов и вакансий**

**Технологии:**
- **Django Rest Framework (DRF):** 
- **PostgreSQL:** 
- **Docker:** 
- **JWT:** 
- **Swagger:** документация API 
- **Pydantic Settings:** управление конфигкрацией

**Для авторизации нужно ввести токен со словом Bearer:** 
Bearer <ТОКЕН>

**Функциональные возможности:**

1. **Публикация резюме кандидата:**
   - Название навыка
   - Уровень владения (начальный, средний, продвинутый)
   - Годы опыта
   - Год последнего использования

2. **Публикация вакансий от рекрутера:**
   - Минимальный уровень владения навыком
   - Минимальное количество лет опыта

3. **CRUD-операции:**
   - **Профиль кандидата:** 
   - **Профиль рекрутера:** 
   - **Навыки кандидата:** 
   - **Вакансии:** 
   - **Требования к вакансии:** 

4. **API для подбора кандидатов:**
   - Возвращает упорядоченный список кандидатов для данной вакансии.

5. **API для подбора вакансий:**
   - Возвращает упорядоченный список вакансий, наиболее релевантных для данного кандидата.


Вот инструкция по скачиванию и запуску проекта с помощью Docker Compose:

### Установка и запуск проекта

1. **Скачайте проект:**

   Клонируйте репозиторий с проектом:
   ```bash
   git clone https://github.com/jahoroshi/DjangoCareerNavigator
   ```

2. **Перейдите в директорию проекта:**
переименуйте файл .env.sample в .env


3. **Запустите Docker Compose:**
   ```bash
   docker-compose up --build
   ```


4. **Просмотр документации API:**

   Swagger-документация будет доступна по адресу:
   ```
   http://localhost:8000/swagger/
   ```
