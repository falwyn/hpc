import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class SaleRecord {
    private String computerId;
    private String computerName;
    private int quantitySold;
    private float pricePerUnit; 
    private float finalAmount;  // Tổng tiền cuối cùng sau khi đã giảm giá
    private LocalDate saleDate;
    private boolean discounted;

    public SaleRecord(String computerId, String computerName, int quantitySold, float pricePerUnit, float finalAmount, LocalDate saleDate, boolean discounted) {
        this.computerId = computerId;
        this.computerName = computerName;
        this.quantitySold = quantitySold;
        this.pricePerUnit = pricePerUnit;
        this.finalAmount = finalAmount;
        this.saleDate = saleDate;
        this.discounted = discounted;
    }

    public float getFinalAmount() {
        return finalAmount;
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String discountInfo = discounted ? " (Giảm giá 10%)" : "";
        return String.format("Ngày bán: %s - ID: %s - Tên: %s - SL: %d - Đơn giá gốc: %,.0f VND - Tổng tiền: %,.0f VND%s",
                saleDate.format(formatter),
                computerId,
                computerName,
                quantitySold,
                pricePerUnit,
                finalAmount,
                discountInfo
        );
    }
}
