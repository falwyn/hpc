import sys

class Student:
    _id_counter = 0

    def __init__(
        self,
        name: str,
        gender: str,
        age: int,
        math_score: float,
        physics_score: float,
        chemistry_score: float,
    ):
        if not (0 <= math_score <= 10 and 0 <= physics_score <= 10 and 0 <= chemistry_score <= 10):
            raise ValueError("Diem so phai nam trong khoang tu 0 den 10.")

        self.student_id = Student._id_counter
        Student._id_counter += 1
        
        self.name = name
        self.gender = gender
        self.age = age
        self.math_score = math_score
        self.physics_score = physics_score
        self.chemistry_score = chemistry_score
        
        self.update_student_average_score()
        self.update_student_rank()

    def update_student_rank(self):
        if self.average_score >= 8:
            self.student_rank = "Gioi"
        elif self.average_score >= 6.5:
            self.student_rank = "Kha"
        elif self.average_score >= 5:
            self.student_rank = "Trung Binh"
        else:
            self.student_rank = "Yeu"

    def update_student_average_score(self):
        self.average_score = (self.math_score + self.physics_score + self.chemistry_score) / 3

    def display_info(self):
        print("---------------")
        print(f"Id: {self.student_id}")
        print(f"Ten: {self.name}")
        print(f"Gioi tinh: {self.gender}")
        print(f"Tuoi: {self.age}")
        print(f"Diem toan: {self.math_score}")
        print(f"Diem ly: {self.physics_score}")
        print(f"Diem hoa: {self.chemistry_score}")
        print(f"Diem trung binh: {self.average_score:.2f}")
        print(f"Hoc luc: {self.student_rank}")
        print("---------------")

def find_student_by_id(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

def main():
    print("---- QUAN LY SINH VIEN ----")

    print("0. Thoat chuong trinh")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien boi ID")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo ten (A-Z)")
    print("6. Sap xep sinh vien theo diem trung binh (Thap - Cao)")
    print("7. Sap xep sinh vien theo ID (Tang dan)")
    print("8. Sap xep sinh vien theo ID (Giam dan)")
    print("9. Hien thi danh sach sinh vien")

    students = []

    while True:
        try:
            choice = int(input("\nNhap lua chon: "))
        except ValueError:
            print("Lua chon phai la mot so. Vui long thu lai.")
            continue
        
        if choice in [2, 3, 4, 5, 6, 7, 8, 9] and not students:
            print("Danh sach sinh vien trong.")
            continue

        match choice:
            case 0:
                print("Dang thoat chuong trinh...")
                sys.exit()
            case 1:
                try:
                    name = input("Nhap ten sinh vien: ")
                    gender = input("Nhap gioi tinh: ")
                    age = int(input("Nhap tuoi: "))
                    math_score = float(input("Nhap diem toan: "))
                    physics_score = float(input("Nhap diem ly: "))
                    chemistry_score = float(input("Nhap diem hoa: "))
                    
                    student = Student(name, gender, age, math_score, physics_score, chemistry_score)
                    students.append(student)
                    print(f"Them sinh vien '{name}' thanh cong voi ID la {student.student_id}.")

                except ValueError as e:
                    print(f"Loi: {e}. Khong the them sinh vien.")

            case 2: 
                student_id = int(input("Nhap ma sinh vien muon cap nhat: "))
                student_to_update = find_student_by_id(students, student_id)
                
                if student_to_update:
                    print(f"Cap nhat thong tin cho sinh vien: {student_to_update.name}")
                    student_to_update.name = input("Nhap ten moi: ")
                    student_to_update.age = int(input("Nhap tuoi moi: "))
                    print("Da cap nhat thanh cong!")
                else:
                    print(f"Khong tim thay sinh vien voi ma {student_id}")

            case 3: 
                student_id = int(input("Nhap ma sinh vien muon xoa: "))
                student_to_delete = find_student_by_id(students, student_id)
                
                if student_to_delete:
                    students.remove(student_to_delete)
                    print(f"Da xoa sinh vien co ma {student_id} ({student_to_delete.name}).")
                else:
                    print(f"Khong tim thay sinh vien voi ma {student_id}")

            case 4: 
                name = input("Nhap ten sinh vien muon tim: ")
                found_students = [s for s in students if name.lower() in s.name.lower()]
                
                if found_students:
                    print(f"Tim thay {len(found_students)} sinh vien co ten chua '{name}':")
                    for student in found_students:
                        student.display_info()
                else:
                    print(f"Khong tim thay sinh vien nao co ten la {name}")

            case 5: 
                students.sort(key=lambda s: s.name)
                print("Da sap xep danh sach theo ten.")
                for s in students: s.display_info()

            case 6: 
                students.sort(key=lambda s: s.average_score)
                print("Da sap xep danh sach theo diem trung binh (thap den cao).")
                for s in students: s.display_info()

            case 7: 
                students.sort(key=lambda s: s.student_id)
                print("Da sap xep danh sach theo ID (tang dan).")
                for s in students: s.display_info()

            case 8: 
                students.sort(key=lambda s: s.student_id, reverse=True)
                print("Da sap xep danh sach theo ID (giam dan).")
                for s in students: s.display_info()

            case 9:
                print("\n--- DANH SACH SINH VIEN ---")
                for student in students:
                    student.display_info()
            case _:
                print("Lua chon khong hop le. Vui long chon lai.")


if __name__ == "__main__":
    main()
