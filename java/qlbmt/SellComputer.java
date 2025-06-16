import java.util.Scanner;

public class SellComputer {
    public void execute(ComputerStore store, Scanner scanner) {
        System.out.print("Nhập mã sản phẩm cần bán: ");
        String id = scanner.nextLine();

        Computer computerToSell = null;
        for (Computer computer : store.getComputers()) {
            if (computer.getId().equalsIgnoreCase(id)) {
                computerToSell = computer;
                break;
            }
        }

        if (computerToSell == null) {
            System.out.println("Không tìm thấy sản phẩm với mã này.");
            return;
        }

        System.out.print("Nhập số lượng muốn bán: ");
        int quantityToSell = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        if (quantityToSell <= 0) {
            System.out.println("Số lượng bán phải lớn hơn 0.");
        } else if (computerToSell.getQuantity() < quantityToSell) {
            System.out.println("Không đủ hàng. Chỉ còn " + computerToSell.getQuantity() + " sản phẩm.");
        } else {
            computerToSell.setQuantity(computerToSell.getQuantity() - quantityToSell);
            float revenueFromSale = computerToSell.getPrice() * quantityToSell;
            store.addRevenue(revenueFromSale);
            System.out.println("Bán thành công " + quantityToSell + " sản phẩm. Doanh thu tăng: " + String.format("%,.0f", revenueFromSale) + " VND.");
        }
    }
}
