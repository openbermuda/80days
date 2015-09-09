.. title: Computing Hermeneutics: let the source be with you.
.. slug: computing-hermeneutics
.. date: 2015-09-09 13:15:28 UTC
.. tags: 
.. category: 
.. link: 
.. description: A brief history of conversations between humans and computers
.. type: text

Someone asked me recently to explain the difference between coding and
programmes, using a suitable analogy.

I am not good at short answers, so here is a longer one.

The difference between the source code and the programme has changed
dramatically over the years.

In essence, the problem boils down to humans specifying what a
computer should do.   We speak different languages, our input/ouput
devices work differently and our central processing units are
fundamentally different.

In short, computer programming is a bit like writing a document for
someone to read, but that someone does not speak your language.

It takes everything you say literally and has no capacity to "do what
I mean, not what I say".

They can do certain tasks incredibly quickly, like the gifted child
that can amaze you with music, maths or art.

Coding
======

Coding is the process of writing the instructions for the computer.

Source Code
===========

The source code is what the computer programmer creates.  It is the
human readable version of the computer instructions.

Programme
=========

The human readable instructions generally need to be converted into
another form for the computer to understand.  The resulting version is
known as the programme.


Electro-Mechanical computing
============================

The computers at dawn of modern computing were electro-mechanical
devices such as the Bombes, designed by Alan Turing to crack the
Enigma codes.

*Programming* the Bombes involved manyally setting dials and using
wires with plugs enter settings for plug boards.

With these devices, the source code and the programme were essentially
the same thing: the physical settings of the wheels, dials and
plug-board.

In short, humans learned to speak the same language as the computers.

Machine Code
============

The first fully electronic computers were programmed with machine
code, essentially just a stream of numbers.

Each operation the computer could do had a numeric code.  Memory
locations were expressed as numbers as were the input values for
calculations.

Again, the human programmers were having to learn the language the
computer actually understood.

There was some help for humans, the machine code might be written in
hexadecimal, not the binary that the computer can actually store.

Assembly Language
=================

All this was incredibly time consuming.  Skilled machine code
programmers were a rare breed.  Computers were also quite rare at this
time, so there were generally enough programmers to go round and they
were too busy writing machine code to worry about creating and
learning new languages.

Further, getting data into and out of these early computers was a
challenge in itself.

Soon punched cards and computer tape took over these roles.

Assembly languages were developed.  These languages used names such as
*add*, *mul* and *mov* to represent the numeric operations the
computer actually understands.

Special programmes, called *assemblers* were used to translate from
this assembly language that was easier for humans to produce to the
machine language that the computers understand.

The task of programming was still very challenging, but by now the
version of the code that the computer understood and was able to use
was different to that the programmer writes.

Computers and programmers were still pretty rare species.

High level languages
====================

Once there were assembly languages it was a natural progression to
higher level languages.

These languages had higher level constructs that *compilers* could
translate into assembly language and in turn the *assembler* could
turn into machine code that computers could run.

This separation later proved invaluable, since different models of
computer had different instruction sets and required different
assembler languages.

Bootstrapping
=============

Writing a compiler for a new language is a challenging task.

It is common practice to write the compiler in the language that it is
intended to compile.

Now this creates a *chicken and egg* situation.

How do you compile your compiler, if it is written in a new language?

There are a number of solutions to this problem that have been used,
but all boil down to using some other compiler to pull you up by your
boot straps.

Often these tools implement a subset of the language, but can be used
to compile the whole compiler including the additional features.

Once you have got this far, you can use your newly compiled compiler
to compile itself.   The language has become *self-hosting*.


Virtual Machines
================

The early computers were extremely slow compared to today's
computers.  Compilers would be written for each specific architecture
in order to take full advantage of the computer's capabilities.

As computers became faster it became feasible to write *virtual
machines*.

These virtual machines would implement a general purpose instruction
set.  To actually run virtual machine code on a specific computer
architecture it is necessary to  create an implementation of that
virtual machine on the specific hardware.

The magic of virtual machines is that it separates the problem of
making a particular machine run fast from the problem of specifying
what you want it to do.

In short, virtual machines promised: *write once, run everywhere*.

Java and .NET are good examples of virtual machine technology.


Interpreted languages
=====================

Compiling code can be time consuming.  The higher level a language is
the more work the computer has to do to translate the language into
something it can run.

Good compilers will also attempt to optimise code, allowing the
programmer to specify what the computer should do, but letting the
compiler figure out an efficient way to do that.

Of course, the programmer can help the compiler by using algorithms
and constructs that they know the compiler will implement
efficiently. 

As computers became faster it became possible to do compilation of
code on the fly.

Programmers using compiled languages go through a cycle of

* writing code
* compiling the code
* running the code
* figuring out why it did not do what they expected
* rinse and repeat

The compile stage can be time consuming and interrupts a programmers
train of thought.

Interpretted languages typically also make use of a virtual machine.
They compile the code into virtual machine byte codes that can then be
executed directly.

Perl and Python are examples of interpretted languages.  I remember
when I first discovered Perl, my productivity went up dramatically.

Literate Programming
====================

Computer programmes can (and in my view should) be considered as works
of literature: written works to communicate not just with computers
but also with other computer programmers.

It turns out that most programmers spend the vast majority of time
reading, maintaining and developing existing code, rather than writing
new code.

There is a strong incentive for programmers to write clear code that
is easy for others to follow:  the most person most likely to read
your code is yourself.  Maybe six hours later, six days, six months or
even six years in the future.

Great languages not only make it easier to express what you want the
computer to do but also make it easier to write readable code.

Truly great languages make it harder to write code that looks like it
does one thing, but really does something else.

At the same time, they allow some level of ambiguity.  They work on
many levels, lika all great literature.

For example, a sort algorithm that can sort anything, just so long as
you tell it how to compare objects.


Open Source
===========

Open source software is software that makes the source code available,
not just the executable.

Why is this important?  Well if you want to understand what the
software is doing, the best way to do that is to have the work of
literature that the programmers creating the programme used.

Open source software makes these works of literature available to
you.  It is like having the actual draft for a book.  Not only do you
get the story, but you get the author's notes.

If the programmer is using version control, you get the whole history
of the book.  All the thoughts, all the experiments that were tried,
the failures and the successes.

Without the source code, you are missing much of the plot.

Free Software
=============

Free software takes this one step further.  Not only does it give you
the work of literature, but it gives you the freedom to examine it, to
change it, to write your own story.

It gives you the freedom to experiment and explore.


Disassembly
===========

Disassembly is the reverse of what an *assembler* does.

Dissassemblers take code that a computer understands and turn it into
code a human can understand better.

Some of them are remarkably good and produce code that an experienced
programmer can understand well.

For example, python bytecodes can be disassembled into very readable
python code.

Code obfustification
====================

Some software is put through an *obfustification* process before it is
released.

The meaningful function and variable names that the programmer used
are replaced with arbitrary labels.  Comments are removed from the
code.  In short, the goal is to make it hard to discover how the
programme actually works.

Of course, the code can always be disassembled and with enough
patience and time it is possible to discover how it actually works.

However, check the license agreement before you do this, much closed
source software explicitly forbids disassembly in the license
agreement. 


Project Jypyter
===============

Nowadays there are many, many computer languages.

This has created a problem for computer programmers: they are not all
speaking the same language.

What is needed is some sort of Bablefish that allows programmers and
programmes to communicate with each other.

Project Jupyter is one such Bablefish.  It supports over 50 languages
and allows seamless interaction between those languages.


It is all about language and communication
==========================================

Software is all about communication.  If you are a computer, machine
code is your friend.

If you are human, *Use the source, Luke.*

And if the source is not available, maybe you need to read a different book.
