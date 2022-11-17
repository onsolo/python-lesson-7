from tkinter import *
from tkinter import ttk
from controllers.MainController import PhoneController


class MainView:
    def __init__(self):
        self.window = Tk()
        self.phone_number = None
        self.phone_name = None
        self.phone_address = None
        self.controller = PhoneController()
        self.numbers = []

        columns = ("#1", "#2", "#3", "#4")
        self.table = ttk.Treeview(show="headings", columns=columns)
        self.table.heading("#1", text="ID")
        self.table.heading("#2", text="Телефон")
        self.table.heading("#3", text="Имя")
        self.table.heading("#4", text="Адрес")

        self.query = None

    def createPhone(self):
        self.controller.create(
            self.phone_number.get(),
            self.phone_name.get(),
            self.phone_address.get()
        )

        self.phone_number.delete(0, END)
        self.phone_name.delete(0, END)
        self.phone_address.delete(0, END)

        self.updateTable()

    def updateTable(self):
        self.numbers = self.controller.get(self.query.get())
        for item in self.table.get_children():
            self.table.delete(item)
        for number in self.numbers:
            self.table.insert('', 'end', values=number.getAttributes())

    def deletePhone(self):
        table_id = self.table.focus()
        item = self.table.item(table_id)
        self.controller.delete(item['values'][0])
        self.updateTable()

    def clearQuery(self):
        self.query.delete(0, 'end')
        self.updateTable()

    def createHTML(self):
        self.controller.exportHTML(self.numbers)

    def createXML(self):
        self.controller.exportXML(self.numbers)

    def initView(self):
        self.window.title('Телефонный справочник')
        Label(text='Телефонный справочник', font=('Arial', 14), pady=5, padx=5).pack()

        # Форма добавления элемента справочника

        master_from_frame = Frame(master=self.window)
        master_from_frame.pack(padx=10, pady=10)

        form_frame_1 = Frame(master=master_from_frame)
        form_frame_1.pack(side=LEFT)
        Label(master=form_frame_1, text='Номер телефона', justify=LEFT).pack()
        self.phone_number = Entry(master=form_frame_1)
        self.phone_number.pack()

        form_frame_2 = Frame(master=master_from_frame)
        form_frame_2.pack(side=LEFT)
        Label(master=form_frame_2, text='Имя абонента', justify=LEFT).pack()
        self.phone_name = Entry(master=form_frame_2)
        self.phone_name.pack()

        form_frame_3 = Frame(master=master_from_frame)
        form_frame_3.pack(side=LEFT)
        Label(master=form_frame_3, text='Адрес абонента', justify=LEFT).pack()
        self.phone_address = Entry(master=form_frame_3)
        self.phone_address.pack()

        form_frame_4 = Frame(master=master_from_frame)
        form_frame_4.pack(side=LEFT, fill=BOTH, expand=True)
        Button(master=form_frame_4, text='Создать абонента', command=self.createPhone).pack(side=LEFT, fill=BOTH, anchor='w')

        # Форма поиска

        master_search_frame = Frame(master=self.window)
        master_search_frame.pack()

        search_frame_1 = Frame(master=master_search_frame)
        search_frame_1.pack(side=LEFT)
        Label(master=search_frame_1, text='Поиск по имени').pack()
        self.query = Entry(master=search_frame_1)
        self.query.pack()

        search_frame_2 = Frame(master=master_search_frame)
        search_frame_2.pack(side=LEFT, fill=BOTH, expand=True)
        Button(master=search_frame_2, text='Найти', command=self.updateTable).pack(side=LEFT, fill=BOTH, anchor='w')
        Button(master=search_frame_2, text='Сбросить поиск', command=self.clearQuery).pack(side=LEFT, fill=BOTH, anchor='w')

        # Список справочника

        master_list_frame = Frame(master=self.window)
        master_list_frame.pack(side=LEFT)

        self.table.master = master_list_frame
        self.table.pack()

        # Управления справочником

        master_control_frame = Frame(master=self.window)
        master_control_frame.pack(side=LEFT)

        Button(master=master_control_frame, text='Удалить', command=self.deletePhone).pack(side=LEFT)
        Button(master=master_control_frame, text='Экспорт xml', command=self.createXML).pack(side=LEFT)
        Button(master=master_control_frame, text='Экспорт html', command=self.createHTML).pack(side=LEFT)

        # Инициализация

        self.updateTable()
        self.window.mainloop()
