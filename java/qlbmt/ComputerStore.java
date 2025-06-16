import java.util.ArrayList;
import java.util.List;

public class ComputerStore {
  private List<Computer> computers = new ArrayList<>();
  private float totalRevenue = 0;

  public List<Computer> getComputers() {
    return computers;
  }

  public float getTotalRevenue() {
    return totalRevenue;
  }

  public void addRevenue(float amount) {
    this.totalRevenue += amount;
  }
}
