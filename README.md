# AirBnB Clone

## Description

The goal of the project is to deploy on a server a simple copy of the AirBnB website.
It is not an implementation of all the features, only some of then fundamental to the learning track.

It consists of:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

* A website (the front-end) that shows the final product to everybody: static and dynamic

* A database or files that store data (data = objects)

* An API that provides a communication interface between the front-end and your data (retrieve, create, delete and update them.)

## The Console

* Creates your data model

* Manages (CRUD) objects via a console / command interpreter

* Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine gives an abstraction between the objects and how they are stored and persisted.

This abstraction is to enable us to change the type of storage easily without updating your codebase.

This console will be a tool to validate this storage engine.
