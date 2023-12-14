# 원본 코드 출처 : https://youtu.be/bKPIcoou9N8


from tkinter import*
import tkinter.ttk as ttk
from tkinter import filedialog 
import tkinter.messagebox as msgbox
from PIL import Image
import os

root=Tk()
root.title("nado GUI")


#####################################################################

#1. 프로그램 내 함수

# 파일추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요 ", \
        filetypes = (("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
            initialdir = os.path.dirname(__file__) )
    
    for file in files:
        lst_file.insert(END, file)

# 파일제거 함수
def delete_file():
    for index in reversed(lst_file.curselection()):
        lst_file.delete(index)
        
# 저장경로 함수
def browse_dst_p():
    f_seclect = filedialog.askdirectory()
    if f_seclect == '':
        print("폴더 선택 취소")
        return
    # print(f_seclect)
    txt_dest_p.delete(0, END)
    txt_dest_p.insert(0, f_seclect)


# 이미지 합치기
def merge_img():
    
    try:
        # 넓이 처리
        img_w = cmb_width.get()
        if img_w == "원본유지":
            img_w = -1
        else:
            img_w = int(img_w)
            
            
        # 간격
        img_spc = cmb_spc.get()
        if img_spc == "좁게":
            img_spc = 30
        elif img_spc == "보통":
            img_spc = 60
        elif img_spc == "넓게":
            img_spc = 90
        else:
            img_spc = 0
            
        # 포맷
        img_format = cmb_format.get().lower()
        
        #print(lst_file.get(0, END)) #모든 파일목록 가져오기
        images = [Image.open(x) for x in lst_file.get(0, END)]
        image_sizes = []
        
        if img_w > -1:
            # 사이즈 변경
            image_sizes = [(int(img_w), int(img_w * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]
        
        widths, heights = zip(*(image_sizes))
        M_w, total_h = max(widths), sum(heights)
        
        
        # 스케치북 준비
        
        if img_spc > 0: #이미지 간격 옵션 반영
            total_h += (img_spc*(len(images)-1))
        
        res_img = Image.new("RGBA", (M_w, total_h), (255, 255, 255)) #배경: 흰색
        y_offset = 0 #y 위치정보
        
        for idx, img in enumerate(images):
            #원본유지 아니면, 이미지 크기조정
            if img_w > -1:
                img = img.resize(image_sizes[idx])
            
            res_img.paste(img, (0, y_offset))
            y_offset += (img.size[1]+img_spc) # height값 + 사용자지정 간격
            
            progress = (idx + 1) / len(images) * 100 # %단위 진척도 
            p_var.set(progress)
            prog_bar.update()
            
            
        # 포맷옵션 처리
        file_name = "emerged_photo." + img_format  # 실행 결과의 파일명
        dest_p = os.path.join(txt_dest_p.get(), file_name)
        res_img.save(dest_p)
        msgbox.showinfo("Info", "작업이 완료됬어요")
        
    except Exception as err:
        msgbox.showerror("에러 발생", err)
    
    
#####################################################################
    
    
# 2. 시작 함수

def start():
    # 파일목록 확인
    if lst_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    
    # 저장경로 확인
    if len(txt_dest_p.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return
    
    # 이미지 통합
    merge_img()



#####################################################################

# 3. 프레임, 라벨 및 콤보 정의 및 지정

# 파일프레임
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

bt_addfile = Button(file_frame, padx = 5, pady = 5, width = 12, text = "파일 추가", command = add_file)
bt_addfile.pack(side = "left")
bt_delfile = Button(file_frame, padx = 5, pady = 5, width = 12, text = "선택 삭제", command = delete_file)
bt_delfile.pack(side = "right")

# 리스트프레임
lst_frame = Frame(root)
lst_frame.pack(fill = "both", padx = 5, pady = 5)

scb = Scrollbar(lst_frame)
scb.pack(side = "right", fill = "y")

lst_file = Listbox(lst_frame, selectmode = "extended", height = 15, yscrollcommand = scb.set)
lst_file.pack(side = "left", fill = "both", expand = True)
scb.config(command = lst_file.yview)


# 저장경로 프레임

path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill = "x", padx = 5, pady = 5)

txt_dest_p = Entry(path_frame) # Text() 면 ("1.0", END)
txt_dest_p.pack(side = "left", fill = "x", expand = True, padx = 5, pady = 5, ipady = 4)

bt_dest_p = Button(path_frame, text = "찾아보기", width = 10, command = browse_dst_p)
bt_dest_p.pack(side="right", padx = 5, pady = 5,)

# 옵션프레임
frame_opt = LabelFrame(root, text = "옵션 프레임")
frame_opt.pack(padx = 5, pady = 5, ipady = 5)

# 가로넓이 라벨
lab_width = Label(frame_opt, text = "가로 넓이", width = 8)
lab_width.pack(side = "left", padx = 5, pady = 5)

# 가로넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_opt, state = "readonly", values = opt_width, width = 10)
cmb_width.current(0)
cmb_width.pack(side = "left", padx = 5, pady = 5)


# 간격
# 간격 라벨
lab_spc = Label(frame_opt, text = "간격", width = 8)
lab_spc.pack(side = "left", padx = 5, pady = 5)

# 간격 콤보
opt_spc = ["없음", "좁게", "보통", "넓게"]
cmb_spc = ttk.Combobox(frame_opt, state = "readonly", values = opt_spc, width = 10)
cmb_spc.current(0)
cmb_spc.pack(side = "left", padx = 5, pady = 5)


# 파일포맷
# 파일포맷 라벨
lab_format = Label(frame_opt, text = "포맷", width = 8)
lab_format.pack(side = "left", padx = 5, pady = 5)

# 파일포맷 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_opt, state = "readonly", values = opt_format, width = 10)
cmb_format.current(0)
cmb_format.pack(side = "left", padx = 5, pady = 5)

# 진행 상황
frame_prog = LabelFrame(root, text = "진행상황")
frame_prog.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

p_var = DoubleVar()
prog_bar = ttk.Progressbar(frame_prog, maximum = 100, variable = p_var)
prog_bar.pack(fill = "x", padx = 5, pady = 5)


# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill = "x", padx = 5, pady = 5)

bt_cl = Button(frame_run, padx = 5, pady = 5, text = "닫기", width = 12, command = root.quit)
bt_cl.pack(side = "right", padx = 5, pady = 5)

bt_st = Button(frame_run, padx = 5, pady = 5, text = "시작", width = 12, command = start)
bt_st.pack(side = "right", padx = 5, pady = 5)

root.resizable(False, False)
root.mainloop()
