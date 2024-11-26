# Diagrams POC

## Description
A proof of concept for Python [Diagrams](https://diagrams.mingrammer.com/), a library that allows the generation of various graphs from Python code.

## Prerequisites
* [Python](https://www.python.org/) (version 3.9.6+)
* [Make](https://www.gnu.org/software/make/): Facility that allows for the easy execution of this POC.
* [Graphviz](https://graphviz.gitlab.io/): This is required by the Diagrams library.
  * [Mac](https://graphviz.gitlab.io/download/#mac)
  * [Windows](https://graphviz.gitlab.io/download/#windows)

## Setup
In the root project directory do the following: 
* If there is no `.venv` folder, that means you will need to create a new virtual environment: `python -m venv .venv`
* Activate the virtual environment: `source .venv/bin/activate`
* Install the required packages: `make install`

## Running the examples
Please note that these examples have been taken directly from the developer's site and lightly modified.
* Event Processing (with Clusters): `make show-event`
* Edge (with Clusters and Edges): `make show-edge`
* GCP: `make show-gcp`
* Kubernetes: `make show-kubernetes`
* On Prem: `make show-on-prem`
* Custom Icons (from remote): `make show-custom-remote`
* Custom Icons (locally stored with some custom settings): `make show-custom-local`
* All Examples: `make show all`

## Observations
This library seems to have pretty exhaustive support for the more notable major providers, including 
AWS and DigitalOcean. I'm wishing that there was built-in support for processes that take place on ones local
machine.

I'm was finding that displaying custom icons from ones local filesystem seems to be broken, at least with the files 
that I tried to use. After looking at 
[one of the issues on the GitHub](https://github.com/mingrammer/diagrams/issues/746), I was able to solve the issue 
(I basically had to move the folder in which I was storing the images), but I do think that the site (and example) 
could have been a bit clearer about how the path to the custom images files were being resolved.

When I first came across this library, I was tempted to attempt creating some sort of JSON or YAML layer
on top of this library so that non-developers would be able to make use of this functionality. After thinking about this, 
I came to the conclusion that such an undertaking would result in a **very** cumbersome DSL that would require some pretty 
dedicated resources for a fair amount of time; besides, the Python layer is pretty thin and fairly intuitive anyway.

## Links
* Diagrams
  * [Project Page](https://diagrams.mingrammer.com/)
  * [GitHub](https://github.com/mingrammer/diagrams)
* [Graphviz](https://www.graphviz.org/)
* [Make](https://www.gnu.org/software/make/)
