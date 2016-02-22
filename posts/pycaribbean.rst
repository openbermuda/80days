.. title: PyCaribbean
.. slug: pycaribbean
.. date: 2016-02-22 15:00:00 UTC
.. tags: python, caribbean, bermuda
.. link: 
.. description: A weekend of magic in Santo Domingo
.. type: text



=================================
 PyCaribbean 20-21 February 2016
=================================

I am just relaxing after three fantastic days here in Santo Domingo.

It was the first PyCaribbean conference: Python, palm trees, wonderful
people, a meeting of languages: Spanish, python, English, Restructured
Text, Markdown, with generous lashings of pandas, ipython and Jupyter
notebooks.

Santo Domingo
=============

Santo Domingo is a bustling city of craziness, motorbikes carrying
three, cars going in all directions, horns and carnivals.

I speak little Spanish, but my wife is here to interpret, saving me
from my failed attempts to communicate.  One waiter looked
particularly perturbed.  Apparently, I had told him I love him in a
failed attempt to say how good the food was.

People have been super friendly.  Mangling of their language is
treated with smiles and help.

Python in Santo Domingo
=======================

The conference organisers have done an amazing job building community
here in DR.   The vast majority of the 200 or so attendees were local
and actively using python.

Jorge Vargas talked about how he and others have worked to build up
community over the last few years.  

Some of the secrets:

* organising monthly meetups, with schedule planned out 3 months
  ahead.

* co-ordinating with other tech groups: Ruby, Javascript, Linux,
  Django Ladies and much more.   Having a shared calendar to avoid
  collisions.

* Multiple organisers for each thread to help avoid burn out.

The venue
=========

The conference was held in the `Biblioteca Pedro Mir`_ on the
University Autonoma de Santo Domingo.

We were staying at a hotel a 15 minute walk, mostly through the
campus. 

Bermuda Shorts
--------------

On the Friday before the conference we walked over to the venue.  It
is hot and humid here, so shorts were the order of the day.

When we got to the centre the security wouldn't let us in.
Interpretter to the rescue: no shorts allowed, a policy for all
government buildings.

I felt for the organisers, this is the sort of rule it is easy not to
think about, fortunately most attendees had at least one pair of
jeans.

The Bermuda shorts had to wait for the evening dinner to make an
appearance. 


Opening Keynote: when languages collide
=======================================

Brandon Rhodes, PyCon 20176 chair, gave the opening keynote.

Brandon is always an entertaining speaker and this was no exception.

It was python's unofficial 25th birthday on 20th February, which just
added to the excitement that Python had come to the Caribbean.

Brandon spoke of the weirdness that occurs when English meets Spanish,
when the English ask, what is that called?  "Rio Grande" comes the
response.  And from then on it is known as the tautological *Rio
Grande River*.

Brandon went through some of the history of the python language and
how its design was shaped by other languages.

Python, like all modern computer languaes, or indeed languages in
general, is a mash-up of ideas borrowed from other languages.  Indeed,
computer languages borrow idioms from natural language all the time.

Much of the power and elegance of python comes not from the features
it has adopted, but from those it has chosen not to implement.

History was a theme in many talks.  I find an understanding of the
history can be very illuminating in understanding how we got to where
we are and why things are how they are now.  It can also be a guide to
the future.

Just ten days ago the world of science had been buzzing with the
announcement of the LIGO experiments detection of gravitational waves
from two black holes, each the mass of more than 30 Suns, colliding
over 1 billion light years away.

What has since emerged is the extent to which python was involved in
the incredible data analyis that has been able to detect a wrinkle in
space time less than the width of a proton as it passed by the earth
from a billion light years away.

The world of physics has finally moved on from Fortran to python.
Brandon joked that physicists only change language once every 50
years, so this is a significant transition.

He said the speed of the transition has caught many by surprise.  And
its not just astro-physics, but many other disciplines: biological
science, finance, weather and climate, geologists, signal processing,
humanities and so much more.

Driving much of this are wonderful tools, in particular, Jupyter
notebook, matplotlib, ipython and more.

In short, the tools have reached the point where regardless of your
discipline you can quickly learn just enough to quickly investigate
ideas.

Python as a way of Thinking
===========================

Allen Downey talked about thinking in python.

He talked about expressing thoughts in natural language, mathematics
and computer code.

When we write computer code we are turning mathematics into something
that computers can run.

The language of mathematics is neither executable or easy for humans
to understand.

Natural language is rich, but ambiguous and not executable.

Python has often been described as executable pseudo-code, and with
good reason.

Allen showed how to move from the world of mathematics and build from
the bottom up to a natural interface to your idea.

A highlight of this talk for me was his wonderful transalation of
Bayes theorem into python.  I will watch out for the code appearing on
github and post a link when it turns up.

Code Review, Revision and Technical Debt
========================================

Geoff Gerrietts followed Allen's talk with a lot of good advice on the
benefits of code review, dealing with technical debt and much, much
more.

Supercomputing with python
==========================

Paul Logston was another speaker who illustrated the subject with some
history.

In his case, this was a brief history of super-computers since the
first Cray-1 in 1976.

Comparisons in FLOPs (floating-point operations) are only part of the
story, but do give a useful yardstick.

* 1976 Cray-1: 160 mega-flops

* 1984 Cray-XMP, 4 cpu's, ~1 giga-flop

* 2013 Tihane, 34 peta-flops, 32,000 intel Xeons.

So, Tihane has roughly the power of 34 million Cray XMP's.  Note
however, that much of this increase comes from scaling up the number
of processors.  To take advantage of this power, your problem needs to
be amenable to parallel processing.  

Paul showed how to write simple code using python interfaces to MPI
(message passing interface) to write code to run on these massively
parallel machines.

Paul just does this in his spare time, helping a friend with
biological science problems related to DNA and RNA, he just happens to
have access to a supercomputer to test his code on.

Keynote: Django Ladies
======================

Ola Sitarska told of her adventure with the django web framework and
how the Django Ladies came into being.

The python world is full of tales like this, someone seeing a need,
figuring out how to help others and creating tools, documentation and
training to build communities.

Django ladies have now run training across the globe.  Their tutorials
have been read by hundreds of thousands.

Ola recognised the challenges for women trying to enter a tech world
dominated by men and provided tips and guides to help them succeed.

Tech communities have long lacked diversity, PyCaribbean has added
another dimension by helping foster community across the Caribbean.

Documentation
=============

The second and final day began with Eric Holscher's keynote on
documentation.

Eric created readthedocs and more recently writethedocs.

Documentation is fundamental to making your code accessible to
others.  And in six months time, even it it is your own code, you will
be glad that you wrote the docs.

Again, there was some history of the world of python documentation.

Integration of documentation generation into automated build processes
has been a major driver in helping documentation stay in sync with
code.

The Django project was mentioned as a project with a process that
positively fosters documentation generation.

Eric mentioned some new developments, including new tools which are
able to extract docstrings from code without having to import (and
hence partially execute) that code.

Eric showed some photos of hundreds of documenation enthusiasts
working together at readthedocs gatherings.  Who knew, 300 people
giving up their time to work together on free software documentation.

I particularly enjoyed this talk as I have a keen interest in
documentation driven development and literate programming ideas.

Virtual Reality
===============

Jose Elias gave a fascinating account of the world of virtual
and augmented reality.

For the purposes of this talk, virtual reality was focussed on
technology that presents virtual worlds using headsets.

Jose gave a history of the subject.  Like many technology developments
early enthusiam ran into technical issues and the subject was
abandonned for a few years.

As technology has caught up, we are reaching a new era of rapid
development of VR technology.

Headsets are becoming:

* lightweight

* low power

* low latency, little lag as your head moves around

* higher resolution

* lower cost  

There is a lot of excitement in the tech world, with a belief that VR
may prove to be as disruptive, if not more so, than smart phones.

Whilst much of the technology is proprietary there are also some
significant open source tools, including python of course.

This technology can, and probably will, fundamentally change how
humans interact with computers.

One video showed someone creating a virtual vase and placing it in a
3-D printer which then created a real version of the vase.  

Machine learning in python
==========================

Nick McClure gave some excellent advise on the challenges of working
with machine learning and encorporating models into a production
environment.

As this talk immediately preceded my own, I missed a lot and look
forward to catching up when the video comes out.


As much typing as you want
==========================

Andy Fundinger gave a clearly illustrated talk on how python
properties can be used to coerce data to specific types.

He began with an overview of how types work in python and the typical
ways pythonistas interact with types.  The most common approach is to
just ignore them altogether, just go with the duck-typing. 

One of the beauties of python is that it allows you to probe around in
its internals.  Done carefully, this can be very powerful.

Andy did not use meta-classes for his tricks, but did raise the
possibility, noting that *Traits* use this approach.

It is something I tend to avoid as you are changing the *normal*
behaviour of python classes.  For instance, 

Andy noted that the decision to take this route is best decided
up-front for a specific framework, being expliicit about just what
tricks are being used.

He also gave some helpful advice on how to do this on a minimally
invasive way.

I came away with a new trick that may well prove very useful in some
future projects.


Building the Caribbean Python Community
=======================================

I had an extended lunch break talking with others from Jamaica, Puerto
Rico and of course the Dominican Republic about how to spread this
community across the Caribbean.

As far as I am aware, I was the only attendee from Bermuda.  With only
65,000 residents, it is challenging to get the critical mass to hold
regular events.

Others are experiencing similar problems on their islands.

We discussed ways to work together and pool resources as well as
virtual meet-ups and of course further conferences and gatherings.

There is excellent support from the wider Python community and a very
promissing future for Python in the Caribbean.

There will undoubtedly be another PyCaribbean in 2017.

We are also starting to explore ideas for a PyData conference in
Bermuda.


Jacob Kaplan-Moss Closing Keynote
=================================

Jacob gave the closing keynote extending the ideas from his PyCon 2015
keynote in 2015.

He explored ideas about how people become experts.  He referred to
research which has shown a lack of evidence of genetic
pre-disposition.

He noted that in today's world what we generally need is not
individual experts but rather expert teams.

Most of the problems we face require a multi-disciplinary approach.
No one individual can hope to know everything and the collective
knowledge and skills of any group is always greater than any
individual. 

The challenge is how to build expert teams.  Jacob identified some of
the key factors that teams that learn quickly have over those that
struggle.

Jacob used data from a research project analysing teams which had been
put together to carry out non-invasive heart surgery.

Teams improved quickly when:

* the team members are kept the same initially

* introduce new members slowly with mentoring from the existing
  members.

* keep the process the same initially (as opposed to a less successful
  team where the lead liked to introduce something new each time).

* have a team review each procedure

* members are chosen based on their ability to work together well,
  rather than just going with who is interested or available.

This is another talk where I look forward to the video, there is much
to digest.

Wrap up and after party
=======================

It is carnival time in Santo Domingo, the streets were full of people
in exotic costumes for the carnival, each Sunday in February is party
time. 

A good time was had by all at the after party at Pasteur 8.

Two days of fun and learning with a wonderful group of people.

I am already looking forward to PyCaribbean 2017 wherever it may be
held. 

.. _Biblioteca Pedro Mir: http://www.uasd.edu.do/index.php/biblioteca

.. _LIGO and Jupyter: http://mybinder.org/repo/minrk/ligo-binder/GW150914_tutorial.ipynb
