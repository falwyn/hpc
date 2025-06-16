import java.util.List;

public class DisplaySalesHistory {
    public void execute(ComputerStore store) {
        List<SaleRecord> history = store.getSaleHistory();
        if (history.isEmpty()) {
            System.out.println("Chưa có lịch sử bán hàng.");
            return;
        }

        System.out.println("--- LỊCH SỬ BÁN HÀNG ---");
        for (SaleRecord record : history) {
            System.out.println(record);
        }
    }
}
