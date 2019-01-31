# Call Register

A django projects that registers domestic, national and international calls in the database.

Calls can be configure in the admin area but are generally divided into three common types.

* Local: Fixed cost of $0.10
* National: Billed at $0.01 per second
* International: Billed at $0.03 per second.

The interface itself permits 

* To register a new call
* To see a list of all the calls (id, type, duration and cost)

## License

This code is open source. So feel free to use, modify, share, download as per your need. I do not take risk nor responsibility for your errors or any commercial damage.

## How to run?
This code is written in python3.6.

## On local machine
Go to the mysite project folder that contains the manage.py file and then

```
python manage.py runserver
```

Else directly access the webapp on this link

http://gurupratap.pythonanywhere.com/calls/



