import random
import sys
# Модули Qt - для графики
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem  # Таблица
from qtconsole.qt import QtGui

import design  # Объявление всей графики, автосгенерированно


# Главный класс, описывает приложение
class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Вызов конструктора родителей
        self.setupUi(self)  # Построение графики из design

        self.part = 1  # Часть месяца
        self.month = 1
        # Для хранения значений кол-ва продажи/покупки
        self.spinValue = 0

        self.corps = [Corp() for _ in range(3)]  # Юзер и ИИ
        # Добавление в таблицу всех игроков, обновление стат
        self.add_to_table()
        self.update_corp()
        self.month_lcd.display(self.month)
        # Привязка кнопок к функциям
        self.build_f_button.clicked.connect(self.build_f)
        self.build_af_button.clicked.connect(self.build_af)

        self.open_f_button.clicked.connect(self.open_f)
        self.open_af_button.clicked.connect(self.open_af)
        self.close_f_button.clicked.connect(self.close_f)
        self.close_af_button.clicked.connect(self.close_af)

        self.update_f.clicked.connect(self.upd_f)
        self.pushButton.clicked.connect(self.turn)

        # Запрет редактирования таблиц
        self.bank_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.players_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.turn()  # Ход игрока и ИИ

    # Добавить в таблицу игроков
    def add_to_table(self):
        for i in range(len(self.corps)):
            self.players_table.insertRow(i)  # Добавление ряда

            # Добавление ячеек таблицы, соответствующих игроку - имя, деньги, фабрика
            self.players_table.setItem(i, 0, QTableWidgetItem(("Player" if i == 0 else "Bot " + str(i)) + " Corp."))
            self.players_table.setItem(i, 1, QTableWidgetItem(str(self.corps[i].money)))
            self.players_table.setItem(i, 2, QTableWidgetItem(str(self.corps[i].factories
                                                                  + self.corps[i].auto_factories)))

    # Постройка
    def build_f(self):
        self.corps[0].build_f()
        self.update_corp()
        self.update_table()

    def build_af(self):
        self.corps[0].build_af()
        self.update_corp()
        self.update_table()

    # Обновление фабрики в автофабрику
    def upd_f(self):
        self.corps[0].update_f()
        self.update_corp()
        self.update_table()

    # Закрытие фабрики
    def close_f(self):
        self.corps[0].close_f()
        self.update_corp()
        self.update_table()

    def close_af(self):
        self.corps[0].close_af()
        self.update_corp()
        self.update_table()

    # Открытие закрытой фабрики
    def open_f(self):
        self.corps[0].open_f()
        self.update_corp()
        self.update_table()

    def open_af(self):
        self.corps[0].open_af()
        self.update_corp()
        self.update_table()

    # Обновление таблицы, для отсеивания банкротов
    def update_table(self):
        for i in range(len(self.corps)):
            self.players_table.setItem(i, 1, QTableWidgetItem(str(self.corps[i].money)))
            self.players_table.setItem(i, 2, QTableWidgetItem(str(self.corps[i].factories
                                                                  + self.corps[i].auto_factories)))

    # Обновление стат
    def update_corp(self):
        if self.corps:
            self.money_lcd.display(self.corps[0].money)
            self.factory_lcd.display(self.corps[0].factories)
            self.auto_lcd.display(self.corps[0].auto_factories)
            self.closed_auto_lcd.display(len(self.corps[0].closed_af) + len(self.corps[0].building_af))
            self.closed_lcd.display(len(self.corps[0].closed_f) + len(self.corps[0].building_f))
            self.prod_lcd.display(self.corps[0].production)
            self.mats_lcd.display(self.corps[0].materials)

    # Ход
    def turn(self):
        # Отображение инфы над полем ввода
        self.label.setText({
                               -1: "GAME OVER",
                               1: "Сколько ЕСМ вы хотите купить?",
                               2: "Установите закупочную цену",
                               3: "Сколько ЕГП вы хотите произвести?",
                               4: "Сколько ЕГП вы хотите продать?",
                               5: "Установите цену продажи",
                               6: "Размер занимаемой ссуды (0 для отмены):",
                               7: "Конец месяца (OK чтобы начать следующий)"
                           }[self.part])

        if self.part == 1:
            # Вычет денег у игроков
            for corp in self.corps:
                corp.money -= corp.materials * 300
                corp.money -= corp.production * 500
                corp.money -= corp.factories * 1000
                corp.money -= corp.auto_factories * 1500
                # Проверка на банкротство
                self.check_corp(corp)

            # Возможные ситуации на рынке - [Кол-во ЕСМ, Цена, Кол-во ЕГП, цена]
            banks = [[len(self.corps), 800, 3 * len(self.corps), 6500],
                     [int(1.5 * len(self.corps)), 650, int(2.5 * len(self.corps)), 6000],
                     [int(1.5 * len(self.corps)), 500, int(2 * len(self.corps)), 5500],
                     [int(1.5 * len(self.corps)), 400, int(1.5 * len(self.corps)), 5000],
                     [int(1.5 * len(self.corps)), 300, int(1 * len(self.corps)), 4500]]

            # Взвешенный выбор ситуации на рынке и установление в таблицу
            chosen_level = random.choices(banks, weights=(15, 25, 20, 25, 15))
            for i in range(4):
                self.bank_table.item(0, i).setText(str(chosen_level[0][i]))

            # Отображение и переход к следующим
            self.update_corp()
            self.update_table()
            self.part += 1

        elif self.part == 2:
            # Запрашиваем у пользователя значение кол-ва ЕСМ
            self.spinValue = self.spinBox.value()
            self.spinBox.setValue(0)
            self.part += 1

        elif self.part == 3:
            # Добавляем заказы на покупку, сначала игрока
            orders = []
            if self.spinBox.value() >= int(self.bank_table.item(0, 1).text()):
                orders.append([self.spinValue, self.spinBox.value(), self.corps[0]])
                self.spinBox.setValue(0)

            # Потом ИИ
            for corp in self.corps[1:]:
                order = corp.set_buy(*[int(self.bank_table.item(0, i).text()) for i in range(2)])
                # Если вернул не None - в заказы
                if order:
                    orders.append(order)
            # Если есть заказ
            if any(orders):
                orders.sort(key=lambda x: x[1], reverse=True)  # сортировка по цене, сначала наибольшие

                mats = int(self.bank_table.item(0, 0).text())  # Количество ЕСМ на продажу из таблицы

                while mats > 0 and any(orders):
                    # Бере каждый заказ и выполняем, пока есть заказы и ЕСМ
                    order = orders.pop(0)
                    order[2].materials += order[0]
                    mats -= order[0]
                    order[2].money -= order[1] * order[0]
                # Проверка и обновление игроков
                self.check_corp(self.corps[0])
                self.update_corp()
                self.update_table()

            self.part += 1

        elif self.part == 4:
            # Производство, спрашиваем у игрока, потом производит игрок и ИИ
            self.corps[0].produce_corp(self.spinBox.value())
            for corp in self.corps[1:]:
                corp.produce(int(self.bank_table.item(0, 3).text()))
                self.check_corp(corp)

            self.check_corp(self.corps[0])
            self.update_corp()
            self.update_table()

            self.part += 1

        elif self.part == 5:
            self.spinValue = self.spinBox.value()
            self.spinBox.setValue(0)
            self.part += 1

        elif self.part == 6:
            # Продажа ЕГП, аналогична покупке ЕСМ
            orders = []
            if self.spinBox.value() < int(self.bank_table.item(0, 3).text()):
                orders.append([self.spinValue, self.spinBox.value(), self.corps[0]])
                self.spinBox.setValue(0)

            for corp in self.corps[1:]:
                size = int(self.bank_table.item(0, 2).text())
                price = int(self.bank_table.item(0, 3).text())
                order = corp.set_sell(size, price)
                if order:
                    orders.append(order)

            if any(orders):
                orders.sort(key=lambda x: x[1])

                prods = int(self.bank_table.item(0, 2).text())

                while prods > 0 and any(orders):
                    order = orders.pop(0)
                    order[2].production -= order[0]
                    prods -= order[0]
                    order[2].money += order[1] * order[0]

                self.check_corp(self.corps[0])
                self.update_corp()
                self.update_table()

            self.part += 1

        elif self.part == 7:
            # Заемы, сначала вычитаем за каждый долг 1 %
            for corp in self.corps:
                for loan in corp.loans:
                    corp.money = int(corp.money - loan[0] * 0.01)
                    loan[1] -= 1
                    # Если долг нужно выплачивать - выплачиваем и удалям
                    if loan[1] == 0:
                        corp.money -= loan[0]
                        corp.loans.remove(loan)
                self.check_corp(corp)
            if self.spinBox.value():
                # Если игрок ввел сумму - пытаемся получить заем
                self.corps[0].set_loan(self.spinBox.value())
            for corp in self.corps[1:]:
                corp.get_loan()  # ИИ думает о заеме

            self.check_corp(self.corps[0])

            # Тикает время для всех заводов - открывающихся, обновляющихся, строящихся
            for corp in self.corps:
                for fact in corp.closed_f:
                    fact -= 1
                    if fact == 0:
                        corp.closed_f.remove(fact)
                        corp.factories += 1

                for fact in corp.closed_af:
                    fact -= 1
                    if fact == 0:
                        corp.closed_af.remove(fact)
                        corp.auto_factories += 1

                for fact in corp.building_f:
                    fact -= 1
                    if fact == 1:
                        corp.money -= 2500
                    elif fact == 0:
                        corp.factories += 1
                        corp.building_f.remove(fact)

                for fact in corp.building_af:
                    fact -= 1
                    if fact == 1:
                        corp.money -= 5000
                    elif fact == 0:
                        corp.auto_factories += 1
                        corp.building_af.remove(fact)

                for fact in corp.renovating:
                    fact -= 1
                    if fact == 0:
                        corp.factories -= 1
                        corp.auto_factories += 1

            for corp in self.corps[1:]:
                corp.consider_factory()  # ИИ думает над заводом

            self.month += 1
            self.part = 1

            # Игра заканчивается на 16 месяц
            if self.month > 15:
                self.label.setText("GAME OVER")
                self.part = -2

            self.update_corp()
            self.update_table()
            self.month_lcd.display(self.month)

    # Проверка на банкротство, если денег < 0 - удаляем из списка, если игрок - игра заканчивается
    def check_corp(self, corp):
        if corp.money <= 0:
            if corp is self.corps[0]:
                self.label.setText("GAME OVER")
                self.part = -2
            else:
                self.corps.remove(corp)
                self.update_table()


# Класс игрока и ботов
class Corp:
    # Конструктор
    def __init__(self):
        self.factories = 2
        self.auto_factories = 0

        self.materials = 4
        self.production = 2
        self.money = 14200
        self.loans = []

        # Заносится сколько времени до открытия, -1 если не открывается
        self.closed_f = []
        self.closed_af = []
        self.renovating = []
        # Строящиеся
        self.building_f = []
        self.building_af = []

    # Построить новую фабрику
    def build_f(self):
        total_facs = len(self.building_f) + len(self.building_f) + self.factories + self.auto_factories
        if self.money > 2500 and total_facs <= 6:
            self.building_f.append(5)
            self.money -= 2500

    # Построить новую автофабрику
    def build_af(self):
        total_facs = len(self.building_f) + len(self.building_f) + self.factories + self.auto_factories
        if self.money > 5000 and total_facs <= 6:
            self.building_af.append(7)
            self.money -= 5000

    # Закрытие фабрик
    def close_f(self):
        if self.factories:
            self.factories -= 1
            self.closed_f.append(-1)

    def close_af(self):
        if self.auto_factories:
            self.auto_factories -= 1
            self.closed_af.append(-1)

    # Открытие фабрик
    def open_f(self):
        if -1 in self.closed_f:
            self.closed_f[self.closed_f.index(-1)] = 2

    def open_af(self):
        if -1 in self.closed_af:
            self.closed_af[self.closed_af.index(-1)] = 2

    # Фабрика -> автофабрика
    def update_f(self):
        if self.factories and self.money > 7000:
            self.renovating.append(9)
            self.money -= 7000

    # Покупка
    def set_buy(self, size, price):
        # Если слишком дорого - возвращает None. иначе пытается рандомить цену в заданных значениях
        if self.materials > self.factories + self.auto_factories * 2 or self.materials * (2000 + price) > self.money:
            return None
        else:
            b_price = random.randint(price, price * 1.5)
            mats = random.randint(0, min(1.5 * (self.factories + self.auto_factories * 2) - self.materials, size))
            if not mats:
                return None
            elif b_price * mats > self.money:
                good_price = self.money - price * mats - mats * 2300
                return [mats, good_price if good_price < b_price else b_price, self]
            return [mats, b_price, self]

    # Производство
    def produce(self, total):
        factories = self.factories + self.auto_factories * 2
        while self.materials and self.money and self.production < total and factories:
            self.money -= 2000
            self.materials -= 1
            self.production += 1
            factories -= 1

    # Производство игрока
    def produce_corp(self, to_produce):
        factories = random.randint(int(self.factories + self.auto_factories * 2 * 0.8),
                                   self.factories + self.auto_factories * 2)
        while self.materials and self.money and factories and to_produce:
            self.money -= 2000
            self.materials -= 1
            self.production += 1
            factories -= 1
            to_produce -= 1

    # Продажа
    def set_sell(self, size, price):
        if not self.production:
            return None
        else:
            return [random.randint(0, min(self.production, size)), random.randint(int(price * 0.7), price), self]

    # Думает о долге
    def get_loan(self):
        if self.money < min(self.materials * 2000, (self.factories + self.auto_factories * 2)) and self.production < 4:
            self.set_loan(min(self.materials * 2000, (self.factories + self.auto_factories * 2)))

    # Занимает
    def set_loan(self, summ):
        if summ < self.factories * 2500 + self.auto_factories * 5000:
            self.loans.append([summ, 12])
            self.money += summ

    # Если есть деньги - строит завод
    def consider_factory(self):
        if self.materials >= (self.factories + self.auto_factories):
            if self.money - self.materials * 2000 > 12000:
                self.build_af()
            elif self.money - self.materials * 2000 > 8000:
                self.update_f()
            elif self.money - self.materials * 2000 > 6000:
                self.build_f()


# Запуск приложения, передаются системные аргументы, его отображение и выполнение кода
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если запущен от себя, а не импортирован
    main()
