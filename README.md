# simulatingpandemic

This was a project I made in my junior year of High School, when Covid protocols started to relax to prepandemic levels. This was my first deep utilization of OOP, so its a little iffy in some places but I learned alot :)

  It seems like every time we open the news there is a new disease in town.  Some like Covid or SARS are here to stay and some like Monkeypox have died down significantly (thankfully).  Identifying the best response to these diseases by governments is imperative.  When Covid struck, some countries used lockdowns heavily (China), while other countries used herd immunity (Sweden), and most like the US used a mix of quarantining, vaccination, and herd immunity.  Uganda used limited lockdowns, quarantining, and other measures to control Ebola.  All of these measures have economic costs either through reduced GDP and/or death rates besides other costs.

  I use Discrete-event-simulation (DES) to identify the best governmental response for various diseases.  To do this I model the economics, infections, and death rates of 3 different viruses, Covid-19, Ebola, and Influenza for various governmental control protocols.  Protocols could be to do nothing, quarantining and enforcing lockdowns to various degrees of strictness.  Independent variables for the disease include incubation length, duration of illness, mortality rate, and contagiousness. I also employed Object Oriented Programming to efficiently separate the various entities in the simulation like Person, Government, Statistics, Simulation Engine, and Viruses.  
  
  Costs from controlling pandemics can be either reduced GDP and/or increased mortality rates depending on the approach.   For instance, in theory, lockdowns seem ideal because they ensure that the disease will be contained, but in practice, they are prone to “leaks”, either through service providers or through people ignoring guidelines and infecting others.  This has been discussed in (Cite papers) where lockdowns while effective in the early days result in increased “mobility” or as I call it “leaks” over time.  Another factor to consider is the nature of social and economic interactions.  The same can be said for quarantining as well.  While most people may follow a quarantine, there will be “leaks” or “mobility” over time.  Realistically, one meets with a certain group of people more often than the general population (bubbles), but people also leave their bubbles either due to travel or occasional interactions outside their regular circles.   Another factor is the so called “flattening of the curve” to minimize impact to hospitals from a storm of critically ill patients.  CITE here.  R-values are a measure of the infectiousness of the disease in the context of various protocols

  For my study, I simulate a population of 10000 individuals, who all live in their respective bubbles.  However people may occasionally interact with those outside their bubble.  Additionally, in the case of pandemics, I study the effects of doing nothing, quarantining, and lockdowns to different dependent variables like GDP, Mortality rates, R-values, Peak Infection rates (that drives the flattening of the curve), and ability to eliminate the disease entirely.  All along I also factor in mobility-related leaks to governmental controls.
  
  My study found that quarantining in all cases is best for GDP and eliminating disease sooner.  Any form of voluntary to enforced quarantining has a slightly higher mortality rate but impacts the economy minimally.  A Draconian lockdown minimizes deaths but usually at a high cost to the economy.  Any lockdown short of a strict one is worse for the economy and does not do anything significant to eliminate disease sooner or reduce mortality compared to Quarantining.  Doing nothing is never a good idea.

you can read the full presentation here: https://docs.google.com/presentation/d/1kZgkJLoj9HiWSXLaUFWKTVMYOtv_74wYL8BdA2C0DgY/edit?usp=sharing

Thanks for reading!






