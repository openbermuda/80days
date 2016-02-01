.. title: Dice passwords
.. slug: dice-passwords
.. date: 2016-01-20 03:05:34 UTC
.. tags: information security, passwords, dice, random
.. category: 
.. link: 
.. description: Passwords suck, but we can make them suck less
.. type: text


Micah Lee wrote an excellent article on `diceware`_.  It covers a lot
of issues, but guides through how to create a secure passphrase with
dice.

It contains some excellent advice, like all security advice, there are
subtleties to consider, but the steps advised will be a vast
improvement over the current situation.

There are some obstacles, however.

Industry standards
==================

For a long while it has been *industry standard* to impose rules such
as:

* password must contain upper and lower case letters
  
* password must contain a digit
  
* password must contain a punctuation
  
* password must not contain *that* character
  
* password must be changed every 90 days
  
These rules had rationale behind them, but they also have many
unintended consequences.

The rules are intended to increase the password space, or the size of
the alphabet of characters that are used.

However, few sites explicitly state their password requirements.
Often it is like a mini adventure game, discovering the rules, one by
one.

And of course, all this is happening when you are having to change
your password, when you have more important things to do.

Oh, and don't forget that critical server that has its password in a
file, but nobody unchecked the expire password box, that stopped
working yesterday.

The end result is by the time all the rules are satisfied the password
has degenerated to P4ssw0rd!.   Relieved that you have solved the
little adventure, you get back to what you were doing.

Until you need to use the password again.  And you can't remember it.
Well you remember what you started with.

You enter a few random guesses, much to the delight of the man in the
middle, because the site is not using http.

Or it is using https, but not securely.

You call a helpdesk and they reset it to W3lcome! for you and everyone else.

Good passwords
--------------

Micah points out that it is incredibly hard to think up a good
password.

He presents a way to generate a phrase instead.   Using rolls of dice
to select words from a long list.

Now sadly, none of these high entropy passwords will work for sites
imposing these rules.

So you end up changing a few characters in the first word.  And this
is good, until you go a month without logging on.  And then you can't
remember which characters you changed.

So, Micah also points out that password managers can be handy for
passwords for internet sites, where you don't care so much if the
password is broken.

Password managers allow you to use a passphrase to in turn generate
random passwords.  The function used includes hashing of the web site
name.

The only problem here is that some generate passwords that don't pass
the site's alphabet soup rules.

Password managers usually allow to specify the alphabet of characters,
but even with that sometimes the password they come up with will not
satisfy the rules.

This is because they are using the full password space, not
arbitrarily shrinking that space.

What can sites do to help?
--------------------------

Do not restrict the size of the password space by imposing alphabet
soup rules.

Run a password cracker on your own password database.  Inform users
whose passwords are crackable.  Advise them on how to use a password
manager.

And about the password expiring thing, that is another story.

Google sends emails about logins from new devices and has a number of
other small things they do which give good feedback which can help
with security.


.. _diceware: https://theintercept.com/2015/03/26/passphrases-can-memorize-attackers-cant-guess/
   
