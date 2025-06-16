public class DisplayRevenue {
  public void execute(ComputerStore store) {
    System.out.println("--- THỐNG KÊ DOANH THU ---");
    System.out.println("Tổng doanh thu bán hàng: " + String.format("%,.0f", store.getTotalRevenue()) + " VND");
  }
}
