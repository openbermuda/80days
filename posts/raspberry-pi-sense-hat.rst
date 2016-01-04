.. title: Raspberry Pi Sense Hat
.. slug: raspberry-pi-sense-hat
.. date: 2016-01-04 00:13:11 UTC
.. tags: raspberry pi, python, pycaribbean, weather
.. category: 
.. link: 
.. description: sensors for raspberry pi's
.. type: text

===========================
Sensors, weather and mopeds
===========================

I just discovered the `raspberry pi sense hat`_.

I have been thinking about putting together raspberry pi's, sensors
and mopeds to make a mobile weather station and more.

So in Bermuda we have mopeds.  Power supplies are one thing that is
causing me some thinking with pi's.  They only need about 5 watts of
power.  With the pizero, I think it is about 1-2 watts.

Solar is always an option, but then the sun goes in.  There is wind
and rain too.  Lots of ways to get enough power.  And batteries to
store for when there is nothing.

And of course, mopeds have batteries.  They also have this thing that
sits between your legs and creates explosions lots of times per
second.

Sense Hat
---------

https://www.raspberrypi.org/products/sense-hat/

So I have spend all of five minutes looking at this.

It has sensors for:

* Gyroscope
  
* Accelerometer
  
* Magnetometer
  
* Temperature
  
* Barometric pressure
  
* Humidity

And it has a mini joystick as well as an 8x8 matrix display.

It plugs neatly into a pi 2's and I expect could be adapted to the
pizero.

Oh, and it is being used for the Astro pi project on the international
space station.

https://astro-pi.org/

I am thinking of adding a wifi chip and a GPS chip.  The latter is
also good for a real time clock.

The sense had also comes with a python library.

http://pythonhosted.org/sense-hat/

There are all sorts of other tools that look useful.

I can't find it now, but I saw another sense hat piece of code that
was storing readings in a python flask app, which is what I have been
trying to do with `sunshine`_.

So, all I need now is one of those Apollo helmets for the moped, with
the gold coated visor.

.. _raspberry pi sense hat: https://www.raspberrypi.org/products/sense-hat/
.. _sunshine: https://github.com/peakrisk/sunshine
