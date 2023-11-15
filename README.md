# Dist-Generator
Generate Lua Procedural Distributions content for your Project Zomboid mod.

<br>

Simplify the process of adding your Procedural Distributions content by supplying some basic information like:
* mod ID
* comma-separated items      :  `-items "item1,item2,item3"`
* or item input file         :  `-itemsFile file.txt`
* comma-separated locations  :  `-loc "location1,location2"`
* or location input file     :  `-locFile file.txt`
* output filename            :  `-out out.txt`

<br>

The output contains the required Lua code for your Procedural Distributions mod file.

<br>

!(https://github.com/PZmodTools/Dist-Generator/blob/main/run-example.png)

<br>

-----
### usage: 
```
distrib.py [-h] -modid MODID [-items ITEMS] [-itemsFile ITEMSFILE] [-loc LOCATIONS]
                  [-locFile LOCATIONSFILE] [-out OUTPUT]
```
