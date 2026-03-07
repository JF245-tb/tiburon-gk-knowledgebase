# Body Control Module

**Source:** `LARGEFILE Searchable_Manuals/Tiburon-Shop-Manual/16. Body Control Module-OCR.pdf`
**Pages:** 75
**Vehicle:** 2003 Hyundai Tiburon (GK)
**Engines:** 2.0L I4 Beta, 2.7L V6 Delta (PRIMARY)

---

  Troubleshooting
Procedure for BCM


  BCM FAILURE DIAGNOSIS USING Hl-SCAN(PRO)    BE-2
  FAILURE DIAGNOSIS BY BCM FUNCTIONS
   - CENTRAL DOOR LOCK                        BE-5
   - KEY REMINDER                            ..BE-11
   -OUTSIDE MIRROR FOLDING                    BE-15
   - FLASHER                                  BE-20
   - POWER WINDOW                             BE-27
   - IGNITION KEY HOLE ILLUMINATION           BE-32
   - FADE OUT ROOM LAMP                      .BE-35
   - SEAT BELT WARNING LAMP TIMER             BE-39
   -TAIL LAMP AUTOMATIC TURN OFF              BE-42
   - REAR WINDOW & OUTSIDE MIRROR DEFOGGER    BE-48
   - AUTO LIGHT CONTROL                       BE-56
   -WIPER &WASHER CONTROL                     BE-61
   - KEYLESS ENTRY & BURGLAR ALARM            BE-67
BE-2                                                                      Tjroy^                                                BCM
BODY CONTROL MODULE                                                       4.   Then the following screen will be displayed.

(BCM)    • >' „ -; ;••:-•'
                                                                                           1. HYUNDAI VEHICLE DIAGNOSIS
BCM FAILURE DIAGNOSIS USING
                                                                                    MODEL : HD COUPE         2002MY ALL
H I - S C ^ N ( P R O ) : KTOB7000                                                  SYSTEM : BODY CONTROL MODULE

1.   BCM (Body Control Module) is an integrative type                                             OUTPUT MONITORING
     control unit, and it includes following functions.                                  02. ACTUATION TEST

     1)   ETACS (various time & alarm control functions
          etc)

     2)   Receiver function of remote door lock

     3)   Performs communication with Hi-scan(pro)
                                                                                                                              KTOB700C
2.   Located in a junction box (power supply and circuit
     joint contact formation), and integrated shape.                           Though self-diagnosis (failure code output) is not pro-
                                                                               vided, we can find out the failure parts more rapidly
3.   Firstly, to diagnose BCM functions, select the menu                       by monitoring input/output values and forced drive in
     of "10.HD COUPE" mode and "07.BODY CONTROL                                failure diagnosis.
     MODULE'1 [ENTER],                                                         If you want to check the current values of input/output
                                                                               values of BCM, select "QUNPUT/OUTPUT MON-
                                                                               ITORING" and press [ENTER] then the following
                 1. HYUNDAI VEHICLE DIAGNOSIS             £J
                                                                               screen will be displayed.
              04 EXCEL                 90-94MY      ALL
              05 SCOUPE                91-96MY      ALL
              06. MATRIX                                                                  1.1 INPUT/OUTPUT MONITORING
                                        2002MY      ALL
              07 ELANTRA             2001-02MY      ALL
                                                                                    MODEL      HD COUPE         2002MYALL
              08. ELANTRA            96-2000MY      ALL                             SYSTEM     BODY CONTROL MODULE
              09. ELANTRA              92-95MY      ALL

              11. HD COUPE           97-2001 MY     ALL                                  02. FLASH
                                                                                         03. LAMP
                                                                                         04. DOOR
                                                                                         05. LOCK & FOLDING
                                                                                         06. WIPER
                                                                                         07. ETC

                 HYUNDAI VEHICLE DIAGNOSIS
                                                                                                                              KTOB700D
          MODEL : HD COUPE                        2002MY ALL

              01. ENGINE                                                                       1.11 CURRENT DATA
              02. AUTOMATIC TRANSAXLE
              03. ANTI-LOCK BRAKE SYSTEM
              04.SRS-AIRBAG
                                                                                   DOOR WARING SW                  OFF
              05, TRACTION CONTROL SYSTEM
                                                                                   KEY STATE - ACC                 OFF
              06. IMMOBILIZER
                                                                                   KEY STATE - ON OR ST            OFF
              37. BODY CONTROL MODULE                                              KEY STATE - ON                  OFF
              08. CODE SAVING
                                                                                   GENERATOR VOLTAGE               0.0 V
                                                                                   STARTER INHIBIT OUTPUT          OFF
                                                               KTOB700B



                                                                                   FIX     SCRN   FULL   PART GRPH    HELP


                                                                                                                              KTOB700E
BODY CONTROL MODULE (BCM)                                                                                          BE »3

     It provides BCM input/output condition such as power           This functions testing by inputting input factors into
     supply condition, flash function, lamp condition, door         BCM.
     condition, locking unit and mirror folding state, wiper
     circuit and so on.                                        8.   If you want forced drive of BCM output factors, select
                                                                    "02.ACTUATION TEST" after selecting "02.OUTPUT
6.   If you want forced drive of BCM input factors, select          ACTUATION", and then press [ENTER].
     "01. INPUT ACTUATION" after selecting "(^.ACTUA-
     TION TEST".
                                                                                        1.2 ACTUATION TEST

                                                                           MODEL : HD COUPE         2002MY ALL
               1. HYUNDAI VEHICLE DIAGNOSIS                                SYSTEM : BODY CONTROL MODULE

          MODEL : HD COUPE         2002MY ALL
                                                                              01. INPUT ACTUATION
          SYSTEM : BODY CONTROL MODULE
                                                                              02. OUTPUT ACTUATION
             01. INPUT/OUTPUT MONITORING




                                                                                                                   KTOB700I



                                                    KTOB700F                           1.11 ACTUATION TEST


                      1.2 ACTUATION TEST                                 j STARTER INHIBIT OUTPUT
                                                                         I DURATION    10 SECONDS
          MODEL : HD COUPE         2002MY ALL                             METHOD         ACTIVATION
          SYSTEM : BODY CONTROL MODULE
                                                                         I CONDITION     IG. KEY ON
             01. INPUT ACTUATION
             02. OUTPUT ACTUATION
                                                                             PRESS [STRT], IF YOU ARE READY


                                                                          STRT


                                                                                                                  KTOB700J

                                                    KTOB700G
                                                                    This functions forced drive testing directly against
7.   Press [ENTER], and then the following screen will be           BCM output factors.
     displayed.
                                                               9.   Examples of BCM self-diagnosis application

                                                                    1)    Symptom: lamp is not operating when left turn
                   1.11 ACTUATION TEST                                    signal switch is turned on.

       I LEFT TURN SIGNAL SW                        j
                                                                    2)    Failure diagnosis: Following are the expected
                                                                          failure ranges.
        DURATION      UNTIL STOP KEY
                                                                          1. Poor switch contact of multi-function switch
        METHOD        ACTIVATION
                                                                          2. Input wiring malfunction
        CONDITION     IG. KEY ON                                          3. BCM malfunction
                                                                          4. Output wiring malfunction
                                                                          5. Left turn signal lamp malfunction
           PRESS [STRT], IF YOU ARE READY !


        STRT   STOP


                                                    KTOB700H
BE »4                                                                  TROUBLESHOOTING PROCEDURE FOR BCM
  3)       Practice input/output monitoring first to approach          INPUT FACTOR FORCED DRIVE
           the above problem rapidly.

                                                                                        1.11 ACTUATION TEST
                 1.1 INPUT/OUTPUT MONITORING

                                                                             LEFT TURN SIGNAL SW
            MODEL : HD COUPE         2002MY ALL
            SYSTEM : BODY CONTROL MODULE                                    DURATION       UNTIL STOP KEY
                                                                            METHOD         ACTIVATION
                01. POWER                                                   CONDITION      IG. KEY ON

                03. LAMP
                04. DOOR
                                                                                  PRESS [STRT], IF YOU ARE READY !
                05. LOCK & FOLDING
                06.WIPER : V,
                07. ETC                                                     |STRT | STOP


                                                                                                                           KTOB700M


                                                                       OUTPUT FACTOR FORCED DRIVE
                      1.11 CURRENT DATA

                                                            A
           1 LEFfT URN SIGNAL SW          OFF           I                               1.11 ACTUATION TEST
             RIGHT TURN SIGNAL SW         OFF
             LEFT TURN SIGNAL LAMP        OFF
                                                            1               LEFT TURN SIGNAL LAMP
             RIGHT TURN SIGNAL LAMP
             HAZARD SW
                                          OFF
                                          OFF
                                                            1               DURATION       UNTIL STOP KEY
                                                                            METHOD         ACTIVATION
                                                                            CONDITION      IG. KEY ON


                                                            •
                                                                                  PRESS [STRT], IF YOU ARE READY !
       I    FIX | |SCRN |FULL    PART |GRPH     HELP|

                                                            KTOB700L
                                                                            |STRT | STOP |
           1.   When switch input is not normal, ^> Possibil-
                ity of malfunction in multi-function contact or                                                            KTOB700N
                input circuit
           2.   Though, switch input is normal, when turn                    1.    When multi-function switch or BCM input cir-
                signal lamp output is not normal rr> Possibil-                     cuit are probably of problem in the above
                ity of BCM malfunction                                             3-1), check the lamp operation by inputting
           3.   If both are normal, ^ Possiblity of malfunc-                       input factors compuisorily into BCM.
                tion in output wiring or lamp                                      If BCM is normal, lamp blinks when turn
                                                                                   signal switch (BCM input factor) in inputted
  4)       To diagnose BCM control function, perform                               compuisorily. If the lamp does not blink,
           forced drive.                                                           drive output factors compuisorily.
                                                                                   => Multi-function switch ==> Wiring ==> Diag-
                                                                                   nose circuit failure before BCM input termi-
                                                                                   nal.
                                                                             2.    Deliver output signals (lamp drive signal) to
                                                                                   lamp compuisorily to test BCM output termi-
                                                                                   nal.
                                                                                   Turn signal lamp (output factor) will blink, if it
                                                                                   is normal when driven compuisorily.
                                                                                   => BCM output terminal => Wiring => Check
                                                                                   any malfunction in BCM control and output
                                                                                   circuit by directly diagnosing circuit to load
                                                                                   (lamp).
BODYCONTRQLMODULE^CBCM)                                                                                           BE-5

FAILURE DIAGNOSIS BY BCWJ
FUNCTIONS    KTOB7050

CENTRAL DOOR LOCK
POWER DOOR LOCK CIRCUIT DIAGRAM




                   8   BCM-EF     6             BCM-FF                                                   5   BCM-LM


             0.5Y               0.5G   0.5G/B       0.5G                 0.5L




              12^MD02             3&        I
                                          2 _ & MD01 13 ^
                                                            0.5G/B

                                                              1_5_^_ _   14     MD04


                                       0.5G/B       0.5G                                    2.0B      2.0B




            O.SB




                                                                                    JOINT
                                                                                    CONNECTOR


            0.5B




                                                                              G02               G12     G11




                                                                                                                 KTOB705G
BE -6                                                                TROUBLESHOOTING PROCEDURE FOR BCM
1.   Function explanation: When lock/unlock knob of                     2)    Actuator inspection
     driver side is controlled, passenger side interlocks.                    1. Select "01.INPUT ACTUATION" and press
     If the passenger side knob is controlled, driver side                        [ENTER].
     interlocks also.                                                             Drive compulsorily driver's side door
                                                                                  lock/unlock switch, passenger side door
2.   Input/output signal                                                          lock/unlock switch.
       • Fuse: F24(15A).
       • Input: Driver's side door lock switch (E8), pas-
                                                                                          1.2 ACTUATION TEST
         senger side door lock switch (E3)
       • Output: Door lock (F6), Door unlock (F8)                             MODEL       HD COUPE        2O02MYALL
                                                                              SYSTEM      BODY CONTROL MODULE

3.   Related Hi-scan(pro) failure diagnosis
                                                                                   01. INF>UT ACTUATION
                                                                                   02. OUTPUT ACTUATION
     1)    Input/output monitoring
           Select "05.LOCK & FOLDING" and press
           [ENTER]. Then, the following screen will be
           displayed.
           Check BCM input/output state against driver's
           side door lock switch, passenger side door lock
           switch, door lock, door unlock.                                                                              KTOB700G




                 1.1 INPUT/OUTPUT MONITORING                                             1.11 ACTUATION TEST

            MODEL : HD COUPE         2002MY ALL
            SYSTEM : BODY CONTROL MODULE                                     DRIVER DOOR LOCK/UNLOCK SW
                                                                             DURATION        UNTIL STOP KEY
               01. POWER                                                     METHOD          ACTIVATION
               02. FLASH                                                     CONDITION       IG.KEYON
               03. LAMP                                                                      CLOSED DOOR
               04. DOOR
                                                                                  PRESS [STRT], IF YOU ARE READY !
               06. WIPER
               07. ETC
                                                                             STRT     STOP

                                                          KTOB705H
                                                                                                                        KTOB705B



                       1.11 CURRENT DATA                                     2.     Select "02.OUTPUT ACTUATION" and then
                                                                                    press [ENTER]. Perform forced drive against
                                                                                    door lock and door unlock.
           WMHE1WTOW
           PASSENGER DOOR LOCK SW           LOCK
           DOOR LOCK                        OFF                                           1.2 ACTUATION TEST
           DOOR UNLOCK                      OFF
           FOLDING MIRROR SW                OFF                               MODEL : HD COUPE         2002MY ALL
           OUTSIDE MIRROR FOLDING           OFF                               SYSTEM : BODY CONTROL MODULE
           OUTSIDE MIRROR UNFOLD'           OFF
                                                                                  01. INPUT ACTUATION
                                                                                               ACTUATION

          | FIX | [SCRN| I FULL J | PART \ \GRPH\ [HELP


                                                          KTOB70SA




                                                                                                                        KTOB700I
BODY CONTROL MODULE (BCM)                                         BE -7

                      1.11 ACTUATION TEST


          | DOOR LOCK
           DURATION     1 SECONDS
           METHOD       ACTIVATION
          CONDITION     IG. KEY ON



              PRESS [STRT], IF YOU ARE READY !


           STRT


                                                       KTOB705C


4.   Expected failure symptoms

     1)    Lock function works but unlock function does not.

     2)    Unlock function works but lock function does not.

     3)    When lock/unlock knob of passenger side is con-
           trolled, driver side interlocks. But when the driver
           side knob is controlled, passenger side does not
           interlock

     4)    When passenger side knob is controlled, driver
           side does not interlock.

     5)    Both sides do not interlock.
BE -8                                                               TROUBLESHOOTING PROCEDURE FOR BCM
5.    Actions by the failure symptoms                                       2)    Unlock function works but lock function does not
                                                                                  interlock.
      1)   Lock function works but unlock function does not                       => Since PCB integrated relay is fail, replace the
           interlock.                                                             BCM
           => Since PCB integrated relay is fail, replace the
           BCM.                                                             3)    When passenger side knob is controlled, driver
                                                                                  side interlocks, but when driver side knob is con-
                                                                                  trolled, passenger side knob does not interlock.




                                   NG        Connection rod defective of
     Passenger's side actuator
                                          passenger's side door lock actuator
     operation

                 OK


                                                                                              1. BCM-EF®-MD02(§>-D09® Check
                                          1. Input wiring short of                            2. D09©- MD02©- G01(Ground) Check
                                   NG        driver's side door lock switch
[Driver's side door lock switch]
        Input monitoring
                                          2. Internal switch contact failure of               Measure resistance of actuator by handling
                                             driver's side door lock actuator                 it by the hand after connecting an
                                                                                              ohmmeter to the both ends of actuator unit.
                                                                                              Locked condition: oo
                                                                                              Unlocked condition: Normal if it is below 1Q

                                                                                                   [D09]

                                                                                                                (Connector terminal of
                                                                                                                driver's side door lock actuator)



                                                                                              1.(BCM-FF®-MD01®)-MD04©
                                                                                                 D19® Check
                                                                                              2. (BCM-FF©- MD01 © ) - MD04©
                                   OK     1. Output wiring short of passenger's
                                                                                      -Us?.
                                                                                                 D19® Check
                                             side door lock actuator
                                                                                              * Normal condition in the parenthesis
                                                                                                (Since passenger's side interlocks)
                                          2. Passenger's side door lock
                                             actuator failure.
                                                                                              Apply 12V to the both ends under uninstalled
                                                                                              condition, and it's normal if it operates.


                                                                                                [D19]

                                                                                                                (Connector terminal of
                                                                                                                passenger's side door lock actuator)
                                                                                              10           oj




                                                                                                                                          KTOB705D
BOPY_CONTROL MODULE (BCM)                                                                                                                  BE-9
     4)    When passenger side knob is controlled, driver
           side interlocks. But when the driver side knob is
           controlled, passenger side does not interlock.




                                        NG          Connection rod defective of
( Driver's side actuator operation. \
                                                 driver's side door lock actuator.


                   OK


                                                                                                1. BCM-EF®- MD04©- D19® Check
                                                 1. Input wiring short of passenger's           2. D 1 9 ® - M D 0 3 © - M 4 5 © - M 4 5 © -
                                        NG          side door lock switch                          G02(Ground) Check
 [Passenger's side door lock switch]
                                         „ — ^
         Input monitoring
                                                 2. Internal switch contact failure             Measure resistance of actuator by handling it
                                                    of passenger's side door lock               by the hand after connecting an ohmmeterto
                                                    actuator.                                   the both ends of actuator unit.
                                                                                                Locked condition : oo
                                                                                                Unlocked condition : Normal if it is below 1Q

                                                                                                    [D19]
                                                                                                             (Connector terminal of
                                                                                                f    I O J O passenger's
                                                                                                             ]           side door lock actuator)
                                                                                                V            J




                                                                                                1. (BCM-FF©- MD01©) - D09® Check
                                                                                        -fas*
                                        OK       1. Output wiring short of driver's             2. (BCM-FF©- MD01®) - D09® Check
                                                    side door lock actuator
                                                                                                * Normal in the parenthesis
                                                                                                  (Since Passenger's side interlocks)
                                                 2. Driver's side door lock actuator
                                                    failure
                                                                                                Apply 12V to the both ends under uninstalled
                                                                                                condition; it's normal if it operates.


                                                                                                    [D09]
                                                                                                                 (Connector terminal of
                                                                                                                 driver's side door lock actuator)
                                                                                                KP          °J




                                                                                                                                          KTOB705E
BE-10                                                                         TROUBLESHOOTING PROCEDURE FOR BCM
    5)    Both sides do not interlock either.



                                          NG
(Does it operate in !GN ON state? \                   BCM main FUSE (F18) short


                   OK



c    FUSE (F24) short check
                                  >
                                          NG
                                                            FUSE replacement


                   OK


                                                                                            NG         BCM 'E' connector is removed
 [Driver's side door lock switch]         NG         [Passenger's side door lock switch]
         Input monitoring                                   Input monitoring                OK
                                                                                                      Driver's side door lock actuator
                                                                                                          connector is removed.

                   OK


                                                                                            NG
                                                                                                 Passenger's side door lock actuator connector
[Passenger's side door lock switch]
       Input monitoring                   OK     /             [Door lock]              \
                                      j        »»|
                                                   In a forced drive, is the 12V applied    NG
                                                       for 0.5 second to connector                Since the PCB integrated relay is fail,
                                                 I      F6 and F8 of the BCM?           )                    replace BCM.



                                                                       OK


                                                                                            HG   1. BCM-FF ® - MD01 © Check
                                                       Does the connector operate
                                                                                                 2. BCM-FF © - MD01 © Check
                                                         when 12V is applied
                                                         to wiring connector
                                                                                            OK   1. Poor terminal contact of BCM V connector
                                                       BCM-FF ©and BCM-FF®?
                                                                                                 2. Both actuator fail at the same time.




                                                                                                                                         KT0B705F
BODY CONTROL MODULE (BCM)                                                                                     BE -11

KEY REMINDER          KTOBYIOO

KEY REMINDER SWITCH CIRCUIT DIAGRAM




                                 4IBCM-HM                                                            BCM-LM


                                                  0.5R




                                                                        JOINT
                                                                       iCONNECTOR
    See Immobilizer
    Control System




                           0.5UO                  0.5R                       0.5Br/B   2.0B   2.0B




                                                              KEY
                                                              REMINDER
                                                              SWITCH




                             0.5B




                                 15   M36
                                            • • " " " " " "'"i JOINT
                                            See Ground iCONNECTOR
                                             Distribution i




                            1.25B




                                 YG11                                                           G12




                                                                                                              KTOB710A
BE -12                              TROUBLESHOOTING PROCEDURE FOR BCfVf
ROOIVf LAMP CIRCUIT DIAGRAM




                                                                \J CLUSTER




             II               G02       G06
             G01
BODY CONTROLftHOBULE(BCM)                                                                                                          |B9 L ;   ™ I Vj)



1.   Function explanation: When ignition key is in the key                       2.     Select "04.DOOR" and press [ENTER].
     cylinder and driver's side door or the passenger's side                            Then, the following screen will be displayed.
     door is open, if the knob is locked, then it outputs                               Check BCM input condition against driver's
     automatically to prevent the door lock.                                            side door switch and passenger's side door
                                                                                        switch.
2.   Input/output signal
       • Fuse: F18 (10A)
       • Input : Door warning switch (H4), Driver's side                                1.1 INPUT/OUTPUT MONITORING
         door switch (E9), Passenger's side door switch
                                                                                 MODEL        HD COUPE        2002MYALL
         (E4)
                                                                                 SYSTEM       BODY CONTROL MODULE

3.   Related Hi-scan(pro) failure diagnosis                                            01. POWER
                                                                                       02. FLASH
     1)   Input/output monitoring
                                                                                       03. LAMP
          1. Select "01.POWER" and press [ENTER].
              Then the following screen will be displayed.                             05. LOCK & FOLDING
              Check BCM input condition against door                                   06. WIPER
              warning switch.                                                          07. ETC



                 1.1 INPUT/OUTPUT MONITORING

          MODEL : HD COUPE         2002MY ALL
          SYSTEM : BODY CONTROL MODULE                                                        1.11 CURRENT DATA

                                                                                                                                     A
                                                                                                              '*?; -C^lfck^??; j
                02. FLASH                                                        PASSENGER DOOR SW                CLOSED
                                                                                                                                     1
                03. LAMP
                04. DOOR
                                                                                 DOORSW-2                         CLOSED
                                                                                                                  OFF
                                                                                                                                    1
                                                                                 KEY HOLE ILLUMINATION
                                                                                                                                    1
                05. LOCK &• FOLDING
                06. WIPER
                                                                                 ROOM LAMP
                                                                                 HOOD SW
                                                                                                                  0    %
                                                                                                                  CLOSED
                                                                                                                                    1
                                                                                                                                    1
                07. ETC                                                          TAIL GATE OPEN SW
                                                                                 TAIL GATE UNLOCK INPUT
                                                                                                                  CLOSED
                                                                                                                  OFF
                                                                                                                                    1
                                                             KTOB700D
                                                                                                                                    f
                                                                                 FIX     |SCRN| I FULL I |RART| |GRPH| 1 HELP 1

                      1.11 CURRENT DATA
                                                                                                                                     KTOB710D


          BATTERY VOLTAGE                                               4.   Expected failure symptoms
                                                                             Key reminder function does not work.
          KEY STATE - ACC                     OFF
          KEY STATE - ON OR ST                OFF
          KEY STATE-ON                        OFF
          GENERATOR VOLTAGE                   0.0
          STARTER INHIBIT OUTPUT              OFF




          FIX     SCRNJ I FULL I J PART| [ G R P H I [HELP


                                                             KTOB710C
BE-14                                                                       TROUBLESHOOTING PROCEDURE FOR BCM
5.     Actions by failure symptoms

 Key reminder function does not work.




c    Does the central door iock work?

                      OK
                                    )
                                        NG
                                                    Check central door lock function




                                        NG ^        1. Removal of door warning                    Connection of door warning switch connector
        [Door warning switch]                          switch
           Input monitoring
                                                   2. input wiring short of door                  1. BCM-HM©- M05© Check
                                                      warning switch                              2. M 0 5 © - M 3 6 © - M 3 6 @ - G 1 1 Check

                                                   3. Internal switch malfunction                 Connect ohmmeterto both ends of door
                                                                                                  warning switch, and check the continuity
                     OK                               of door warning switch                      when key is inserted of removed.
                                                                                                     [M05]
                                                                                                                   (Connector terminal
                                                                                                       up          of door warning switch)
                                                                                                         o   o


                                        NG     f      Do the door warning lamp           ^   NG
     [Driver's side door switch]                                                                    Driver's side door switch is removed
                                                      of cluster and driver's side
          Input monitoring                            door lamp work?                               or broken

                                                                     OK


                     OK                              Input wiring short of Driver's               1. BCM-EF©- M53© Check
                                                           side door switch                       2. M53®- G01 (Ground) Check




 [Passenger's side door switch]         NG         Do the door warning lamp of cluster       NG      Passenger's side door switch
       Input monitoring                            and driver's side door lamp work?                 is removed or broken

                                                                     OK
                     OK
                                                                                                  1. BCM-EF©- M54© Check
                                                   Input wiring short of passenger's              2. M54® - M45 © - M45 © - G02
Since BCM is defective, replace BCM.                       side door switch.                         (Ground) Check



                                                                                                                                         KTOB710E
BODY CONTROL MODULE (BCJVf)                                I D Ezn ™ I T^l



OUTSIDE MIRROR FOLDING            KTOBTISO

CIRCUIT DIAGRAM OF POWER OUTSIDE MIRROR


                                             § BCM
                                               BOX




                                                     5l'BCM-LM




                »"i••»• ™ ~ •-«
                                                            KTOB715A
BE-16                                                             TROUBLESHOOTING PROCEDURE FOR BCWl
1.   Function explanation: When folding mirror switch is             2)   Actuator inspection
     turned on, Mirror folds or unfolds.                                  1. Select "01.INPUT ACTUATION" and then
                                                                              press [ENTER].
2.   Input/output signal                                                      Perform forced drive against folding mirror
       * Fuse : F13 (15A)                                                     switch.
       * Input: Folding mirror switch (E5)
       * Output: Mirror folding (F20), Door unlock (F12)
                                                                                       1.2 ACTUATION TEST
3.   Related Hi-scan(pro) failure diagnosis
                                                                           MODEL : HD COUPE         2002MY ALL
                                                                           SYSTEM : BODY CONTROL MODULE
     1)   Input/output monitoring
          1. Select "05.LOCK & FOLDING" and press                              .01. INPUT ACTUATION
              [ENTER]. Then, the following screen will be                       02. OUTPUT ACTUATION
              displayed.
              Check BCM input/output state against fold-
              ing mirror switch, outside mirror folding, out-
              side mirror unfolding.


               1.1 INPUT/OUTPUT MONITORING                                                                          KTOB700G


          MODEL : HD COUPE         2002MY ALL
          SYSTEM : BODY CONTROL MODULE
                                                                                      1.11 ACTUATION TEST

             01. POWER
             02. FLASH                                                    FOLDING MIRROR SW
             03. LAMP                                                     DURATION   UNTIL STOP KEY
             04. DOOR                                                     METHOD     ACTIVATION
             05.LOCK':& FOLDING
                                                                          CONDITION     !G. KEY ON
             06. WIPER
             07. ETC

                                                                               PRESS [STRT], IF YOU ARE READY


                                                                          STRTi ISTOPI
                     1.11 CURRENT DATA
                                                                                                                    KTOB715C

          DRIVER DOOR LOCK SW            LOCK
          PASSENGER DOOR LOCK SW         LOCK                             2.    Select "02.OUTPUT ACTUATION" and then
          DOOR LOCK                      OFF                                    press [ENTER].
          DOOR UNLOCK                    OFF                                    Perform forced drive against outside mirror
                                                                                folding, outside mirror unfolding.
          OUTSIDE MIRROR FOLDING         OFF
          OUTSIDE MIRROR UNFOLD*         OFF
                                                                                       1.2 ACTUATION TEST

                                                                          MODEL : HD COUPE         2002MY ALL
          FIX J ISCRNl j FULL I [PART| JGRPHl | HELP                      SYSTEM : BODY CONTROL MODULE

                                                                               01. INPUT ACTUATION
                                                       KTOB715B
                                                                          •    02. OU"fPUT ACTUATION            •     •




                                                                                                                    KTOB700I
BODY CONTROL MODULE (BCM)                                       BE-17

                     1.11 ACTUATION TEST


          OUTSIDE MIRROR FOLDING
          DURATION     10 SECONDS
          METHOD       ACTIVATION
          CONDITION    IG.KEYON



             PRESS [STRT], IF YOU ARE READY !


          |STRTJ


                                                     KTOB715D


4.   Expected failure symptoms

     1)    Folding function works but unfolding function
           does not.

     2)    Unfolding function works, but folding function
           does not.

     3)    Driver side mirror works, but passenger side mir-
           ror does not.

     4)    Passenger side mirror works, but driver side does
           not.

     5)    Both sides do not work.
BE_-18                                                               TROUBLE^OOTING PTOgEDUREFOR BCM
5.   Actions by the failure symptoms                                                           => Since unfolding relay is fail, replace the relay

     1)   Folding function works, but unfolding function                           3)          Driver side mirror works, but passenger side
          does not.                                                                            does not.
          => Since unfolding relay is fail, replace the relay.

     2)   Unfolding function works, but folding function
          does not




                                                                     1. (BCM-FF©- MD03©) - D16© Check
                     1. Passenger's side folding mirror
                                                                     2. (BCM-FF©- MD03®) - D 1 6 ® Check
                        Output wiring short
                                                                 * Normal condition inside the parenthesis
                     2. Passenger's side folding mirror            (Since driver's side works)
                        failure                                      Normal if the unit operate when 12V is applied
                                                                     to ends of terminal
                                                                               [D16]
                                                                 n     s~—N                    n   (Connector terminal of
                                                                                   o       o       passenger's side folding mirror)




                                                                                                                                          KT0B715E


     4)   Passenger side mirror works, but driver side does
          not.




                                                                     1. (BCM-FF ©-MD03©) - MD02©- D06© Check
                      1. Driver's side folding mirror                2. (BCM-FF©-MD03®) - MD02®- D06® Check
                         Output wiring short
                                                                 * Normal condition in the parenthesis
                      2. Driver's side folding mirror              (Since passenger's side works)
                         failure                                     If the unit works when 12V is applied
                                                                     under uninstalled condition, it is normal.
                                                                               [D06]
                                                                 n     •   *   -   -   N       n   (Connector terminal of
                                                                                   o       o       driver's side folding mirror)




                                                                                                                                          KT0B715F
BODY CONTROL MODULE (BCM)                                                                                                   BE -19

    5) Both sides do not work



                                      NG
    Fuse (F13) short check                              Fuse replacement



                  OK




                                      NG          1. Input wiring short                 1. BCM-EF©- MD02©- DOS© Check
                                  I         £&.
     [Folding mirror switch]                         of folding mirror switch           2. D05®- MD01©- G01 (Ground) Check
        Input monitoring
                                                  2. Internal switch contact malfunc-   Connect ohmmeter to both ends of folding
                                                     tion of folding mirror switch.     mirror switch, and check the continuity.
                                                                                        (Continues only while pressed)
                                                                                             [D05]
                  OK                                                                                      (Connector terminal
                                                                                              of          of power window switch)




                                                   Folding relay malfunction &
                                                   unfolding relay malfunction                 Replace two relays at once
 [Mirror folding] Is the 12V applied ] NO               at the same time
to F20 and F12 terminals of BCM
   connectors in forced drive?
                                                         BCM malfunction                             BCM replacement



                  YES



  Does the mirror work when
  12V is applied to BCM-FF©       I NG            1. BCM-FF©- MD03® Check
  and BCM-FF® terminals                           2. BCM-FF©- MD03® Check
  of wiring BCM-FF?


                                      OK
                                                  Poor contact of BCM 'F
                                                  connector terminal




                                                                                                                            KTOB715Q
BE -20                                                            TROUBLESHOOTING PROCEDURE FOR BCM
FLASHER         KTOB7200

TURN SIGNAL LAMP AND HAZARD LAMP CIRCUIT DIAGRAM (1)




                                                                                                                       -,                 *

                                                                                         s^/ ......:•.
                                                                     9IBCM-IM     m   „ ^     - „ „ —                 5     BCM-CE
                                                                                      17IBCM-FF




  0.5W                   0.5R/O                0.5L/O           0.5W/O            0.5O                              0.5L




                                   M82                                                      M84

                                              'LEFT                                                      BRIGHT
                                         —     REAR                                                      J REAR
                                              iCOMBl-                                                    I COMBI-
                                             1 NATION                                                    NATION
                                              *LAM>                                                        LAMP


         See Tail &                M82                                                6&M84                                 See Tail &
         License Lamps                                                                                                      License Lamps


                                                                                                                              0.5
                                                                                                                             Br/O
                                                        M10-2       10 M10-1
                                                                                                                                  2 E31



                                                                                                                            3 E31


                                                                         M10-1



                                                                                 0.85B
     0.5B                0.85B                                    0.5B                                                0.5B




                             A
         G15                 G05                                    G11               G02                                   G16


                                                                                                                                              KTOB720A
BODY CONTROL WIODULE (BCM)                                                                                                                                                                             BE-21
TURN SIGNAL LAMP AND HAZARD LAMP CIRCUIT DIAGRAM (2)


                                                                                                                                                                                               *!BCM
                                                                                                                                                                                                ?BOX

    *.'.'-vi.S\                "• ••-•;i;:T
                                          ' ":.:'vj.'
   f.v;:\..-••;;.,;;;..;: .:.:•:•:.                                                                                                                                            '• " •::-. •»
      ;
  r;:| ;?:nElillSsS|l|:«


   11111                                                                                                                  3 'utput •<• •;•••••: •                        -"-•-• •-^---i^'s

                                                                                                                          V:::r:.:^::^;^^;./•':'^:;::•'•':''':::,.-••^^:::^:^•::..;•:•^''^|;

                                                                                                                                                                                v::-:v"'::.:   j




                                                                                                                                  ••.          •            • |             ......
                                                                                                                                                          13 BCM-HM

                                                               See illuminations




                                                                0.5P/B             0.5W                          0.5LVB                             0.5Y/B


                                                                                                                                                                 M01-2
                                                                                          M13
                                                                                                HAZARD       i
                                                                                                LAMP     i
                                                                                                         d
                                                                                                SWITCH




                                                                                                                                             M01-2


                      2.0B                              2.0B     0.5Gr             0.5B                                          0.5B




                                                               See Illuminations

                                                                                                                                             M36
                                                                                                                                            ^ | JOINT
                                                                                                                                             • CONNECTOR


                                                                                                                                            M36




                                                                                                                               1.25B




                            G12
                                                                                                                                   i    G11


                                                                                                                                                                                                       KTOB720B
                                                                       TROUBLESHOOTING PROCEDURE FOR BCM          sajaaHsaaaasEfflsaisBS^ESffiiKSBisa




1.   Function explanation: It works at battery(B+) state                         Perform forced drive against hazard lamp
     when hazard switch turns on, and works at IGN state                         switch, left turn signal lamp switch, right turn
     when turn signal lamp turns on.                                             signal lamp switch.
     When the bulb burnt, hazard lamp blinks with the
     same interval, but turn signal lamp (left/right) blinks
     quickly.                                                                            1.2 ACTUATION TEST

                                                                             MODEL : HD COUPE         2002MY ALL
2.    input/output signal                                                    SYSTEM : BODY CONTROL MODULE
        • Fuse: F07 (10A)
        • Input : Hazard switch (H18), left turn signal                         0-1 .'"INPUT
          switch (H13), right turn signal switch (H3)                           02. OUTPUT ACTUATION
        • Output: Left turn signal lamp (C9J7.F13), Right
          turn signal lamp (C5J9.F17)

3.   Related Hi-scan(pro) failure diagnosis

     1)    Input/output monitoring
                                                                                                                                  KTOB700G
           1. Select "02.FLASH". Press [ENTER] then fol-
               lowing screen will be displayed.
               Check BCM input/output state against left                               1.11 ACTUATION TEST
               turn signal lamp switch, right turn signal
               lamp switch, left turn signal lamp, right turn
               signal lamp and hazard lamp switch.                          HAZARD SW
                                                                            DURATION     UNTIL STOP KEY
                                                                            METHOD       ACTIVATION
                1.1 INPUT/OUTPUT MONITORING                                 CONDITION    IG.KEYON

           MODEL : HD GOUPE         2002MY ALL
           SYSTEM : BODY CONTROL MODULE
                                                                              PRESS [STRT], IF YOU ARE READY !
              01. POWER
                                                                            STRTJ I STOP I
              03. LAMP
              04. DOOR
                                                                                                                                  KTOB720D
              05. LOCK & FOLDING
              06. WIPER
                                                                                Select "02.OUTPUT ACTUATION" and then
              07. ETC
                                                                                press [ENTER].
                                                                                Perform forced drive against left turn signal
                                                            KTOB720K            lamp, right turn signal lamp.

                    1.11 CURRENT DATA
                                                                                        1.2 ACTUATION TEST
                                                            A
          | LEFT TURN SIGNAL SW          OFF: ,        ||                   MODEL : HD COUPE         2002MYALL
            RIGHT TURN SIGNAL SW         OFF                                SYSTEM : BODY CONTROL MODULE
            LEFT TURN SIGNAL LAMP        OFF
            RIGHT TURN SIGNAL LAMP       OFF                                   01. INPUT ACTUATION
            HAZARD SW                    OFF                                  EWWWHW

                                                            T
          FIX | SCRN||FULL|    PART   GRPH | H E L P

                                                            KTOB700L
                                                                                                                                  KTOB700I


     2)   Actuator inspection
          1. Select "01.INPUT ACTUATION" and then
              press [ENTER].
BODY CONTROL MODULE (BCM)                                         BE-23

                      1.11 ACTUATION TEST


          | LEFT TURN SIGNAL LAMP
           DURATION     UNTIL STOP KEY
           METHOD       ACTIVATION
          CONDITION     IG. KEY ON



              PRESS [STRT], IF YOU ARE READY !


           STRT   STOP I


                                                       KTOB700N


4.   Expected failure symptoms

     1)    Hazard lamps do not work.

     2)    Right turn signal lamp does not work.

     3)    Left turn signal lamp does not work.

     4)    It blinks quickly. (When the bulb is not burnt)

     5)    One turn signal lamp does not work.
BE-24                                                   T R O U ^ L ^ H O O T I N G PROCEDURE FOR BCM

5. Actions by the failure symptoms                              1) Hazard lamp does not work.



           Does the turn signal lamp work,
                                                NO
           when turn signal lamp switch is                           Fuse (F7) short
           turned on in IGN state?

                                                                     BCM malfunction
                            YES




               [Hazard lamp switch]             YES
                 Input monitoring                                    Fuse (F18) short



                            NO

                                                       1.BCM-HM©-M13© Check
            Input wiring short of hazard               2. M13®- M36©- M36© - G11 (Ground)
                    lamp switch                           Check

          Hazard lamp switch malfunction               Connect ohmmeter to both ends of hazard
                                                        lamp switch, and check the continuity.

                                                                [M13]
                                                                                 (Connector terminal
                                                                                 of hazard lamp switch)



                                                                                                               KTOB720F


   2) Right turn signal lamp does not work.



                                                      1. BCM-HM © - M01 -2 © Check
                                                      2. M01-2®- M36®- M36© - G11(Ground)
                  Input wiring short of right
                                                         Check
                   turn signal lamp switch.

                   Right turn signal lamp
                    switch malfunction                        Connect ohmmeter to both ends
                                                              of right turn signal lamp switch,
                                                                  and check the continuity.

                                                               [M01-2]
                                                          I      n       t
                                                                         O
                                                                             O     (Connector terminal
                                                                                   of multi-function switch)




                                                                                                               KTOB720Q
BODY CONTROL MODULE (BCM)                                                                                                 BE-25
  3)   Right turn signal lamp does not work.




                                                        1. BCM-HM@-M01-2® Check
                 Input wiring short of left turn        2. M 0 1 - 2 ® - M 3 6 ® - M 3 6 © -G11 (Ground)
                     signal lamp switch.                   Check

                 Left turn signal lamp switch
                          malfunction                     Connect ohmmeter to both ends of left turn
                                                         signal lamp switch, and check the continuity.


                                                                   [M01-2]
                                                              i.     i i     I
                                                                                 o   o!   (Connector terminal
                                                                                          of multi-function switch)




                                                                                                                          KTOB720H


  4)   It blinks quickly (When bulb is not burnt)




         When the hazard lamp                 YES
       switch blinks too frequently,
                                        I                     BCM malfunction
           when it is turned on.

                       NO
                                                                                           © EC & General area
       When the right turn signal lamp |        YES   Wrong bulb specification of
        switch blinks too frequently,                                                      Front turn signal lamp : 21W
                                                      the right turn signal lamp.
            when it is turned on.                                                          Rear turn signal lamp : 21W
                                                                                           © U.S,A area
                                                          BCM malfunction                  Front turn signal lamp : 28W
                                                                                           Rear turn signal lamp : 27W
                       NO


                                                                                           © EC & General area
       When the left turn signal lamp ,               Wrong bulb specification of
                                                                                           Front turn signal lamp : 21W
       switch blinks too frequently,                   the left turn signal lamp.
                                                                                           Rear turn signal lamp : 21W
           when it is turned on.
                                                                                           © U.S.A area
                                                          BCM malfunction                  Front turn signal lamp : 28W
                                                                                           Rear turn signal lamp : 27W




                                                                                                                          KTOB720I
BE -26                                                          TROUBLESHOOTING PROCEDURE FOR BCM
  5)   One turn signal lamp does not work.




                                                                   1. Bulb burnt
               Poor operation of front left turn signal lamp       2. BCM-CE®- E06© Check
                                                                   3. E06® - G15(Ground) Check


                                                                   1. Bulb burnt in cluster
                    Poor operation of left cluster                 2. BCM-IM®- M10-2© Check
                                                                   3. M10-1©- G11 (Ground) Check


                                                                   1. Bulb burnt
               Poor operation of rear left turn signal lamp        2. BCM-FF©- M82© Check
                                                                   3. M82©- GOS(Ground) Check


                                                                   1. Bulb burnt
               Poor operation of front right turn signal lamp      2. BCM-CE© - E31 © Check          I
                                                                   3. E31® - G16(Ground) Check


                                                                   1. Bulb burnt in cluster
           I       Poor operation of right cluster                 2. BCM-IM®- M10-1© Check
                                                                   3. M10-1 © - G11(Ground) Check


                                                                    1. Bulb burnt
               Poor operation of rear right turn signal lamp        2. BCM-FF©- M84© Check
                                                                  . 3. M 8 4 ® - G02(Ground) Check




                                                                                                         KTOB720J
BODY CONTROL MODULE (BCM)                                                                                                                            BE-27
POWER   WINDOW                         KTOB7250


POWER WINDOW CIRCUIT DIAGRAM (1)




                                                                                                          HOT AT ALL TIMES
                                                                                                                                            I BCM
                                                                                                                                             'BOX
                                                                             ' See Power
                                                                              •• .distribution.


                                                                                                                          FUSE1S
                                                                                                                          30A

                                                                                                              '••:': \/




                                    ,m^!ZA :"">:•
                                                                                                                                     ••~m*
                                                                                                                                     ":,;::s-;!
           B-:'::::.;i:.::-;:;-::




                                                                                                                                             I


                                                                                                                                     .'"•-••'1


                                                                                                                                             I

                                                                                                                                     •:::..:':.;:i
                                                                                                                  A
           a':;;:?:;,::T:.;                                                                                                          ;;;:'•:••: 1
                                                                                                                            WINDOW
           1:18
           i::l::::?l:i?
                                                                                                                            RELAY
                                                                                                                                     II-
                                                                                                  •rrrr^7



           mm:                                                              hti$M>;

           mm
                                                                                      ,|.......... ...;

                                                    Grounds
           E ':;':..,,,:»:-: :                      _^x__
                                                                                                    •«-.- *> • ,»*••••;*•
                                                                 5 BCM-LM                                               BCM-GF
                                                                                                                2



                                                                                                          2.0Gr




                                     2.0B                     2.0B                                          13^MD01




                                                                                                          2.0Gr




                                                                                                             V
                                                                                       To Left Power Window Switch
                                       G12                      G11




                                                                                                                                                     KTOB725A
BE -28                                                               TROUBLESHOOTING PROCEDURE FOR BCM
POWER WINDOW CIRCUIT DIAGRAM (2)


                                                    From Power
                                                    Window Relay
                                                                                                          See Illuminations
                                                                                                                    T
                                                                                                           0.5P/B

                                                                                                                              LEFT
                                                                                                                              POWER
                                                                                                                              WINDOW
                                                                                                                              SWITCH




                                                                7
                                               See Ground                                         DOS
                                               Distribution


                                                     I    2.0B




 0.5W               2.0Br             2.00                2.08           2.0Y    2.0L      2.0P


                                           1^>D01             10-
                                                                                 ~~5~Y         V^MDOI

                                                                        2.0Y     2.0L      2.0P


                                                                           3^                  6<*>MD03 See Illuminations

See Power Outside           LEFT POWER
Mirror Folding              WINDOW MOTOR
                                                          2.0B                                             0.5P/B



                                                                                                                              RIGHT
                                                                                                                              POWER
                                                                                                                              WINDOW
                                                                                                                              SWITCH




                                                                                                                3k.
                                                                                               V-                   v
                                                                                               7                     D15

                                                                        2.0Gr             2.0W               2.0B

                                                                                                    D11
                                                                                                                 %7
                                                                                                            See Illuminations




                                                                                RIGHT POWER
                                                               G01              WINDOW MOTOR


                                                                                                                                KTOB725B
BODYJttNTROLMODULE (BCM)                                                                                                BE : 29
1.   Function explanation                                                 2.     Select "07.ETC" and press [ENTER]. Then,
                                                                                 the following screen will be displayed.
     1)   BCM controls power supply to power window                              Check output condition against power win-
          switch when IGN on state, and it keep supplying                        dow relay.
          power to the switch for 30 seconds when IGN is
          off.
                                                                                 1.1 INPUT/OUTPUT MONITORING
     2)   If the door is opened within the 30 seconds, it
          turns off immediately.                                 !        MODEL : HDCOUPE          2002MY ALL
                                                                          SYSTEM : BODY CONTROL MODULE
2.   Input/output signal
       • Fuse : F19 (30A)                                        \              01. POWER
       • Output: Power window output (G2)                                       02. FLASH
                                                                                03. LAMP
3.   Related Hi-scan(pro) failure diagnosis                                     04. DOOR
                                                                                05. LOCK & FOLDING
     1)   Input/output monitoring                                               06. WIPER
          1. Select "01.POWER" and press [ENTER].                              • i l i i M l M |^llSlf^iSii|liilil HH
              Then the following screen will be displayed.
              Check BCM input condition against key state
                                                                                                                         KTOB725F
              -ON or ST, key state - ON.

                                                                                       1.11 CURRENT DATA
                 1.1 INPUT/OUTPUT MONITORING

          MODEL : HD COUPE         2002MY ALL
          SYSTEM : BODY CONTROL MODULE                                    SEATBELT SW                     UNBUCKLED
                                                                          SEATBELT INDICATOR              OFF
                mW^mm^^M^^m^^mi                                           CHIME BELL                      OFF
                02. FLASH                                                 OVERSPEED                       OFF
                03. LAMP                                                  REAR DEFOGGER SW                OFF
                04. DOOR                                                  REAR DEFOGGER                   OFF
                05. LOCK & FOLDING                                        CRASH SENSOR VOLTAGE            0.0 V
                06. WIPER
                07. ETC
                                                                          FIX I [SCRNJ [FULL] I PART | lGRPH| [HELP[

                                                      KTOB700D




                       1.11 CURRENT DATA                             2)   Actuator inspection
                                                                          Select "02.OUTPUT ACTUATION" and press
                                                                          [ENTER].
          illillfii                        OFF                            Perform forced drive against power window
          DOOR WARING SW                                                  power supply.
                                           OFF
          KEY STATE - ACC
                                           OFF
          KEY STATE - ON OR ST
                                           OFF
          KEY STATE - ON
                                           0.0 V                                       1.2 ACTUATION TEST
          GENERATOR VOLTAGE
                                           OFF
          STARTER INHIBIT OUTPUT                                          MODEL : HD COUPE         2002MY ALL
                                                                          SYSTEM : BODY CONTROL MODULE

          FIX     SCRN   FULL   PART! GRPH     HELP                            01. INPUT ACTUATION
                                                                                   OUTPUT ACTUATION




                                                                                                                         KTOB700I
BE-30                                                      TROUBLESHOOTING PROCEDURE FOR BCM

                    1.11 ACTUATION TEST


       | POWER WINDOW POWER OFF
       I DURATION       UNTIL STOP KEY
        METHOD          ACTIVATION
       [ CONDITION      IG. KEY ON



           PRESS [STRT], IF YOU ARE READY !


         STRT    STOP




4.   Expected failure symptoms
     Power is not supplied to power window switch.

     (Qj| NOTE
     As for the power window motor malfunction, refer to
     power window motor circuit [Refer to workshop man-
     ual(BE-75~BE-77)]
BODY CONTROL MODULE (BCM)                                                                                                          BE »31
5.     Actions by failure symptoms

    Power is not supplied to power window switch.




                                                NG
(       Fuse (F19) short check              \                                                             Fuse replacement

                      OK



                [Power]                         NG
            Input monitoring                                                                          Check power supply circuit



                      OK

                                                NG                                                       Relay replacement
         [Power window power]           i            p»
                                                          1. Power window relay malfunction
       Is the 12V applied to BCM G2
    terminal and both ends of grounding
    when output signal is forced driven?                  2. BCM malfunction
                                                                                                         BCM replacement
                                                                                              **



                                                OK
                                                                                                   BCM-GF© - MD01@ - DOS© Check




                                                                                                                                   KTOB725E
BE-32                                                                                TROUBLESHOOTING PROCEDURE FOR BCM

IGNITION KEY HOLE
ILLUMINATION KTOBTSOO
KEY REMIND SWITCH CIRCUIT DIAGRAM




                                                                                                    ~ " " " " " " " - - - - - - " " **" "« BCM
                                                                                                                                                                 'BOX
                       IBS;?
                       t
                                         •;•:•••12Volt
                                                :.      output                                          ..:,„........:..:...:..,.,,.,,,.....:,.,..



                                      •                I •••'."
                      6
                      ."•:.••:•••:-•,:..•;.:

                                          4IBCM-HM                                                                                                          BCM-LM



                                                                  0.5R




                                                                                     JOINT
                                                                                     CONNECTOR
    See Immobilizer
    Control System




                              0.5L/O                              0.5R                    0.5Br/B   2.0B                                             2.0B




                                                                            KEY
                                                                            REMINDER
                                                                            SWITCH




                                      0.5B




                                                  <•":-"• f: 1^ ".;*" ":™ ^S JOINT
                                                    ^ See Ground sCONNECTOR
                                                       r^ Distribution E

                                          20 M36




                                   1.25B



                                            A
                                             G11                                                                                                       G12




                                                                                                                                                                     KTOB710A
BODY CONTROL MODULE (BCM)                                                                                            BE »33

1.   Function explanation: When driver's side door is                    2)    Actuator inspection
     opened and closed, ignition key hole illumination                         Select "02.OUTPUT ACTUATION" and press
     turns on for 10 seconds so that the driver can insert                     [ENTER].
     the key.                                                                  Perform forced drive against key hole illumina-
                                                                               tion.
2.   input/output signal
       • Fuse : F18(10A)
       • input : Driver's side door switch (E9), Passen-                                  1.2 ACTUATION TEST
         ger's side door switch (E4)
                                                                               MODEL : HD COUPE         2002MY ALL
       • Output: Key hole illumination (J3)                                    SYSTEM : BODY CONTROL MODULE

3.   Related Hi-scan(pro) failure diagnosis                                       01. INPUT ACTUATION

     1)   Input/output monitoring                                                wmwmmm
          Select "04.DOOR" and press [ENTER]. Then, the
          following screen will be displayed.
          Check BCM output condition against key hole il-
          lumination.


                 1.1 INPUT/OUTPUT MONITORING

          MODEL : HD COUPE         2002MY ALL
          SYSTEM : BODY CONTROL MODULE
                                                                     |                    1.11 ACTUATION TEST

                01. POWER
                02. FLASH                                                     KEY HOLE ILLUMINATION
                03. LAMP                                                      DURATION      UNTIL STOP KEY
                 & DOOR                                                       METHOD        ACTIVATION
                05. LOCK & FOLDING
                                                                              CONDITION     IG.KEYON
                06. WIPER
                07. ETC

                                                                                 PRESS [STRT], IF YOU ARE READY !


                                                                              |STRT| I STOP I
                       1.11 CURRENT DATA
                                                                                                                       KTOB730C

          DRIVER DOOR SW                   CLOSED
          PASSENGER DOOR SW                CLOSED               4.       Expected failure symptoms
          DOORSW-2                         CLOSED                        Key hole illumination does not work.
          I!MWI.1JIIIWJI^U*I»1^4M
          ROOM LAMP                        0    %
          HOOD SW                          CLOSED
          TAIL GATE OPEN SW                CLOSED
          TAIL GATE UNLOCK INPUT           OFF
                                                     •
          FIX     SCRN   FULL   PART   GRPH   HELP


                                                     KTOB730B
BE-34                                           TROUBLESHOOTING PROCEDURE FOR BCM
5.     Actions by failure symptoms

    Key hole illumination does not work.




                                           NO
(     Key reminder function check Jr                             Key reminder function check

                      YES



c      Fuse short check (F18)
                                 >
                                           HG
                                                                       Fuse replacement

                      OK



       [Key hole illumination]             NO
         Output monitoring                                             BCM malfunction



                      YES
                 1f
                                                          1. BCM-JM ® - M05© Check
Output circuit wiring short of key                        2.Check whether 12V is applied
 hole illumination output circuit                            to terminal M05®

       Key hole illumination                                   Apply 12V to both ends of key hole
           malfunction                                    illumination bulbs, and check the operation.

                                                               [M05]
                                                                          (Connector terminal
                                                                C3        of key reminder switch)
                                                           o   o




                                                                                                KTO8730D
BODY CONTROL MODULE (BCM)                                                                                                      BE-35
B«iwanM»«B«g»MmiMiiiiiiiiiii.iiii.iiiiiM»iiiiiiiiiiii        wmaumn   i i m i i i M i n n i M ^ " — • — •



FADE OUT ROOM LAMP                                                                       KTTOKO

ROOM LAMP CIRCUTI DIAGRAM (1)




                                                        • •::•:;'}:• .. .: : •••••••': •••..:. .^^•v./. ."••••• .'.':":.' '.
                        ••.••.;•• .;w ""':' . :":..•,:..'•
                                                     •..•/;• •^•••::.Vr-.:.\ ^ - ^ j ^ : ^ : / '
                        ."••.••.•: ;. •:'• -.;••./;: ^-^' : :
                                                     ••-• ••-•.^:'v.;';:-r-v;-5:,-.y-.c.^;;:.;;.:: 'F^ •;:. v: .' v .:':':•
                            -.•/'••::f:y::?->
                            •'• •••^;#H.^il
                        •rliil11
                        ..;    :.::.::•..'. ••••••••••   ;r.±>-.




                                                                                                     G11          G12



                                                                                                                               KTOB735A
BE -36                                                                                                 TROUBLESHOOTING PROCEDURE FOR BCM
ROOM LAMP CIRCUIT DIAGRAM (2)




                                                                                                                                                               'BCM-JM




                   M46
                                                                                                                          *JOINT
                                                                                                                           CONNEC-
                                                                                                                          TOR




           0.5R                                                                                                              0.3G/B    0.3Y/B         0.3G/O


            21^MD02
                                                                                                                          LUGGA-
                        0.5Gr/B                  0.5Y           0.5Gr                                                     GE
                                                                                                                          ROOM                                 M10-1
                                                                                                                          LAMP                                    ,,., S i l l INSTRU-
                           LEFT                                                                                                                                  TRUNK •MENT
                           DOOR                                                                                                                                              ^CLUSTER
                           LAMP




                                                 0.5Y                                                                                                          M10-2


            20^MD02                                                                                                                                     0.5R


         0.5Gr/B       J          '
                                05Y
                   /
              1 I_                2   M53                                                                  0.5G/B                                        16 M35
                                            LEFT                                                       RIGHT                            9 - " " ~ '•::~ ••• " ••" • M "Ji JOINT
                                            DOOR                                                       DOOR                             c
                                                                                                                                                                   j  CONNECTOR
                   -----                    SWITCH                                                     SWITCH                           8
                                                                                                                                        BV7 - I ; ; , .... ;;|IV4M
                                                                                                                                              j                    ? •
                                                      Of                           *-*
               -"T- . » . ":1-                       -=• ":l:.;.:..v.:.;; .->•—,uz.^-^J. .                             R17
                                                                                                                                                           *-
                                                                ••••• - Y / : •::.:'.•                                                   17              20 M35
                            *                                                                                    -A       LUGGAUGE                                       From
                                M53                                                                                       LAMP                                           Fuse 18



                                                                                                                    - *R17
                                                                                                                          SWITCH
                                                                                                                                       0.5R             0.5R
                                                                                                                                                                         V
                                                                                                         JOINT
                       0.3B                                                              _ Ground       "CON-
                                                                                         ,tribut!Of>    SECTOR                        T o Key
                                                                                                                                      Remind Switch



                                                                2.0B                                            0.5B


                           <k
                           G01                                        G02                                           GOG



                                                                                                                                                                              KTOB711B
BODY CONTROL MODULE (BCM)
1.       Function explanation: It turns on when door is                      2)     Actuator inspection
         opened, and fades out after 5 or 6 seconds when                            Select "02.OUTPUT ACTUATION" and press
         closed.                                                                    [ENTER].
                                                                                    Perform forced drive against room lamp.
2.       Input/output signal
           • Fuse : F18(10A)
           • Input: Door switch (F11)                                                           1.2 ACTUATION TEST
           • Output: Room lamp (M3)
                                                                                    MODEL : HD COUPE         2002MY ALL
                                                                                    SYSTEM : BODY CONTROL MODULE
3.       Related Hi-scan(pro) failure diagnosis

         1)    Input/output monitoring                                                 01. INPUT ACTUATION
               Select "04.DOOR" and press [ENTER]. Then, the
               following screen will be displayed.
                                                                                          . c, m a s
               Check BCM input/output condition against all
               door switches and room lamp.


                    1.1 INPUT/OUTPUT MONITORING
                                                                                                                          KTOB700I
               MODEL : HD COUPE         2002MY ALL
               SYSTEM : BODY CONTROL MODULE
                                                                                             1.11 ACTUATION TEST
                   01. POWER
                   02. FLASH
                   03. LAMP                                                       | ROOM LAMP
                                                                                  I DURATION  UNTIL STOP KEY
                   05. LOCK & FOLDING                                             j METHOD      ACTIVATION
                   06. WIPER
                                                                                  I CONDITION   IG. KEY ON
                   07. ETC
                                                                                                ROOM LAMP : DOOR POS.


                                                             KTOB710F                 PRESS [STRT], IF YOU ARE READY !


     j                    1.11 CURRENT DATA                                        STRT    STOP!

                                                             A
                                                                                                                          KTOB735C
              IDRIVERDOQRSW                   CLOSED    1
               PASSENGER DOOR SW              CLOSED
               DOOR SW-2                      CLOSED
                                                                        4.   Expected failure symptoms
               KEY HOLE ILLUMINATION          OFF                            Room lamp does not work.
               ROOM U M P                     0    %
               HOODSW                         CLOSED
               TAIL GATE OPEN SW              CLOSED
               TAIL GATE UNLOCK INPUT         OFF       1



     I        I FIX | |SCRN| 1 FULL| |PART| |GRPH| 1 HELP|
                                                             KTOB710D
Dt B38                                                         TROUBLESHOOTING PROCEDURE FOR BCM
5.     Actions by failure symptoms

 Room lamp does not work.




 Check whether room lamp switch      NO
                                          Place it on the door position
    is placed at door position.


                      YES



          [Room lamp]                NG
         Output monitoring                     BCM malfunction



                      OK



     Does the room lamp turn on
                                  YES        Output wiring short
      when room lamp switch                                                 B C M - M R 0 - M 9 5 © Check
            is turned on?                      of room lamp


                      NO
                 'r
      Room lamp power supply
                                                                             BCM-MR0-M95© Check
            malfunction


     Room lamp bulb malfunction                                             Room lamp bulb replacement
BODY CONTROL MODULE (BCM)                                                                                                                        BE ""39

SEAT BELT WARNING LAMP
TIMER     KTOB7400

WARNING LAMP & GAUGE CIRCUIT DIAGRAM




                                                                                             BCM-IM


   0.3P                                              0.3R/O                         0.3P/B


                                                         2 M10-2                        3 M10-1




                                                                                                                                   M10-2



                                                                      V °
                                                                   0.5P/BI
                                                                                                                         0.3Y/O



  See Airbag                       See ECM Circuit       See           3y              4^    MM03
                                   (2.0L/2.7L)         Charging
                                                        Circuit    0.5P/B            0.3Y
                                                                                             M55

                                                                                                                FUEL
                                                                            -—-——                        FUEL   SENDER      10 BCM-EF
                           MC01(2.0L)                FULL Fuel                                           SENDER &FUEL
                           MC101(27L)                     levei                                                 PUMP
                                                                             Gauge            |.Flier-          MOTOR    0 5P/B
                                                                             Sender          .mister


                                                                                                                                   ;M48
               0.5Gr/B
                                                                                                                                        SEAT
                                                                               1^M55                                                    BELT
                                                                                                                                        SWITCH

                                                                             0.5B

                          C1S(2.0L)
                          C115(2
                            OIL                                              0.5BI                                          0.5B

                     \l     PRESSURE
                            SWITCH

                         2Ss~                                                  k                                                  GOI
                                                                               G13


                                                                                                                                                  KTOB740A
BE -40                                                           TROUBLESHOOTING PROCEDURE FOR BCM
1.   Function explanation: Seat belt indicator lamp blinks            2)    Actuator inspection
     for 6 seconds when IGN is turned on to recommend                       Select "02.OUTPUT ACTUATION" and press
     driver to buckle up.                                                   [ENTER].
                                                                            Perform forced drive against seat belt indicator
2.   Input/output signal                                                    lamp.
       • Fuse : F17 (10A)
       • Output: Seat belt indicator lamp (J12)
                                                                                        1.2 ACTUATION TEST
3.   Related Hi-scan(pro) failure diagnosis
                                                                            MODEL : HD COUPE         2002MY ALL
     1)   Input/output monitoring                                           SYSTEM : BODY CONTROL MODULE
          Select "07.ETC" and press [ENTER]. Then, the
          following screen will be displayed.                                  01. INPUT ACTUATION
          Check output condition against seat belt indicator
          lamp.


               1.1 INPUT/OUTPUT MONITORING

          MODEL : HD COUPE         2002MY ALL
          SYSTEM ; BODY CONTROL MODULE
                                                                                                                     KTOB700I

             01. POWER
             02. FLASH
                                                                                       1.11 ACTUATION TEST
             03. LAMP
             04. DOOR
             05. LOCK & FOLDING                                            SEATBELT INDICATOR
             06. WIPER                                                     DURATION       UNTIL STOP KEY
                                                                           METHOD         ACTIVATION
                                                                           CONDITION      IG. KEY ON
                                                      KTOB725F                            NAS AREA NOT SUPPORT

                                                                              PRESS [STRT], IF YOU ARE READY
                     1.11 CURRENT DATA


          POWER WINDOW RELAY             OFF
                                                                           ISTRTj [STOP
          SEATBELT SW                    UNBUCKLED
                                                                                                                    KTOB740B
          CHIME BELL          ^          OFF
          OVERSPEED                      OFF                     4.   Expected failure symptoms
          REAR DEFOGGER SW               OFF                          Seat belt indicator lamp does not work.
          REARDEFOGGER                   OFF
          CRASH SENSOR VOLTAGE           0.0   V


          FIX ||SCRN| I FULL | [PARTJ |GRPH [ [HELP
BODY CONTROL MODULE (BCM)                                                BE -41
5.    Actions by failure symptoms

 Seat belt indicator lamp does not work.




      [Seat belt indicator lamp]       NO
         Output monitoring                      BCM malfunction



                    YES


       Does the other indicator
     inside cluster lamp turn on       NO
          when IGN is on?                       Fuse (F17) Check
                                   '


                    YES


     Output circuit wiring short            BCM-JM@-M10-2® Check
     of seat belt indicator lamp


        Cluster malfunction                 Indicator lamp malfunction
                                                   inside cluster




                                                                         KTOB740C
BE -42                                            TROUBLESHOOTING PROCEDURE FOR BCM
TAIL L A M P AUTOMATIC T U R N O F F   KTOB745O


TAIL LAMP & LICENSE LAMP CIRCUIT LAMP (1)




                                                     'JOINT
                                                     ?CONNECTOR




                                                                              KTOB745A
BODY CONTROL MODULE ( B C M ) _                                                                                                                                                                                                                                   BE-43

TAIL LAMP & LICENSE LAMP CIRCUIT LAMP (2)


                                                                                                                                                                                                                                 "*BCM
                                                                                                                                                                                                                                  •BOX
                e •:•:.: y--'-. •                                                                                                                                                      wzyy:..
                                                                                                                                                                                                                                 '1
                                                                                          From Tail Lamp Relay
               /••••••••••:••.:••:••••                                                                                                                                                 'Vft^'ftft           y : . ?- ;-t^
               ^;::;:-;.-v:V-v-^.;-:-::--V.y.;/-:;v.                                       T=rn,
                                                                                                                      A
          i-/••"••'
             '.V.'-:- •:•••••:••:•-'•.                                            ."': • r ••                                                                                          •;'••:'•;•":::';....':":; ;••;'"/•••;;-f.ii- V
                                                                                                                                                                                                                                    •:S
          ;,•.:••'•;'••••••-••;                                                      '.':V:.'."-".:'
           4 !.•'.•".                                  .          •'                               :'.:•"'. ••"•"•'         •.••••• • ••••:•- :••                                                      i::-:" ^ ^-\-:>-;:-^ :i
                                                                                                                                    •z yzz




                                                                                                                                                                            :
                                                                                                                                      •'            ••         ...•:..•:;.j(.I-.v•-v
                                                                                                                          yzyyz.                             -if,;.
                                                                 ••;' "" : .:•• •'; /'" : .-.•••••' • ••. f •'•,••••','".: .:
                                                                  ::                                     ;                                           . ••            -T"
                                                                                                                  ' 1-^.                                       •..":ft: • : ' ? !
                                                                                                                                           ;.:•::;,:;: :^ -^/.v^;-..
                                                             BCM-CE



                                                                                                                                                                                                                                                         •'.":.:;.: •»
                                                                                                                                                                                                                                                                     ' BOX
                                                                                                                                                                                                                                          .-.,- —   -i JOINT-"




                        See Turn and
                        Hazard Lamp
                               w

0.5Br/B                          0.5W

                                                           2IE06

                             TURN^™5TAIL)"5

                                                           E06




                                                                                                                                                                                                                                            £••"'^^"-"iRIGHT
                                                                                                                                                                                                                                              • "MillllHEAD
                                                                                                                                                                                                                                                  ^JIIlfLAMP




                                                       G15                                                     G05                         G02                                                           G16



                                                                                                                                                                                                                                                                    KTOB745B
BE -44                                                                     TROUBLESHOOTING PROCEDURE FOR BCM
1.   Function explanation: Remove key at the tail lamp                           2.         Select "03.LAMP" and press [ENTER].
     on state & Tail lamp turns off automatically when the                                  Then, the following screen will be displayed.
     driver's door is opened. So, Battery discharging is                                    Check BCM input condition against tail lamp
     prevented by turning the tail lamp off.                                                switch and tail lamp.

2.   Input/output signal
       • Fuse: F9(10A), F14(10A)                                                             1.1 INPUT/OUTPUT MONITORING
       • Input : Driver's side door switch (E9), Tail lamp
         switch (H5), Door warning switch (H4)                                    MODEL : HD COUPE          2002MY ALL
                                                                                  SYSTEM : BODY CONTROL MODULE
       • Output: Tail lamp (C10, C11, F5, F109 J5, 115)
                                                                                            01. POWER
3.   Related Hi-scan(pro) failure diagnosis
                                                                                            02. FLASH
     1)   Input/output monitoring
                                                                                        04. DOOR
          1. Select "01.POWER" and press [ENTER].
                                                                                        05. LOCK & FOLDING
              Then, the following screen will be displayed.
                                                                                        06. WIPER
              Check BCM input condition against door
                                                                                        07. ETC
              warning switch.

                                                                                                                                        KTOB745I
                  1.1 INPUT/OUTPUT MONITORING

          MODEL : HD COUPE          2002MYALL                                                           1.11 CURRENT DATA
          SYSTEM : BODY CONTROL MODULE
                                                                                                                                       A
                                                                                 •'•:.-.;     •..•-,_;* :•-';'/   -         •. •: '.
                01. POWER
                02. FLASH
                                                                                 TAIL LAMP
                                                                                 HEAD LAMP SW
                                                                                                                            OFF
                                                                                                                            OFF
                                                                                                                                        1
                                                                                                                                        1
                03. LAMP
                04. DOOR
                                                                                 HEAD LAMP
                                                                                 AUTO LIGHT OPTION
                                                                                                                            OFF
                                                                                                                            OFF
                                                                                                                                       I1
                05. LOCK & FOLDING
                06. WIPER
                07. ETC
                                                                                 AUTO LIGHT SW
                                                                                 AUTO LIGHT SENSOR
                                                                                                                            OFF
                                                                                                                            0.0 V
                                                                                                                                        1
                                                                                                                                        I
                                                                                 FRONT FOG SW                               OFF

                                                                                                                                       ?
                                                                KTOB700D
                                                                                I FIX | |SCRN| I FULL| PART |GRPH||HELP
                          1.11 CURRENT DATA                                                                                            KTOB745C


                                                                A                3.         Select "04.DOOR" and press [ENTER].
          BATTERY VOLTAGE                        0.8        V
                                                                                            Then, the following screen will be displayed.
          >" ic y'-<rt''•'•/••. V •[ • ••'••     • -'t)Fr                                   Check BCM input condition against driver's
          KEY STATE - ACC                        OFF
          KEY STATE - ON OR ST                   OFF
                                                                                            side door switch.
          KEY STATE - ON                         OFF
          GENERATOR VOLTAGE                      0.0 V
                                                                                            1.1 INPUT/OUTPUT MONITORING
          STARTER INHIBIT OUTPUT                 OFF
                                                                                 MODEL : HD COUPE         2002MY ALL
                                                                                 SYSTEM : BODY CONTROL MODULE

          FIX J [SCRN [FULL | | PART           GRPHj |HELP
                                                                                       01. POWER
                                                                                       02. FLASH
                                                                KTOB710C               03. LAMP

                                                                                       05. LOCK & FOLDING
                                                                                       06. WIPER
                                                                                       07. ETC


                                                                                                                                       KTOB710F
BODY CONTROL MODULE (BCM)                                                                                             BE -45
                                                                              2.     Select "02.OUTPUT ACTUATION" and
                        1.11 CURRENT DATA                                            press [ENTER].
                                                                                     Perform forced drive against tail lamp.
         DRIVER DOORS)                           3p>
         PASSENGER DOOR SW                  CLOSED
         DOOR SW-2                          CLOSED                                         1.2 ACTUATION TEST
         KEY HOLE ILLUMINATION              OFF
         ROOM LAMP                          0    %                            MODEL : HD COUPE         2002MY ALL
                                                                              SYSTEM : BODY CONTROL MODULE
         HOOD SW                            CLOSED
         TAIL GATE OPEN SW                  CLOSED
                                                                                   01. INPUT ACTUATION
         TAIL GATE UNLOCK INPUT             OFF
                                                                                   02. OUTPUT ACTUATION

         FIX     SCRN     FULL   PART    GRPH   HELP


                                                       KTOB710D


  2)     Actuator inspection
         1. Select "01.INPUT ACTUATION" and press
             [ENTER].
             Perform forced drive against tail lamp switch.
                                                                                          1.11 ACTUATION TEST

                     1.2 ACTUATION TEST
                                                                            | TAIL LAMP
         MODEL : HD COUPE         2002MY ALL                                I DURATION       UNTIL STOP KEY
         SYSTEM : BODY CONTROL MODULE
                                                                             METHOD          ACTIVATION

           EHHH                                                             I CONDITION      IG.KEYON
               02. OUTPUT ACTUATION

                                                                                   PRESS [STRT], IF YOU ARE READY !


                                                                             STRT     STOP


                                                       KTOB700G                                                       KTOB745E




                    1.11 ACTUATION TEST                           4.   Expected failure symptoms

                                                                       1)    Tail lamp does not work.
       | TAIL LAMP SW
        DURATION        UNTIL STOP KEY                                 2)     Left tail lamp only does not work.
        METHOD          ACTIVATION
        CONDITION       IG. KEY ON                                     3)     Right tail lamp only does not work.

                                                                       4)    External tail lamp works, but internal tail lamp
           PRESS [STRT], IF YOU ARE READY !                                  does not.

                                                                       5)    Only one tail lamp does not work.
        STRT     STOP
                                                                       6)    Tail lamp automatic turn off function does not
                                                       KTOB745D              work.
BE-46                                                                   T R O U B ^ H O O T I N G P R O C E D U R E FOR B C M

5.   Actions by the failure symptoms                                           1)   Tail lamp does not work.




     Does the tail lamp work         NO
                                                     Fuse(F18)short
      when IG on state?


                    YES

                                                                                            1. BCM-HM © - M01 -2 @ Check
                                                  Input wiring short of tail                2. M01-2©- M 3 6 © - M36@ - G11
          [Tail lamp switch]         NO
                                           j            lamp switch.                           (Ground) Check
           input monitoring
                                           |    Tail lamp switch malfunction                  Connect ohmmeter to both terminals of
                                                                                            tail lamp switch, and check the continuity.

                                                                                                      [MOt-2]
                    YES
                                                                                                 n,     D   pi j — i — i   (Connector terminal
                                                                                                        o        o         of multi-function
                                                                                                                           switch)
             [Tail lamp]             NO
          Output monitoring                           BCM malfunction



                    YES


                                     NG
  RH Fuse(F9) & LH Fuse(F14) |
                                                     Fuse replacement
 checks the short simultaneously?


                    OK


 [Tail lamp switch] Is 12V applied   NO        Since PCB internal relay is fail,
  to F10 and both terminals of
                                                      replace BCM.
   grounding after grounding?


                                     YES          BCM 'C & 'F Connector
                                                    installation check




                                                                                                                                         KT0B745F


     2)    Left tail lamp only does not work.
           => Fuse F(14) short check

     3)    Right tail lamp only does not work.
           => Fuse F(9) short check
BODY CONTROL MODULE (BCM)                                                               BE-47
  4)   External tail lamp works but internal tail lamp
       does not.




             Dose tail lamp of the power               NO
             window switch work?                            Check the joint connector
                                               )

                             YES




       c   Check shut connector installation
                                               )
                                                       NO
                                                                     Install it



                             YES


                                                              Rheostat malfunction




                                                                                        KTOB745G


  5)   One taii lamp only does not work.
       ^> Check related wire bulb burnt

  6)   Tail lamp automatic turn off function does not
       work.




                  [Power warning switch]           |   NO
                     Input monitoring                       See key reminder function


                              YES



                 [Driver's side door switch]       |   NO
                                                            See key reminder function
                      Input monitoring



                              YES


                                                                BCM malfunction




                                                                                        KTOB745H
BE-48                                     TROUBLESHOOTING PROCEDURE FOR BCM
REAR WINDOW & OUTSIDE MIRROR
DEFOGGER    KTOB75OO

REAR WINDOW & OUTSIDE MIRROR DEFOGGER CIRCUIT DIAGRAM (1)




                                             ^"-^mm:mMimMmfi^




                                                                      KTO8750A
BODY CONTROL MODULE (BCM)                                                                                                                       BE-49
REAR WINDOW & OUTSIDE MIRROR DEFOGGER CIRCUIT DIAGRAM (2)




                                                                      • •." " m " " 1 BCM
                                                                                 : i BOX
                                                                                     •'- --'"'.-•
                                                                                     •:;:; :.:|




                 MANUAL A/G                                                                                   iilii«:
                                                  From Fuse 6




                                                                  mmm
       0.317B                 0.3R/B                               0.3R/B                                           0.3L



                                                                          11                                         21         M19-1
                                              ftA/C               B      . ,,... I                        :     :          .1           !«A/C
                                                  CONTROL                                                                               I? CONTROL
                                                  MODULE                                                                                  MODULE




                                                                      ' K i 3 K ^ * ^ S ^ & & ,
                                                                                                                                M19-1



          0.5B                                                           0.5B                                       0.5B



            19                                                               18 f M 3 6
                                                        •PWTOI^                ::-^:            | JOINT
                                                                                              | CONNECTOR
                                                                                               I
                                                                                         M36



                                                                        1.25B
                                       2.0B



                                                                        4      G11
BE-50                                                                                       TROUBLESHOOTING PROCEDURE FOR BCM

CHARGING CIRCUIT DIAGRAM

                                                                2.0L
                                                                                                         HOT AT ALL TIMES
                                                                                                 ....                                                 B IGNITION
                                                                                                                                                      [SWITCH
                                                                                               iLOGK^                           START
                                                                                               e
                                                                                                  mwmON
                                                                                               * — ^
                                                                                                                             6^MG4
                                                                                                                     3.0R
                                                                                                                             4 BCM-LM
   20B                                                                        See Power ^
                                                                              Distribution                                                                 . '.::./^v::::V:;/v:.;:.:::r-:::::'::.::.;;:V:::;:.;::;:::';:.v   : ' ; . \ 7 .5



                                                           :                                 :
                   See Power^_j SJOINT              •./•^.••'>
                                                             .::•'r::•^:••'.:::<k:'.:•3:-.'-v:•--i.H :';ie::, .^.S
                  »Distribution^"? •CONNE-                                                         :v •:•;:••: ' ••.;.;••:
                                   CTOR.
                                                     • .,-.,^.--:,^ ;,.:-v:: :••;:•;•;
                                                                    •'••'••' '"'.::.'•' '':•••::'.':::'••'•
                                                      :;•{.:••••::.

                                                     .... : ..'v....'.:.'
                                                     .. '..:' :..':.



                                               13 BCM-CE

    20B     15W          2.0R/B              0.5W                                                                   0.3O                        0.3P/B                              0.3R/O

                                                                                                                                                                      M10-1                                       M10-2
                                                                                                                                                                                                                                               i INSTRU-
                                                                                                                                                                                                                                              P# MENT
                                                                                                                                                                                                                                              P
                                                                                                                                                                                                                                                » CLUSTER




      M
                                                2 E20-2
                                                                                                                                                           GENERATOR




                                                           -•••:•••                           :"•:••-•               •:,-™ :";:-;-                     :
                                                                                                                                                       ' -'r
                                                                                                                                 ::
                                                            .'••;••:                                            •                    -'....•"'': ::

                                                                                                                                                                                                                                                  KTOB750C
BODY CONTROL MODULE (BCMQ                                                                                          BE -51
1.   Function explanation: When rear window defogger                           Select "07.ETC" and press [ENTER]. Then
     switch on while engine is running, it works.                              the following screen will be displayed.
                                                                               Check BCM input/output condition against
2.   Input/output signal                                                       rear window defogger switch and rear win-
       • Fuse : F12 (30A)                                                      dow defogger.
       • Input: Rear defogger switch (H19), Generator L
         (C13)
       • Output : Rear defogger output [Rear window             j              1.1 INPUT/OUTPUT MONITORING
         (G1), Rear window defogger indicator lamp (110),
         Outside mirror defogger (F19)]                                   MODEL : HD COUPE          2002MY ALL
                                                                          SYSTEM : BODY CONTROL MODULE                   |
3.   Related Hi-scan(pro) failure diagnosis
                                                                I             01. POWER
     1)   Input/output monitoring                               [             02. FLASH
          1. Select "01.POWER" and press [ENTER].                             03. LAMP
              Then, the following screen will be displayed.                   04. DOOR
              Check BCM input condition against genera-         j             05. LOCK & FOLDING
                                                                |             06.WIPER
              tor voltage.
                                                                •         •   07. ETC.:,'v   ''               •         •


              1.1 INPUT/OUTPUT MONITORING                                                                             KTOB725F


          MODEL : HD COUPE         2002MY ALL
          SYSTEM : BODY CONTROL MODULE
                                                                |                    1.11 CURRENT DATA

                                                                                                                   A
                                                                           POWER WINDOW RELAY        OFF
             02. FLASH
                                                                                                                   1
             03. LAMP                                                      SEATBELT SW               UNBUCKLED
                                                                                                                   1
             04. DOOR                                                     SEATBELT INDICATOR
                                                                          CHIME BELL
                                                                                                     OFF
                                                                                                     OFF
                                                                                                                   1
             05. LOCK & FOLDING                                                                                    1
             06. WIPER                                                    OVERSPEED                  OFF
             07. ETC                                                     1 REAR DEFOGGER SW          OFF       I
                                                                           REAR DEFOGGER             OFF
                                                                          CRASH SENSOR VOLTAGE       0.0  V
                                                     KTOB700D
                                                                                                                   ?
                                                                         FIX | |SCRN| 1 FULL 1 |PART| |GRPH] |HELP|
                    1.11 CURRENT DATA                           I I
                                                                                                                   KTOB750K

          BATTERY VOLTAGE               0.8 V
          DOOR WARING SW                OFF                         2)   Actuator inspection
          KEY STATE - ACC               OFF                              1. Select "01.INPUT ACTUATION" and press
          KEY STATE - ON OR ST          OFF                                  [ENTER].
          KEY STATE - ON                OFF                                  Perform forced drive against rear window de-
                                                                             fogger switch.
          STARTER INHIBIT OUTPUT        OFF


                                                                                    1.2 ACTUATION TEST
          RX~| |SCRNJ [FULL] I PART | |GRPHJ [HELP
                                                                         MODEL : HD COUPE         2002MY ALL
                                                                         SYSTEM : BODY CONTROL MODULE
                                                     KTOB750J


                                                                              02. OUTPUT ACTUATION




                                                                                                                   KTOB700G
BE-52                                                          TROUBLESHOOTING PROCEDURE FOR BCM
                                                               4.   Expected failure symptoms
                   1.11 ACTUATION TEST
                                                                    1)   Rear window defogger indicator lamp does not
                                                                         work.
    REAR DEFOGGER SW
    DURATION           UNTIL STOP KEY                               2)   Rear window defogger does not work.
    METHOD             ACTIVATION
    CONDITION          IG. KEY ON
                                                                    3)   Left side outside mirror defogger does not work.
                       ENGINE RUNNING
                                                                    4)   Right outside mirror defogger does not work.
             PRESS [STRT], IF YOU ARE READY !


    STRT        STOP


                                                    KTOB750D


        2.     Select "G2.QUTPUT ACTUATION" and
               press [ENTER].
               Perform forced drive against rear window de-
               fogger.


                     1.2 ACTUATION TEST

        MODEL : HD COUPE         2002MY ALL
        SYSTEM : BODY CONTROL MODULE

              01. INPUT ACTUATION




                                                    KTOB700I




                   1.11 ACTUATION TEST


    REAR DEFOGGER
    DURATION           10 SECONDS
    METHOD             ACTIVATION
    CONDITION          IG. KEY ON
                       ENGINE RUNNING


             PRESS [STRT], IF YOU ARE READY !


    STRT


                                                   KTOB750E
BODY CONTROL MODULE (BCM)                                                                                                                BE-53
5.     Actions by the failure symptoms                                                 1)   Rear window defogger does not work.



                                      NG
C     Fuse(F12, F6) check short   J                       Fuse replacement

                   OK

                                    Below
         [Generator voltage]      | 10V             1. BCM-CE@-E20-2© Check
           Input monitoring                         2. Check generator condition                1. BCM-HM©- M20© Check (Manual A/C)
                                                                                                2. M20® - M36© - M36 © - G11 Check
                                                                                                   (Manual A/C)
                   Above 10V
                                                                                                3. BCM-HM© - M19-1© Check (Auto A/C)
                                                                                                4. M19-1 © - M36® - M36@ - G11 Check
                                                    1. [Rear window defogger switch]
    [Rear window defogger switch] I NO                                                        ^    (Auto A/C)
                                            .^ar-
                                                       Input wiring short
           Input monitoring
                                                    2. [Rear window defogger switch]             Install the ohmmeter at the both ends of air
                                                       Malfunction                               conditioner terminals and check the continuity.
                   YES                                                                           M20 © - M20® (Manual A/C)
                                                                                                 M19-1©-M19-1© (Auto A/C)                        j

      [Rear window defogger]
                                      NO
         Output monitoring                                 BCM malfunction
          after positioning
                                                                                                1. BCM-IM © - M20© Check (Manual A/C)
                                                                                                2. M20® - M36©- M36® - G11 Check
                                                                                                   (Manual A/C)
                   YES
                                                                                                3. BCM-IM© - M19-1© Check (Auto A/C)
                                                                                                4. M19-1© - M36©- M36©- G11 Check
   [Rear window defogger]                            1. Output wiring short of                     (Auto A/C)
Is 12V applied to both ends of        YES               Rear window defogger
BCM G1 and GND after output
                                                     2. Rear window defogger                     Apply 12V to both terminals of air
     signal forced drive?
                                                        indicator lamp malfunction               conditioner and check lamp operation.
                                                                                                 M20© - M20® (Manual A/C)
                   NO                                                                            M19-1 © - M19-1® (Auto A/C)
       Rear defogger relay                               Relay replacement
       malfunction




                                                                                                                                          KTOB750F
BE ™54                                               TROUBLESHOOTING PROCEDURE FOR BCM
  2)   Rear window defogger does not work.




               Does rear window defogger        NO          See 5-1 [Rear window defogger
         ,        indicator lamp work?                       indicator [amp does not work]



                              | YES



              1.. Output wiring short of             1. BCM-GF©- MR01©- RR01©- R15© Check
                  rear window defogger               2. RO60-GO8 Check

              2. Rear window defogger
                                                     See workshop manual page BE-78-BE-79




                                                                                                 KTOB750G


  3)   Left outside mirror defogger does not work.




               Does rear window defogger        NO          See 5-1 [Rear window defogger
                  indicator lamp work?                       indicator lamp does not work]



                               YES



                                                     1. BCM-FF©- MD01® - D06© Check
             1. Output wiring short of left
                                                     2. D06©- MD01© - G01 Check
                outside mirror defogger

             2. Left outside mirror defogger
                                                            It is normal if the measured
                malfunction                                 defogger resistance is 10Cl.

                                                            [D06]
                                                      In        i—in   (Connector terminal
                                                            o          of left outside mirror)
                                                        °


                                                                                                 KTOB750H
BODY CONTROL MODJ^EgCM^                                                                             BE -55
  4)   Right outside mirror defogger does not work.




                  Does rear window           |   NO          See 5-1 [Rear window defogger
                indicator lamp work?                          indicator lamp does not work]



                            YES



                                                      1. BCM-FF©- MD01® - MD04©-D06© Check
           1. Output wiring short of right
                                                      2. D16®- MD03© - M45©- M45©- G02 Check
              outside mirror defogger

          2. Right outside mirror defogger                   It is normal, if the measured
             unit malfunction                                defogger resistance is 10CI.

                                                             [D16]
                                                       In    i—i     n   (Connector terminal
                                                         o   0           of right outside mirror)




                                                                                                     KTOB750I
BE-56                            TROUBLESHOOTING PROCEDURE FOR BCM

AUTO LIGHT CONTROL KTOBTSBO
AUTO LIGHT CIRCUIT DIAGRAM (1)



                                                                                                                 sE/R
        See Power ^g.                                                                                            jBOX
        •Distribution —
                                                                                                       ::
                                                                                                            V:': B
                                                     • '.                                         •                 °
                                                                                                        •.'•'::.:::•.
                                                .:':'•";•.'•'•-.••' ••'••'•••      '
                                            ..,. ....;;.......:;:,.. ':...:.;. ':..,:.,•'.";..'.'.•:.::.".:"•.: 1
                                                                              :-•'•"••:•;.     ' ;:'.'-!l




                                                                                               MULTIFUNCTION
                                                                                               SWITCH




                                     G11



                                                                                                                        KTOB755A
BODY CONTROL MODULE (BCM)                                                                                                                                      BE »57

AUTO LIGHT CIRCUIT DIAGRAM (2)



                                                                                                                                                               »BCM
                                                                                                                                                               !BOX




                      »••• • -':.:•."'...': .     •                   . -.••.•;••:•''
                      i    .




                                                                                                                                                    §m


                                     14 BCM-HM                                             5 BCM-LM          BCM-IM                       15] BCM-JM




              From Head Lamp
              Relay (LOW)


                V
    0.3W      0.5Br            0.3B/O                         2.0B                      2.0B          0.5B            0.5L              0.5R

                                                M01-2
                                                        HE MULTI-
                                                          «FUNC-
                                                          TION
                                                         ISWITCH




                                                                                                                                           2JM27
                                                                                                                                                AUTO
                                                                                                       Ground           Signal     Sensor Power LIGHT
                                                                                                                                                SENSOR

                                                                                                                                               ' ' ' • •.,•§
                                                                §                         G11
                                                                                                                             •   •• •             • •••-•
                                                                G12                                                                                 :: j




                                                                                                                                                               KT0B755B
BE -58                                                           TROUBLESHOOTING PROCEDURE FOR BCM
1.   Function explanation : When multi-function lighting              2)    Actuator inspection
     switch is put at AUTO position in ignition key is on                   Select "01.INPUT ACTUATION" and press [EN-
     state, tail lamp and headlamp turns on automatically                   TER].
     depending on the auto light sensor values.                             Perform forced drive against auto light switch.

2.   Input/output signal
       • Fuse : Headlamp (Low) Fuse(15A), Headlamp                                     1.2 ACTUATION TEST
         (High) Fuse(15A), F21(10A)
       • Input: Auto light switch (H14), Auto light sensor                  MODEL : HD COUPE         2002MY ALL
                                                                            SYSTEM : BODY CONTROL MODULE
         voltage (J11)
       • Output: Tail lamp, headlamp
                                                                                        ACTUATION
                                                                               02. OUTPUT ACTUATION
3.   Related Hi-scan(pro) failure diagnosis

     1)   Input/output monitoring
          Select "03.LAMP" and press [ENTER]. Then the
          following screen will be displayed.
          Check BCM input/output condition against auto
          light switch, auto light sensor voltage, auto light                                                         KTOB700G
          option, tail lamp and headlamp.

                                                                                      1.11 ACTUATION TEST
               1.1 INPUT/OUTPUT MONITORING

          MODEL     HD COUPE        2002MY ALL                             AUTO LIGHT SW
          SYSTEM    BODY CONTROL MODULE                                    DURATION     UNTIL STOP KEY
                                                                           METHOD       ACTIVATION
             01. POWER
                                                                           CONDITION    COVER A/LIGHT SENSOR
             02. FLASH

             04. DOOR
             05. LOCK & FOLDING                                               PRESS [STRT], IF YOU ARE READY !
             06. WIPER
             07. ETC
                                                                           STRTJ I STOP I

                                                      KTOB745!                                                        KTOB755C


                                                                 4.   Expected failure diagnosis
                     1.11 CURRENT DATA
                                                                      1)   Auto light does not work. (Tall lamp and head-
                                                     A
          TAIL LAMP SW                   OFF                               lamp works by the switch)
          TAIL LAMP                      OFF
          HEAD LAMP SW                   OFF                          2)   When auto light Is turned on, tail lamp and head-
          HEAD LAMP                      OFF                               lamp turns on simultaneously.
          AUTO LIGHT OPTION              OFF
                                                                      iQJ NOTE
          AUTO LIGHT SENSOR              0.0 V
                                                                       When the ambient luminous intensity is dark, tail lamp
          FRONT FOG SW                   OFF
                                                                      and headlamp may turn on simultaneously in auto
                                                                      light on condition.
          FIX | |SCRN   FULL   PART | |GRPH| |HELP                    In this case it's not the failure.

                                                     KTOB755F
BODY CONTROL MODULE (BCM)                                                                                            BE -59
5.     Actions by failure symptoms

       1)    Auto light does not work. (Tail lamp and head-
             lamp work by the switches)




                                                  Input wiring short of   1.BCM-HM@-M01-2© Check
            [Auto light switch]         NO          auto light switch     2. M01-2@-M36©-M36@-G11 (Ground) Check
             input monitoring
                                                    Poor contact of       Install ohmmeter at both ends of auto light
                                                    auto light switch     switch and check the continuity

                                                                                   [M01-2]
                                                                               q     n       pi—     (Connector terminal
                      YES
                                                                                                     of multifunction switch)
                                                                                             o o




                                      Remain                              1.BCM-JM©-M27® Check
      Transmitting / Eliminating     ^un-         Input wiring short of   2. BCM-JM©-M27® Check
         to auto light sensor         changed       auto light sensor     3. BCM-IM © - M27© Check
      [Auto light sensor voltage]
           input monitoring                        Auto light sensor
                                                                               Auto light sensor re-installation
                                                    disconnection

                                                   Auto light sensor
                      Change                                                   Auto light sensor replacement
                                                     malfunction



       After covering as light is    ] Does not
     not transmitted to auto light     work
                                                   BCM malfunction
      sensor, [Auto light switch]
              forced drive




                                                                                                                        KT0B755D
BE -60                                                         TROUBLESHOOTING PROCEDURE FOR BOW
  2)     When auto light is turned on, tail lamp and head-
         lamp turn on simultaneously.




       [Auto light option]        ON         Auto light option               CutBCM-H©
        Input monitoring      —
                              -        &* Wrong wiring connection



                 OFF



       BCM malfunction




                                                                                           KTQB755E
BODY CONTROL MODULE (BCM)              BE -61

WIPER & WASHER CONTROL KTOBTSOO
FRONT WIPER & WASHER CIRCUIT DIAGRAM




                                       KTOB760A
BE -62                                                            TROUBLESHOOTING PROCEDURE FOR BCM
1.   Function explanation                                            2)    Actuator inspection
                                                                           1. Select "01.INPUT ACTUATION" and press
     1)   When washer switch is turned on, wiper operates                      [ENTER].
          two or three rotation.                                               Perform forced drive against front washer
                                                                               switch, intermittent wiper switch.
     2)   Intermittent time varies by the vehicle speed and
          intermittent wiper volume control.
                                                                                       1.2 ACTUATION TEST
2.   input/output signal
       • Fuse : F10 (20A)                                                  MODEL : HD COUPE         2002MY ALL
       • Input: Washer switch (K6), wiper INT switch (J9),                 SYSTEM : BODY CONTROL MODULE
         wiper INT (T) (J10), Wiper parking (K14)
       • Output: Wiper relay (C3)                                              •MfcMfcumi
                                                                                02. OUTPUT ACTUATION
3.   Related Hi-scan(pro) failure diagnosis

     1)   Input/output monitoring
          Select "06.WIPER" and press [ENTER]. Then,
          the following screen will be displayed.
          Check BCM input/output condition against front
          washer switch, intermittent wiper switch, intermit-
          tent wiper relay, intermittent wiper variable volt-
          age, wiper parking, snow safety relay.
                                                                                     1.11 ACTUATION TEST


               1.1 INPUT/OUTPUT MONITORING                                INTERMITTENT WIPER SW
                                                                          DURATION        UNTIL STOP KEY
          MODEL : HD COUPE         2002MY ALL                             METHOD          ACTIVATION
          SYSTEM : BODY CONTROL MODULE
                                                                          CONDITION       IG. KEY ON
              01. POWER
              02. FLASH
              03. LAMP                                                         PRESS [STRT], IF YOU ARE READY !
              04. DOOR
              05. LOCK & FOLDING
             $                                                            STRT    STOP!
              07. ETC
                                                                                                                   KTOB760C

                                                       KTOB760K
                                                                          2.     Select "02.OUTPUT ACTUATION" and
                                                                                 press [ENTER].
                        1.11 CURRENT DATA
                                                                                 Perform forced drive against intermittent
                                                                                 wiper relay and snow safety relay.

                                            M
          INTERMITTENT WIPER SW             OFF
                                                                                      1.2 ACTUATION TEST
          FRONT INT. WIPER RELAY            OFF
          WIPER INT TIMER                   0.7 V                         MODEL : HD COUPE         2002MY ALL
          WIPER-PARKING                     OFF                           SYSTEM : BODY CONTROL MODULE
          SNOW SAFETY RELAY                 OFF
                                                                               01. INPUT ACTUATION
                                                                               02. OUTPUT ACTUATION


          FIX I |SCRN[ I FULL I [PART I lGRPH| |HELF

                                                       KTOB760B




                                                                                                                   KTOB700I
BODY CONTROL MODULE (BCM)                                       BE-63

                      1.11 ACTUATION TEST


          | FRONT INT WIPER RELAY                    |
           DURATION     1 SECONDS
           METHOD       ACTIVATION
           CONDITION    IG. KEY ON



              PRESS [STRT], IF YOU ARE READY !


           STRT

                                                     KTOB760D


4.   Expected failure symptoms

     1}    Wiper low and Wiper high does not work.

     2)    Wiper does not work when wiper INT is turned
           on.

     3)    When washer switch is turned on, wiper does not
           interlock.

     4)    When wiper INT volume is controlled, wiper inter-
           mittent time does not change.

     5)    Wiper intermittent time does not change by the
           vehicle speed.

     6)    When wiper INT operating, wiper stops in-be-
           tween.
BE -64                                                               TROUBLESHOOTING PROCEDURE FOR BCM
5.     Actions by failure symptoms                                           Since wire drives directly wiper low and high op-
                                                                             eration, check the following 3 items by referring
       1)   Wiper low and Wiper high does not work.                          to front wiper & washer




       Check multi-function switch connector removal


                       Check wiper motor


                           Check wiring



                                                                                                                          KTOB760E


       2)   When wiper INT is ON, wiper does not work.




                                          NG
f       Check Fuse(F10) short        J-             Fuse replacement


                      OK



                                                    Input wiring short of            1.BCM-JM®-M01-1© Check
      [Intermittent wiper switch]         NO     intermittent wiper switch           2. M O M © - BCM-LM© Check
            Input monitoring
                                                 Intermittent wiper switch
                                                                                         Install ohmmeter at both ends of
                                                       malfunction
                                                                                        intermittent wiper switch terminals
                                                                                             and check the continuity
                      YES
                                                                                             [M01-1]

                                                                                         q            pL.
                                                                                                            (Connector of
                                                                                                  o    o    multi-function
                                                                                                            wiper switch)
       [Intermittent wiper relay]         NO
        Does output monitoring                         BCM malfunction
            turn on and off?


                      YES

                  i

     Wiper relay malfunction of
                                                    Relay replacement
    engine room relay & fuse box

     Output wiring malfunction
                                               1. BCM-CE®- E46® Check
     of intermittent wiper relay
                                               2. E46©- EM01© - M01-1®
                                                  Check




                                                                                                                         KTOB760F
BODY CONTROL MODULE (BCM)                                                                                                              BE-65
        3)    When washer switch is on, wiper does not inter-
              lock.

                                              NG
f       Check fuse(F10) short             \         Fuse replacement


                      OK


                                                                                              1.BCM-KM®-M01-1© Check
                                                   Input wiring short of
         [Front washer switch]                NO                                              2. M01 -1 © - BCM-LM © Check
                                                   front washer switch
            Input monitoring
                                                   Front washer switch
                                                                                                  Install the ohmmeter at the both
                                                       malfunction
                                                                                                ends of front washer switch terminals
                                                                                                      and check the continuity


                                                                                                       [M01-1]
                      YES
                                                                                                                            (Connector of
                                                                                                   n              p .
                                                                                                              o         o   multi-function
                                                                                                                            wiper switch)
                                                          See 5-2
        Does the wiper work                   NO
                                                   [Wiper does not work
        when wiper INT is on?                      when wiper INT is on]

                      YES


             BCM malfunction

                                                                                                                                        KTOB760G


        4)    When wiper INT volume is controlled, wiper inter-
              mittent does not vary.


      [Intermittent wiper variable
    voltage] Does it change within | Changes
                                                               BCM malfunction
     the range of 0.7V and 3.5V
     in case of input monitoring?


                      Remain unchanged



        Wiring short in relation to                1.BCM-JM®-M01-1® Check
    intermittent wiper variable voltage            2. M01-1©- BCM-JM© Check

        Intermittent wiper variable                Install the ohmmeter at the both terminals
       voltage switch malfunction                  of intermittent wiper variable switch, and
                                                   check whether the resistance changes
                                                   within the ranges of 0Q and 50kO by
                                                   changing the INT volume

                                                            [M01-1]
                                                        n          n           (Connector of
                                                                               multi-function wiper switch)
                                                                       O   O



                                                                                                                                        KTOB760H
BE -66                                                         TROUBLESHOOTING PROCEDURE FOR BCM
   5)     Wiper intermittent time does not change with the
          vehicle speed.




   Wiring short in relation                   1, BCM-JM©- M34© Check
      to speed sensor                         2. M340-M1O-1® Check



                                                                                                               KTOB760I


   6)     When wiper INT is operating, wiper stops in-be-               2.   When wiper Low / High is operating, this
          tween.                                                             function is not available.
          1. If parking signal is inputted when wiper INT
              or OFF is operating, wiper stops judging
              wiper motor overload.




                                            Wiper motor inner plate                      Wiper replacement
 Does the wiper turns on and
                                  NO             malfunction                  ^
off in case of input monitoring
   while operating wiper low
                                           Wring short in relation to
        [Wiper parking]?                                                          BCM-KM@-MC103©-C107©
                                                wiper parking
                                                                                  Check (2.7 ENG)

                                                                                  BCM-KM@- MC03©- C07®
                  YES                                                             Check (2.0 ENG)



        Check wiring short                 BCM-CE@-E46© Check




                                                                                                              KTOB760J
BODY CONTROL MODULE (BCM)                                                                             BE-67
KEYLESS ENTRY & BURGLAR
A L A R M   KTOB7650


ANTI-THEFT ALARM CIRCUIT DIAGRAM


                                                                                                      *IBCM
                                                                                                        °80X
                                     12Volt output        12Volt output                               :::;:;g
                                     •;.;•,;.v.ai "fit   -mS&immo^BSmmmm




                                                                                     Grounds


                                                                    BCM-EF      1              *5~| BCM-LfVt




                                                         0.5Y/O



                                                                    MR02
                                               MC102(2.7L)




                                   0.5G/O                0.5Y/O              2.0B          2.0B




            0.5R/B



                9^?EM01                14: ;EC01(2.0L) 8"           RR02
                                            EC101<2.7L)


            0.5R/B                 0.5G/O                0.5Y/O



                 1 E17 BURGLAR                                1 IR03
                       ALARM                                       I TAIL GATE
                       HORN                                         UNLOCK
                                                                    SWITCH


                                                                    R03



              0.5B                                           0.5B
                                                   HOOD
                                                   SWITCH


                                                                                               m
                                                                               G12             G11


                                                                                                        KTOB765A
BE-68                                                                                 TROUBLESHOOTING PROCEDURE FOR BCMsssass^^sgg



ROOM LAMP CIRCUIT DIAGRAM



                                                                                                                                                                     'BCM
                                                                                                                                                                      BOX
              '"'7^:':::: ••'•;:::.'::'•'•:'. g'Sipf : "
                                                    DOOR AJAR




              jiKDOonsw]                                    RH DOOR




        I, ^ BCM-FF
              * = L1  ~f, i ^ ^ ^11^8CM-FF
                    9 BCM-EF
                                     ^ i ^4 ^                                              ^ss^^^^s^^.BCM-EF 8\                                  _«•
                                                                                                                                                 16   BCM-JM




                                                                         " ,           •    mmm           'TOR



                                                                         6                        5   M46


                                                                      0.5R                    0.5R           0.3G/B    0.3Y/B             0.3G/O


        21                                                             2lAMD04                    1 M73
                                                                                                           LUGGA-
              0.5Gr/B                                0.5Y   0.5Gr     0.5R                                 GE
                                                                                                           ROOM                      M l 0-2          M10-1
                                                                          1 .Die
                                                                                                          ILAMP          ,--£•---"•&                   . . " ; " . " r i INSTRU-
                                                                                                                                                        TRUNK »MENT
                                                                                   RIGHT              M73                                               AJAR       J CLUSTER
                                                                                   DOOR
                                                                                   LAMP                                                                     ||ii§i
                                                                                           0.5G/B

                                                                         2     D18

                                                     0.5Y
                                                                      0.5Gr
                                                                                                  V.  MR02                                            M10-2



                                                                               MD04        0.5G/B                                              0.5R




                               M53                                                         0.5G/B                                               16    M35
                                       LEFT                                          RIGHT                               •           "•* ~ " " "* " ^KT " • JOINT
                                       DOOR                                          DOOR                                I                                 'CONNECTOR
                                      1SWITCH                                        SWITCH
                                                                                                                         E
                                                                                                                         1
                                                                                                                             e V^y -» •= *" •*=* ™ •* 'VSJ|f
                                                                                                      R17                    17                 20    M35
                                                                                                                                                                 From
                                                                                                                                                                 Fuse 18

                                                                                                                        0.5R                   0.5R
                                                                                                                                                                 V
             0.3B
                                                                                     JOINT
                                                                              QjitliCON-
                                                                               tion 8NECTOR                           To Key
                                                                                                                             V
                                                                                                                      Remind Switch



                                                                                               0.5B




               G01                                              G02
                                                                                                      k
                                                                                                    G06
BODY CONTROL MODULE (BCM)                                                                                           BE -69
1.   Function explanation: Door is opened and closed by                   Select "04.DOOR" and press [ENTER].
     using the transmitter.                                               Then, the following screen will be displayed.
     When the vehicle is broken in, alarm works and vehi-                 Check BCM input condition against hood
     cle cannot be started.                                               switch, tailgate switch, tailgate key unlock
                                                                          switch.
2.   Input/output signal
       • Input: Hood switch, tailgate switch, door switch,
         tailgate unlock switch                                           1.1 INPUT/OUTPUT MONITORING
       • Output: Starter inhibit, burglar alarm relay, bur-
         glar alarm horn                                            MODEL : HD COUPE         2002MY ALL
                                                                    SYSTEM : BODY CONTROL MODULE

3.   Related Hi-scan(pro) failure diagnosis                              01. POWER
                                                                         02. FLASH
     1)   Input/output monitoring
                                                                         03. LAMP
          1. Select "01.POWER" and press [ENTER].
              Then, the following screen will be displayed.              05. LOCK & FOLDING
              Check BCM output condition against starter                 06. WIPER
              inhibit output.                                            07. ETC



               1.1 INPUT/OUTPUT MONITORING

          MODEL : HD COUPE         2002MY ALL
          SYSTEM : BODY CONTROL MODULE                                          1.11 CURRENT DATA


                                                                     DRIVER DOOR SW                  CLOSED
             02. FLASH                                               PASSENGER DOOR SW               CLOSED
             03. LAMP                                                DOOR SW-2                       CLOSED
             04. DOOR                                                KEY HOLE ILLUMINATION           OFF
             05. LOCK & FOLDING                                      ROOM LAMP                       0   %
             06. WIPER
             07. ETC                                                TAIL GATE OPEN SW                CLOSED
                                                                    TAIL GATE UNLOCK INPUT           OFF

                                                        KTOB700D

                                                                   | FIX | |SCRN| I FULL I |PART| |GRPH| I HELP I
                    1.11 CURRENT DATA
                                                                                                                    KTOB765N


          BATTERY VOLTAGE                 0.8 V                     3.    Select "07.ETC" and press [ENTER]. Then,
          DOOR WARING SW                  OFF                             the following screen will be displayed.
          KEY STATE - ACC                 OFF                             Check BCM output condition against burglar
          KEY STATE - ON OR ST            OFF                             alarm horn.
          KEY STATE - ON                  OFF
          GENERATOR VOLTAGE               0.0 V
                                         P                               1.1 INPUT/OUTPUT MONITORING

                                                                    MODEL : HD COUPE         2002MY ALL
                                                                    SYSTEM : BODY CONTROL MODULE
          FIX | |SCRN| I FULL I | PART I |GRPH| [HELP
                                                                         01. POWER
                                                        KTOB765M
                                                                         02. FLASH
                                                                         03. LAMP
                                                                         04. DOOR
                                                                         05. LOCK & FOLDING
                                                                         06. WIPER




                                                                                                                    KTOB725F
BE-70                                                            TROUBLESHOOTING PROCEDURE FOR BCM
                                                                 4.   Expected failure symptoms
                    1.11 CURRENT DATA
                                                                      1)   Alarm does not work. (Hazard lamp works)
                                                     A
        OVERSPEED                    OFF
                                                                      2)   When hood is opened inside the car like alarm
        REAR DEFOGGER SW             OFF
                                                                           test, horn does not work.
        REAR DEFOGGER                OFF
        CRASH SENSOR VOLTAGE         0.0 V                            3)   When door is opened inside the car like alarm
                                                                           test, horn does not work.
        POWER WINDOW RELAY           OFF
        SEATBELT SW                  UNBUCKLED                        4)   When tailgate is opened inside the car like alarm
        SEATBELT INDICATOR           OFF                                   test, horn does not work.
                                                     T
       | FIX | |SCRN| I FULL| |PART| |GRPH| [HELPI
                                                                      5)   When the vehicle is locked by the remote trans-
                                                                           mitter, central door lock functions, but hazard
                                                                           lamp does not work once.
                                                     KTOB765C

                                                                      6)   When system is arm condition, if the tailgate is
  2)    Actuator inspection                                                tried open by the key, then the horn will works.
        Select "G2.0UTPUT ACTUATION" and press
        [ENTER].
        Perform forced drive against starter inhibit output           QJ NOTE
        and burglar alarm horn.                                       When the door (driver's or passenger's) is opened by
                                                                      the key horn will work. —»it's not malfunction (normal
                                                                      operation)
                    1.2 ACTUATION TEST
                                                                      7)   When the alarm is released condition, engine
        MODEL : HD COUPE         2002MY ALL                                does not start.
        SYSTEM : BODY CONTROL MODULE
                                                                      8)   Central door lock function works, but keyless en-
           01. INPUT ACTUATION                                             try system does not work.




                                                      KTOB700I




                   1.11 ACTUATION TEST


       STARTER INHIBIT OUTPUT
       DURATION    10 SECONDS
       METHOD      ACTIVATION
       CONDITION     IG. KEY ON



          PRESS [STRT], IF YOU ARE READY !


       STRT


                                                     KTOB765D
BODY CONTROL MODULE (BCM)                                                                                BE-71

5.   Actions by failure symptoms                               1)   Alarm does not work. (Hazard lamp works.;


                                               NG
                Check fuse(F13) short                               Fuse replacement


                                   OK



                 [Burglar alarm horn]
            Does not horn when forced drive
                                                          1. BCM-KM@-MC01®-M39©-M39®
                                                             Check (2.0 Engine)
                                   OK                        BCM-KM@-MC101®-iv139©-M39®
                                                             Check (2.7 Engine)
                                                          2. BCM-JM®- M39® Check
              Output wiring malfunction                   3. M39©-EM01®-E17© Check
                of burglar alarm horn                     4. E17©- G15(Ground) Check

                 Burglar alarm relay
                                                                    Relay replacement
                    malfunction

                 Burglar alarm horn
                                                              Burglar alarm horn replacement
                    malfunction




                                                                                                          KT0B765E


     2)   When hood is opened inside the car like alarm
          test, horn does not work.




                     [Hood switch]
                    Input monitoring



                                   NO
                                                          1. BCM-HM®-MC02®-EC01©-E38©
                           1   r                             (2.0 Engine)
                Check input wiring                        2. BCM-HM®-MC102©-EC101@-E38©
                short of hood switch                         (2.7 Engine)


               Hood switch malfunction                          Hood switch replacement



                                                                                                          KT0B765F
BE-72                                                      TROUBLESHOOTING PROCEDURE FOR BCM
  3)   When door is opened inside the car like alarm
       test, horn does not work (If tailgate and hood is
       opened, alarm works)




                  [All door switch]
                  Input monitoring



                              NO
                          f
                                                           1. B C M - F F © - M 5 3 © Check
        Check input wiring short of all doors
                                                           2. M53@-G01 Check
                                                           3. BCM - FF@- M54©Check
                                                           4. M54® - M45© - M45© - G02 Check
            All door switch malfunction




                                                                                               KT0B765G


  4)   When tailgate is opened inside the car like alarm
       test, horn does not work.




                     [Tailgate]
                  Input monitoring



                              NO
                         }
                                                           1. BCM-EF®- MR02©- RR02©- R17©
        Check input wiring short of tailgate                  Check
                                                           2. R17©-G06 Check

           Tailgate switcli malfunction




                                                                                               KTOB765H
BODY CONTROL MODULE (BCM)                                                                                      BE -73
  5)   When the vehicle is locked by the transmitter,
       central door lock function works but hazard lamp
       works only once.




                 [All door switch]             NO
                                                                            See 5-3
                 Input monitoring


                           YES


                 [Tailgate switch]             NO
                                                                            See 5-4                      |
                 Input monitoring


                           YES

                                          Display
          When checking [Hood switch]     open condition          Rubber at the above hood is not
            under closed condition                                pressing enough the hood switch.




  6)   When tailgate is opened by the key under system            QJI NOTE
       arm condition, horn works.
                                                                 When the door (driver's or passenger's) is opened by
                                                                 the key horn will work. ~» it's not malfunction (normal
                                                                 operation)
                                                                 (Arm system is released by the transmitter unlock
                                                                 only)




           [Tailgate key unlock switch]
                 Input monitoring


                           NO

             Check wiring short of                         1. BCM-EF©-MR02®-RR02®-R03© Check
           tailgate key unlock switch                      2. R03® - G06(Ground) Check

           Tailgate key unlock switch
                                                            Check the continuity while key in
                   malfunction

                                                                [R03]

                                                                            (Connector of tailgate
                                                                            key unlock switch)




                                                                                                                 KT0B765J
BE-74                                                            TROUBLESHOOTING PROCEDURE FOR BCM
  7)    Engine does not start, when the alarm released
        condition




                                                       YES
            Does the start motor move?                             Check the starting circuit


                             NO

                                                     Change in
         [Starter inhibit output] Turn the key   ]    on state      BCM is currently alarm
           into start position as monitoring.                          condition mode



                              Remain off

                                                                   Check the starting circuit
BODY CONTROL MODULE (BCM)                                                                                                       BE-75
     8)   Central door lock function works, but keyless en-
          try system does not work.




                               YES            Does the transmitter lamp work                NO
                                              when its button is depressed?
                                         V                                        J
                                                                                                         f
                                                                                         Transmitter battery replacement



                                                      f              j
                               YES           Does the hazard lamp turn on once              NO
                                             when transmitter is resynchronized
                                                    under ACC position?


                                                                                        After replacing transmitter, register
                                                                                        the transmitter code using Hi-scan
                                                                                       (See workshop manual page BE-54)




                               YES           Does the keyless entry operation               NO
                                              work after removing the key?




                      Normal                                                          Since BCM is defective, replace trans-
                                                                                       mitter and register transmitter code




                                                                                                                                KTOB765L



                                                                      3.   Transmitter resynchronization is not available in the
     \MN0TE                                                                following cases.
     Transmitter resynchronization                                         - When resynchronized by the other people's trans-
     When transmitters are not resynchronized, which has                   mitter,
     been registered already by the number 1, it can be                    - When resynchronized with new transmitter.
     used without registration of code registration.
     Since new transmitters are not registered by the
     resynchronization procedures, follow the transmitter
     code registration procedures.

1.   Perform transmitter resynchronization in the following
     cases.
     - After replacing transmitter battery
     - When synchronization between transmitter and
     BCM is not made.
2.   Transmitter resynchronization methods
     Turn off the ignition key after releasing the ignition key
     from OFF state to ACC position, and then press lock
     or unlock of the transmitter within 10 seconds, then
     hazard lamps blinks once.
