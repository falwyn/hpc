public class Computer {
  private String id;
  private String name;
  private float price;
  private int quantity;

  public Computer(String id, String name, float price, int quantity) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }

  @Override
  public String toString() {
    return "ID: " + this.id +
        ", Tên: " + this.name +
        ", Giá: " + String.format("%,.0f", this.price) + " VND" +
        ", Số lượng tồn: " + this.quantity;
  }

  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public float getPrice() {
    return price;
  }

  public void setPrice(float price) {
    this.price = price;
  }

  public int getQuantity() {
    return quantity;
  }

  public void setQuantity(int quantity) {
    this.quantity = quantity;
  }
}
