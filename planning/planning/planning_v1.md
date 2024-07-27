
# Introduction 
I am looking for an interesting way to get myself out of the house and out to the real world while still being able to integrate my interests of

- programming
- Networking
- Machine Learning
- And offensive cybersecurity


## Idea:
To do this I intend to build my own alternative to the [Pwnagotchi](https://pwnagotchi.ai/) reinforcement learning based Wi-Fi pwning platform. I want to create a system which is capable of using the same reinforcement learning techniques to learn about the networks it is scanning and then use that information to make decisions about how to proceed with the network assessments 

My longer term goal is to create a system that is `module driven` similar to the `metasploit framework` by `Rapid7` 
The idea would be the Modules would be ways that the agent based system can interact with a variety of advanced `tools`, `services`, & `actions` which we grant the agents access to in the form of `python functions` which the agents can call when they deem it a valid time to do so.


This would look like `Pwnagachi` combined with [langchain](https://langchain.com) style tools allowing for advanced research, environment management and assessment, as well as advanced reasoning and understanding when making decisions about how to move forward in the network assessments

We are essentially looking to create a device designed for the `war-driving` equivalent of what spear phishing is to spam phishing attacks 

Ideally, each time I bring the device back to the same location, it would be able to recognize that and pick up where it last left off in terms of wireless network assessments


## Development Plan / Outline

We will build these using 

### Hardware

#### Mobile Device
**[Libre Computer](https://libre.computer)**
Model: [Le Potato](https://libre.computer/products/aml-s905x-cc/) 
specs & configs:
    - 2GB RAM
    - 2 Wi-Fi adapters
    - 1 ethernet
    - 1 mobile power supply
    - Debian as the OS
    - Python 3.12
    - PDM python package manager
**Server Device**
Simply a more powerful linux device for you to leave behind while you are out and about with the mobile device.

### Software

#### Language(s)
- Python
    - Keras RL
    - container based scanning & network assessment
        - Nmap
        - Rustscan
        - MAC address randomization
        - Write output to Postgres database using:
            - Sqlalchemy
            - Geoalchemy for geo-location
    - python telegram bot for the UI handlers as simple chats should be more than enough to convey relevant information about the state of the system and agents running within it

when assessing networks, the ultimate goal is to identify vulnerabilities in systems and return known information about said vulnerabilities to the user via the telegram bot

My intention is to create a system where I am forced to travel to find optimal test environments

Ideally I would be able to walk around with this system running in either a pocket or backpack or something, and have it sending information back to the telegram bot, allowing us to get instant messages from the bot containing relevant information about the events & state of the scanner 

This will incentivize me to explore the possibilities of Houston, Texas while I am here.

I am willing to travel quite far within the greater Houston area, however downtown & other urban areas with high population density ideally locations with large quantities of condensed wireless network access points are my primary focus 

- malls
    - Many wireless access points at some?
        - If each store has to handle their own internet rather than the mall itself, then it’s likely there are more targets available in that location
- Apartments
- Large enough stores
- Hotels
- Motels
- Large condensed buildings like business district buildings
    - Many many wireless networks near each other but probably have advanced EDR
- Museums (free Wi-Fi ez pwn? Maybe?)


