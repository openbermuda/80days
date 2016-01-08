.. title: Guido's clock and the Raspberry Pi Sense Hat
.. slug: guidos-clock-and-the-raspberry-pi-sense-hat
.. date: 2016-01-08 19:17:42 UTC
.. tags: raspberry pi, python, sense hat, mclock2
.. category: 
.. link: 
.. description: raspberry pi sense hat and pretty clocks
.. type: text

=============
Guido's clock
=============

Many years ago I was working a simple app to run on a Nokia Series 60
phone.

It was actually before phone apps were really a thing, or even called
apps.  Nokia had ported python to the Series 60 phones and had some
simple libraries you could use to build your Nokia apps.

I created one called `anorak`_.  Around the same time Guido Van Rossum
posted some code to a thing he called `mclock2`_.  Growing up his
family had a clock which had three coloured discs and a bright light
behind them.  The disks rotate through the day giving pretty patterns
on the clock.  The clock was designed by Rob Juda.

Here is a screenshot from Guido's code.

.. image:: ../galleries/Fishnet/guido.png

Guido created a Tkinter application to simulate the clock.  I liked
the clock, so ported it to Series 60 and used it as the default screen
for *anorak* which was a sort of poorman's GPS using cell tower
locations to figure out where I was.  

Fast-forward to today and there is the Raspberry Pi and the Sense Hat.

The latter is on the International Space Station.  It plugs into the
pins on a pi and has:

* Gyroscope
  
* Accelerometer
  
* Magnetometer
  
* Temperature
  
* Humidity
  
* Barometric pressure

In addition it has an 8x8 coloured LED array.

I am working on hooking all this up to my moped and wanted to learn
about to use the `sense hat python interface`_.

The interface is simple to use, just import the library and create a
SenseHat object and then you can talk to the device.

I could not find a drawing library to draw directly onto the 8*8 pixel
grid.  Instead I used PIL and ImageDraw.Draw.

This allowed me to create a 64x64 image with PIL, with very few
changes to the code.  I just needed the ImageDraw.Draw().pieslice
method.

Now to get down to 8*8 I just divided the image into an 8*8 grid with
8*8 pixels in each grid point.

I then just take the average pixel value and use hat.set_pixel() to
set that value.

The hands of the clock did not work too well.  In the end I made the
hour hand all black with a 10 pixel wide line.  The minute hand I did
in white, again 10 pixels wide.

Here is a photo of the end result.

.. image:: ../galleries/Fishnet/sense_hat_mclock.jpg

So, not quite as neat as the Tkinter version, but I have found I can
actually figure out the time from this thing.
           

.. _anorak: http://anorak.sourceforge.net/

.. _mclock2: https://www.python.org/~guido/mclock2.py

.. _sense hat: https://www.raspberrypi.org/products/sense-hat/

.. _code for mclock2 on sense hat: https://github.com/openbermuda/fishnet/blob/master/mclock2.py

.. _sense hat python interface: https://github.com/RPi-Distro/python-sense-hat
