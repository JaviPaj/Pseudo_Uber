import java.util.Date;

public class Card extends Payment{
    Integer numbercard;
    Date enddate;
    Integer cvv;

    public Card(Integer id, Integer numbercard, Date enddate, Integer cvv) {
        super(id);
        this.numbercard = numbercard;
        this.enddate = enddate;
        this.cvv = cvv;
    }
}