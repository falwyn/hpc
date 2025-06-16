import java.util.Scanner;

public class AddComputer {
    public void execute(ComputerStore store, Scanner scanner) {
        System.out.println("--- THÊM MÁY TÍNH MỚI ---");
        System.out.print("Nhập mã sản phẩm: ");
        String id = scanner.nextLine();

        for (Computer existingComputer : store.getComputers()) {
            if (existingComputer.getId().equalsIgnoreCase(id)) {
                System.out.println("Lỗi: Mã sản phẩm '" + id + "' đã tồn tại. Vui lòng chọn một mã khác.");
                return; 
            }
        }

        System.out.print("Nhập tên sản phẩm: ");
        String name = scanner.nextLine();
        System.out.print("Nhập giá sản phẩm: ");
        float price = scanner.nextFloat();

        if (price <= 0) {
          System.out.println("Lỗi: Giá sản phẩm phải lớn hơn 0");
          return;
        }

        System.out.print("Nhập số lượng: ");
        int quantity = scanner.nextInt();

        if (quantity < 0) {
          System.out.println("Lỗi: Số lượng sản phải là số dương");
        }
        scanner.nextLine(); 

        store.getComputers().add(new Computer(id, name, price, quantity));
        System.out.println("Đã thêm sản phẩm thành công!");
    }
}
