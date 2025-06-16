// SellComputer.java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
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
            return;
        }
        if (computerToSell.getQuantity() < quantityToSell) {
            System.out.println("Không đủ hàng. Chỉ còn " + computerToSell.getQuantity() + " sản phẩm.");
            return;
        }

        LocalDate saleDate;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        while (true) {
            System.out.print("Nhập ngày bán (định dạng dd/MM/yyyy): " + ": ");
            String dateString = scanner.nextLine();
            try {
                saleDate = LocalDate.parse(dateString, formatter);
                break; 
            } catch (DateTimeParseException e) {
                System.out.println(" Định dạng ngày không hợp lệ. Vui lòng nhập lại.");
            }
        }

        LocalDate today = LocalDate.now();
        boolean isDiscounted = saleDate.equals(today);

        float basePrice = computerToSell.getPrice();
        float finalPricePerUnit = basePrice;

        if (isDiscounted) {
            finalPricePerUnit = basePrice * 0.90f;
            System.out.println("Giao dịch vào ngày hôm nay! Đơn hàng được giảm giá 10%.");
        }

        float totalSaleAmount = finalPricePerUnit * quantityToSell;

        computerToSell.setQuantity(computerToSell.getQuantity() - quantityToSell);

        SaleRecord record = new SaleRecord(
                computerToSell.getId(),
                computerToSell.getName(),
                quantityToSell,
                basePrice,
                totalSaleAmount,
                saleDate, 
                isDiscounted
        );

        store.addSaleRecord(record);

        System.out.printf("Bán thành công! Tổng tiền: %,.0f VND.%n", totalSaleAmount);
    }
}
