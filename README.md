Family Relationship Chatbot
===========================
A Python-based chatbot leveraging Prolog to build and query a knowledge base of family relationships from natural language input.

--------------------------------------------------------------------------------

🌟 PROJECT OVERVIEW
------------------

This project implements a chatbot capable of understanding and inferring family relationships. It uses Python for the user interface and basic text processing, while a Prolog knowledge base handles the complex logical inference. Users can input natural language statements to assert facts (e.g., "John is the father of Jane.") and then ask questions to query the knowledge base about relationships (e.g., "Are John and Jane siblings?").


🎯 MOTIVATION
------------

The motivation behind this project is to explore the integration of symbolic AI (Prolog) with conventional programming languages (Python) for building intelligent systems. It serves as a practical demonstration of:

  * Knowledge Representation: How to represent facts and rules about family relationships in Prolog.
  * Logical Inference: Utilizing Prolog's powerful inference engine to deduce new relationships.
  * Natural Language Processing (Basic): Converting human-readable sentences into a machine-understandable format.
  * Prolog-Python Integration: Using 'pyswip' to seamlessly communicate between Python and a Prolog environment.


🛠️ TECHNOLOGIES USED
-------------------

  * Python 3.x: The main programming language for the chatbot interface and text processing.
  * Prolog (SWI-Prolog): The logic programming language used for the knowledge base and inference engine.
  * pyswip: A Python library for interfacing with SWI-Prolog.


🚀 GETTING STARTED
-----------------

Follow these steps to set up and run the Family Relationship Chatbot on your local machine.

### Prerequisites

  * Python 3.x: Download and install from python.org.
  * SWI-Prolog: Download and install from swi-prolog.org. Ensure it's added to your system's PATH.

### Installation

1.  Clone the repository:

        git clone https://github.com/[YOUR_USERNAME]/[YOUR_REPO].git
        cd [YOUR_REPO]

2.  Install the 'pyswip' library:

        pip install git+https://github.com/yuce/pyswip@master#egg=pyswip

### Project Structure

The project consists of several key files:

  * 'main.py': The application's entry point, handling the main interaction loop.
  * 'process.py': Contains functions for processing user prompts and interacting with the Prolog engine.
  * 'format.py': Handles text formatting and conversion of sentences into Prolog statements.
  * 'knowledge_base.pl': The Prolog file containing the facts and rules that define family relationships.
  * 'familyKeywords.txt' & 'removedKeywords.txt': Text files used for parsing user input.


💬 USAGE
-------

1.  Run the chatbot from the project's root directory:

        python main.py

2.  Interact with the chatbot:
    The chatbot will prompt you for input with '[ ] :'.

    *   To assert a fact, type a statement ending with a period ('.'):
        '[ ] : John is the father of Jane.'

    *   To ask a question, type a query ending with a question mark ('?'):
        '[ ] : Is John the brother of Mike?'

    *   To exit the chatbot, type 'terminate':
        '[ ] : terminate'


🧠 KNOWLEDGE BASE STRUCTURE
--------------------------

The 'knowledge_base.pl' file is central to this project. It defines various predicates and rules:

  * Facts: Basic assertions like 'male(john).' or 'female(jane).' that form the foundation of the knowledge.
  * Rules: Logical definitions for deriving complex relationships from basic facts. For example:
        siblings(X,Y) :- father(F,X), father(F,Y), mother(M,X), mother(M,Y), X \= Y.
  * Dynamic Assertions: The file also includes helper predicates (e.g., 'assertFather/2') that are called by the Python script to dynamically add new facts to the Prolog runtime during a session.
