public class DisplayAllComputers {
    public void execute(ComputerStore store) {
        if (store.getComputers().isEmpty()) {
            System.out.println("Danh sách sản phẩm trống.");
            return;
        }
        System.out.println("--- DANH SÁCH SẢN PHẨM ---");
        for (Computer computer : store.getComputers()) {
            System.out.println(computer);
        }
    }
}
