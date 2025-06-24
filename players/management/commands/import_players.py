from django.core.management.base import BaseCommand
from players.models import Player
import json

class Command(BaseCommand):
    help = 'Import players from JSON data'
    
    def handle(self, *args, **options):
        # Пример данных (замени на свои)
        players_data = [
            {
    'id': 1,
    'name': 'Байзак Бектур уулу',
    'number': 84,
    'position': 'goalkeeper',
    'positionName': 'Вратарь',
    'age': 18,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 0,
    'assists': 2,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/bekturuulubaizak_1.jpg',
    'height': '177 см',
    'weight': '71 кг',
    'birthDate': ' 01.03.2007',
    'career': [
      'Академия «Дордой»',
    ],
    'achievements': [
    ]
  },
  {
    'id': 2,
    'name': 'Курманбек Нурланбеков',
    'number': 35,
    'position': 'goalkeeper',
    'positionName': 'Вратарь',
    'age': 21,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 0,
    'assists': 2,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/nurlanbekov_1.jpg',
    'height': '193 см',
    'weight': '79 кг',
    'birthDate': ' 01.04.2004',
    'career': [
      '2021-2022 «Илбирс» (Бишкек, Кыргызстан)',
      'с 2023 «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
    ]
  },
  {
    'id': 3,
    'name': 'Адилет Абдырайымов',
    'number': 1,
    'position': 'goalkeeper',
    'positionName': 'Вратарь',
    'age': 19,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 0,
    'assists': 2,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/abdyraiymov_1.jpg',
    'height': '184 см',
    'weight': '75 кг',
    'birthDate': '09.09.2006',
    'career': [
      'Выпускник академии «Дордой»',
      'С 2023 – «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Вице-чемпион Кыргызстана (2024)'
    ]
  },
  {
    'id': 4,
    'name': 'Салим Мамбетов',
    'number': 5,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 27,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.9,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/mambetov_1.jpg',
    'height': '182 см',
    'weight': '78 кг',
    'birthDate': '15.03.1998',
    'career': [
      'Академия «Дордой»',
      '2018-2020 – «Алга»',
      'С 2021 – «Дордой»'
    ],
    'achievements': [
      'Чемпион Кыргызстана (2023)',
      'Обладатель Кубка Кыргызстана (2022)'
    ]
  },
  {
    'id': 5,
    'name': 'Камолидин Ташиев',
    'number': 44,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 25,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/tashiev_1.jpg',
    'height': '180 см',
    'weight': '75 кг',
    'birthDate': '09.02.2000',
    'career': [
      '2016-2018 - «Абдыш-Ата 2» (Кант, Кыргызстан)',
      '2018-2019 - Абдыш Ата» (Кант, Кыргызстан)',
      '2020-2021 – «Гейланг Интернэшнл» (Сингапур)',
      '2020-2022 – «Абдыш Ата» (Кант, Кыргызстан)',
      '2023-2024 – «Талант» (Беш-Кунгей, Кыргызстан)',
      '2024 – «Алга» (Бишкек, Кыргызстан)',
      '2025 – «Дордой» (Бишкек, Кыргызстан)',
    ],
    'achievements': [
      'Чемпион Кыргызстана (2022)',
      'Обладатель Кубка Кыргызстана (2022)'
    ]
  },
  {
    'id': 6,
    'name': 'Вениамин Шумейко',
    'number': 24,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 36,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/shumejko_1.jpg',
    'height': '192 см',
    'weight': '89 кг',
    'birthDate': '02.02.1989',
    'career': [
      '2007-2012 – «Абдыш-Ата» (Кант, Кыргызстан)',
      '2013 – «Алай» (Ош, Кыргызстан)',
      '2014-2015 – «Абдыш-Ата» (Кант, Кыргызстан)',
      '2016-2017 – «Алга» (Бишкек, Кыргызстан)',
      '2017-2018 – «Ченнаи» (Индия)',
      '2018 – «UiTM» (Малайзия)',
      '2019 – “Binh Duong” (Вьетнам)',
      '2020-2021 – «Алга» (Бишкек, Кыргызстан)',
      '2021-2022 – “Persikabo” (Индонезия)',
      '2022-2023 – «Алга» (Бишкек, Кыргызстан)',
      '2023-2024 – «Мурас Юнайтед» (Джалал-Абад, Кыргызстан)',
      'С 2025 – «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Чемпион Кыргызстана (2013)',
      'Обладатель Кубка Кыргызстана (2007, 2009, 2011, 2013, 2023, 2024)'
    ]
  },
  {
    'id': 7,
    'name': 'Папи Серинье Ло Ндойе',
    'number': 77,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 26,
    'nationality': 'Италия',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/londojepapi_1.jpg',
    'height': '186 см',
    'weight': '80 кг',
    'birthDate': '03.03.1999',
    'career': [
      '2017-2019 – “Casale calcio” (Италия)',
      '2020/2021 – “Kurilovec” (Хорватия)',
      '2021/2022 – “Mininja” (Литва)',
      '2022/2023 – “Loko Vltavin” (Чехия)',
      '2024/2025 – “Fushe” (Косово)',
      'С 2025 - «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
    ]
  },
  {
    'id': 8,
    'name': 'Арслан Бекбердинов',
    'number': 70,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 22,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/bekberdinov_1.jpg',
    'height': '180 см',
    'weight': '77 кг',
    'birthDate': '14.08.2003',
    'career': [
      '2021-2023 – «Илбирс» (Бишкек, Кыргызстан)',
      '2023 – «Абдыш-Ата» (Кант, Кыргызстан)',
      'С 2024 – «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Чемпион Кыргызстана (2023)',
      'Серебряный призер Кубка Кыргызстана (2023)',
      'Участник финального этапа Кубка Азии U-20 (Узбекистан-2023)'
    ]
  },
  {
    'id': 9,
    'name': 'Владимир Заименко',
    'number': 1,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 28,
    'nationality': 'Украина',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/zaimenko_1.jpg',
    'height': '184 см',
    'weight': '80 кг',
    'birthDate': '18.04.1997',
    'career': [
      '2008-2013 - Академия «Кривбасс» (Кривой Рог, Украина)',
      '2013-2014 - RVUFK Kyiv',
      '2014-2016 – «Скала Стрый» U19 (Украина)',
      '2016-2018 – «Заря» U-21 (Луганск, Украина)',
      '2018-2020 – «Горняк» (Кривой Рог, Украина)',
      '2020-2022 – «Кривбасс» (Кривой Рог, Украина)',
      '2022 – «Игрос» (Красноброд, Польша)',
      '2022-2023 - DV Solingen (Германия)',
      '2023 – «Алай» (Ош, Кыргызстан)',
      'С 2024 – «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Вице-чемпион 2 Лиги Украины (2020-2021)',
      'Вице-чемпион 1 Лиги Украины (2021-2022)',
      'Обладатель Суперкубка Кыргызстана (2023)',
      'Вице-чемпион Кыргызстана (2023, 2024)'
    ]
  },
  {
    'id': 10,
    'name': 'Эламан Акылбеков',
    'number': 27,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 22,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/3704_akylbekov_1.jpg',
    'height': '179 см',
    'weight': '67 кг',
    'birthDate': '11.08.2003',
    'career': [
      'Выпускник академии имени Асылбека Момунова',
      '2020 – «Каганат» (г. Ош, Кыргызстан)',
      '2021-2022 – «Илбирс» (г. Бишкек, Кыргызстан)',
      '2023 – «Алай» (г. Ош, Кыргызстан)',
      '2024 – «Дордой» (г. Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Вице-чемпион Кыргызстана (2023, 2024)'
    ]
  },
  {
    'id': 11,
    'name': 'Мамыралиев Суйунтбек',
    'number': 17,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 27,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/mamyraliev_1.jpg',
    'height': '172 см',
    'weight': '70 кг',
    'birthDate': '07.01.1998',
    'career': [
      'Выпускник академии «Дордой»',
      '2016 – «Дордой-2» (г. Бишкек, Кыргызстан)',
      '2017-2018 - «Дордой» (г. Бишкек, Кыргызстан)',
      '2019 – «Илбирс» (г. Бишкек, Кыргызстан)',
      '2020 – «Алга» (г. Бишкек, Кыргызстан)',
      '2021 – «Алай» (г. Бишкек, Кыргызстан)',
      'С 2022 – «Дордой» (г. Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Чемпион Кыргызстана (2018)',
      'Обладатель Суперкубка Кыргызстана (2022)'
    ]
  },
  {
    'id': 12,
    'name': 'Александр Мищенко',
    'number': 31,
    'position': 'defender',
    'positionName': 'Защитник',
    'age': 28,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/mishenko_1.jpg',
    'height': '176 см',
    'weight': '68 кг',
    'birthDate': '30.07.1997',
    'career': [
      '2006-2010 - TSC Euskirchen (Германия)',
      '2010-2012 - Bonner SC (Германия)',
      '2012-2014 - TSC Euskirchen (Германия)',
      '2014-2017 - "Borussia Mönchengladbach" (Германия);',
      'С 2017 – «Дордой» (г. Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Чемпион Кыргызстана (2018, 2019, 2020, 2021)',
      'Обладатель Кубка Кыргызстана (2017, 2018)',
      'Обладатель Суперкубка Кыргызстана (2019, 2021, 2022)',
      'Член символической сборной Кыргызской Премьер-Лиги 2019'
    ]
  },
  {
    'id': 13,
    'name': 'Владислав Кобылянский',
    'number': 8,
    'position': 'midfielder',
    'positionName': 'Полузащитник',
    'age': 23,
    'nationality': 'Украина',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/kobylianskij_1.jpg',
    'height': '177 см',
    'weight': '74 кг',
    'birthDate': ' 02.02.2002',
    'career': [
      'Выпускник академии «Шахтер» (Донецк, Украина)',
      '2019/2020 - «Шахтер-2» (Донецк, Украина)',
      '2020/2021 - «Газиантепспор» (Газиантеп, Турция)',
      '2021/2022 - «Титус Петанж» (Петанж, Люксембург)',
      '2022/2023 - «Лейрия» (Лейрия, Португалия)',
      'С 2025 - «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      '2020-2022 – «Илбирс» (Бишкек, Кыргызстан)',
      '2023 – «Талант» (Беш-Кунгей, Кыргызстан)'
    ]
  },
  {
    'id': 14,
    'name': 'Мирлан Бекбердинов',
    'number': 71,
    'position': 'midfielder',
    'positionName': 'Полузащитник',
    'age': 22,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/bekberdinov_m_1.jpg',
    'height': '179 см',
    'weight': '76 кг',
    'birthDate': '14.08.2003',
    'career': [
      'Воспитанник академии «Дордой»',
      '2020 – «Абдыш-Ата-2» (Кант, Кыргызстан)',
      '2021-2023 – «Илбирс» (Бишкек, Кыргызстан)',
      '2023 - «Нефтчи» (Кочкор-Ата, Кыргызстан)',
      '2024 – «Алга» (Бишкек, Кыргызстан)',
      'C 2025 – «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
    ]
  },
  {
    'id': 15,
    'name': 'Эдиль Осмонов',
    'number': 19,
    'position': 'midfielder',
    'positionName': 'Полузащитник',
    'age': 22,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/osmonov_1.jpg',
    'height': '175 см',
    'weight': '66 кг',
    'birthDate': '31.01.2003',
    'career': [
      '2020-2022 – «Илбирс» (Бишкек, Кыргызстан)',
      '2023 – «Талант» (Беш-Кунгей, Кыргызстан)'
    ],
    'achievements': [
    ]
  },
  {
    'id': 16,
    'name': 'Алексей Лобов',
    'number': 55,
    'position': 'midfielder',
    'positionName': 'Полузащитник',
    'age': 21,
    'nationality': 'Украина',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/3486_lobov_1.jpg',
    'height': '187 см',
    'weight': '80 кг',
    'birthDate': '16.08.1997',
    'career': [
      '2017-2020 – «Авангард» (Краматорск, Украина)',
      '2020 – «Колос» (Ковалевка, Украина)',
      '2021 – «Оболонь» (Киев, Украина)',
      '2022 – «Хебыр» (Пазарджик, Болгария)',
      'С 2023 - «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
    ]
  },
  {
    'id': 17,
    'name': 'Адиль Кадыржанов',
    'number': 14,
    'position': 'midfielder',
    'positionName': 'Полузащитник',
    'age': 25,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/kadyrzhanov_1.jpg',
    'height': '180 см',
    'weight': '72 кг',
    'birthDate': '14.07.2000',
    'career': [
      '2013-2017 – Академия «Дордой» (Бишкек, Кыргызстан)',
      '2017-2020 – На правах аренды «Алга» (Бишкек, Кыргызстан)',
      '2020-2022 – «Алга» (Бишкек, Кыргызстан)',
      'С 2023 - «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Вице-чемпион Кыргызстана (2020, 2024)',
      'Серебряный призер Кубка Кыргызстана (2021)'
    ]
  },
  {
    'id': 18,
    'name': 'Эрназ Абилов',
    'number': 9,
    'position': 'midfielder',
    'positionName': 'Полузащитник',
    'age': 24,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/abilov_1.jpg',
    'height': '168 см',
    'weight': '73 кг',
    'birthDate': '30.03.2001',
    'career': [
      'Выпускник академии ФК «Дордой»',
      '2019-2020 – на правах аренды ФК «Илбирс» (Бишкек, Кыргызстан)',
      '2021-2022 – «Дордой» (Бишкек, Кыргызстан)',
      '2023-2024 – «Алга» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Чемпион Кыргызстана (2021)',
      'Обладатель Суперкубка Кыргызстана (2022)'
    ]
  },
  {
    'id': 19,
    'name': 'Ислам Юнусов',
    'number': 1,
    'position': 'forward',
    'positionName': 'Нападающий',
    'age': 21,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/junusov_1.jpg',
    'height': '175 см',
    'weight': '70 кг',
    'birthDate': '26.01.2000',
    'career': [
      '2017-2018 - "Рузаевка" (г. Алма-Ата, Казахстан)',
      '2018-2019 - "Алга" (г. Бишкек, Кыргызстан)',
      '2019-2020 - "Экибастуз" (г. Экибастуз, Казахстан)',
      '2021 - "Мактаарал" (г. Атакент, Казахстан)',
      'С 2022 - "Дордой" (г. Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Обладатель Суперкубка Кыргызстана (2022)',
    ]
  },
  {
    'id': 20,
    'name': 'Алекса Мрджа',
    'number': 91,
    'position': 'forward',
    'positionName': 'Нападающий',
    'age': 26,
    'nationality': 'Босния и Герцеговина',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/mrdzhaalexa_1.jpg',
    'height': '193 см',
    'weight': '88 кг',
    'birthDate': '15.08.1999',
    'career': [
      '2024 – «Абдыш-Ата» (Кант, Кыргызстан)',
    ],
    'achievements': [
      'Чемпион Кыргызстана (2024)'
    ]
  },
  {
    'id': 21,
    'name': 'Юрий Сеницкий',
    'number': 45,
    'position': 'forward',
    'positionName': 'Нападающий',
    'age': 28,
    'nationality': 'Украина',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/senyitskij_1.jpg',
    'height': '186 см',
    'weight': '85 кг',
    'birthDate': '15.05.1997',
    'career': [
      '2014-2016 – «Шахтёр» U-19 (Донецк, Украина)',
      '2016-2018 – «Мариуполь» (Мариуполь, Украина)',
      '2018-2022 – «Авангард» (Краматорск, Украина)',
      '2022 – «Горняк-Спорт» (Украина)',
      '2023 – «Игрос» (Польша)',
      '2023 – «Алай» (Ош, Кыргызстан)',
      'С 2024 – «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Чемпион Украины U-19 (2015)',
      'Финалист юношеской Лиги Чемпионов УЕФА (2015)',
      'Вице-чемпион Кыргызстана (2023, 2024)'
    ]
  },
  {
    'id': 22,
    'name': 'Кадырбек Шаарбеков',
    'number': 11,
    'position': 'forward',
    'positionName': 'Нападающий',
    'age': 27,
    'nationality': 'Кыргызстан',
    'matches': 10,
    'goals': 15,
    'assists': 22,
    'rating': 8.7,
    'image': 'https://fc-dordoi.kg/images/stories/photos/mar_2025/shaarbekov_1.jpg',
    'height': '181 см',
    'weight': '70 кг',
    'birthDate': '02.02.1998',
    'career': [
      '2009-2010 – «Алга» (Бишкек, Кыргызстан)',
      '2010-2018 - «Дордой» (Бишкек, Кыргызстан)',
      '2019 – «Илбирс» (Бишкек, Кыргызстан)',
      '2020-2023 – «Алга» (Бишкек, Кыргызстан)',
      '2023 – «Афиф» (Афиа, Саудовская Аравия)',
      '2024 – «Мурас Юнайтед» (Джалал-Абад, Кыргызстан)',
      'С 2025 – «Дордой» (Бишкек, Кыргызстан)'
    ],
    'achievements': [
      'Чемпион Кыргызстана (2018)',
      'Обладатель Кубка Кыргызстана (2018, 2024)'
    ]
  },
        ]
        
        for player_data in players_data:
            Player.objects.create(
                name=player_data['name'],
                number=player_data['number'],
                position=player_data['position'],
                positionName=player_data['positionName'],
                age=player_data['age'],
                nationality=player_data['nationality'],
                matches=player_data['matches'],
                goals=player_data['goals'],
                assists=player_data['assists'],
                rating=player_data['rating'],
                image=player_data['image'],
                height=player_data['height'],
                weight=player_data['weight'],
                birthDate=player_data['birthDate'],
                # career и achievements можно сохранить как JSON
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully imported players'))