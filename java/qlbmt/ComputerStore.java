import java.util.ArrayList;
import java.util.List;

public class ComputerStore {
    private List<Computer> computers = new ArrayList<>();
    private List<SaleRecord> saleHistory = new ArrayList<>();

    public List<Computer> getComputers() {
        return computers;
    }

    public List<SaleRecord> getSaleHistory() {
        return saleHistory;
    }

    public void addSaleRecord(SaleRecord record) {
        this.saleHistory.add(record);
    }

    // Tính tổng doanh thu bằng cách duyệt qua lịch sử
    public float getTotalRevenue() {
        float total = 0;
        for (SaleRecord record : saleHistory) {
            total += record.getFinalAmount();
        }
        return total;
    }
}
