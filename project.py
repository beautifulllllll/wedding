import tkinter as tk

# 버튼을 눌렀을 때 실행되는 함수
def make_message():
    groom = groom_entry.get()      # 신랑 이름 가져오기
    bride = bride_entry.get()      # 신부 이름 가져오기

    result.config(
        text="10월 11일"f" {groom}님과 {bride}님의 결혼을\n"
             f"진심으로 축하드립니다!\n"
             f"엘로힘 하나님 안에서 행복한 가정을 이루시길 바랍니다."
    )

# 창 만들기
window = tk.Tk()
window.title("💍 결혼 축하 프로그램")
window.geometry("500x350")

# 제목
title = tk.Label(
    window,
    text="💍 결혼 축하 프로그램",
    font=("prentendard", 18)
)
title.pack(pady=10)

# 신랑
tk.Label(window, text="신랑 이름").pack()
groom_entry = tk.Entry(window, width=30)
groom_entry.pack()

# 신부
tk.Label(window, text="신부 이름").pack()
bride_entry = tk.Entry(window, width=30)
bride_entry.pack(pady=5)

# 버튼
button = tk.Button(
    window,
    text="축하 메시지 만들기",
    command=make_message
)
button.pack(pady=10)

# 결과 출력(Label)
result = tk.Label(
    window,
    text="",
    font=("prentendard", 12),
    justify="center"
)
result.pack(pady=20)

window.mainloop()