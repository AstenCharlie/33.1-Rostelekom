Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии»
В данной работе необходимо было протестировать сайт от компании «Ростелеком Информационные Технологии».
Заказчик предоставил техническое задание (бриф) с описанием целей, задач и требований. В процессе тестирования применялись различные инструменты и техники тест-дизайна. Все тест-кейсы разрабатывались по методу «черного ящика».
Тестовые данные были определены техникой попарного тестирования, используя классы эквивалентности и анализ граничных значений. Используя онлайн инструмент Random String Generator, сгенерированы строки необходимой длины и состава. С помощью онлайн инструмента Pairwise найдены уникальные пары комбинаций. Для всех полей ввода форм регистрации были учтены позитивные и негативные варианты данных. Для правильного составления предусловий и шагов в тест-кейсах использовались диаграммы состояний и переходов.
Автоматизированное тестирование через веб-интерфейс проведено с помощью среды разработки PyCharm при помощи Selenium WebDriver. Для анализа работы элементов страницы применены инструменты разработчика в браузере DevTools. Для нахождения необходимого веб-элемента на странице определяем Elements locator



Тестирование требований, тест-кейсы, отчет о найденных ошибках:
Шаги по запуску тестов: 
1) Установить requirements (Python3, библиотеки: PyTest , PyTest - Selenium; PageObject, Smart Page Object): pip3 install -r requirements.txt
2) Скачать драйвер для вашей версии браузера
3) Запустить тесты: python -m pytest -v —driver Chrome —driver-path
