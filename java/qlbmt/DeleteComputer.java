import java.util.Scanner;

public class DeleteComputer {
    public void execute(ComputerStore store, Scanner scanner) {
        System.out.print("Nhập mã sản phẩm cần xóa: ");
        String id = scanner.nextLine();

        boolean removed = store.getComputers().removeIf(computer -> computer.getId().equalsIgnoreCase(id));

        if (removed) {
            System.out.println("Đã xóa sản phẩm thành công!");
        } else {
            System.out.println("Không tìm thấy sản phẩm với mã này.");
        }
    }
}
