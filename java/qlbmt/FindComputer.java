import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FindComputer {
    public void execute(ComputerStore store, Scanner scanner) {
        System.out.print("Nhập mã hoặc tên sản phẩm cần tìm: ");
        String keyword = scanner.nextLine().toLowerCase();
        List<Computer> foundComputers = new ArrayList<>();

        for (Computer computer : store.getComputers()) {
            if (computer.getId().toLowerCase().contains(keyword) || computer.getName().toLowerCase().contains(keyword)) {
                foundComputers.add(computer);
            }
        }

        if (foundComputers.isEmpty()) {
            System.out.println("Không tìm thấy sản phẩm nào phù hợp.");
        } else {
            System.out.println("--- KẾT QUẢ TÌM KIẾM ---");
            for (Computer computer : foundComputers) {
                System.out.println(computer);
            }
        }
    }
}
