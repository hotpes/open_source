from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END

# 전체 할 일 보기 기능
def show_all():
    todo_list.delete(0, END)
    for work, date in todo.items():
        todo_list.insert(END, f"{work} - {date}")

# 날짜별 할 일 보기 기능
def show_by_date():
    selected_date = date_entry.get()
    todo_list.delete(0, END)                                                            #
    for work, date in todo.items():
        if date == selected_date:
            todo_list.insert(END, f"{work} - {date}")

# 할 일 추가 기능
def add_work():
    work = work_entry.get()
    date = date_entry.get()
    todo[work] = date                                                                   #
    show_all()

# 할 일 삭제 기능
def delete_work():
    selected_work = todo_list.get(todo_list.curselection())
    work, _ = selected_work.split(" - ")                                    #
    if work in todo:
        todo.pop(work)
        show_all()

# 할 일을 저장할 딕셔너리
todo = {}
list1 = []

# Tkinter 윈도우 생성
root = Tk()
root.title("할 일 관리 프로그램")

# 레이블과 입력 공간 생성
label = Label(root, text="할 일")
label.grid(row=0, column=0)

work_entry = Entry(root)
work_entry.grid(row=0, column=1)

date_label = Label(root, text="날짜")
date_label.grid(row=1, column=0)

date_entry = Entry(root)
date_entry.grid(row=1, column=1)

# 버튼 생성 및 기능 할당
add_button = Button(root, text="추가", command=add_work)
add_button.grid(row=2, column=0, columnspan=2)

show_all_button = Button(root, text="전체 보기", command=show_all)
show_all_button.grid(row=3, column=0, columnspan=2)

show_by_date_button = Button(root, text="날짜로 보기", command=show_by_date)
show_by_date_button.grid(row=4, column=0, columnspan=2)

delete_button = Button(root, text="삭제", command=delete_work)
delete_button.grid(row=5, column=0, columnspan=2)

# 할 일 목록을 표시할 리스트박스 생성
todo_list = Listbox(root)
todo_list.grid(row=6, column=0, columnspan=2)

# 스크롤바 생성
scrollbar = Scrollbar(root)
scrollbar.grid(row=6, column=2, sticky="NS")

# 리스트박스에 스크롤바 연결
todo_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todo_list.yview)

# Tkinter 메인 루프 시작
root.mainloop()
