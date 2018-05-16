/*
This round is with hiring manager. I think this is the worst round I have ever had.
Given a class, bankAccount as follows, tell where to improve
*/

class bankAccount {
    double balance;
    public credit (double a) {
        balance -= a;
    }
    public debit (double a) {
        balance += a;
    }
}

// First answer, there is no string, so we should add
    String account;
// I mentioned that two methods are kind of redundant, should merge into one
// The manager asked what could go wrong with this set up. I answer, we need to use .this? He said not necessary. He gave an example:
bankAccount ba  = new bankAccount()
ba.balance = 500;
// I answer, we cannot accept non-inilizaed object with no account, so I changed the code to
class bankAccount {
    String account;
    double balance;
    public void change(double a) {
        balance += a;
    }
    bankAccount(String account) {
        if (account == null) {
            // do something
        }
        this.account = account;
    }
}

// He asked how to tell if the input is not valid, I answered, throw an error, he asked, how? I have not used that for a very long time, I answered that from Python, VALUEERROR, but in Java, not sure.
// He said, we can throw an exception. Feeing I am dead......

// Then he asked what if we have multhread working environment. I answered, we should put a lock around function change, to protect there is only one thread entering the instance.
// I told him all my lock experience is with c/c++ and Python, but I assume there is Lock library in Java.
import java.Lock.*;
class bankAccount {
    Lock lock;
    String account;
    double balance;
    public void change(double a) {
        lock.acquire();
        balance += a;
        lock.release();
    }
    bankAccount(String account) {
        if (account == null) {
            // do something
        }
        this.account = account;
    }
}

// Then he asked what could introduce a problem here? I thought for a while and could not come up with it, he said, if balance += a actually is very long codes.
// Maybe somethere there is error, exit the codes, other process might not be able to access the object because lock is not released. I answered, we can use try-exception to release it anyway.
// Not sure in java if it is try-exception or try-catch. Have not used this for a very very long time......Dead......

// Next, he asked, what about somebody wants to access somebody else account? I said, we should set account public but balance private. He asked how to make sure he is the account holder. I answered,
// we can write a function to ask him to type the account to check if it is the person. He hinted, in java there is getter function.
// I changed my codes to as follows:
import java.Lock.*;
class bankAccount {
    Lock lock;
    public String account;
    private double balance;
    public void change(double a) {
        lock.acquire();
        balance += a;
        lock.release();
    }
    public double getter(String input) {
        input == account ? balance : throw Exception
    }
    bankAccount(String account) {
        if (account == null) {
            // do something
        }
        this.account = account;
    }
}

// THen he asked how do I know what is getter doing? I answered, we can change the name to make it more straightforward, like CheckAccountCorrect. Then I said, if you look at my codes, all variables and function have pretty str names for others to understand.
// Last question from him, how to make others easy reading this codes? I answered, for co-workers, we write comments inside the class. For outsiders, we write comments outside the class and hide the private variables. Finally done.
