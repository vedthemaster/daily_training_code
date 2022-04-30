package april4;

class Bank extends Thread
{
	public int bala;
	public void display(int bal)
	{
		bala = bal;
		System.out.println("Current balance:"+bala);
		try
		{
			Thread.sleep(500);
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		
	}
	public void withdraw(int bal2)
	{
		bala = bal2 - 100;
		System.out.println("Balance after withdrawal:"+bala);
		try
		{
			Thread.sleep(500);
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		
	}
	public void deposit(int bal1)
	{
		this.bala = bala + 1000;
		System.out.println("Balance after Deposit:"+bala);
		try
		{
			Thread.sleep(500);
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		
		
	}
}
class BankDetails extends Thread
{
	private int bal;
	Bank bank;
	BankDetails(int b1, Bank obj)
	{
		bal = b1;
		bank = obj;
	}
	public void run()
	{
		synchronized(bank)
		{
			bank.display(bal);
			bank.withdraw(bal);
			bank.deposit(bal);
			// bank.display(bal);
		}
	}
}
public class bank_implementation{
    public static void main(String[] args) 
	{
		Bank bnk = new Bank();
		BankDetails bdt = new BankDetails(2000,bnk);
		bdt.start();
		

	}


}