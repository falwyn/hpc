class Worker:
    def __init__(self, worker_id, name, sex, birth, base_salary, salary_rate):
        """
        Constructor for the Worker class.
        """
        self.worker_id = worker_id
        self.name = name
        self.sex = sex
        self.birth = birth
        self.base_salary = base_salary
        self.salary_rate = salary_rate
        self.update_total_salary()

    def update_total_salary(self):
        """
        Calculates the total salary based on base salary and rate.
        """
        self.total_salary = self.base_salary * self.salary_rate

    def display_info(self):
        """
        Prints the worker's information in a readable format.
        """
        print("-" * 20)
        print(f"Ma nhan vien: {self.worker_id}")
        print(f"Ten: {self.name}")
        print(f"Gioi tinh: {self.sex}")
        print(f"Ngay sinh: {self.birth}")
        print(f"Luong co ban: {self.base_salary:,.0f}") # Format for readability
        print(f"He so luong: {self.salary_rate}")
        print(f"Thuc linh: {self.total_salary:,.0f}") # Format for readability
        print("-" * 20)


def find_worker_by_id(workers, worker_id):
    for worker in workers:
        if worker.worker_id == worker_id:
            return worker
    return None


def main():
    print("---- QUAN LY NHAN VIEN ----")

    print("0. Thoat chuong trinh")
    print("1. Them nhan vien")
    print("2. Cap nhat thong tin nhan vien boi ID")
    print("3. Xoa nhan vien boi ID")
    print("4. Tim kiem nhan vien theo ID")
    print("5. Sap xep nhan vien theo thuc linh (giam dan)")
    print("6. Hien thi danh sach nhan vien")

    workers = []

    while True:
        try:
            choice = int(input("\nNhap lua chon: "))
        except ValueError:
            print("Vui long nhap mot so.")
            continue

        match choice:
            case 0:
                print("Dang thoat chuong trinh...")
                exit()

            case 1:
                worker_id = input("Nhap ma nhan vien: ")
                if find_worker_by_id(workers, worker_id) is not None:
                    print(f"Loi: Ma nhan vien '{worker_id}' da ton tai.")
                    continue

                name = input("Nhap ten nhan vien: ")
                sex = input("Nhap gioi tinh: ")
                birth = input("Nhap ngay sinh (dd/mm/yyyy): ")
                base_salary = float(input("Nhap luong co ban: "))
                salary_rate = float(input("Nhap he so luong: "))

                new_worker = Worker(worker_id, name, sex, birth, base_salary, salary_rate)
                workers.append(new_worker)
                print(f"Da them nhan vien '{name}' thanh cong!")


            case 2:
                if not workers:
                    print("Danh sach nhan vien trong.")
                    continue
                
                worker_id = input("Nhap ma nhan vien muon cap nhat: ")
                worker_to_update = find_worker_by_id(workers, worker_id)

                if worker_to_update:
                    print("Tim thay nhan vien. Nhap thong tin moi:")
                    worker_to_update.name = input(f"Nhap ten moi (hien tai: {worker_to_update.name}): ")
                    worker_to_update.sex = input(f"Nhap gioi tinh moi (hien tai: {worker_to_update.sex}): ")
                    worker_to_update.birth = input(f"Nhap ngay sinh moi (hien tai: {worker_to_update.birth}): ")
                    worker_to_update.base_salary = float(input(f"Nhap luong co ban moi (hien tai: {worker_to_update.base_salary}): "))
                    worker_to_update.salary_rate = float(input(f"Nhap he so luong moi (hien tai: {worker_to_update.salary_rate}): "))
                    
                    worker_to_update.update_total_salary()
                    print("Da cap nhat thong tin nhan vien thanh cong!")
                else:
                    print(f"Khong tim thay nhan vien voi ma '{worker_id}'.")

            case 3:
                if not workers:
                    print("Danh sach nhan vien trong.")
                    continue
                
                worker_id = input("Nhap ma nhan vien muon xoa: ")
                worker_to_delete = find_worker_by_id(workers, worker_id)

                if worker_to_delete:
                    workers.remove(worker_to_delete)
                    print(f"Da xoa nhan vien co ma '{worker_id}' thanh cong.")
                else:
                    print(f"Khong tim thay nhan vien voi ma '{worker_id}'.")

            case 4:
                if not workers:
                    print("Danh sach nhan vien trong.")
                    continue

                worker_id = input("Nhap ma nhan vien muon tim: ")
                found_worker = find_worker_by_id(workers, worker_id)

                if found_worker:
                    print("Thong tin nhan vien:")
                    found_worker.display_info()
                else:
                    print(f"Khong tim thay nhan vien voi ma '{worker_id}'.")

            case 5:
                if not workers:
                    print("Danh sach nhan vien trong.")
                    continue
                
                workers.sort(key=lambda worker: worker.total_salary, reverse=True)
                print("Da sap xep danh sach nhan vien theo thuc linh giam dan.")
                for worker in workers:
                    worker.display_info()

            case 6:
                if not workers:
                    print("Danh sach nhan vien trong.")
                else:
                    print("\n--- DANH SACH NHAN VIEN ---")
                    for worker in workers:
                        worker.display_info()

            case _:
                print("Lua chon khong hop le. Vui long chon lai.")


if __name__ == "__main__":
    main()
