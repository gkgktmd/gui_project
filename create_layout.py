from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.title('project')

#시작
def start():
    print('가로넓이:', cmb_width.get())
    #get함수를 통해 어떤 것이 선택되어있는지 가져오기
    print('간격:', cmb_space.get())
    print('포멧:', cmb_format.get())

#레이아웃을 잡을때는 프레임 단위로 관리하는 것이 편함
#파일 프레임
file_frame=Frame(root)
file_frame.pack(fill='x', padx=5, pady=5) #간격 띄우기

btn_add_file=Button(file_frame, padx=5,pady=5,width=10,text='파일추가')
btn_add_file.pack(side='left')
btn_del_file=Button(file_frame, padx=5,pady=5,width=10,text='선택삭제')
btn_del_file.pack(side='right')

#리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar=Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file=Listbox(list_frame, selectmode='extended', height=15, yscrollcommand= scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

#저장경로 프레임
path_frame=LabelFrame(root, text='저장경로', padx=5, pady=5)
path_frame.pack(fill='x', padx=5, pady=5)

txt_dest_path=Entry(path_frame)
txt_dest_path.pack(side='left',fill='x',expand=True,ipady=4, padx=5, pady=5)

btn_dest_path=Button(path_frame, text='찾아보기', width=10)
btn_dest_path.pack(side='right', padx=5, pady=5)

#옵션 프레임
frame_option=LabelFrame(root,text='옵션', padx=5, pady=5)
frame_option.pack(padx=5, pady=5)

# 1. 가로 넓이 옵션
lbl_width=Label(frame_option, text='가로넓이', width=8)
lbl_width.pack(side='left', padx=5, pady=5)
#가로 넓이 콤보박스
opt_width=['원본유지','1024','800','640']
cmb_width=ttk.Combobox(frame_option,state='readonly', values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side='left', padx=5, pady=5)

#2.간격 옵션
lbl_space=Label(frame_option, text='간격', width=8)
lbl_space.pack(side='left', padx=5, pady=5)
#간격옵션 콤보박스
opt_space=['없음','좁게','보통','넓게']
cmb_space=ttk.Combobox(frame_option,state='readonly', values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side='left', padx=5, pady=5)

#3.파일 포멧 옵션
lbl_format=Label(frame_option, text='포멧', width=8)
lbl_format.pack(side='left', padx=5, pady=5)
#파일 포멧 콤보박스
opt_format=['PNG','JPG','BMP']
cmb_format=ttk.Combobox(frame_option,state='readonly', values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side='left', padx=5, pady=5)

#실행 프레임
frame_run=Frame(root)
#프레임에 이름이 필요하면 FrameLabel, 필요없다면 Frame
frame_run.pack(fill='x', padx=5, pady=5)

btn_close=Button(frame_run, padx=5, pady=5, width=12, text='닫기', command=root.quit)
#root.quit는 종료하는 내부 함수
btn_close.pack(side='right', padx=5, pady=5)

btn_start=Button(frame_run, padx=5, pady=5, width=12, text='시작', command=start)
btn_start.pack(side='right', padx=5, pady=5)

root.resizable(False,False)
root.mainloop()