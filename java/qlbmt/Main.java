import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ComputerStore store = new ComputerStore();

        AddComputer addComputer = new AddComputer();
        DisplayAllComputers displayAll = new DisplayAllComputers();
        FindComputer findComputer = new FindComputer();
        SellComputer sellComputer = new SellComputer();
        DisplayRevenue displayRevenue = new DisplayRevenue();
        DeleteComputer deleteComputer = new DeleteComputer();

        int choice = -1;

        while (choice != 0) {
            System.out.println("\n--- CHƯƠNG TRÌNH QUẢN LÝ BÁN MÁY TÍNH ---");
            System.out.println("1. Thêm máy tính mới");
            System.out.println("2. Hiển thị tất cả sản phẩm");
            System.out.println("3. Tìm kiếm máy tính");
            System.out.println("4. Bán máy tính");
            System.out.println("5. Xem tổng doanh thu");
            System.out.println("6. Xóa sản phẩm");
            System.out.println("0. Thoát chương trình");
            System.out.print("Vui lòng chọn chức năng: ");

            try {
                choice = scanner.nextInt();
                scanner.nextLine(); 
                switch (choice) {
                    case 1:
                        addComputer.execute(store, scanner);
                        break;
                    case 2:
                        displayAll.execute(store);
                        break;
                    case 3:
                        findComputer.execute(store, scanner);
                        break;
                    case 4:
                        sellComputer.execute(store, scanner);
                        break;
                    case 5:
                        displayRevenue.execute(store);
                        break;
                    case 6:
                        deleteComputer.execute(store, scanner);
                        break;
                    case 0:
                        System.out.println("Đang thoát chương trình...");
                        break;
                    default:
                        System.out.println("Lựa chọn không hợp lệ. Vui lòng chọn lại.");
                        break;
                }
            } catch (Exception e) {
                System.out.println("Dữ liệu nhập không hợp lệ. Vui lòng thử lại.");
                scanner.nextLine(); // Clear invalid input
            }
        }
        scanner.close();
    }
}
