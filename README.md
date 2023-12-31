## Обзор проекта
В данном проекте исследовалось создание системы рекомендаций для свиданий в Telegram боте. Система использует вложения (embeddings) профилей пользователей для выявления кластеров, что в теории позволило бы более тонко подбирать рекомендации для людей с совпадающими интересами (если профили близки в эмбеддинге, то предпологаем, что эти люди подходят друг другу). Проект включает в себя базу данных для хранения профилей пользователей (`main.db`) и несколько Python скриптов и Jupyter блокнот для генерации и анализа этих вложений.


## Результаты эмбеддинга
- База данных для анализа взята из телеграм бота для дейтинга.
- Каждая точка - анкета пользователя, при наведении на точку отображается анкета пользователя.
- Цвет обозначает возраст (красный - возраст меньше, синий - больше)
![alt text](https://github.com/gregoryginzburg/Dating-Recommendation-System/blob/master/results/visualization.png)

## Установка
Для запуска проекта выполните следующие шаги:
1. Клонируйте репозиторий: 
  ```
  git clone https://github.com/gregoryginzburg/Dating-Recommendation-System.git
  ```

2. Установите необходимые пакеты Python:
  ```
  pip install -r requirements.txt
  ```

## Конфигурация
1. Вставьте свои ключи API OpenAI и Yandex в файле `create_embeddings.py`.
2. Убедитесь, что `main.db` правильно инициализирована с данными пользователей.

## Использование
1. **Генерация вложений**: Запустите `create_embeddings.py` для создания вложений профилей пользователей.
2. **Визуализация данных**: Используйте `visualize.py` для визуализации кластеризации вложений.



## Компоненты

### База данных: `main.db`
- **Таблицы**:
  - `users`: Содержит подробные профили пользователей, включая предпочтения и демографические данные, которые являются ключевыми для создания значимых вложений.

### Python Скрипты
1. **create_embeddings.py**: Генерирует вложения из данных пользователей, используя OpenAI и Yandex API (для перевода анкет на английский). Эти вложения являются ключевыми для определения схожести профилей пользователей.
2. **visualize.py**: Визуализирует вложения с помощью инструментов, таких как Matplotlib и t-SNE из scikit-learn. Этот скрипт помогает анализировать и понимать кластеризацию профилей пользователей.
3. **yandex_api.py**: Обертка под Yandex API для перевода с русского на английский профилей пользователей.

### Jupyter Блокнот
- **test_embeddings_api.ipynb**: Тестирует API для вложений, обеспечивая правильную генерацию вложений, которые могут быть использованы для анализа кластеров.



