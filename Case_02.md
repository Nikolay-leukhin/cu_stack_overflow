# **Кейс 2. Система управления складом с аналитикой и отчётами**

Вы работаете в логистической компании. Нужно разработать систему для управления складом, которая:
- автоматически отслеживает остатки на складе,
- обрабатывает заказы от клиентов и обновляет запасы на складе,
- оповещает о товарах с низким уровнем запасов,
- предоставляет менеджеру отчёт по текущим запасам с рекомендациями по закупкам.


#### **Этапы работы**

1. **Загрузка данных о текущих запасах** — **`Участник 2`**
   - Загрузи файл CSV с данными о текущих запасах на складе.
   - Преобразуй данные в словарь, где ключ — это артикул товара, а значение — количество на складе.

2. **Обработка заказов** — **`Участник 1`**
   - Настрой загрузку данных и обновление остатка товаров на складе.
   - Если заказ превышает количество товара на складе, система должна либо частично исполнить заказ, либо отклонить его с логированием (подход выбери самостоятельно).

3. **Аналитика по складу** — **`Участник 3`**
   - Определи, какие товары находятся на складе в критически малом количестве (менее 10 единиц).
   - Рассчитай:
     - суммарную стоимость всех товаров на складе,
     - количество категорий товаров, представленных на складе.

4. **Оповещение о низком уровне запасов** — **`Участник 2`**
   - Настрой автоматическую генерацию списка товаров с низкими остатками и рекомендациями объёма для пополнения (например, удвоить текущие запасы).
   - Список должен сохраняться в текстовый файл.

5. **Визуализация складских остатков** — **`Участник 3`**
   - Построй круговую диаграмму с распределением товаров по категориям и сохрани её как изображение.
   - Построй линейный график, отображающий изменение запасов по времени (используй данные о заказах за несколько дней).

6. **Генерация отчёта** — **`Участник 1`**
   - Сформируй отчёт для менеджера:
     - общее количество товаров на складе,
     - товары с критическими запасами,
     - рекомендации по закупкам.
   - Отчёт должен быть сохранен в формате `.txt` и автоматически обновляться ежедневно.

7. **Обработка ошибок и логирование** — **`Общекомандная задача`**
   - Добавьте обработку ошибок на уровне чтения файлов, работы с данными (например, если данных не хватает или они некорректны). Все ошибки должны записываться в лог-файл.

#### **Ожидаемые результаты**
- Система управления складом с обновлением данных по заказам.
- Оповещение менеджера о необходимости пополнения запасов.
- Визуализация складских остатков по категориям товаров.
- Автоматический отчёт по складу с рекомендациями по закупкам.