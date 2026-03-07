# Restraints

**Source:** `LARGEFILE Searchable_Manuals/Tiburon-Shop-Manual/11. Restraints-OCR.pdf`
**Pages:** 60
**Vehicle:** 2003 Hyundai Tiburon (GK)
**Engines:** 2.0L I4 Beta, 2.7L V6 Delta (PRIMARY)

---

                      Restraints
GENERAL                                        .„   RT-2

SRSCM (SUPPLEMENTAL RESTRAINTS SYSTEM

CONTROL MODULE)                    ..               RT-7

ASR BAG MODULE (DRIVE SIDE) AND CLOCK SPRING        RT-15

AIR BAG MODULE (PASSENGER SIDE)                     RT-18

TROUBLESHOOTING                                     RT-23

ASRBAG MODULE DISPOSAL                              RT-58
RT-2                                                                                                     j^CTRAINTS

GENERAL                                                         1.   Be sure to proceed with airbag related service only
                                                                     after approx. 30 seconds or longer from the time the
                                                                     ignition switch is turned to the LOCK position and the
GENERAL         ERJBOO-IO                                            negative (-) terminal cable is disconnected from the
                                                                     battery. The airbag system is equipped with a back-up
The Supplemental Restraint System (SRS AIRBAG) is de-                power source to assure the deployment of airbags
signed to supplement the seat belts to help reduce the risk          when the battery cable is disconneted during an ac-
or severity of injury to the driver and passenger by activat-        cident. The back-up power is available for approx.
ing and deploying the driver, passenger and side airbag              150ms.
as well as the belt pretensioner in certain frontal or side
collisions.                                                     2.   When the nqgative(-) terminal cable is disconnected
                                                                     from the battery, the clock and audio system's mem-
The SRS (Airbag) consists of : a driver airbag module                ory will be wiped out. So before starting work, make a
located in the center of the steering wheel, which contains          record of the contents of the audio system's memory.
a folded cushion and an infiator unit; a passenger airbag            When the work is finished, reset the audio system and
module located in the passenger side crash pad which                 adjust the clock.
contains a folded cushion together with an infiator unit ;
side airbag modules located in the driver and passenger         3.   Symptoms of malfunction of the airbag system are
seat which contain folded cushions and infiator units;               difficult to detect, so the diagnostic codes become
SRSCM located on the floor center console core which                 the most important source of information when trou-
monitors the system,; an accelerometer which senses                  bleshooting.
vehicle deceleration,; a spring interconnection (clock
spring) located within the steering column; system wiring       4.   When troubleshooting the airbag system, always in-
and wiring connectors; and a knee bolster located under              spect the diagnostic codes before disconnecting the
the steering column. The impact sensing function of the              battery.
SRSCM is carried out by the electronic accelerometer
that continuously measures the vehicle's acceleration and       5.   Never use airbag parts from another vehicle. When
delivers a corresponding signal through an amplifying and            replacing parts, replace them with new parts.
filtering circuit to the microprocessor. Deployment of the
airbag is designed to occur in frontal or near-frontal side     6.   Never attempt to disassemble and repair the airbag
impacts of moderate to severe force.                                 modules (DAB, PAB, SAB, BPT), clock spring and
                                                                     wiring in order to reuse them.
Only authorized service personnel should work on or             7.   If any component of SRS has been dropped, or if there
around SRS components. Those service personnel                       are cracks, dents or other defects in the case, bracket
should read this manual carefully before doing any such              or connector, replace them with new ones.
work. Extreme care must be used when servicing the
SRS to avoid injury to the service personnel (by inadver-       8.   After work on the airbag system is completed, perform
tent deployment of the airbag) or the driver (by rendering           the SRS SRI check. The airbag indicator lamp can
the SRS inoperative).                                                be triggered by faults in other circuit in some cases.
                                                                     Therefore if the airbag indicator lamp goes on, be sure
CUSTOMER CAUTIONS                 ERJBOO2O                           to erase the DTC codes using Hi-scan just after re-
                                                                     pairing or replacing the troubled parts, including the
Failure to carry out service operations in the correct se-           fuse.
quence could cause the airbag system to unexpectedly
                                                                9.   Especially when earring out body welding, never fail
deploy during servicing, possibly leading to serious injury.
                                                                     to disconnect the battery's negative (-) terminal.
Further, if a mistake is made in servicing the airbag sys-
tem, it is possible that the airbag may fail to operate when
required.

Before performing servicing (including removal or installa-
tion of parts, inspection or replacement), be sure to read
the following items carefully.
GENERAL                                                                                          RT-3
SPECIAL SERVICE TOOL        ERJB0030


 Tool
                                           Illustration                             Use
 (Number and name)
 0957A-34100A                                                          Airbag deployment tool
 Deployment tool                                                     ! RAB, SAB :0957A-38100
                                                                       DAB, BPT : 0957A-38500




                                                          ERHA010A

 0957A-38000                                                         Wring harness checker for
 Diagnosis checker                                                   each module




                                                          ERHA010B

 0957A-38200                                                         Simulator to check the resistance
 Dummy                                                               of each wiring harness
                                                                     Dummy adapter                     !
                                                                     RAB, SAB : 0957A-38300
                                                                     DAB, BPT : 0957A-38400
                                       ^   •        ^


                                                          ERHA010C



* DAB : Driver Airbag

* RAB : Passenger Airbag

* SAB : Side Airbag

* BPT : Belt Pretensioner
RT-4                                                              RESTRAINTS
WARNING/CAUTION LABELS                      EROC0035



A number of caution labels relating to the SRS are found
in the vehicle, as shown in the following illustration. Follow
label instructions when servicing the SRS.

if labels are dirty or damaged, replace them with new ones.




                                                       ERNC003A        ERKB003A




                                                       EROC003A        EROC003B




                                                                       ERA9001C
GENERAL                                                                                                             RT-5
  ERNC0040


A. DAB + PAB                                             B. SUPPLEMENTAL RESTRAINT SYSTEM
CAUTION                                                  (AIRBAG) INFORMATION
TO AVOID SERIOUS INJURY :                                The airbag is a Supplemental Restraint System (SRS).
  • For maximum safety protection in all types of        You must always wear the seat belts. The airbag
    crashes, you must always wear your safety belt.      system condition is normal when the "SRS" lamp in the
  • Do not install rearward-facing child seats in        cluster flashes approximately 6 times after the ignition
    any front passenger seat position.                   key is turned on and then goes off.
  • Do not sit or lean unnecessarily close
    to the airbag.                                       If any of the following conditions occur, the sys-
  • Do not place any objects over the airbag or          tem must be serviced.
    between the airbag and yourself.
  • See the owner's manual for further information       1.   "SRS" lamp does not light up when the key is turned on.
    and explanation.                                     2.   "SRS" lamp stays lit or flashes continuously.
                                                         3.   The airbag has inflated.

                                                         The airbag system must be inspected by an authorized dealer
                                                         ten years after the vehicle manufacture date shown on the
                                                         certification label, located on left front door opening area.

                                                              ©WARNING
                                                              Failure to follow the above Instructions- may result in
                                                              injury to you or other occupants in the vehicle.
                                                              See the "SRS" section in Owner's Manual for more
                                                              information about airfoags.
G, WARNING :                                             D, WARNING
Contents are poisonous and extremely flammable.          This car is equipped with a side airbag for each front seat.
Do not probe with electrical devices or otherwise          • Do not use any accessory seat covers.
tamper with item in any way. Servicing of this unit to     • Use of other seat covers could reduce the
be performed only by authorized personnel.                   effect of the system.
                                                           • Do not install any accessories on the side or
                                                             near the side airbag.
                                                           • Do not use excessive force on the side of the seat.
                                                           • For further information, see the owner's manual.
E. CAUTION : SRS clock spring                              F. CAUTION : AIRBAG ESPS UNIT
This is not a repairable part. Do not disassemble          Detach connector before unmounting. Assemble strictly
or tamper. If defective, replace entire unit as            according to manual instructions.
per service manual instructions.
To re-center, rotate clockwise until tight. Then rotate in
opposite direction approximately 3 turns and align -^<—
Failure to follow instructions may render SRS system
inoperative possibly resulting in serious driver injury.
G. CAUTION : SRS
Before removal of steering gearbox, read
service manual, center the front wheels and
remove the ignition key.
Failure to do so may damage the SRS clock spring
and render SRS system inoperative, possibly
resulting in serious the injury to the driver.
RT-6                                                                                                RESTRAINTS
ELECTRICAL SYSTEM                  ERHA0250                       Crash output
                                                                  The crash output is used to unlock the doors in case
The SRS airbag system has sophisticated electrical and            of a crash. The crash output is : 0-200 \xA in OFF
electronic components. Therefore the airbag operating             mode and 200mA in ON mode. During the unlock
components should be handled very carefully.                      command, the switch is closed for 200 mS.

SRSCM (Supplement Restraint System Control Mod-
ule)

The SRSCM will deploy the airbag modules by sensing the
frontal impact sensed by the sensor built in to the SRSCM.

1.   DC/DC converter; The DC/DC converter in the power
     supply includes a step-up and a step-down converter,
     which provides the firing voltage for four firing circuits
     and the internal operating voltage. If the internal op-
     erating voltage fails below a defined threshold, a reset
     is executed.

2.   Arming sensor/safing sensor : The arming/safing
     sensor built in to the airbag firing circuit has the
     function of arming the airbag circuit under all required
     deployment conditions and maintaining the airbag fir-
     ing circuits unarmed under normal driving conditions.
     The safing sensor is a dual-contact electromechani-
     cal switch that closes if it experiences a deceleration
     exceeding a specified threshold.

3.   Back-up power: The SRSCM reserves an energy re-
     serve to provide deployment energy for a short period
     when the vehicle voltage is low or if lost in a vehicle
     frontal crash.

4.   Malfunction detection : The SRSCM continuously
     monitors SRS operating status while the ignition key
     is turned on and detects possible malfunctions in the
     system. The malfunction can be displayed in the form
     of a diagnostic trouble codes using the Hi-Scan Pro.

5.   MIL (Malfunction Indication Lamp) notification : If any
     fault is detected, the SRSCM sends a signal to the
     indicator lamp on the instrument cluster to warn the
     vehicle driver.
     The MIL indicator is the key item in notifying the driver
     of SRS faults. It verifies lamp and SRSCM operation
     by flashing 6 times when the ignition switch is first
     turned on.

6.   Malfunction recording : Once a fault occurs in the
     system, the SRSCM records the fault in memory in
     the form of a DTC, which can only be erased by the
     Hi-Scan Pro.

7.   Data link connector; SRSCM memory stored is linked
     through this connector located underneath the driver
     side crash pad to an external output device such as
     the Hi-Scan Pro.

8.   After firing the airbags once, the SRSCM cannot be
     used again and must be replaced.
 SRSCM (SUPPLEMENTAL RESTRAINTS SYSTEM CONTROL MODULE)                                                                 RT-7

 SRSCM (SUPPLEMENTAL                                              all consist of an inflator and cushion. The initiator (a gas
                                                                  generator igniting device) is part the inflator. When the
 RESTRAINTS SYSTEM                                                vehicle is in a frontal or side crash of sufficient force to
 CONTROL MODULE)                                                  close the sensor of the SRSCM, current flows through the
                                                                  deployment loop. This current ignites the material and
                                                                  inflates the airbag.
 INFLATOR IODULE (DAB, PAB,
 SAB) ERJB0060
 DAB (Driver airbag), PAB (Passenger airbag) module,
 DSAB (Driver side airbag), PSAB (Passenger side airbag)




                                                            DAB



                                                                                    Clock spring




                                                                                                        PAB


                   BPT




                                                                                     SRSCM
                                Satellite sensor
                                                        SAB (option)




                                                                                                                      ERA9002A


1.   When removing the airbag module or handling a new                 Store the airbag module where the ambient tempera-
     airbag module, it should be placed with the pad top               ture remains below 93°C (200°F), without high humid-
     surface facing up. In this case, the twin-lock type con-          ity and away from electrical noise.
     nector lock lever should be in the locked state and
     care should be taken to place it so the connecter will       4.   During electric welding, disconnect the airbag under
     not be damaged. Do not store a steering wheel pad                 the steering column near the MULTI-FUNCTION
     on top of another one. (Storing the pad with its metal-           SWITCH connector before starting work.
     lic surface up may lead to a serious accident if the
     airbag should inflate accidentally.)

2.   Heyer measure the resistance of the airbag squib.
     (This may cause the airbag to deploy, which is very
     dangerous.)
RT~8                                                                                                         RESTRAINTS

SRS H A R N E S S      EROCOOTO                                MIL OPERATING METHOD                       ERJB0080


The SRS harness is wrapped in a yellow tube to be dis-                  Operating situation           Operating method
criminated from other system harnesses. A shorting bar
is included inside the wiring connectors of DAB, PAB, SAB        R
                                                                      o Return to normal from
and BPT inflator side. The shorting bar shorts the current       u      temporary fault
flow the DAB, PAB, SAB and BPT module circuits when the          N                                      O N ^ O f - b v . . r..
                                                                 N
connectors are disconnected. The circuits to the inflator        \    o Total faults frequency
module are shorted in this way to help prevent unwanted          N      ^ 5
deployment of the airbag when servicing the airbag mod-          G    o Active fault                 Turn it on continuously
ule.
SBSCM INDEPENDENT U W P ACTIVATION
                                                                 S
                                                                      o Normal                      JITLTLRJIJI
                                                                 T                                       Blink 6 times            j
The SRS malfunction indicator lamp (MIL) is located in the
cluster giving information of SRS operating conditions by        A
                                                                 R    o Total faults frequency
control signals from the SRSCM.                                  T
                                                                 I      <4                          On to off after 6 seconds
                                                                 N
                                                                 G    o Total faults frequency

                                                                      ©Active fault                 J                        1
                                                                                                     Turn it on continuously }
                                                                                                                          ERJB008A




                                                               CLOCK SPRING              ERJBOO90

                                                               The clock spring (coil spring) consists of two current carry-
                                                               ing coils. It is attached between the steering column and
                                                     KTOCOQU   the steering wheel. It allows rotation of the steering wheel
                                                               while maintaining continuous contact of the deployment
There are certain fault conditions in which the SRSCM          loop through the inflator module.
(SRS Control Module) cannot function and thus cannot
control the operation of the lamp. In these cases, the lamp
is directly activated by appropriate circuitry that operates
independently of the SRSCM, as follow :

1.   Loss of ignition voltage supply to the SRSCM : lamp
     turned on continuously.

2.   Loss of internal operating voltage : lamp turned on
     continuously.

3.   SRSCM not connected : lamp turned on through
     shorting bar in wiring harness connector.
                                                                                                                          ERJA010E


                                                               The steering wheel must be fitted correctly to the steering
                                                               column with the clock spring at the neutral position, other-
                                                               wise cable disconnection and other troubles may result.
SRSCM (SUPPLEMENTAL RESTRAINTS SYSTEM CONTROL MODULE)                                                       RT-9




                                                                                      Cover




                 Uppercase                                                         Rotor



                                                                                              Gear


                            Mark


                                                                                     Ring gear




                                                                Lower case


    When the rotor is rotated clockwise

                                                                                                           ERLB002C



SATELLITE SENSOR                ERKB0110                        a hammer, etc. Otherwise it could cause the airbag
                                                                system to unexpectedly deploy during servicing.
The release system for the side airbag consists of a
SRSCM installed in the middle of the vehicle and two
satellites - one on the left-hand side and one on the right.
Only the SRSCM is capable of deploying the airbags or
the seat-belt pretensioners systems in the vehicle. In
the dialog between the SRSCM and the satellite, it is the
SRSCM that makes the deployment decision.

The SRSCM is supported with the side airbag function by
two satellites, which act as intelligent acceleration sensors
and as such back up the central airbag controller. Both the
satellites continuously report the system status on the left
and right-hand sides of the vehicle to the SRSCM.

It monitors the acceleration sensor continuously. The test
results are reported to the SRSCM by means of periodic
status signals.

     mNOTE
    When the ignition is ON, never cause a sudden shock
    around the installation area of the satellite sensor by
RT-10                  RESTRAINTS
SYSTEM COMPONENT AND
LAYOUT   ERKB0120




                            ERKB012A
SRSCM (SUPPLEMENTAL RESTRAINTS SYSTEM CONTROL MODULE)   RT-11

SRSCM (SRS CONTROL MODULE) ERJBOISO




                                                        ERB9004A
IT -12                                                                                        RESTRAINTS
AIRBAG SYSTEM (SRS)



                                                                                                "^STEERING
                                                                                                Ri;iWHEEL




                                                                                                   ;MULTI-
                                                                                        , ,   .. , FUNCTION
                                                                                         •;    & , .VITCH




                                              :.•:;:•;•;:rBigfv;.:;; .     .::•:;:;-.Low-::..:•:/ CONTROL
                                                     S r S S I ^ S S S B l ^ . MODULE




                                                                         0.5P/B


                        Air bag
               DATA LINK CONNECTOR
                        Ground
                          V
                         5 M07
                       0.5B
                         10 M36
                         ^ A " . - | JOINT
                              -• -CONNECTOR

                        20 T M36                                                  I07
                      1.25B                         •O                                  PASSENGER
                                                                              -v        AIR BAG
                         A
         Q09             G11



                                                                                                            EROC014A
SRSCM (SUPPLEMENTAL RESTRAINTS SYSTEM CONTROL MODULE)                                                                              RT-13

SRSCM CONNECTOR
DAB+PAB4-SAB4-BPT EROCOISO
                                                            j
    11     2    3   4     5    6    7 | 0 I 3        10   11 12 13 14      15 16    17 18   19 20 I 21 I 22 I 23 24 25
                                                                                                         I        J
                          •    S    IP 1 ®    3 IP   •          %       . @ @   •   ®   @ #'    •   •'       •         •       •     &
                                                                    L


    26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ! 48 49 50

                                                ^L
                                                                                                                                   EROC016A


         PIN NO.                                            Function                                         Input/output
            1           Not used                                                                                           "
           2        1 Not used                                                                                             -
           3        1 Not used                                                                                             -
           4        : Not used •                                                                                           -
           5            Passenger satellite sensor, High                                                               Input
           6            Driver satellite sensor, High                                                                  Input
           7            Passenger side airbag, High                                                                   Output
           8            Passenger side airbag, Low                                                                    Output
           9            Driver side airbag, Low                                                                       Output
           10           Driver side airbag, High                                                                      Output
           11           Not used                                                                                           -
           12           Passenger airbag, Low                                                                         Output
           13           Passenger airbag, High                                                                        Output
I          14           Passenger seat belt buckle switch, High                                                       Input               |
           15           Driver airbag, Low                                                                            Output
           16           Driver airbag, High                                                                           Output
I          17           K-diagnostic line                                                                        Input/output
           18           Driver seat belt buckle switch, High                                                          Input               |
           19           Warning lamp                                                                                  Output
           20           GND                                                                                           Input
           21           Battery supply                                                                                Input
          22            Passenger belt pretensioner, Low                                                           Output
          23            Passenger belt pretensioner, High                                                          Output
           24           Driver belt pretensioner, High                                                             Output
1
           25           Driver belt pretensioner, Low                                                              Output
          26            Not used
          27            Not used                                                                                           -
          28            Not used                                                                                           "
          29            Not used                                                                                        "
          30            Passenger satellite sensor, Low                                                               Input
RT -14                                                   RESTRAINTS

|   PIN NO.                                   Function   Input/output
J    31       Driver satellite sensor, Low                  Input
|    32-33    Shorting bar                                    -
J   34-35     Shorting bar                                    "
I    36       Not used                                        "
!   37-38     Shorting bar                                    -
|     39      Passenger seat belt buckle switch, Low        input       ]
    40-41     Shorting bar                                   "
      42      Crash output                                 Output       |
      43      Driver seat belt buckle switch, Low           Input
    44-45     Shorting bar                                    •
      46      Seat buckle switch                           Output       |
    47-48     Shorting bar                                    '
    49-50     Shorting bar                                    "
AIR BAG MODULE (DRIVE SIDE) AND CLOCK SPRING                                                           RT-15

AIR BAG MODULE (DRIVE
SIDE) AND CLOCK SPRING
COMPONENTS       EROC0200




                                Clock spring


                                                                Steering wheel lock nut
                                                                40-50 (400-500,29-36)

                                                                                          DAB module




              Steering column


                                               Steering wheel



                                                                         4-6 (40-60,2.9-4.4)




   TORQUE : Nm (kg-em, lb-ft)

                                                                                                       EROC020A
                                                                                                     RESTRAINTS

REMOVAL         EROC0210                                      4.   Remove the drive airbag module.

1.   Disconnect the negative battery cable and keep se-
                                                                   & CAUTION
     cure from battery.
                                                                   The removed airbag module should be stored in a
                                                                   clean, dry place with the pad cover face up.
     $S CAUTION
     Wait at least 30 seconds after disconnecting the
     battery cable before doing any further work.




                                                                                                                KROB210C


                                                              5.   Remove    the    steering   wheel    using      SST
                                                   EADA011A        (09561-11002).

2.   Remove the side protect cover of steering wheel and           </fN> CAUTION
     airbag module mounting bolts using a hexagonal
     wrench.                                                       Do not hammer on the steering wheel. Doing so
                                                                   may damage the collapsible column mechanism.




                                                                                                       09561-11002




                                                   KROB210B

                                                                                                                KPKA014A
3.   When disconnecting the connector of the clock spring
     from the airbag module, pull the airbag's lock toward
     the outer side to spread it open.


     && CAUTION
     When disconnecting the airbag module-clock
     spring connector, take care not to apply exces-
     sive force to it




                                                   ERA9007C
AIR BAG; MODULE (DRIVE SIDE) AMD CLOCK SPRING                                                                      RT-17
INSPECTION         EROC0220                                    CLOCK SPRING              ,, :     .                 - ; •

AIRBAG MODULE                                                  1.   If, as a result of the following checks, even one abnor-
                                                                    mal point is discovered, replace the clock spring with
If any improper parts are found during the following inspec-        a new one.
tion, replace the airbag module with a new one.
                                                               2.   Check connectors and protective tube for damage,
Dispose the old one according to the specified procedure.           and terminals for deformities.

     </j\ CAUTION
     Never attempt to measure the circuit resistance
     of the airbag module (squib) even if you are us-
     ing the specified tester. If the circuit resistance is
     measured with a tester, accidental airbag deploy-
     ment will result in serious personal injury.

     Check pad cover for dents, cracks or deformities.

     Check the airbag module for denting, cracking or de-
     formation.                                                                                                     KPOB060F


     Check hooks and connectors for damage, terminals
     for deformities, and harness for binds.

4.   Check airbag inflator case for dents, cracks or defor-
     mities.




                                                    KFWE001A


5.   Install the airbag module to the steering wheel to
     check for fit or alignment with the wheel.




                                                    KPOB060B
RT-18                                                         RESTRAINTS

AIR BAG MODULE
(PASSENGER SIDE)
REMOVAL           ERKB0250

     g j j NOTE
     1. Never attempt to disassemble or repair the airbag
        module.
     2. Do not drop the airbag module or allow contact
        with water, grease or oil. Replace it if a dent
        crack, deformation or rust are detected.
     3. The airbag module should be stored on a flat sur-
        face and placed so that the pad surface is facing
        upward. Do not place anything on top of it
     4. Do not expose the airbag module to temperature
        over 93>C (20CTF)
     5. An undeployed airbag module should only be dis-
        posed in accordance with the procedures.
     6. Never attempt to measure the circuit resistance
        of the airbag module (squib) even if you are us-
        ing the specified tester. If the circuit resistance
        is measured with a tester, accidental airbag de-
        ployment will result in serious personal injury
     7. Whenever the PAB is deployed it should be re-
        placed with a new one assembled with an exten-
        sion wire. The squib is melt down if the PAB is
        deployed making the extension wire useless.

1.   Disconnect the battery negative (-) terminal cable.

     $\> CAUTION
     Wast at least 30 seconds.




                                                   EADA011A


2.   Remove the glove box.

3.   Disconnect the PAB module connector.

4.   Remove the crash pad assembly and then undo the
     PAB module. (Refer to the BD section)

5.   The skin of the passenger airbag module is integrated
     with the crash pad, therefore, the crash pad must be
     replaced if the PAB deploys.
AIR BAG MODULE (PASSENGER SIDE)                                                                               RT-19

PRETENSIONER SEAT BELT

COMPONENTS         ERJBO26O




                                                                    34 12       ! 3 14
                                                                    ft^     /     ///IS



                                                                            'A
                                                                          26




 1.COVER-L/RH                 13. BALL STOPPING SPRING    31. DISTANCE SHEET       43. SOLENOID ASSY
 2. BEARING PLATE-L7RH        14. BALL TRAP-L/RH          32. PINION GEAR          44. RETURN SPRING
 3. INTERTIA MASS             15. SCREW                   33. LABEL                45. SOLENOID LEVER-L/RH
 4. WEB SENSOR PAWL           16.TUBECOVER-L/RH           34. BALL ALUMINUM        46. T/R COVER-URH
 5. WEB SENSOR SPRING         17. REWINDING SPRING        35. TUB COVER (T/R)-L/RH 47. LOCK G ELEMENT (LA)-LyRH
 6. STEERING DISC-URH         18. SPRING CORE-L/RH        36. RIVET (T/R)          48. NECK
 7. BASE L/RH                 19. SPRING COVER-L/RH       37. RETAINER-L7RH        49. TREAD HEAD (W/STOP)-L/RH
 8. BALL L7RH                 20. RIVET                   38. BUSH SHAFT           50. TORSION BAR-5.5KN
 9. GAS GENERATOR             27. RETAINING WASHER-L/RH   39. REDUCE SPRING        51. SPINDLE (L/D-L/RH
 10. TUBE SPRING              28. LOCK DISC SPRING        40. HOLDER-L/RH          52. TREAD HEAD (W/OUT STOP)-L/RH
 11. PISTON                   29. LOCKING ELEMENT-L7RH    41. NORMAL SPRING
 12.TUBE-L/RH                 30. SPINDLE-LVRH            42. STAY SHAFT


                                                                                                              KFWE004A
RjjgO                                                                                                       RESIR^JNfS
FUNCTiOW O F PRETENSIONER                       ERHAO90O            The rack gear, rotates a piston gear arid a pinion rotates
                                                                    the planet gears.
When a vehicle crashes with a certain degree of frontal
impact, the gas generator will ignited an electrical firing         Finally, the webbing is retracted by the rotation of the
signal from the SRSCM (Supplemental Restraint System                spool. Therefore, the pretensioner seat belt helps to
Control Module).                                                    reduce the severity of injury to the front seat occupant
                                                                    by retracting the seat belt webbing. This prevents the
Gas from the gas generator causes movement of the pis-              occupant from thrusting forward and hitting the steering
ton in the manifold case (cylinder), which operates the rack        wheel or the instrument panel when the vehicle crashes.
gear.




                                                                        Gas generator
                                                               Spring




                                                                        Ball
                                                                        stopper
            Tube




                                Initial state              Operating state          Exploded state




                                                                                                                      KFWE005A
AIR BAG MODULE (PASSENGER SIDE)                                                                                     RT™21

LOAD LIMITER                                                     the crash force reaches a certain value, the torsion bar
                                                                 in the pretensioned seat belt will deform and cause the
The load limiter is designed to relieve the impact force to      webbing to extracted from the seat belt, thus, relieving the
an occupant chest's of the seat belt webbing when the            impact force.
occupant is restrained by the seat belt during a crash. If




                                                       Spindle




                                                                      Torsion bar




                                                                       Load = 5.5 kN

                                       Load < 5.5 kN




                                Webbing retracted                   Torsion bar deformed


                                                                                                                    KFWE006A
 RT-22                                                                                              RESTRAINTS
 REMOVAL         EROC0290

 1.   Disconnect the battery negative (-) terminal.

      $S CAUTION
      Wait at least 30 seconds.




                                                                                                              ESHA040J



                                                                 </f\> CAUTION
                                                                     Never attempt to disassemble or repair the
                                                                     BPT.
                                                                     Do not drop the BPT or allow contact with wa-
                                                      EADA011A
                                                                     ter, grease, oil.
                                                                     Replace it if a dent, crack, deformation or rust
2.    Remove the door scuff trim.                                    are detected.
                                                                     Do not place anything on the BPT.
                                                                     Do not expose the BPT to temperature over
                                                                     93PC(20(fF).
                                                                     BPT functions one time only. Be sure to re-
                                                                     place the BPT after it is deployed.
                                                                     Be sure to wear gloves and safety goggles
                                                                 a   when handling the deployed BPT.




                                                      KSOB170B


3.    Remove the quarter trim after removing seat belt
      lower anchor bolt.




                                                      KSOB170F


4.    Remove the upper anchor plate cover and upper an-
      chor plate.

5.    Remove the lower anchor plate and front seat belt.
TROUBLESHOOTING                                                    RT-23

TROUBLESHOOTING
DIAGNOSIS WITH SCAN TOOL ERKBO3OO

CHECK PROCEDURES

1.   Connect the Hi-Scan Pro DLC to the vehicle's data
     link connector located underneath the dash panel.

2.   Turn the ignition key to the "ON" position and turn the
     Hi-Scan Pro ON.

3.   Perform the SRS diagnosis according to the vehicle
     model configuration.

4.   If a fault code is assured, then replace the component.
     Never attempt to repair the component.

5.   If the Hi-Scan Pro finds that a component of the sys-
     tem is faulty, there is a possibility that the fault is not
     in the component, but in SRS wiring or connector.




                                                        ERLB005D
RT-24                                                                                                             RESTRAINTS
DIAGNOSTIC TROUBLESHOOTING
FLOW    ERNC0310 -




    Gathering information frorri               A              Verify complaint
|   the customer
                                                    * neuujuis                         * uues not reoccur

                              Check diagnostic trouble code      j                Check diagnostic trouble code
                                                      Diagnostic trouble                    Diagnostic trouble 1 No trouble
    No trouble code or can't                          code displayed                        code displayed       code
    communicate with
    Hi-Scan Pro                                                                        \r
                                                  Record diagnostic trouble code(s)
                                                | then erase them                   J


                                                                  »
                                               j    Check trouble code symptom               |



                                                j
                                                                     t
                                                    Check diagnostic trouble code            |
                                                                                                 No trouble
                                                                                                 code
                                                                                                              p


                                                                          Diagnostic trouble
                                                                          code displayed
                                 ]j                                  !J                                           j

                     Inspection chart for              Inspection chart for                       Intermittent malfunction
                      trout)le sym ptoms               diagnostic t rouble codes




                                                                                                                        ERA9035A
TROUBLESHOOTING                                                                                            RT-25
SPECIFICATION    EROC0320


                                                                                                     Unit: Q
    MIN     Coil, Re        Squib, Rs      Wiring harness, Rw         Connector terminal, RT Total resistance

    DAB         0.24           1.7                 0.05                        0.0                  1.99

    PAB          -             1.8                0.05                         0.0                  1.85

    BPT          -             1.8                0.06                         0.0                  1.86

    SAB          -             1.8                0.05                         0.0                  1.85


    MAX     Coil, RL        Squib, Rs      Wiring harness, Rw        Connector terminal, RT Total resistance

    DAB         0.54           2.3                0.20                        0.06                 3.10

    PAB          -             2.2                0.20                        0.06                 2.46

!   BPT          -             2.5                0.23                        0.04                 2.77

    SAB          -             2.2                0.20                        0.06                 2.46
                                                                                                           EROC032A




                                                                    Squib


                                                          Rs + Rt

                                                                            Rs: Squib resistance
                                                                            Rt: Terminal resistance
                                                                            Re : Contact coil resistance
                       Wiring harness
                                        Contact coil                        Rw : Wiring harness resistance




                                        R = Rs + Rt + Rw + Re



                                                                                                           EROC0328
RT-26                                                                             RESTRAINTS
AIRBAG SQUIB RESISTANCE
LIMITS    EROC0325


um
            R < 1.060      Resistance too low             Fault definitely detected
        1.801) < R<3.40O   Resistance whithin tolerance   Definitely no fault detected
           R > 6.70O       Resistance too high            Fault definitely detected
      1.06O< R < 1.80O
                           Tolerance band                 Fault may or may not be detected
      3.40O < R < 6.70O

PAB5 SAB, BPT

            R < 0.40       Resistance too low             Fault definitely detected
         1.60 < R < 2.80   Resistance whithin tolerance   Definitely no fault detected
            R > 5.40       Resistance too high            Fault definitely detected
         0.4O<R<1.6O
                           Tolerance band                 Fault may or may not be detected
         2.80 < R < 5.40
TROUBLESHOOTING                                                                                     RT -27
[MlMMIirciMlllOTIMIMffl^^     HIM     I IT



INSPECTION CHART FOR DIAGNOSTIC
TROUBLE CODE EROCOSSO
OPTIONS : DAB + PAB + SAB + BPT

                    DTC No.         Fault description
                      B1111         Battery voltage too high
                      B1112         Battery voltage too low
                      B1346         Driver airbag (DAB), Resistance too high
                      B1347         Driver airbag (DAB), Resistance too low
                      B1348         Driver airbag (DAB), Short to GND
                      B1349         Driver airbag (DAB), Short to Battery
                      B1352         Passenger airbag (PAB), Resistance too high
                      B1353         Passenger airbag (PAB), Resistance too low
                      B1354         Passenger airbag (PAB), Short to GND
                      B1355         Passenger airbag (PAB), Short to Battery
                      B1361         Driver seat belt pretensioner (DBPT), Resistance too high
                      B1362         Driver seat belt pretensioner (DBPT), Resistance too low
                      B1363         Driver seat belt pretensioner (DBPT), Short to GND
                      B1364         Driver seat belt pretensioner (DBPT), Short Battery
                      B1367         Passenger seat belt prestensioner (PBPT), Resistance too high
                      B1368         Passenger seat belt prestensioner (PBPT), Resistance too low
                      B1369         Passenger seat belt prestensioner (PBPT), Short to GND
                      B1370         Passenger seat belt prestensioner (PBPT), Short to Battery
                      B1378         Driver side airbag (DSAB), Resistance too High
                      B1379         Driver side airbag (DSAB), Resistance too Low
                      B1380         Driver side airbag (DSAB), Short to GND
                      B1381         Driver side airbag (DSAB), Short to Battery
                     B1382          Passenger side airbag (PSAB), Resistance too high
                     B1383          Passenger side airbag (PSAB), Resistance too low
                     B1384          Passenger side airbag (PSAB), Short to GND
                     B1385          Passenger side airbag (PSAB), Short to Battery
                     B1400          Satellite left side sensor defect
                     B1401          Satellite sensor left side short to GND
                     B1402          Satellite sensor left side open/short to battery
                     B1403          Satellite right side sensor defect
                     B1404          Satellire sensor right side short to GND
                     B1405          Satellire sensor right side open/short to battery
                     B1409          Satellite left side sensor communication error
                     B1410          Satellite right side sensor communication error
                     B1511          Driver seat belt buckle switch open/short to battery
RT-28                                                                              RESTRAINTS

        DTC No.          Fault description
1        B1512           Driver seat belt buckle switch short to GND
         B1513           Passenger seat belt buckle switch open/short to battery
        B1514            Passenger seat belt buckle switch short to GND
        B1620            Airbag unit internal failure                                       \
        B1650            SRSCM crash recorded
        B1655            Side airbag crash recorded
        B1657            Crash recorded-Belt pretensioner only
        B1661            ECU mismatching
        B2500            Warning lamp failure


        NOTE
    • The DAB is located in the steering wheel.
    • The PAB is located in the crash pad.
    • The DSAB is located in the left side of driver's
      seat.
    • The PSAB is located in the right side of passen-
      ger's seat
TROUBLESHOOTING                                                                                                                                    RT-29
     EROC0400



CIRCUIT INSPECTION

                                  B1111           Battery voltage too high (Vbaft > 19.2V)
            DTC
                                  B1112           Battery voltage too low (Vbaft < 7.2V)

CIRCUIT DESCRIPTION                                               2.   Check source voltage.

The SRS is equipped with a voltage-increase or decrease                1)    Connect the negative (-) terminal cable to the bat-
circuit (DC-DC converter) in the SRSCM in case the                           tery.
source voltage goes down or up. When the battery volt-
age is down or up the voltage-increase or decrease circuit             2)   Turn the ignition switch ON.
(DC-DC converter) function will increase or decrease the
voltage of the SRS to normal voltage. The diagnosis                                ON
system malfunction display for this circuit is different to
other circuits. When the SRS warning lamp remains lit up                    Connect SST
and the DTC is a B1111 or B1112 code, battery voltage                       0957A-38000
too high or low is indicated. When voltage returns to
normal, the SRS warning light automatically goes off and
                                                                                                                                   i
a malfunction is no longer indicated.                                                     \ 1»1 > 1. 111.1->| 11»M"j» MM-»HwH"M»'|°M*M
                                                                                          M IT|JW K f o l * « I " M " *I"P» » H " " t * «1"H"H"M


INSPECTION PROCEDURE

1.    Preparation
                                                                                                                                                   ERKB002B
      1)   Disconnect the negative (-) terminal cable from
           the battery, and wait at least 30 seconds.             [CHECK]

      2)   Remove the DAB module.                                 Measure voltage between the battery supply terminal 21
                                                                  of the SRS connector and body ground.
      3)   Disconnect the connectors of the PAB, left and
           right side airbags, belt pretensioners and satellite   LIMIT : 9-16V
           sensors.

      4)   Disconnect the SRSCM connector.
                                                                               Check the harness between the battery
                                                                               and the SRSCM. Check the battery and
                                                                               charging system




                                                                                                                                                   ERJB040A




                                                       EADA011A




      &    CAUTION
      Place the DAB with the front surface facing up-
      ward.
RT-30                                                       RESTRAINTS
    Does the SRS warning light turn off ?
    [PREPARATION]

    1)   Turn the ignition switch to LOCK.

    2)   Connect the DAB module.

    3)   Connect the PAB connector, left and right side
         airbag, belt pretensioner and satellite connec-
         tors.

    4)   Connect the SRSCM connector.

    5)   Turn the ignition switch ON.




                                                  KTOCOOU


[CHECK]

Check that the SRS warning light goes off.

           Check for DTCs. If a DTC is output,
           perform troubleshooting for the DTC.
           if B1111 or B1112 is output, replace the
           SRSCM.


From the results of the above inspection, the mal-
functioning part can now be considered normal. t
                                                 ERJB040B
TROUBLESHOOTING                                                                                                RT-31
                                                                                                                   '"""!"¥'''I1

    ERAC0410


CIRCUIT INSPECTION

                                B1348           DAB short to ground
                                 B1354          RAB short to ground
                                 B1363          DBPT short to ground
                                B1369           PBPT short to ground
           DTC
                                B1380           DSAB short to ground
                                B1384           PASB short to ground
                                B1401           Satellite sensor left side short to ground
                                B1404           Satellite sensor right side short to ground


CIRCUIT DESCRIPTION                                              satisfied. The above DTCs are recorded when a short to
                                                                 ground is detected in a squib circuit.
The squib circuit consists of the SRSCM, clock spring,
DAB, PAB, SAB, BPT, and satellite sensors. It causes the
SRS to deploy when the SRS deployment conditions are

i                  DTC Detecting Condition                                             Trouble Area
    •   Short circuit in squib wire harness (to ground)           • DAB squib
    •   Squib malfunction                                         • PAB squib
    •   Clock spring malfunction                                  • DSAB squib
    •   SRSCM malfunction                                         • PSAB squib
                                                                  • BPT squib
                                                                  • Satellite sensor
                                                                  • Clock spring
                                                                  * SRSCM
                                                                  • Wire harness


WIRING DIAGRAM



                                                                    High (+)
                                                           m         Low (-)
                                                                                 DSAB or PSAB
                                                                                 Squib

                                                                    High (+)
                                              Clock
                            S                 Spring   [>=DD         Low (-)
                                                                                  DAB Squib
                            R
                                                                    High (+)
                            S                             m          Low (-)   0 PAB Squib
                           C
                                                                    High {+)
                           M                                                   0 BPT Squib
                                                                     Low (-)

                                                                    High (+)

                                                                     Low (-)
                                                                             a Satellite
                                                                               Sensors



                                                                                                                ERA9011A
RT-32                                                                                                                   RESTRAINTS
INSPECTION PROCEDURE
                                                                           LOCK     I       1.

1.   Preparation
                                                                            ®           s
                                                                                        R                          High( + )
                                                                                        S                                      QPAB
     1)    Disconnect negative (-) terminal cable from the                                                          Low(-)-

           battery, and wait at least 30 seconds.                                       c
                                                                                        M

     2)    Remove the DAB module.                                                                  High (+)
                                                                                                              |!J-<G>
     3)    Disconnect the connectors of the PAB, left and                                           Low (-)                    X
           right side airbag, space belt pretensioner and
           satellite sensor.                                                                                                          ERA9011C


     4)    Disconnect the connector of the SRSCM.
                                                                        [CHECK]
                                                                        For the connector (on the SRSCM side) between
     &     CAUTION                                                      SRSCM and PAB, measure the resistance between
     Place the DAB with the front surface facing up-                    PAB high and body ground.
     ward.                                                              Resistance : «.

2.   Check DAB squib circuit.                                                    Repair or replace harness or connector
                                                                                 between the SRSCM and the PAB.
          LOCK   r——

          ft     s
                 R         r Clock
                                       High(+)

                 s                               QDAB
                           L Spring    Low (-)"
                 c                                                  Go to step "9'
                 M
                                                                                                                                      ERJB041B
                          High (+) r

                          Low (-)                                  4.   Check PSAB and DSAB squib circuits.

                                                        ERA9011B          LOCK   r"—""i.


     [CHECK]
                                                                          ®       S
                                                                                  R                                        SAB <LH)

                                                                                  S
     For the connector (on the clock spring side) between                         C
                                                                                                                           SAB (RH)

     clock spring and DAB, measure the resistance be-                             M
     tween DAB high and body ground.
     Resistance : °°                                                                             High (+)

                                                                                                 Low (-)
               Go to step "13"
                                                                                                                                      ERA9011D



                                                                        [CHECK]
                                                                        For the connector (on the SRSCM side) between
 Go to step "8'                                                         SRSCM and the SABs, measure the resistance
                                                                        between the SABs high and body ground.
                                                        ERJB041A
                                                                        Resistance : °°
3.   Check the PAB squib circuit.
                                                                                 Repair or replace the harness between
                                                                                 the SRSCM and the SAB.




                                                                    Go to step "10'

                                                                                                                                      ERJB041C
TROUBLESHOOTING                                                                                                                           RT-33

5.   Check the BPTs squib circuit.
                                                                        EB           Repair or replace the harness between
                                                                                     the SRSCM and the Satellite sensor.
       LOCK


        0s     R
                                             BPT (RH)

              Is
               c                      ==Q BPT (LH)
              IM                                                        Go to step" 12"

                       High (+)                                                                                                           ERJB041E



                       Low (-)                                         7.   Check the SRSCM.
                                                                            [PREPARATION]
                                                            ERA9011E
                                                                                Connect the connector to SRSCM.
                                                                                Using a service wire, connect the DAB high and
     [CHECK]                                                                    DAB low on the clock spring side of connector.
     For the connector (on the SRSCM side) between the                          Using a service wire, connect the PAB high and
     SRSCM and BPT, measure the resistance between                              low on SRSCM side of connector.
     the BPTs high and body ground.                                         4. Connect the SABs and BPT using the same
     Resistance : °°                                                            method.
                                                                            5. Connect the negative (-) terminal cable to battery,
                                                                                and wait it least 30 seconds.
              Repair or replace the harness between
              the SRSCM and the BPTs.
                                                                                ON
                                                                                                               :Q|SAB(L.H)            |

                                                                                                        m
                                                                                                        =00:          SAB (RH)


                                                                                                   gg,D=ap=nEZ]
 Go to step "11                                                                                    =0D==O|PAB                       1
                                                                                                                fl[
                                                            ERJB041D                                            :Q|BFT(LH)           I

                                                                                                                ; f l | Satellite (LH)]
6.   Check the Satellite sensor circuit
                                                                                                                 ] | Satellite (RH)|


       LOCK                                                                                                                               ERA9011G
                                     i^%

       ®      s
              R
                                           Satellite (LH)
                                                                            [CHECK]
              s
              c                            Satellite (RH)                   1. Turn ignition switch to ON, and wait for at least 30
              M                                                                seconds.
                                                                            2. Clear any codes stored in the memory with the
                      High (+)                                                 Hi-Scan Pro.
                                                                            3. Turn the ignition switch to LOCK, and wait for 30
                      Low (-)                                                  seconds.
                                                                            4. Turn the ignition switch to ON, and wait for 30
                                                            ERA9011F
                                                                               seconds.
                                                                            5. Using the Hi-Sacn Pro, check for DTCs.
     [CHECK]                                                                   There is no DTC.
     For the connector (on the SRSCM side) between the
     SRSCM and the Satellite sensor, measure the resis-
     tance between the Satellite high and body ground.
     Resistance : «>
RT-34                                                                                                            RESTRAINTS
     [HINT]
     Codes other than these may be output at this time, but          E 3 « # Replace the DAB.
     they are not relevant to this check.


               Replace the SRSCM.

                                                                     From the results of the above inspection, the mal-
                                                                     functioning part can now be considered normal.

                                                                                                                                 ERJB041G
 From the results of the above inspection, the mal-
 functioning part can now be considered normal.                         Check the PAB squib.
                                                                        [PREPARATION]
                                                                           Turn the ignition switch to LOCK.
                                                                            Disconnect the negative (-) terminal cable from
8.   Check the DAB squib.                                                  the battery, and wait for 30 seconds.
     [PREPARATION]                                                         Connect the PAB connector.
        Turn the ignition switch to LOCK.                                   Connect the negative (-) terminal cable from the
         Disconnect the negative (-) terminal cable from                    battery, and wait for 30 seconds.
        the battery, and wait for 30 seconds.
         Connect the DAB connector.
         Connect the negative (-) terminal cable to the bat-                 ON
                                                                                                    =DD=
        tery, and wait for 30 seconds.
                                                                                                    flit

          ON
                                 d&         SAB (LH)                                                 [J
                                                                                                    ®&%      i

                                 m                                                                                    (LH)




                          ==o[J=3i[                                                                                    m
                                                                                                            0 11 Sensor
                                                                                                                 Satellite
                                                                                                                          (HH)
                          =     Q     [
                                            BPT (LH)
                                                                                                                                 ERA9011J
                                                   <LH)

                                                                        [CHECK]
                                                                        1. Turn the ignition switch to ON, and wait for at least
                                                          ERA9011!         30 seconds.
                                                                        2. Clear the malfunction code stored in the memory
     [CHECK]                                                               with the Hi-Scan Pro.
     1. Turn the ignition switch to ON, and wait for at least           3. Turn the ignition switch to LOCK, and wait for 30
        30 seconds.                                                        seconds.
     2. Clear the malfunction code stored in the memory                 4. Turn the ignition switch to ON, and wait for 30
        of the Hi-Scan Pro.                                                seconds.
     3. Turn the ignition switch to LOCK, and wait for 30               5. Using the Hi-Sacn Pro, check for DTCs.
        seconds.                                                           There is no DTC.
     4. Turn the ignition switch to ON, and wait for 30
        seconds.
     5. Using the Hi-Scan Pro, check for DTCs.
        There is no DTC.

     [HINT]
     Codes other than these may be output at this time, but
     they are not relevant to this procedure.
TROUBLESHOOTING                                                                                                                   RT-35
    [HINT]
    Codes other than these may be output at this time, but                      Replace the SAB.
    they are not relevant to this procedure.


              Replace the PAB.
                                                                   From the results of the above inspection, the mal-
                                                                   functioning part can now be considered normal.

                                                                                                                                   ERJB041I

 From the results of the above inspection, the mal-
                                                                  11. Check BPT squib.
 functioning part can now be considered normal.
                                                                      [PREPARATION]
                                                       ERJB041H          Turn the ignition swich to LOCK.
                                                                          Disconnect the negative (-) terminal cable from
10. Check the SABs squib.                                                the battery, and wait for 30 seconds.
    [PREPARATION]                                                        Connect the BPTs connector.
    1. Turn the ignition switch to LOCK.                                 Connect the negative (-) terminal cable from the
       Disconnect the negative (-) terminal cable from                   battery, and wait for 30 seconds.
       the battery, and wait for 30 seconds.
       Connect the SAB connector.                                          ON
       Connect the negative (-) terminal cable from the
       battery and wait for 30 seconds.
                                                                                                   m          SAB (RH)
                                                                                                   m
                                                                                             =00=
                                                                                                        €
         ON                            a                                                                      BPT(RH)

                                                                                                              BPT(LH) : |

                                                                                                         j ] | Satellite (LH) |


                           =OD=OEL                                                                      4     Satellite (RH)!



                                                                                                                                  ERA9011K



                                              m
                                         Satellite
                                                                     [CHECK]
                                         Sensor (RH)
                                                                     1. Turn the ignition switch to ON, and wait for 30
                                                                        seconds.
                                                       ERJB001A
                                                                     2. Clear the malfunction code stored in the memory
                                                                        with the Hi-Scan Pro.
   [CHECK]                                                           3. Turn the ignition switch to LOCK, and wait for 30
                                                                        seconds.
   1. Turn the ignition switch to ON, and wait for at least
                                                                     4. Turn the ignition switch to ON, and wait for 30
      30 seconds.
                                                                        seconds.
   2. Clear the malfunction code stored in the memory
                                                                     5. Using the Hi-Scan Pro, check for DTCs.
      with the Hi-Scan Pro.
                                                                        There is no DTC.
   3. Turn the ignition switch to LOCK, and wait for 30
      seconds.
   4. Turn the ignition switch ON, and wait for 30 sec-
      onds.
   5. Using the Hi-Sacn Pro, check for DTCs.
      There is no DTC.


   [HINT]
   Codes other than these ones may be output at this
   time, but they are not relevant to this checking proce-
   dure.

       NOTE
   Check the DSAB using the same procedure.
RT-36                                                                                                           RESTRAINTS
    [HINT]
    Codes other than these may be output at this time, but                          Replace the Satellite sensor.
    they are not relevant to this procedure.


             Replace the BPT.

                                                                       From the results of the above inspection, the mal-
                                                                       functioning part can now be considered normal.

                                                                                                                            ERJB041K

 From the results of the above inspection, the mal-
 functioning part can now be considered normal.                        13. Check clock spring circuit.
                                                                           [PREPARAION]
                                                            ERJB041J       Disconnect connector between SRSCM and clock
                                                                           spring.
12. Check the Satellite sensors.
    [PREPARATION]
    1. Turn ignition switch to LOCK.                                         LOCK    i       |.

    2. Disconnect negative (-) terminal cable from the
        battery, and wait at least 30 seconds.
                                                                              ® R    Is
                                                                                         S
    3. Connect the Satellite sensor connector.
    4. Connect the negative (-) terminal cable from the
                                                                                         c
                                                                                         M
        battery, and wait at least 30 seconds.

                                                                                                  Low (-)
        ON
                                m      a SAB{LH)
                                lQ0    D[SAB(RH)
                                                                                                                        ERKB010B
                          S£|]=0D=te
                                flft                                      [CHECK]
                                           BPT (LH)
                                                                          Measure resistance between the DAB high on the
                                       :Q|BPT(RH)                         clock spring side of connector between clock spring
                                           Satellite (LH)                 and DAB and body ground.
                                                                          Resistance : <*>
                                       OL Satellite (RH)
                                                            ERAC041A
                                                                                 Replace the clock spring.
    [CHECK]
    1. Turn the ignition switch to ON, and wait at least
       30 seconds.
    2. Clear the malfunction code stored in memory
       with the Hi-Scan Pro.
                                                                       Repair or replace the harness or the connector
    3. Turn the ignition switch to LOCK, and wait at least
                                                                       between the SRSCM and the clock spring.
       30 seconds.
    4. Turn the ignition switch to ON, and wait at least                                                                ERDA027R
       30 seconds.
    5. Using the Hi-Scan Pro, check for DTCs.
       There is no DTC.

   [HINT]
   Codes other than these may be output at this time, but
   they are not relevant to this procedure.
TROUBLESHOOTING                                                                                                     RT-37
  ERAC0420


CIRCUIT INSPECTION

                                B1349          DAB short to battery
                                B135.5         PAB short to battery
                               B1364           DBPT short to battery
                               B1370           PBPT short to battery
          DTC
                               B1381           DSAB short to battery
                               B1385           PSAB short to battery
                               B1402           Satellite left side short to battery
                               B1405           Satellite right side short to battery

CIRCUIT DESCRIPTION                                                  causes the SRS to deploy when the SRS deployment con-
                                                                     ditions are satisfied. The above DTCs are recorded when
The squib circuit consists of the SRSCM, clock spring,               a B+ short is detected in the squib circuit.
DAB, PAB, DSAB, PSAB, BPT and satellite sensor. If it

                  DTC Detecting Condition                                                   Trouble Area
   •   Short circuit in squib wire harness (to B+)                   • DAB squib
   •   Squib malfunction                                             • PAB squib
   •   Clock spring cable malfunction                                • DSAB or PSAB squib
   •   SRSCM malfunction                                             • BPT squib
                                                                     • Satellite sensor
                                                                     • Wire harness

WIRING DIAGRAM



                                                                       High (+)
                                                           m            Low (-
                                                                                     DSAB or PSAB
                                                                               0 Squib
                                                                       High (+)
                                          r Clock ~1      ,[-] r i
                          S               L
                                            Sorina _ l    U    U                     DAB Squib
                                                                        Low (-}
                          R                                            High (+)
                          S                               m             Low (-)
                                                                                  a PAB Squib
                          C
                                                                       High (+)
                          M                                                          BPT Squib
                                                                        Low (-)

                                                                       High (+)
                                                                                     Satellite
                                                                        Low (-)
                                                                                D Sensors

                                                                                                                     ERA9011A
RT-38                                                                                                                    RESTRAINTS

INSPECTION PROCEDURE                                                    ON I       1,


1.   Preparation                                                      0        s
                                                                               R                                     High (+)
                                                                                                                                PAB
                                                                               S !                                   Low(-)
                                                                               C
     1)   Disconnect negative (-) terminal cable from the
                                                                               M i
          battery, and wait at least 30 seconds.                                                         /
                                                                                             High (+) _ r    (+) ^   H


     2)   Remove the DAB module.
                                                                                             Low(-

     3)   Disconnect the connectors of the PAB, left and
          right side airbag,belt pretensioner and satellite
          sensor.                                                                                                                     ERA9011P

     4)   Disconnect the connector of the SRSCM.
                                                                   [CHECK]
                                                                   For the connector (on the SRSCM side) between the
     /h> CAUTION                                                   SRSCM and PAB, measure the voltage between the
     Place the DAB with the front surface facing up-               PAB high and body ground.
     ward.                                                         Voltage : 0 V

2.   Check the DAB squib circuit.
                                                               MM           Repair or replace the harness between
                                                                            the SRSCM and the PAB.
           ON
                s
                R          Clock        Hg
                                         i h (•)
                S          Spring I
                                       o==aDAB
                                        Low(-}*
                c                                              Go to step "9'
                M
                      High (+)
                                  /I                                                                                                  ERJB042A


                       Low (-)                                4.   Check the SAB squib circuit.

                                                   ERAC042A            ON

                                                                                                                           SAB (LH)

     [CHECK]
     For the connector (on the clock spring side) between
     the clock spring and DAB, measure the voltage be-                                                   HBD=D SAB (RH)
     tween the DAB high and body ground.
     Voltage : 0 V                                                                      High (+)
                                                                                                     /

                                                                                        Low (-)

 E 3 - # G O to step "131
                                                                                                                                      ERA9011Q


                                                                   [CHECK]
                                                                   For the connector (on the SRSCM side) between the
 Go to step "8'                                                    SRSCM and SAB, measure the voltage between the
                                                                   SAB high and body ground.
                                                   ERJB041A        Voltage : 0 V

3.   Check the PAB squib circuit.
                                                               I f f B j ^ Repair or replace the harness between
                                                               • * * a " * the SRSCM and the SAB.




                                                               Go to step "10'

                                                                                                                                      ERJB041C
TROUBLESHOOTING                                                                                                                        RT -39

5.   Check the BPTs squib circuits.
                                                                                        Repair or replace the harness between
                                                                                        the SRSCM and the Satellite sensor.
         ON

                                            =0 BPT <RH)

                                             m     BPT (LH)

                                                                             Go to step "12'

                       High (+)   /                                                                                                     ERJB041E


                       Low (-)                                              7.   Check the SRSCM.

                                                                 ERA9011R             ON                    flU

     [CHECK]                                                                        0                       flD:
     For the connector between SRSCM and the BPTs,                                                      =0D=       =00
     measure the voltage between the BPTs high and body                                                            ^3[8PT(RH)      j
     ground.
     Voltage : 0 V
                                                                                                                      Sensor fH)

                                                                                                                           Lies.
              Repair or replace the harness between
              the SRSCM and the BPTs.
                                                                                                                                        ERJB002B


                                                                                 [PREPARATION]
                                                                                 1. Connect the connector to the SRSCM.
 Go to step "11                                                                  2. Using a service wire, connect the DAB high and
                                                                                     low on the clock spring side of connector between
                                                                 ERJB041D           the clock spring and the DAB.
                                                                                 3. Using a service wire, connect the PAB high and
6.   Check the Satellite sensor circuit.                                             low on the SRSCM side of the connector between
                                                                                    the SRSCM and the PAB.
         ON                                                                      4. Using a service wire, connect the SAB high and
       0       s
              ! R
                                                Satellite (LH)                       low on the SRSCM side connector between the
                                                                                    SRSCM and the SAB.
               S
               C                                                                 5. Using a service wire, connect the BPT high and



                                 z
               M
                                          =0 Satellite (RH)                         low on the SRSCM side connector between the
                                                                                    SRSCM and the BPT
                                                                                 6. Using a service wire, connect the satellite high
                     High (+)

                                r^^L
                                      W /T\ H                                       and low on the SRSCM side connector between
                      Low (-)
                                                                                    the SRSCM and the satellite sensor.
                                                                                 7. Connect negative (-) terminal cable to battery,
                                                                                    and wait at least 30 seconds.
                                                                 ERA9011S


     [CHECK]                                                                     [CHECK]
     For the connector between the SRSCM and the Satel-                          1. Turn the ignition switch to ON, and wait at least
     lite sensor, measure the voltage between the Satellite                         30 seconds.
     sensor high and body ground.                                                2. Clear the malfunction code stored in memory
     Voltage : 0 V                                                                  with the Hi-Scan Pro.
                                                                                 3. Turn the ignition switch to LOCK, and wait at least
                                                                                    30 seconds.
                                                                                 4. Turn the ignition switch to ON, and wait at least
                                                                                    30 seconds.
                                                                                 5. Using the Hi-Scan Pro, check for DTCs.
                                                                                    There is no DTC.
RT -40                                                                                                                     RESTRAINTS
   [HINT]
   Codes other than these may be output at this time, but                      I f l M -#> Replace the DAB.
   they are not relevant to this check.


          Replace the SRSCM.

                                                                               From the results of the above inspection, the mal-
                                                                               functioning part can now be considered normal.

                                                                                                                                         ERJB041G

From the results of the above inspection, the mal-
functioning part can now be considered normal.                                    Check the PAB squib.
                                                                                  [PREPARATION]
                                                                                     Turn the ignition switch to LOCK.
                                                                                      Disconnect the negative (-) terminal cable from
   Check the DAB squib.                                                              the battery, and wait for 30 seconds.
   [PREPARATION]                                                                      Connect the PAB connector.
   1. Turn the ignition switch to LOCK.                                              Connect the negative (-) terminal cable from the
       Disconnect the negative (-) terminal cable from                                battery, and wait for 30 seconds.
      the battery, and wait for 30 seconds.
      Connect the DAB connector.
      Connect the negative (-) terminal cable to the bat-                              ON
      tery, and wait for 30 seconds.                                                                               flU
                                                                                                                   flU
                                                                                                          Clock
                                                                                                          Spring   C=0D=0[

         ON
                                                                                                                   = * [   Satellite

                         Clock h    ™      H|
                                                9   h(+
                                                          U
                                                              DAB
                                                                                                                   = o [   Sensor (LH)


                         Spring
                                   -i>#;                                                                                         isa.
                                                                                                                                         ERA9011J


                                                                                  [CHECK]
                                                                                  1. Turn the ignition switch to ON, and wait for at least
                                                                    ERA9011U         30 seconds.
                                                                                  2. Clear the malfunction code stored in the memory
   [CHECK]                                                                           with the Hi-Scan Pro.
   1. Turn the ignition switch ON, and wait for at least                          3. Turn the ignition switch to LOCK, and wait for 30
      30 seconds.                                                                    seconds.
   2. Clear the malfunction code stored in the memory                             4. Turn the ignition switch ON, and wait for 30 sec-
      of the Hi-Scan Pro.                                                            onds.
   3. Turn the ignition switch to LOCK, and wait for 30                           5. Using the Hi-Sacn Pro, check for DTCs.
      seconds.                                                                       There is no DTC.
   4. Turn the ignition switch to ON, and wait for 30
      seconds.
   5. Using the Hi-Scan Pro, check for DTCs.
      There is no DTC.

   [HINT]
   Codes other than these may be output at this time, but
   they are not relevant to this procedure.
TROUBLESHOOTING                                                                                                            RT-41
    [HINT]
    Codes other than these may be output at this time, but                         Replace the SAB.
    they are not relevant to this procedure.


             Replace the PAB.

                                                                       From the results of the above inspection, the mal-
                                                                       functioning part can now be considered normal.

                                                                                                                            ERJB041I
 From the results of the above inspection, the mal-
 functioning part can now be considered normal.                       11. Check the BPTs squib.
                                                                          [PREPARATION]
                                                           ERJB041H          Turn the ignition swich to LOCK.
                                                                              Disconnect the negative (-) terminal cable from
10. Check the SAB squib.                                                     the battery, and wait for 30 seconds.
    [PREPARATION]                                                            Connect the BPTs connector.
    1. Turn the ignition switch to LOCK.                                     Connect the negative (-) terminal cable from the
    2. Disconnect the negative (-) terminal cable from                       battery, and wait for 30 seconds.
       the battery, and wait for 30 seconds.
    3. Connect the SAB connector.
    4. Connect the negative (-) terminal cable from the
       battery, and wait for 30 seconds.                                      ON

                                                                                                            D   BPT (RH)




        ON
             *>«»                                                                                               BPT{LH)


      u2                           Low (-)
                                                SAB (LH)


                                  High (+) H>
                                                SAB(RH)
                                   Low {-)
                                                                                                                           ERA9011X


                                                                         [CHECK]
                                                                         1. Turn the ignition switch to ON, and wait for 30
                                                           ERA9011W         seconds.
                                                                         2. Clear the malfunction code stored in the memory
   [CHECK]                                                                  with the Hi-Scan Pro.
   1. Turn the ignition switch to ON, and wait for at least              3. Turn the ignition switch to LOCK, and wait for 30
      30 seconds.                                                           seconds.
   2. Clear the malfunction code stored in the memory                    4. Turn the ignition switch to ON, and wait for 30
      with the Hi-Scan Pro.                                                 seconds.
   3. Turn the ignition switch to LOCK, and wait for 30                  5. Using the Hi-Scan Pro, check for DTCs.
      seconds.                                                              There is no DTC.
   4. Turn the ignition switch ON, and wait for 30 sec-
      onds.
   5. Using the Hi-Sacn Pro, check for DTCs.
      There Is no DTC.

   [HINT]
   Codes other than these may be output at this time, but
   they are not relevant to this procedure.
RT-42                                                                                                               RESTRAINTS

   [HINT]
   Codes other than these may be output at this time, but                       Replace the Satellite sensor.
   they are not relevant to this procedure.


| 2 | | <«|> Replace the BPT.
                                                                     From the results of the above inspection, the mal-
                                                                     functioning part can now be considered normal.

                                                                                                                                ERJB041K

From the results of the above inspection, the mal-
functioning part can now be considered normal.                       13. Check the Clock spring.
                                                                         [PREPARAION]
                                                          ERJB041J       1. Turn the ignition switch to LOCK.
                                                                         2. Disconnect the connector between the SRSCM
12. Check the Satellite sensors.                                            and the clock spring.
    [PREPARATION]
    1. Turn ignition switch to LOCK.
    2. Disconnect the negative (-) terminal cable from                        ON
       the battery, and wait at least 30 seconds.
    3. Connect the Satellite sensor connector.                                                Clock
                                                                                                               HighM
                                                                                                                         ]DAB
    4. Connect the negative (-) terminal cable from the                                       Spring            Low(-)

        battery, and wait at least 30 seconds.
                                                                                          High(+) ,_,f /   w/^(-)


                                                                                          Low (-)                    J_
        ON

                                     U Satellite (LH)
                                                                                                                                ERAC042A


                                     0   Satellite (RH)                  [CHECK]
                                                                         Turn the ignition switch ON, and measure the voltage
                                                                         between the DAB high side and the body ground.
                                                                         Voltage : 0V

                                                          ERA9011Y
                                                                                Replace the clock spring.
    [CHECK]
    1. Turn the ignition switch to ON, and wait at least
       30 seconds.
    2. Clear the malfunction code stored in memory
       with Hi-scan.
    3. Turn the ignition switch to LOCK, and wait at least            Repair or replace the harness or the connector
       30 seconds.                                                    between the SRSCM and the clock spring.
    4. Turn the ignition switch to ON, and wait at least
                                                                                                                                ERDA027R
       30 seconds.
    5. Using the Hi-Scan Pro, check for DTCs.
       There is no DTC.

   [HINT]
   Codes other than these may be output at this time, but
   they are not relevant to this procedure.
TROUBLESHOOTING                                                                                           RT -43
  EROC0430


CIRCUIT INSPECTION

                             B1346          DAB resistance too high (R > 6.70 0)
         DTC
                             B1347          DAB resistance too low (R < 1.06 H)

CIRCUIT DESCRIPTION                                          DAB resistance too high or low is detected in the DAB
                                                             squib circuit.
The DAB squib circuit consists of the SRSCM, the clock
spring, the DAB. It causes the airbag to deploy when the
airbag deployment conditions are satisfied. The above
DTCs are recorded when the DAB circuit is open or the

                DTC Detecting Condition                                         Trouble Area
   ® Too high or low resistane between DAB high (t) wiring   • DAB squib
     harness and DAB low (-) wiring harness of squib.
   ® DAB malfunction                                         • Clock spring
   • Clock spring malfunction                                • SRSCM
   ® SRSCM malfunction                                       • Wire harness

WIRING DIAGRAM
RT-44                                                                                                                         RESTRAINTS

INSPECTION PROCEDURE                                                LOCK


1.   Preparation                                                                                 Clock
                                                                                                                        High (+)
                                                                                                 Spring
                                                                                                                                       DAB
                                                                                                                        Low {-)
     1)   Disconnect the negative (-) terminal cable from
          the battery, and wait at least 30 seconds.                        UH                                  i
                                                                            L_lw                                |
     2)   Remove the DAB module.                                               ,—. High (+) i         1        J*       ,


     3)   Disconnect the connectors of the PAB, left and
          right side airbags, belt pretensioners and satellite
                                                                    C^      M H                 ciock — r n — DUMMY
                                                                                                                    4
                                                                                                           Dummy adapter
          sensors.                                                                                                                           ERKB010C

     4)   Disconnect the SRSCM connector.                        [CHECK]
                                                                 Measure the resistance between the DAB high (-$-) and
                                                                 low (-).
                                                                 1.80O<R<3.40O


                                                                           Go to step "41




                                                      EADA011A                                                                               ERJB043A



     ^    CAUTION                                                Check the DAB squib.
                                                                 [PREPARATION]
     Place the DAB with the front surface facing up-
                                                                 1. Turn the ignition switch to LOCK.
     ward.                                                       2. Disconnect the negative (-) terminal cable from
                                                                    the battery, and wait for 30 seconds.
     Check the DAB resistance.
                                                                 3. Connect the DAB connector.
     [PREPARATION]
                                                                 4. Connect the negative {-) terminal cable to the bat-
     Release the airbag activation prevention mechanism
                                                                    tery, and wait for 30 seconds.
     on SRSCM side of airbag squib side. Connect the
     dummy (0957A-38200) and dummy adapter (0957A-
     38400) to the clock spring side connector.

                                                                       ON
     </?\> CAUTION
     Never attempt to measure the circuit resistance                ©         s
                                                                              R                   Clock I
                                                                                                         i-,                High (+)

     of the airbag moduie (squib) even if you are using                       S        —        L Spring Jfc=0D==aLow{-r DAB
                                                                              C                                     «^4->
     the specified tester                                                     M


     m NOTE
     Before checking the resistance, you have to insert the
     shorting bar insert plastic that is attached to the diag-                                                                               ERA9011U

     nosis checker into the SRSCM connector.
TROUBLESHOOTING                                                                                                               RT-45
    [CHECK]
    1. Turn the ignition switch to ON, and wait for at least                           Replace the clock spring.
       30 seconds.
    2. Clear the malfunction code stored in the memory
       with the Hi-Scan Pro.
    3. Turn the ignition switch to LOCK, and wait for 30
                                                                             EZ3
       seconds.
    4. Turn the ignition switch to ON, and wait for 30                       Repair or replace the harness or the connector
       seconds.                                                              between the SRSCM and the clock spring.
    5. Using Hi-Scan Pro, check the DTC.
                                                                                                                              ERDA027R
       There Is no DTC.

    [HIMT]
    Codes other than these may be output at this time, but
    they are not relevant to this procedure.


              Replace the DAB.




From the results of the above inspection, the mal-
functioning part can now be considered normal.

                                                                  ERJB041G


:   Check the clock spring.
    [PREPARAION]
    Disconnect the connector between the SRSCM
    clock spring, and connect the dummy connector
    (0957A-38200) and dummy adapter (0957A-38400)
    to the clock spring side connector.

    Qj NOTE
    Before checking the resistance, you have to insert the
    shorting bar insert plastic that is attached to the diag-
    nosis checker into the SRSCM connector.

       LOCK

       ©        S
                R                 Clock            High {+) _,
                S                ^Spring       D          'RDAB
                                                    Low (-)'
                C
                M

                    High {+) i      ,        I_


       dO                     Clock
                    — — ~ Spring
                     Low (-) I———J
                                             V
                                             TT
                                             U-
                                                        DUMMY


                                           Dummy adapter



    [CHECK]
    Measure the resistance between the DAB high (+) and
    low (-).
    1.80O<R<3.40£}
RT-46                                                                                           RESTRAINTS
  EROC0440


CIRCUIT INSPECTION

                            B1352          PAB resistance too high (R > 5.4 0)
         DTC
                            B1353          PAB resistance too low (R < 0.4 0)

CIRCUIT DESCRIPTION                                        when the PAB circuit is open or the PAB resistance too
                                                           high or low is detected in the PAB squib circuit.
The PAB squib circuit consists of the SRSCM and PAB. It
causes the airbag to deploy when the airbag deployment
conditions are satisfied. The above DTCs are recorded

                DTC Detecting Condition                                          Trouble Area
   • Too high or low resistance between PAB                • PAB squib
     high (+) wiring harness and PAB low (-)
     wiring harness of squib.
   • PAB malfunction                                       * SRSCM
   • SRSCM malfunction                                     © Wire harness

WIRING DIAGRAM




                                                                                                          ERA9012E
TROUBLESHOOTING                                                                                                                   RT-47

INSPECTION PROCEDURE                                                         Measure the resistance between the PAB high (n-) and
                                                                             the PAB low (-).
1.   Preparation                                                             1.6 0 < R < 2 . 8 0

     1)   Disconnect the negative (-) terminal cable from
          the battery, and wait at least 30 seconds.                                Repair or replace the harness between
                                                                                    the SRSCM and the PAB.
     2)    Remove the DAB module.

     3)   Disconnect the connectors of the PAB, left and
          right side airbags, belt pretensioners and satellite
          sensors.
                                                                                                                                  ERJB044A

     4)    Disconnect the SRSCM connector.
                                                                        3.   Check the PAB squib.
                                                                             [PREPARATION]
                                                                             1. Turn the ignition switch to LOCK.
                                                                             2. Disconnect the negative (-) terminal cable from
                                                                                the battery, and wait for 30 seconds.
                                                                             3. Connect the PAB connector.
                                                                             4. Connect the negative (-) terminal cable to the bat-
                                                                                tery, and wait for 30 seconds.




                                                             EADA011A             ON


                                                                                                                    High(+)
     ^    CAUTION                                                                                           CD       Low   JPAB
                                                                                                            E#>4a          H
     Place the DAB with the front surface facing up-
     ward.

     Check the PAB resistance.
     [PREPARATION]
     Release the airbag activation prevention mechanism                                                                           ERA9011V

     on the SRSCM side of the airbag squib side. Con-
     nect the dummy (0957A-38200) and dummy adapter                          [CHECK]
     (0957A-38300) to PAB connector of the SRSCM con-                        1. Turn the ignition switch to ON, and wait for at least
     nector side.                                                               30 seconds.
                                                                             2. Clear the malfunction code stored in the memory
                                                                                with the Hi-Scan Pro.
          NOTE
                                                                             3. Turn the ignition switch to LOCK, and wait for 30
     Before checking the resistance, you have to insert the                     seconds.
     shorting bar insert plastic that is attached to the diag-               4. Turn the ignition switch to ON, and wait for 30
     nosis checker into the SRSCM connector.                                    seconds.
                                                                             5. Using Hi-Scan Pro, check the DTC.
          LOCK                                                                  There is no DTC.
          ft
                                          High (+)
                                                    JPAB |
                                           Low(-)




                 High (+)
                                  I
                 «OE
                 Low (-)
                                      4
                                           DUMMY


                                 Dummy adapter
                                                             ERKB010E


     [CHECK]
RT-48                                                       RESTRAINTS
   [HINT]
   Codes other than these may be output at this time, but
   they are not relevant to this procedure.


          Replace the PAB.




From the results of the above inspection, the mal-
functioning part can now be considered normal.
TROUBLESHOOTING                                                                                                    RT-49

     EROC0450


CIRCUIT INSPECTION

                                B1378         DSAB Resistance too high (R > 5.4 ft)
                                B1379         DSAB Resistance too low (R < 0.4 fi)
t           DTC
                                B1382         PSAB Resistance too high (R > 5.4 Q)
                                B 1.383       PSAB Resistance too low (R < 0.4 tt)


CIRCUIT DESCRIPTION                                            conditions are satisfied. The above DTCs are recorded
                                                               when the SAB circuit is open or the SAB resistance too
The SAB squib circuit consists of the SRSCM and SAB. It        high or low is detected in the SAB squib circuit.
causes the airbag to deploy when the airbag deployment

                    DTC Detecting Condition                                         Trouble Area
     • Too high or low resistane between SAB high (+) wiring   • SAB squib
i      harness and SAB low («) wiring harness of squib.
|    ® SAB malfunction                                         • SRSCM
     « SRSCM malfunction                                       • Wire harness


WIRING DIAGRAM




                            S                                      High (+)
                                                                               SAB (LH)
                            R
                            S
                            C                                      High (+)
                            M                                                  SAB (RH)




                                                                                                                    ERJB045B


INSPECTION PROCEDURE                                               2)   Remove the DAB module.

1.    Preparation                                                  3)   Disconnect the connectors of the RAB, left and
                                                                        right side airbags, belt pretensioners and satellite
      1)   Disconnect the negative (-) terminal cable from              sensors.
           the battery, and wait at least 30 seconds.
RT -50                                                                                                        RESTRAINTS
   4)    Disconnect the SRSCM connector.                          Check the SAB squib.
                                                                  [PREPARATION]
                                                                  1. Turn the ignition switch to LOCK,
                                                                  2. Disconnect the negative (-) terminal cable from
                                                                     the battery, and wait for 30 seconds.
                                                                  3. Connect the SAB connector.
                                                                  4. Connect the negative (-) terminal cable to the bat-
                                                                     tery, and wait for 30 seconds.




                                                                       ON
                                                                              •*$><$*
                                                                            . "-""i
                                                    EADA011A
                                                                    0 s     R
                                                                                             qj    ,"
                                                                                                   Low (-)
                                                                                                             D SAB (LH)
                                                                            S
   /^    CAUTION                                                            C
                                                                                                  High (+)

                                                                                             =[D •Low (-) [ SAB(RH)
                                                                            M
   Place the DAB with the front surface facing up-
   ward.

   Check the SAB resistance.
   [PREPARATION]                                                                                                          ERA9012K
   Release the airbag activation prevention mechanism
   on the SRSCM side of the airbag squib side. Con-               [CHECK]
   nect the dummy (0957A-38200) and dummy adapter                 1. Turn the ignition switch to ON, and wait for at least
   (0957A-38300) to the SAB connector of the SRSCM                   30 seconds.
   connector side.                                                2. Clear the malfunction code stored in the memory
                                                                     with the Hi-Scan Pro.
                                                                  3. Turn the ignition switch to LOCK, and wait for 30
                                                                     seconds.
                                                                  4. Turn the ignition switch to ON, and wait for 30
                                                                     seconds.
                                                                  5. Using Hi-Scan Pro, check the DTC.
                                                                     There Ss no DTC.

                                                                  [HINT]
                                                                  Codes other than these may be output at this time, but
                                                                  they are not relevant to this procedure.
                            Dummy adapter
                                                   ERKB020A

                                                                     « # Replace the SAB.
   US NOTE
   Before checking the resistance, you have to insert the
   shorting bar insert plastic that is attached to the diag-
   nosis checker into the SRSCM connector.

  [CHECK]                                                      From the results of the above inspection, the mal-
                                                               functioning part can now be considered normal.
  Measure the resistance between the SAB high (+) and
  the SAB low (-).                                                                                                        ERJB041I
  1.6 0 < R < 1 8 0


          Repair or replace the harness between
          the SRSCM and the SAB.
TROUBLESHOOTING                                                                                                    RT -51
     EROC0460


CIRCUIT INSPECTION

                               B1361          DBPT Resistance too high (R > 5.4 tt)
            DTO
                               B1362          DBPT Resistance too low (R < 0.4 0)
                               B1367          PBPT Resistance too high (R > 5.4 0)
                               B1368          PBPT Resistance too low (R < 0.4 H)


CIRCUIT DESCRIPTION                                            conditions are satisfied. The above DTCs are recorded
                                                               when the BPT circuit is open or the BPT resistance too
The BPT squib circuit consists of the SRSCM and BPT. It        high or low is detected in the BPT squib circuit.
causes the airbag to deploy when the airbag deployment

                    DTC Detecting Condition                                          Trouble Area
     • Too high or low resistane between BPT high (+) wiring   • BPT squib
       harness and BPT low (-) wiring harness of squib.
     • BPT malfunction                                         • SRSCM
                                                               9
     • SRSCM malfunction                                         Wire harness


WIRING DIAGRAM




                           S                                      High (+)

                           R                             CD        Low (-)   0 BPT (LH)
                           S
                           C                                      High (+)

                           M
                                                         CD        Low (-)   0 BPT (RH)




                                                                                                                    ERJB046A


INSPECTION PROCEDURE                                              2)    Remove the DAB module.

1.    Preparation                                                 3)    Disconnect the connectors of the PAB, left and
                                                                        right side airbags, belt pretensioners and satellite
      1)   Disconnect the negative (-) terminal cable from              sensors.
           the battery, and wait at least 30 seconds.
RT -52                                                                                                                           RESTRAINTS
     4)     Disconnect the SRSCM connector.                                   3.   Check the BPT squib.
                                                                                   [PREPARATION]
                                                                                   1. Turn the ignition switch to LOCK.
                                                                                   2. Disconnect the negative (•) terminal cable from
                                                                                      the battery, and wait for 30 seconds.
                                                                                   3. Connect the BPT connector.
                                                                                   4. Connect the negative (-) terminal cable to the bat-
                                                                                      tery, and wait for 30 seconds.




                                                                                      ON
                                                                                            *>««
                                                                                               i .




                                                                   EADA011A
                                                                                     0     s
                                                                                           1R
                                                                                                                 tD
                                                                                                                      High (+)
                                                                                                                         " J
                                                                                                                       Low (-)
                                                                                                                                 BPT (LH)

                                                                                           1s                         High (+)
     £s> CAUTION                                                                           c                     ffl= Low (-) Q BPT (RH)
                                                                                           M
     Place the DAB with the front surface facing up-
     ward.

2.   Check the BPT resistance.                                                                                                              ERJB046C
     [PREPARATION]
     Release the airbag activation prevention mechanism                            [CHECK]
     on the SRSCM side of the airbag squib side. Con-                              1. Turn the ignition switch to ON, and wait for at least
     nect the dummy (0957A-38200) and dummy adapter                                   30 seconds.
     (0957A-38300) to the BPT connector of the SRSCM                               2. Clear the malfunction code stored in the memory
     connector side.                                                                  with the Hi-Scan Pro.
                                                                                   3. Turn the ignition switch to LOCK, and wait for 30
           NOTE                                                                       seconds.
                                                                                   4. Turn the ignition switch to ON, and wait for 30
     Before checking the resistance, you have to insert the
                                                                                      seconds.
     shorting bar insert plastic that is attached to the diag-
                                                                                   5. Using Hi-Scan Pro, check the DTC.
     nosis checker into the SRSCM connector.
                                                                                      There is no DTC.
          LOCK
                                        /"^\                                       [HINT]
                                         =op            BPT (LH)
                                                                                   Codes other than these may be output at this time, but
                                          fly         D[BPT(RH)                    they are not relevant to this procedure.
                                        v_y




                     I—i   High (+)
                                        I                                     f H f f i • • • Replace the BPT.


                 <OS       Low (-)

                                         4
                                                DUMMY


                                      Dummy adapter
                                                                   ERJB046D
                                                                              From the results of the above inspection, the mal-
                                                                              functioning part can now be considered normal.
     [CHECK]
     Measure the resistance between the BPT high (+) and                                                                                    ERJB041J
     the BPT low (-).
     1.6n<R<2.8n


 MtM «»• Repair or replace the harness between
         the SRSCM and the BPT.




                                                                   ERJB046B
TROUBLESHOOTING                                                                                                   RT-53


CIRCUIT INSPECTION

                               B1400          Satellite left side defect
                               B1403          Satellite right side defect
                               B1409          Satellite left communication error
                              B1410           Satellite right communication error

CIRCUIT DESCRIPTION                                             or communication error of the satellite is detected in the
                                                                satellite circuit.
The release system for the airbag consists of the SRSCM
and two satellites - one on the left - hand side and one on
the right. The above DTCs are recorded when a defect
WIRING DIAGRAM




                             s                                        High (+)
                                                                                   Satellite
                             R                                                     Sensor (LH)
                                                                       Low (-)
                             S
                             c                                                     Satellite
                                                                                   Sensor (RH)
                                                                       Low (-)
                             M
RT-54                                                                                                                       RESTRAINTS
INSPECTION PROCEDURE
                                                                             UJeJ m^ Repair or replace the harness between
1.   Preparation      -                                                              the SRSCM and the Satellite sensor.
     1)     Disconnect the negative (-) terminal cable from
            the battery, and wait at least 30 seconds.

     2)     Remove the DAB module.
                                                                                                                                            ERJB047A
     3)     Disconnect the connectors of the PAB, left and
            right side airbags, belt pretensioners and satellite                Check the satellite sensor (defect).
            sensors.                                                            [PREPARATION]
                                                                                1. Turn the ignition switch to LOCK.
     4)     Disconnect the SRSCM connector.                                     2. Disconnect the negative (-) terminal cable from
                                                                                   the battery, and wait for 30 seconds.
                                                                                3. Connect the satellite connector.
                                                                                4. Connect the negative (-) terminal cable to the bat-
                                                                                   tery, and wait for 30 seconds.




                                                                                          —   i
                                                                                     ON

                                                                                  0s      R
                                                                                                               High (+)f

                                                                                                                Low{-)
                                                                                                                           Satellite (LH)

                                                                                          S
                                                                                                               High (+)
                                                                  EADA011A                C                                Satellite (RH)
                                                                                          M                     Low (-)'

     $S> CAUTION
     Place the DAB with the front surface facing up-
     ward,
                                                                                                                                            ERA9012N
2.   Check satellite circuit (communication error).
                                                                                [CHECK]
                                                                                1. Turn the ignition switch to ON, and wait for at least
                                                                                   30 seconds.
          LOCK                                                                  2. Clear the malfunction code stored in the memory
          ®s     R
                                     High (+).
                                      LowH
                                                 Satellite (LH)                    of the Hi-Scan Pro.
                                                                                3. Turn the ignition switch to LOCK, and wait for 30
                 S
                 C
                                     High {+)
                                                 Satellite (RH)
                                                                                   seconds.
                 M                   Low{-)                                     4. Turn the ignition switch to ON, and wait for 30
                                                                                   seconds.
                                                                                5. Using the Hi-Scan Pro, check DTC.
                                                                                   There is no DTC.
                                                                  ERA9012M

                                                                                [HINT]
     [PREPARATION]                                                              Codes other than these may be output at this time, but
     Check continuity between the SRSCM connector and                           they are not relevant to this check.
     the satellite connector as high (+) and high, low (-)
     and low (-).
     OK : Continuity                                                                      Replace the Satellite sensor.




                                                                               #
                                                                             From the results of the above inspection, the mal-
                                                                             functioning part can now be considered normal.

                                                                                                                                            ERJB041K
TROUBLESHOOTING                                                                                                                       RT -55
asawagwayi   I W W M — ^ — — i ^ —


     EROC0480

CIRCUIT INSPECTION

                                           B1511                  Driver seat belt switch open/short to Battery
                                           B1512                  Driver seat belt switch short to GND
               DTC
                                           B1513                  Passenger seat belt switch open/short to Battery
                                           B1514                  Passenger seat belt switch short to GND

CIRCUIT DESCRIPTION
                                                                                                 Repair or replace the harness between
This system decides whether the seat belt of the driver                                          the SRSCSVI and the seat belt swtich.
or passenger are locked and then prevent the belt preten-
sioner from deploying on crash.
IMSPECTIOM PROCEDURE

1.      Preparation
                                                                                                                                       ERKB049B
2.     Check buckle switch sensor circuit (Short to GND/Bat-
       tery).                                                                        3.   Check the seat belt switch




                                                                          EROC048A                                                     ERKB030D


                                                                                          [CHECK]
             ON
                                                                                          Check the resistance with the switch on and off.
             0                                fcfjl   [ s e a t belt switch
                                                                                          SWITCH OPEN : R = 4KO ± 10% (Belted)
                                                                                          SWITCH OPEN : R = 1KO ± 10% (Unbelted)


                                                                                                 Replace the seat belt switch
                        High (+)


                        Low{-)     I   I
                                              H~T-

                                                                          ERKB030C
                                                                                      From the results of the above inspection the
       [CHECK]                                                                        malfunctioning part can now be considered normal.
       Measure the voltage and resistance of the seat belt
                                                                                                                                       ERKB049C
       switch high and body ground between the SRSCM
       connector and the seat belt switch connector.
       Resistance : °o
       Voltage : 0V
RT-56                                                                                                       RESTRAINTS
     EROC0490


CIRCUIT INSPECTION

            DTC                 B2500          Warning lamp failure

CIRCUIT DESCRIPTION
                                                                             Check the SRS warning light bulb/repair
The SRS warning lamp is located in the cluster. When the                     the SRS warning light circuit.
airbag system is normal, the SRI flashes for approx. 6 sec-
onds after the ignition switch is turned ON, and then turns
off automatically. If there is a malfunction in the airbag
system, the SRI lights up to inform the driver of the ab-
normality. The SRSCM shall measure the voltage at the
airbag SRI (Malfunction Indicator Lamp) output pin, both
when the lamp is on and when the lamp is off, to detect
                                                                                                                      ERDA032A
whether the commanded state matches the actual state.
INSPECTION PROCEDURE                                                  2.   Check the SRS SRI (Service Reminder Indica-
                                                                           tor).
1.    Check the fuse.                                                      OK : SRS SRI ON
      [PREPARATION]
      1. Remove airbag fuse and airbag warning lamp
         fuse from the junction block.                                       If no fault is found in wiring or connector,
      2. Inspect the state of the fuses.                                     replace the SRSCM.
      3. Replace if necessary.

2.    Check the SRS warning lamp circuit.
      [PREPARATION]
                                                                From the results of the above inspection, the part can
      1. Connect the negative (-) terminal cable to the bat-
                                                                now be considered to be normal.
         tery.
      2. Turn the ignition switch to ON.                                                                              ERDA032B



                  ON


          Connect SST
          0957A-38000



                        HHHSH9H


                                                    ERKB049A


      [CHECK]
      1. Measure voltage at the harness side connector
         of the SRSCM.
         Voltage: 9-16 V
TROUBLESHOOTING                                                                           RT-57
     H H n B H

     EROC0500


CIRCUIT INSPECTION

                                  B1620           Airbag unit internal failure
                                  B1650           SRSCM crash recorded
             DTC                  B1655           Side airbay crash recorded
                                  B1657           Crash recorded-Belt pretensioner only
                                  B1661           ECU mismatching

CIRCUIT DESCRIPTION

SRSCM MALFUNCTION

The SRSCM shall also cyclically monitor the following :

1.     Functional readiness of the firing circuit activation
       transistors.

2.     Adequacy of deployment energy reserves.

3.     Safing sensor integrity : detection of faulty closure.

4.     Plausibility of accelerometer signal.

5.     Operation of SRSCM components.

The timely completion of all tests is monitored by a sep-
arate hardware watchdog. During normal operation, the
watch dog is triggered periodically by the SRSCM : If the
SRSCM fails to trigger the watchdog, the watchdog will
reset the SRSCM and activate the SRI (Service Reminder
Indicator). The SRSCM must be replaced once the fault
codes mentioned above are confirmed.
RT-58                                                                                                      RESTRAINTS

AIRBAG MODULE                                                   AIRBAG MODULE DISPOSAL PROCEDURES

DISPOSAL                                                        Before disposing of a vehicle equipped with an airbag, or
                                                                prior to disposing of the airbag module, be sure to first fol-
                                                                low the procedures described below to deploy the airbag.
HELD DEPLOYMENT
PROCEDURES ERNCOBOO

       </f\> CAUTION
       When handling the deployed airbag he careful that
       not the dust enters your eyes and always wear
       gloves to avoid direct contact with the dust

AIRBAG REMOTE DEPLOYMENT DEVICES

|                      Tool, Number, Name                                                     Use
    Deployment tool (0957A-34100A)                                    Deployment inside the vehicle (if the vehicle
    SRS DEPLOYMENT ADAPTER HARNESS                                    will no longer be driven)
    DAB, BPT : 0957A-38500
    PAB, SAB : 0957A-38100




            K"5c_                                          ERDA034A



DISPOSAL PLAN

Take the following disposal steps.

                        CASE                                                   DISPOSAL PLAN
    Abnormal problems in airbag module              Deploy and discard
    Car scrapping            DAB, PAB, SAB, BPT     Deploy the airbag module with the SST
    Crash (Deployed)                                Discard
AIR-BAG MODULE DISPOSAL                                                                                RT-59

UNDEPLOYED A1BBAG MODULE
DISPOSAL         ERKB0610


     ^    CAUTION
     1.   If the vehicle Is to be scrapped, junked, or oth-
          erwise disposed of, deploy the airhag inside
          the vehicle.
     2.   Since there is a loud noise when the airhag
          is deployed, avoid residential areas whenever
          possible, if anyone is nearby, give warning of                                                ERA9O09B

          the impending noise.
     3.   Since a large amount of smoke is produced           ^    CAUTION
          when the airbag is deployed, select a well-
                                                              1.  Before, deploying the airbag in this manner,
          ventilated site. Moreover, never attempt the
                                                                 first check to be sure that there is no one in
          test near a fire or smoke sensor.
                                                                 or near the vehicle. Wear safety glasses,
DEPLOYMENT INSIDE THE VEHICLE                                 2. The inflatqr will be quite hot immediately fol-
                                                                 lowing the deployment, so wait at least 30
when wehlele will no longer be driven                            minutes to allow it to cool before attempting
                                                                 to handle it Although not poisonous, do not
1.   Open all windows and doors of the vehicle. Move the         inhale gas from airbag deployment See De-
     vehicle to an isolated spot.                                ployed Airbag Module Disposal Procedures
                                                                 for post-deployment handling instructions.
2.   Disconnect the negative (-) and positive (+) battery     3. If the airbag fails to deploy when the proce-
     cables from the battery terminals, and then remove          dures above are followed, do not go near the
     the battery from the vehicle                                module. Contact your local distributor.

     ^    CAUTION
     Wait at least 30 seconds after disconnecting the
     battery cable before doing any further work.

3.   Remove the center crash pad side cover.

4.   Remove Airbag SRSCM connector.

5.   Connect deployment tool to the connector of each
     module.




                                                   ERLB005D


6.   At location as far away from the vehicle as possible,
     press the push button (removed from the vehicle) to
     deploy the airbag.
RT -60                                                                                                                             RESTRAINTS
._ .__._.. ...    'i'i'ri"i'"iiNiiiiiiiiiiiiiiiiiiMiiiniBiiiMiTriiiiiii   i ' " iiiiiiiiiiiiiiiiiiiiiiirmiiiirmiiiii^



DEPLOYED AIRBAG MODULE DISPOSAL
PROCEDURES.                                                               ERJBO620

After deployment, the airbag module should be disposed
of in the same manner as any other scrap part, except
that the following points should be carefully noted during
disposal.

1.               The inflator will be quite hot immediately following de-
                 ployment, so wait at least 30 minutes to allow \t to coo!
                 before attempting to handle it.

2.               Do not put water or oil on the airbag after deployment.

3.               There may be adhered to the deployed airbag mod-
                 ule, material that could irritate the eyes and/or skin,
                 so wear gloves and safety glasses when handling a
                 deployed airbag module. If despite these precau-
                 tions, the material does get into your eyes or on your
                 skin, immediately rinse the affected area with a large
                 amount of clean water. If any irritation develops, seek
                 medical attention.

4.               Tightly seal the airbag module in a strong vinyl bag for
                 disposal.




                                               Vinyl




                                                                                                                        ERA9009C


                 Be sure to always wash your hands after completing
                 this operation.
