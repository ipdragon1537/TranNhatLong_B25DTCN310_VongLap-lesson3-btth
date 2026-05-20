while True:
    number_of_employees = int(input("Nhập số lượng nhân viên: "))
    for i in range(0 , number_of_employees):
        print(f"Số lượng nhân viên: {number_of_employees}")
        name = input("Tên nhân viên: ")
        number_of_work_days = int(input("Số ngày đi làm: "))

        print("--- THÔNG TIN NHÂN VIÊN ---")
        print(f"Tên: {name}")
        print(f"Số ngày đi làm: {number_of_work_days}")

        if number_of_work_days < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")


    choice = input("Tiếp tục chương trình? (y/n): ")
    if choice == "n" or choice == "N":
            print("Chương trình kết thúc")
            exit()
