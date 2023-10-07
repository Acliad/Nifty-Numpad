Nifty Numpad is a full sized numpad with an extra row and two extra columns of macro keys. It was created because I wanted a companion to my TKL keyboard for work. My main workflow involves heavy use of ECAD programs, so the design was tailored for that, but it is generic enough to be nice for many workflows! 


The main features are:
- Full sized numpad with row of macro/function keys on the top
- Two extra columns of macro keys
- Cherry MX style socketed switches
- Backlit keys
- 3D printable case (FDM or resin)

![render](Docs/Render%20(Blue,%20SS%20screws).png "Render of Nifty Numpad")

# Contents
- [Contents](#contents)
- [Building One](#building-one)
  - [1. PCB Assembly](#1-pcb-assembly)
  - [2. 3D Printed Case](#2-3d-printed-case)
  - [3. Switch Mounting Plate](#3-switch-mounting-plate)
  - [4. Switches/Keycaps](#4-switcheskeycaps)
  - [5. Software](#5-software)
- [TODO](#todo)
  - [Software](#software)
- [Changelog](#changelog)
  - [PCB](#pcb)
    - [Rev 1](#rev-1)
  - [Software](#software-1)
  - [Mechanical](#mechanical)

# Building One
All of the files needed to build this numpad are in this repo (with software as a submodule and in the main QMK repo). The total BOM cost will be somewhere around $65-$85 shipped, but depends heavily on where and how you source things like switches, keycaps, plate, etc. For example, I bought 120x switches, but if you could get 33 switches for cheaper, you might save ~$10. 

## 1. PCB Assembly
The most difficult part of the build is soldering the RP2040 (microcontroller used) and associated components. It is highly recommended that you have the PCBs assembled. The files are in this repo for getting the PCB assembled through JLC PCB. You may save some money by soldering some of the components yourself (especially the sockets and LEDs). However, if you just love to solder this can be done with a stencil and plenty of time. I should know 🥲

You can choose to omit the LEDs if you're not into that sort of thing. It'll save you a few bucks. 

Parts marked as (DNF) in the BOM are not meant to be populated. If you want easy debugging for software development, you can populate R103, SW101, and SW102.

To have the PCB assembled:
1. Upload the gerber files from PCB/Main PCB/production/Nifty_Numpad.zip to JLC PCB.
2. Check the PCB Assembly toggle on the JLC PCB order page.
   1. Choose the PCBA Type. If you want JLC to solder the LEDs and sockets for you, you need to choose Standard. Otherwise, choose economy. Economy is a bit cheaper.
3. On the PCB Assembly page, you will need to upload the bom.csv and positions.csv file from PCB/Main PCB/production/
4. On the Components Placements page, make sure all of the ICs are orientated correctly. They usually aren't by default since JLC's library orientation is generally different from KiCad's.

To Solder the PCB assembly yourself:
1. Order PCBs (I use JLC, you can use whomever you like).
2. Order a stencil (you can usually do this at the same time as the PCB).
3. Order parts (I have DigiKey PNs in the electrical BOM, but again feel free to substitute)
   - The switch sockets are not available on DigiKey. [I bought mine on Amazon](https://www.amazon.com/dp/B0BVH6M5FP?psc=1&ref=ppx_yo2ov_dt_b_product_details), but you can source them from most keyboard suppliers.
   - The LEDs come in packs of 10. You can get them from DigiKey or Adafruit, but note if you upload the BOM directly to DigiKey it will put in a quantity of 33, which is actually 330.
4. Solder it!
    - I recommend a reflow oven, but a hot air station or hot plate works too.


## 2. 3D Printed Case
This case was initially designed to be 3D printed on a resin printer, but it actually prints best on an FDM printer. There are not special instructions here. You can either print the case yourself or have it printed using a service. JLC offers printing of many varieties. This might be a good choice if you're already ordering the PCB from them.

All the screw holes are designed to be tapped by a self-tapping screw. The BOM has some recommendations for some plastic-threading screws. 

I have added a "[shadow line](https://www.youtube.com/watch?v=8dhFhU7Nl_0)" to the case outline. There's a top-case print option with and without this line. I think it helps the look a bit for FDM prints, but it's up to you. 

It helps the sound profile considerably to fill up the case with some kind of dampening material. You could use foam or pour castable silicone into the case (I used [this one](https://www.amazon.com/gp/product/B07V5FFPWC/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)). You can (and probably should) pour the silicone directly into the case. However, I've also included a mold for this in the Mechanical folder.

## 3. Switch Mounting Plate
I used [plate-mount](https://switchandclick.com/plate-mounted-vs-pcb-mounted-keyboard/) switches on this design. You can either make your own plate or have one made for you. There's a model of the plate as well as a DXF file in the Mechanical folder. Here is some information about some options:

1. Order a plate out of FR-4 when you order the PCB
   - This is a good option if you're already ordering the PCB from JLC. You can order the plate at the same time and save on shipping. 
   - This plate is quite rigid and I've found it to work well.
2. Order or make a custom plate out of your preferred material.
    - If you have a laser cutter or CNC, you can use the DXF or step file to make a plate out of whatever material you like! Many people use plexilgass, but you could use wood or metal. 
3. Use the provided 3D model of the plate to 3D print a plate.
   - The plate works, but it's quite flimsy and makes taking all the switches off the PCB tedious

Whatever you choose to do, you should find appropriate files in the Mechanical folder.

## 4. Switches/Keycaps
The fun part! Choose your favorite Cherry MX compatible switches and pop them in. If you're using LEDs, make sure you get switches with a clear top. 

I found it difficult to source backlit keycaps that fit this build well. You might be better off using non-backlit keycaps. There are [some AliExpress sellers](https://www.aliexpress.us/item/3256801609324454.html?spm=a2g0o.order_list.order_list_main.18.27561802CbfaCa&gatewayAdapt=glo2usa) who will sell portions of a keyboard at a time so you can mix and match colors. This is what I ended up doing, but I couldn't find any in a uniform profile like XDA or DSA. If you find a good source of keycaps, please share! 

If you're feeling plush, I think the numpad + icono kits of [these keycaps](https://drop.com/buy/drop-biip-mt3-extended-custom-keycap-set?mode%5B0%5D=shop_open&mode%5B1%5D=shop_open&defaultSelectionIds=969832&utm_source=google&utm_medium=cpc&utm_campaign=14650997430&utm_term=126026139486&utm_content=545898905914&utm_keyword=&utm_placement=pla-1392002507270&utm_network=u%3Ac%3A%3A&utm_device=&gad=1&gclid=CjwKCAjwlJimBhAsEiwA1hrp5i-AwICvpmNDm80DELJZylLo96oIX7IjxFvtUybMUVPNlUNpxAKwlxoCEOMQAvD_BwE&gclsrc=aw.ds) would be really nice. 

You'll also need 3x 2u plate-mount stabilizers. You can source these from most keyboard part suppliers or Ali Express.

## 5. Software
I've used [QMK](https://qmk.fm) for this build. Theere are builds for the [VIA](https://www.caniusevia.com) GUI configurator, a basic default usage, and an example for how to use the "fancy" RGB Idle mode and some tap-dance features. VIA is probably the easiest way to configure the keymap since you can configure it over a GUI, but if you're comfortable with QMK, you can do some cool customizations.

The Nifty Numpad has been merged into the main QMK repo, which you can find [here](https://github.com/qmk/qmk_firmware). My personal fork for developing the keyboard software is a submodule of this repo. You can find it [here](https://github.com/Acliad/qmk_firmware).

QMK and the build/flash process is pretty well document, so I'll leave that to the QMK community. If you have specific issues with the Nifty Numpad, feel free to message me. 

# TODO
## Software
- ~Implement VIAL for GUI remapping of buttons~
- ~Add other keymaps (an actual default and rename current to Cadence is a good start)~
- Create visual legend for RGB settings layer

# Changelog
## PCB
### Rev 1
- Changed footprint for W25Q40CLSNIG from wide to narrow footprint to match DigiKey PN
- Changed standoff holes to 6.0mm (from 4.6mm)
- Update LED footprint
- Add WASD graphic

## Software
- Added additional keymaps: default, VIA, and example. Old default moved to "Cadence" keymap
- Cleaned up code and file structure to align with QMK standards

## Mechanical
- Updated plate to use pan head screws
- Added clearance to top piece for pan head plate mount screws
- Moved "Designed By" tag to inside numpad
- Added a silicone sound dampening mold
- Added a "[shadow line](https://www.youtube.com/watch?v=8dhFhU7Nl_0)" model