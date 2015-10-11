.. title: Setting up a new email account
.. slug: setting-up-a-new-email-account
.. date: 2015-10-09 21:40:59 UTC
.. tags: 
.. category: 
.. link: 
.. description: A tale of woe
.. type: text

Here is the gist of an actual email exchange between John Doe, setting
up his new email account and Fred, the unfortunate system
administrator doing the setup work.

It started with this email:

   Hi Joe,

   please find your account details below:

   Username: jdoe@foo.com

   Password: W3lcome

   Primary Email: john@foo.com

   Display Name: John Doe

   You will be prompted to change password when you first connect. If
   you are using Windows 7 you can install the Citrix PNAgent Plugin
   which is under downloads on our website: http://www.orifice.com. If
   Windows 8, you will need to go to the Citrix website and install
   the Citrix Receiver.

   I will set you up with an account on our helpdesk too. I have attached
   instructions on obtaining support from Orifice when needed.

   thanks

   Kind Regards,

   Fred

So, John only half digested the message and replied with:
   
   Hi Fred,

   Thanks for setting this up.

   I am using linux.

   I do not have Windows.

   What protocols does the email server support?

   John

Which got this reply:
   
   John, the server path for Citrix login is login.orifice.com. For
   email there is owa and activesync using mail.orifice.com Thanks,
   Fred

Which led to:

    Fred,

    I just got round to looking at this.

    Can you send details of:

    * how to connect to email from an android phone
    * how to change email password once I have connected.

    Re: citrix, whilst there is a linux client, I prefer not to use
    proprietary software on my linux machines (it is a security issue
    as far as I am concerned).

    I do not require the orifice access, but would like to be able to
    access email with standard protocols such as imap.

    Many thanks.

    John

Fred:    
    
   Hi John,

   You can use exchange activesync for email, or imap (993), pop3
   (995). For password resets you can either use owa access
   (https://mail.orifice.com/owa). Or (preferred) enroll on our self
   service portal:
   https://selfservice.orifice.com/user/home.aspx. (username: jdoe)

   Thanks, Fred

John goes to the selfservice orifice and after some trials and
tribulations manages to change his password.

But attempts to connect using IMAP or POP3 fail.
   
John:

   Hi Fred,

   I've been tried to connect both with imap and pop3 with no luck so far.

   If I run nmap on mail.orifice.com I see port 143 and 995 open.

   I think what is tripping me up is the user ID/password combination.

   I was able to change the password successfully via
   https://selfservice.orifice.com/user/home.aspx

   I then tried to connect to both imap and pop3, but without success.

   John 

   [aside: the interface wasn't ideal, each time it rejected my password
   choice due to the alphabet soup password restrictions (incidentally
   these lower security in general -- I started with a very secure, but all
   lower case password and ended up with a password with less entropy due
   to the rules).

   Each time I gave a password which did not meet the password rules, which
   are not explicitly stated, I got logged out and had to try again.]

Fred:

   For account try: orifice\jdoe

John:

   No joy with that.

   I am trying to add as POP3 to gmail.

   email: john@foo.com

   username:  tried orifice\jdoe and john@foo.com

   password: xxxxxxx

   POP server: mail.orifice.com

   port: 995

   No joy so far.

   John

   
Fred:

   Try using activesync on your android?

Fred:
   
   Can you log into owa with your new password?
   
Fred:

   Can you send me your password john...I will test

John:   
   
   No, I cannot send you my password.

John:
   
   I haven't managed to log onto the account with owa either.

   If you send me clear instructions how to do so then I can check.

   I did successfully reset my password via https://selfservice.orifice.com

   Re: password.  If you wish me to reset to a password of your choice let
   me know, but please do not go asking people to email you their
   passwords.

   John

More hacking around, John:
   
   Activesync looks like it will work.

   server: mail.orifice.com
   user: orifice\jdoe

   I entered details and then was told your server wants to be able to
   control some security features on my phone.

   It doesn't say which features.

   I am not happy letting your server control my phone.

   Sorry to be a pain.

   John

Fred:
   
   John, we generally don't use POP3 but I have found a device that
   does and is working fine. Please use the following account format:

   Username: jdoe@foo.com
   SSL/POPS (995)
   TLS enabled
   Server: mail.orifice.com

At this point the coffee kicks in and John, with the knowledge that
POP3 is working for at least one account, actually reads the email:
   
   Thanks Fred.

   The good news is I now have gmail talking to foo.com successfully.

   The key bit of information was:

   Username: jdoe@foo.com

   I had been trying: john@foo.com and orifice\jdoe, but hadn't
   considered trying jdoe@foo.com

   The jdoe@foo.com was also the key to getting owa working too.

   Thanks for your patience.

   John

Now the user ID was actually in the very first email Fred sent out,
but John missed that :(
   
John:    

   Hi Fred,

   The Google/gmail thing is that it is simpler for me to collect my
   email from just one place: google.

   gmail supports pulling down email from other accounts via pop3 or
   imap (imap generally works better).

   The snafu over jdoe v john was what was stopping stuff working
   here.

   If you want to chat more about the security issues that have been
   raised here I would be happy to do so.

   Thanks for your help.

Fred:
   
   Only issue I see with that is you won’t be able to reply from
   jdoe@foo.com if you are pulling into your gmail account. What
   security issues have been raised?

Fred:

   Hi John, I hadn’t seen your comments below:

   >>>> [aside: the interface wasn't ideal, each time it rejected my
   >>>> password choice due to the alphabet soup password restrictions
   >>>> (incidentally these lower security in general -- I started with a
   >>>> very secure, but all lower case password and ended up with a
   >>>> password with less entropy due to the rules).

   We use the Microsoft *complex passwords* option which requires the
   use of upper/lowercase letters, numbers, and symbols. This is more
   secure than not enforcing complex passwords. We do not install any
   3rd party password software as like you, I prefer not to install
   *proprietary* software on my operating system unless necessary

   Thanks, Fred

So, what security issues have been raised here?
===============================================

Answers on a postcard.

Talking of postcards, plain text email is about as secure as sending a
postcard.

Asking a user to send their password
------------------------------------

Unless this is a phishing scam, then please do not do this.

Microsoft complex passwords
---------------------------

Alphabet soup password restrictions lower security.

The motivation is noble, to ensure the password has characters from a
larger alphabet, including upper/lower case, numbers and symbols.

It sounds good, but the restrictions reduce the size of the password
space.

Further, they result in users trying passwords until they find one
that fits all the restrictions.

John started with a long, securely generated password.  By the time
the alphabet soup rules had all been satisfied, the password had
degenerated to p4ssw0rd!

Support for multiple platforms
------------------------------

Most of the time Fred is dealing with Windows users.  

John doesn't do Windows.  Based on past experiences he is expecting
this to be painful.  He was thrashing around in the dark until Fred
provided confirmation that POP3 was working for at least one account.

This extra bit of information made him look more closely to figure out
why it wasn't working for him.  When you know for sure something works
then you can dig into the problem without the fear you are wasting
your time.  It helps focus the mind.

Google defaults
---------------

When you try to configure gmail to collect email from a POP3 acount
the dialogs try to be helpful and guess the field values based on your
email address.

They try to guess the email server, ports and other fields.  If the
email setup follows the same standards, the process can be quite
smooth.

In this case, most of the guesses that gmail made were wrong.

Further, John was confused.  The new email address was
*john@foo.com*, but the login name was *jdoe@foo.com*.

The result was multiple failed logins, repeated entry of passwords and
general confusion.

Uninformative error messages
----------------------------

When a login attempt fails all a user is generally told is that the
username/password combination is not valid.

The idea is not to help the hackers by allowing them to discover valid
user names.

In principle, this sounds good.

In practice, it is a disaster.  Users can end up making repeated
password guesses, when in fact it is the username that is incorrect.

What we have here is security through obscurity.

Further, we have a system that causes end users to reveal more
information as they try to figure out what is up.

A man-in-the-middle could get a really useful collection of password
hashes whilst the user is thrashing around.

The harder you make it to set up a password, the less likely the
resulting password will be strong.

Somewhere, in a parallel universe
=================================

Relying on passwords for security is not working too well.  There is
this thing called public key cryptography.  How to use it is a story
for another day, but here is how the conversation might have gone:

Fred:

   Hi John,

   Just setting up your new *securemail* account.

   Could you send me your public key fingerprint?

   Fred

John:

   Thanks Fred,

   Here you go: 941F FB75 FD21 D407 A1E7  F2BF FA8D 73C3 39E6 C3F2

   The full key is loaded up here: hkp://pool.sks-keyservers.net

   John

 Fred:

   -----BEGIN PGP MESSAGE-----

   hQEMAw0iXtWMJ1AEAQf+NGNQ134hwNePBBeTxiwj018mxeiaGHz7RvH/rRKWHHXU
   n5wS/DbbD/xniVNJzULP5wPBv1gWQ/tzmQBfCVStf3P0h5RCkiKmU90tuXK4225R
   AOpJYu21KaT0jbfnsC9FX6vLF2l45NS+Ruw9liqRVYZd80MEpZR0Oe+Us+mDtD6l
   nPfTDUS8URgMwkFyb8ry+pGHXnRj+dxIcwJRPuYDXRsVjx3e+efgM/pgMwNY8mZZ
   RPHpaaxuRVUXl2bOm4S5LWPnSL/Y64jfaXkWv+05X+WjSc7Vs2X2a85IB7Ht92QJ
   CfsEcvSUv4Bv2EF+AUkGz/fBv99UoxTiwgxn28gzKtJcAaytvwu8tHWJN8VxCDt4
   WvR/i0lAzHsa8+Q5OE2OytLRnQOukCXnjUXnBAGPKLHPJRJIhd/W5NZWF/fXKjZD
   SJZm+y4mmdQ7bgecu2M/QH/ppRg+BbY/QkWaHCQ=
   =uOgp
   -----END PGP MESSAGE-----

Of course, things are not this simple.  Use of public key tools is not
widespread.  People currently using public key cryptography are a bit
like the first owners of telephones or fax machines.  There is nobody
to call.

Michael Hayden, former director of NSA, just called for greater use of
encryption.   He recognises that our lack of defensive capabilities in
information security are causing vast quantities of sensitive
information to leak.

It is time to beef up our security.

This will only truly happen when the tools are widely available, with
good understanding of their strengths and weaknesses and working in
such a way as to minimise the possibilities of compromise.
