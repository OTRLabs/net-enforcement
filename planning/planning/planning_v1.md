
# Introduction 
I am looking for an interesting way to get myself out of the house and out to the real world while still being able to integrate my interests of

- programming
- Networking
- Machine Learning
- And offensive cybersecurity

# Goal:
I want to create a system which is capable of scanning wireless networks and assessing them for vulnerabilities, and then sending that information back to me in a way that is easy to understand and act upon

## Target Audience:
This project is intended for people who are interested in cybersecurity, networking, and machine learning. It is intended to be a fun and interesting way to get out of the house and explore the world around you while still being able to learn and grow in your field of interest, I am the target audience for this project haha.


## Idea:
To do this I intend to build my own alternative to the [Pwnagotchi](https://pwnagotchi.ai/) reinforcement learning based Wi-Fi pwning platform. I want to create a system which is capable of using the same reinforcement learning techniques to learn about the networks it is scanning and then use that information to make decisions about how to proceed with the network assessments 

My longer term goal is to create a system that is `module driven` similar to the `metasploit framework` by `Rapid7` 
The idea would be the Modules would be ways that the agent based system can interact with a variety of advanced `tools`, `services`, & `actions` which we grant the agents access to in the form of `python functions` which the agents can call when they deem it a valid time to do so.


This would look like `Pwnagachi` combined with [langchain](https://langchain.com) style tools allowing for advanced research, environment management and assessment, as well as advanced reasoning and understanding when making decisions about how to move forward in the network assessments

We are essentially looking to create a device designed for the `war-driving` equivalent of what spear phishing is to spam phishing attacks 

Ideally, each time I bring the device back to the same location, it would be able to recognize that and pick up where it last left off in terms of wireless network assessments


## Development Plan / Outline

Development will be broken down into 3 main parts
1. Mobile Device
2. Server Device
3. Shared Libraries & Tools

### Mobile Device
This is the device which will be brought out into the field with you to scan networks and assess them
**[Libre Computer](https://libre.computer)**
Model: [Le Potato](https://libre.computer/products/aml-s905x-cc/) 
specs & configs:
    - 2GB RAM
    - 2 Wi-Fi adapters
    - 1 ethernet
    - 1 mobile power supply
    - Debian as the OS
    - zsh as the shell
    - [docker]()
    - SQlite for local caching of data
    - Python 3.12
    - [PDM](https://github.com/pdm-project/pdm) python package manager


#### Language(s)
- Python v3.12
    **Libraries**
    - Keras RL for reinforcement learning, The use of reinforcement learning within this project is in how the mobile device is able to preform detailed and efficient assessments of the environment and it’s current state. We use Keras RL to effectively detect the state of the environment and make the next scan preformed relevant to the environment. Ideally over time as the `mobile device` analyzes more environments it becomes faster and faster at scanning them because of prior experience
    **Tools**
    - Scapy for packet manipulation
    - Custom tools for network discovery (based on python & Keras RL)
    - container based scanning & network assessment
        - Docker for container management, we intend to containerize individual tools and services to allow for easy management and deployment of the tools and services we intend to use, as well as Operational Security (OPSEC) and protecting the operators in addition to giving us the ability to easily update and maintain the tools and services we intend to use
          - Nmap for service detection once on a network
          - Rustscan for faster network scanning
          - Masscan for large scale network scanning

        - MAC address randomization
        - Write output to Postgres database using:
            - [Sqlalchemy](https://www.sqlalchemy.org/) for database management as well as potentially using [advanced alchemy](https://github.com/litestar-org/advanced-alchemy) for advanced database management as well as other DBMSs like [DuckDB](https://duckdb.org/)
            - Geoalchemy for geo-location
    - [python telegram bot v21.4](https://docs.python-telegram-bot.org/en/v21.4/) for the UI. Works by sending updates to user(s) as simple chats from a [Telegram Bot](https://core.telegram.org/bots/api) should be more than enough to convey relevant information about the state of the system and agents running within it




### Server Device
The `server device` is a more powerful linux device for you to leave behind while you are out and about with the `mobile device`.

It mainly functions as a [Litestar ASGI API Server](https://litestar.dev) which will be able to receive information from the `mobile device` & process it for storage or later analysis. It can even send updates about the information it is getting from the `mobile device` to the `telegram bot` for you to view
If configured properly the `mobile device` should be able to send information back to the `server device` which will then be able to send that information to the `telegram bot` for you to view

One of the other main use cases of the server, in addition to information & data management/processing, is simply acting as the "muscle", allowing us to offload the heavy lifting required for effective use of tools like [HashCat](), or other password cracking tools, to the server device rather than the mobile device

Ideally the server could be one single Debain based device or a k8s cluster using [microk8s](https://microk8s.io/) or [k3s](https://k3s.io/) for easy management and deployment of the server device

We intend to have the server be able to support multiple `mobile devices` at once, allowing for multiple `mobile devices` to be out in the field at once and all sending information back to the same server device

#### Server Tech Stack
- [Litestar ASGI API Server](https://litestar.dev)
- [Postgres](https://www.postgresql.org/) for database management
- [Sqlalchemy](https://www.sqlalchemy.org/) for database management as well as potentially using [advanced alchemy](
- [DuckDB](https://duckdb.org/) for advanced database management as well as other DBMSs like [DuckDB](https://duckdb.org/)
- [Geoalchemy](https://geoalchemy-2.readthedocs.io/en/latest/) for geo-location
- [python telegram bot v21.4](https://docs.python-telegram-bot.org/en/v21.4/) for the UI. Works by sending updates to user(s) as simple chats from a [Telegram Bot](https://core.telegram.org/bots/api) should be more than enough to convey relevant information about the state of the system and agents running within it



### Shared Libraries & Tools
To ensure ultimate consistency when communicating across the `mobile device` and the `server device` we will be using a shared library of tools and services which will be used by both devices to ensure that the information being sent back and forth is consistent and reliable.

This will also allow us to easily update and maintain the tools and services we intend to use across both devices

- Pydantic for data validation
- JSON
- 




### Reinforcement Learning

Diving more into the reinforcement learning and how we will use Keras RL, we intend to break this system down to work in the following way:

**environment**

This is the 2.4GHz & 5GHz networks we can detect with the tools we are using at the time

**Environment Objects**

Objects in the environment include networks which contain hosts, which are running services

**Action**
Actions are the things the system can do to interact with the environment.
For this project that will include things like:
- nmap scans. Basically gathering data on the networks. Hosts or services to detect vulnerabilities 
- search engine queries. To gather more information about the networks, hosts, or services
  - this could include
  - Shodan
  - Censys
  - google
  - brave
  - bing
  - if it offers an API we can use it
- brute force attacks. To attempt to gain access to the networks, hosts, or services
- etc
**rewards**

Rewards will be given at various stages but primarily when:

- the system gains access to a new network
- Identifies hosts on the network
- Identifies a service on those hosts
- the system is able to accurately detect a vulnerability as this is the ultimate goal

---
---

## Goals & Random Thoughts

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


