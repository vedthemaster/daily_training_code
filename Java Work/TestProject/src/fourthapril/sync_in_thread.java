package fourthapril;

class Bank extends Thread
{
	public int bal1,bal2;
	public void display(int bal)
	{
		System.out.println("Current balance:"+bal);
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
		bal2 = bal2 - 1000;
		System.out.println("Balance after withdrawal:"+bal2);
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
		this.bal1 = bal2 + 1000;
		System.out.println("Balance after Deposit:"+bal1);
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
		}
	}
}
public class sync_in_thread{
    public static void main(String[] args) 
	{
		Bank bnk = new Bank();
		BankDetails bdt = new BankDetails(2000,bnk);
		bdt.start();
		

	}


}