# Elite 2500 Wiring Diagram - Rev 6

**Source:** `Haltech/Elite 2500 Wiring Diagram - Rev 6.pdf`

---

                                                                                                                                                                                                       ELITE 2500 WIRING DIAGRAM
                                                                                                                                                                                                                                                                                                 EXAMPLE CONNECTIONS
           EXAMPLE CONNECTIONS                                                                    [L]             INJECTOR #1
                                                                      INJECTORS                                                 19
                                                                                                                                                                                 SIGNAL GROUND FROM        [B/W]
                                                                  8 X INJECTOR DRIVERS           [L/B]            INJECTOR #2                                                        ECU PIN B15                                                                                                                                    FUEL
                                                                                                                                20                                                                                                  AVI 9 - 10                                                                                E            F
                                                                                                                                                                                 1
                                                                  CURRENT CONTROLLED                                                                             AVI 10 (TPS * )                            [W]
                                                                                                 [L/BR]           INJECTOR #3                               14                                                              ANALOGUE VOLTAGE INPUT
                                                                     0A - 8A PEAK CURRENT                                       21
                                                                     0A - 2A HOLD CURRENT                                                                        +5V SENSOR SUPPLY                          [O]            SWITCHABLE 1K PULL-UP
                                                                                                 [L/R]            INJECTOR #4                               9                                                              20V MAX INPUT VOLTAGE                                  THROTTLE POSITION SENSORS              FUEL LEVEL SENSOR
                                                                 INJECTOR OUTPUTS CAN BE                                        22                                                                                         1.5KHz MAX INPUT FREQUENCY
                                                                   USED AS GENERIC DPO’S
                                                                    WITH 1A MAX OUTPUT           [L/O]            INJECTOR #5
                                                                                                                                27                                               SIGNAL GROUND FROM        [B/W]
                                                                                                                                                                                                                           INPUT: 0V - 5V (20V MAXIMUM)

                                                                   WIRE INJECTOR                                                                                                     ECU PIN B15
                                                                 OUTPUT TO CYLINDER              [L/Y]            INJECTOR #6
                                                                                                                                28                                           1
                                                                                                                                                                 AVI 9 (MAP* )                              [Y]
                                                                      NUMBER
                                                                                                                                                            15
                                                                                                 [L/G]            INJECTOR #7
                                                                                                                                29                               +5V SENSOR SUPPLY                          [O]
                                 INJECTORS                                                                                                                  9
                                                                                                 [L/V]            INJECTOR #8                                                                                                                                                   MANIFOLD ABSOLUTE PRESSURE SENSOR        TEMPERATURE SENSORS
                                                                      OUTPUT: GROUND                                            30




                                                                                                                                     34 PIN CONNECTOR (A)
                                                                                                 [Y/B]            IGNITION #1
                                                                       IGNITION                                                 3                                +8V SENSOR SUPPLY                         [O/W]       +8V SENSOR SUPPLY
                                                                                                 [Y/R]            IGNITION #2                               12
                                                                 8 X IGNITION DRIVERS                                           4                                                                                           1A MAX OUTPUT CURRENT
                                     HALTECH HPI                  1A MAX CURRENT                                                                                                                                                                                                                                                     A/C
                                                                  OVERCURRENT PROTECTED          [Y/O]            IGNITION #3
IGNITION COIL WITHOUT                                                                                                           5
  INTERNAL IGNITER                                                IGNITION OUTPUTS CAN BE
                                                                   USED AS GENERIC DPO’S         [Y/G]            IGNITION #4
                                                                    WITH 1A MAX OUTPUT                                          6                                                                                                                                                       PRESSURE SENSORS                          SWITCHES
                                                                WIRE IGNITION OUTPUT             [Y/BR]           IGNITION #5                                                           ECU                INJECTION          IGNITION               FUEL PUMP
                                                                TO CYLINDER NUMBER                                              7
                                                                   FOR DIRECT FIRE                                                                               HALTECH 6 CIRCUIT                                                                                                  FUSE BLOCK NOTES:             RELAY PIN LAYOUT & SCHEMATIC
                                                                                                 [Y/L]            IGNITION #6
                       IGNITION COIL WITH                            OUTPUT: GROUND                                             8                                   FUSE BLOCK                                                                                                      15A CONTINUOUS, 20A PEAK
                                                                                                                                                                  PART #HT030102
                        INTERNAL IGNITER                                                                                                                                                                                                                                            MAX CURRENT RATING PER CIRCUIT

                                                                                                                                                                                                       1               2                         3                          4       FUSE ALLOCATIONS
           7
               8   9
                       10
                                                                            DPO                  [V/B]                  DPO 1
       6                    11                                   6 X DIGITAL PULSED OUTPUTS                                     18                                                                                                                                                  FUSE 1: 10A - ECU
                                              BOOST
                                                                   LOW SIDE DRIVE                                                                                                                                                                                                   FUSE 2: 20A - INJECTION
   5                                         CONTROL
                                             SOLENOID
                                                                   1A MAX CURRENT
                                                                                                 [V/BR]                 DPO 2                                                                                                                                                       FUSE 3: 15A - IGNITION        SUITS 4 OR 5 PIN
   4                                                                                                                            1




                                                                                                                                                                                                                                                            SPARE


                                                                                                                                                                                                                                                                    SPARE
                                                                                                                                                                                                                                                                                    FUSE 4: 20A - FUEL PUMP       STANDARD BOSCH RELAY




                                                                                                                                                                                                                                                     FUEL
                RPM                                                OVERCURRENT PROTECTED




                                                                                                                                                                                                                                 ECU




                                                                                                                                                                                                                                             IGN
                                                                                                                                                                                                                                       INJ
       3       X1000                                                                                                                                                                                                                                                                FUSE 5: SPARE
           2                                                      DPO 1: 0-12V PULL-UP           [V/R]                  DPO 3
               1                                                                                                                23                                                                                                                                                  FUSE 6: SPARE
                                                                  DPO 2: FIXED 5V PULL-UP
                                                                  DPO 3-6: FIXED 12V PULL-UP
   TACHOMETER                     BOOST CONTROL SOLENOID                                                                                                                                           5                   6        1      2     3       4      5       6
                                                                      OUTPUT: GROUND                                                                                                    SPARE              SPARE


                                                                   STEPPER 1 / DPO
                                                                 CAN BE CONFIGURED AS             [G]     STEPPER 1 P1 / DPO
                                                                                                                                31
                                                                  1 X STEPPER MOTOR DRIVER                                                                                                                                                                                                       [R/G]            FROM BATTERY POSITIVE ( + )
                                                                      PAIRED P1 & P2 / P3 & P4
                                                                  4 X HI/LOW SIDE DRIVERS        [G/B]    STEPPER 1 P2 / DPO                                                                                                                                                                                            *2 [SEE NOTE]
                                                                                                                                32                                        TO 26 POSITION CONNECTOR
                                                                     SPECIFICATIONS                                                                                               ECU PIN B11
                                                                   1A MAX CURRENT DRIVE          [G/BR]   STEPPER 1 P3 / DPO                                                                                                                                                                      [R]             FROM BATTERY POSITIVE ( + )
                                                                                                                                33
                                                                   1A MAX CURRENT SINK                                                                             +12V SWITCHED ECU SUPPLY [R/W]                                                                                                                       *2 [SEE NOTE]
                                                                   OVERCURRENT PROTECTED
                                                                                                 [G/R]    STEPPER 1 P4 / DPO
                                                                                                                                34                                                                                                                                                               [R/W]
                                                                 OUTPUT: BATT V OR GROUND                                                                                                                                                                                                                         FROM BATTERY POSITIVE ( + )

  VTEC SOLENOIDS                         IDLE MOTOR
                                                                                                                                                                 DPO 5 (FUEL PUMP TRIGGER)      [B/Y]                                                                                                                   *2 [SEE NOTE]
                                                                                                                                                            24
                                                                                                                                                                                                                                                                                                 [O/L]
                                                                                                                                                                                                                                                                                                                  TO POSITIVE SIDE OF FUEL PUMP (+)
                                                                       AVI  2-5                  [O/Y]                  AVI 4
                                                                          AVI                                                   2                                DPO 6 (ECR OUT)                [B/R]
                                                                 ANALOGUE VOLTAGE INPUTS
                                                                10 X ANALOGUE VOLTAGE INPUTS
                                                                                                                                                            25                                                                                                                                   [R/Y]
                                                                  SWITCHABLE 1K PULL-UP                                                                                                                                                                                                                           TO IGNITION COILS (+)
                                                                  20V MAX INPUT VOLTAGE
                                                                                                 [O/R]                  AVI 3
                                                                  1.5KHz MAX INPUT FREQUENCY
                                                                                                                                17                                                                                                                                                               [R/L]
                                                                                                                                                                 *3 ECU INJECTOR POWER INPUT [R/L]                                                                                                                   TO INJECTORS (+)
                                                                  RECOMMENDED AVIs FOR                                                                      26
                                                                  DBW SYSTEM                     [O/B]                  AVI 2                                                                                                                                                                                        *3 [SEE NOTE]
                                                                 INPUT: 0V - 5V (20V MAXIMUM)
                                                                 INPUT: 0V - 5V (20V MAXIMUM)                                   16                                (REQUIRED CONNECTION FOR ECU TO OPERATE)                                                                                      [GY/R]

                                                                                                                                                                                                                                                                                                                     13.8V OUTPUT TO SENSORS,
               APP AND                                          +5V SENSOR SUPPLY                 [O]     +5V SENSOR SUPPLY                                      BATTERY GROUND                                                                                                                                      RELAYS AND SOLENOIDS
               E-THROTTLE                                                                                                       9                           10
                                                                  100mA MAX OUTPUT CURRENT
               (DBW)
                                                                                                                                                                 BATTERY GROUND                  [B]                                                                                              [B]
                                                                                                                                                            11                                                                                                                                                    TO BATTERY (      ) TERMINAL
   LOOKING INTO CONNECTOR ON ECU
                                                                                                                                                                                                                                                                                                  [P]             SWITCHED +12V SUPPLY
                                                                                                                                                                 12V IGNITION INPUT
                                                                                                                                                            13                                                                                                                                                    FROM IGNITION SWITCH
                                                                                                                                                                                                                                                                                                                  (12V ON IGN AND CRANKING ONLY)
       1                                                   9                                                 9
                                                                                                    1
       10                                                  17                                                              LEGEND - WIRE COLOUR                                                                        NOTES:
                                                                                                                           B = BLACK   BR = BROWN   G = GREEN   GY = GREY   L = BLUE
                                                                                                                                                                                                                       *1 RECOMMENDED FUNCTION ALLOCATION,
       18                                                  25                                                              O = ORANGE P = PINK R = RED V = VIOLET Y = YELLOW W = WHITE                                                                                                    ELITE 2500 PREMIUM UNIVERSAL HARNESS 2.5M (8')
                                                                                                                           WHEN TWO COLOURS ARE USED IN A WIRE BY THE ALPHABETICAL CODE,                                   BUT NOT LIMITED TO
                                                                                                                                                                                                                       2
       26                                                  34                                                34            THE FIRST LETTER INDICATES THE BASIC WIRE COLOUR,                                           * CAN USE 75A CIRCUIT BREAKER                                  DOCUMENT REVISION:      6                   HT-141304
                                                                                                    26                     THE SECOND COLOUR INDICATES THE COLOUR OF THE STRIPE.
                                                                                                                                                                                                                       *3 DBW AND STEPPER SUPPLY, CURRENT
                                                                                                                                                                                                                          RETURN PATH                                                 DATE: MAY 2024                          SHEET 1 OF 2
                                                                                                                                                                                                                                          ELITE 2500 WIRING DIAGRAM
     EXAMPLE CONNECTIONS                                                                                                  IGNITION                                                                                                                                                                                          EXAMPLE CONNECTIONS
                                                                                                   [Y/V]          8 X IGNITION DRIVERS
                                                                                                                                                               IGNITION #7
                HP  NIT
                       ER
                            8                                                                                     1A MAX CURRENT                                                  17
                                                                                                                                                                                                                   SIGNAL GROUND                                            [B/W]
                 IG
                                                                                                                                                                                                              15
                                                                                                   [Y/GY]
                                                                                                                  OVERCURRENT PROTECTED                                                                                                                                                              A
                                                                                                                        ALL SPARE                              IGNITION #8                                                                         AVI 7 - 8
                                                          HECU3
                                                                                                                    IGNITION OUTPUTS                                              18                                           1
                                                                                                                                                                                                                   AVI 7 (ATS * )           ANALOGUE VOLTAGE INPUT           [GY]
                                                      7 6 5 4 3 2 1
                                                                                                                     CAN BE USED AS                                                                           3                                                                                      B
                                                                                                                   GENERIC DPO’S WITH                                                                                                      SWITCHABLE 1K PULL-UP
                                                                                                                      1A MAX OUTPUT                                                                                                        20V MAX INPUT VOLTAGE
                                                                                                                                                                                                                                           1.5KHz MAX INPUT FREQUENCY
                                                                                                                      OUTPUT: GROUND                                                                                                                                        [B/W]
      HALTECH HPI                             IGNITION MODULE                                                                                                                                                      SIGNAL GROUND
                                                                                                                                                                                                              15                                                                                     A
                                                                                                                                                                                                                                           INPUT: 0V - 5V (20V MAXIMUM)                                   AIR TEMPERATURE SENSOR             COOLANT TEMPERATURE SENSOR
                                                                                                                              DPO                                                                                              1
                                                                                                                                                                                                                   AVI 8 (CTS * )                                            [V]
      85       87
                                                                                                                 6 X DIGITAL PULSED OUTPUTS                                                                   4                                                                                      B
                                                                     RELAY                                         LOW SIDE DRIVE
                                                                                                   [V/O]           1A MAX CURRENT                                      DPO4                                                                                                                                           DBW RECOMMENDED WIRING INFORMATION
                                                                                                                   OVERCURRENT PROTECTED                                          19
      86         30

                                                                                                                  DPO 1: 0-12V PULL-UP                                                                                                                                                                                      +5V                      +5V
                                                                                                                  DPO 2: FIXED 5V PULL-UP                                                                                                                                                                                  AVI 2                     TPS 1
                                                                                                                  DPO 3-6: FIXED 12V PULL-UP
                                                                                                                                                                                                                                                                                                                           AVI 3                     TPS 2




                                                                                                                                                                                       26 PIN CONNECTOR (B)
     RELAYS                       THERMOFAN RELAY                                                                     OUTPUT: GROUND                                                                                                             DBW / DPO                                                                                           S.GND
                                                                                                                                                                                                                                                                                                                 SIGNAL GROUND
                                                                                                                                                                                                                   DBW 1 / DPO                  2 X HIGH CURRENT            [BR/B]
                                                                                                                                                                                                              25                               HI/LOW SIDE DRIVERS                                                        DBW 1                      MOTOR 1
                                                                                                                                                                                                                                                                                                                          DBW 2                      MOTOR 2
                                                                                                                           AVI 2-5
                                                                                                                             AVI
                                                                                                                                                                                                                                           5A PEAK MAX CURRENT
                                                                                                                  ANALOGUE VOLTAGE INPUTS                                                                          DBW 2 / DPO             1A AVERAGE CURRENT               [BR/R]
           APP AND                                                                                              10 X ANALOGUE VOLTAGE INPUTS
                                                                                                                  SWITCHABLE 1K PULL-UP
                                                                                                                                                                                                              26                           100KHz MAX FREQUENCY
                                                                                                   [O/G]                                                               AVI 5
           E-THROTTLE                                                                                             20V MAX INPUT VOLTAGE                                           20                                                       OUTPUT: BATT V OR GROUND                                                         +5V                      +5V
           (DBW)                                                                                                  1.5KHz MAX INPUT FREQUENCY                                                                                                                                                                               AVI 4                     APP 1
                                                                                                                  RECOMMENDED AVIs FOR
                                                                                                                  DBW SYSTEM
                                                                                                                                                                                                                                                AVI 1 / AVI 6                                                    SIGNAL GROUND                       S.GND
                                                                                                                 INPUT: 0V - 5V (20V MAXIMUM)                                                                                               ANALOGUE VOLTAGE INPUTS                                                         +5V                      +5V
                                                                                                                 INPUT: 0V - 5V (20V MAXIMUM)
                                                                                                                                                                                                                                          AVI 1 AND AVI 6 ARE COMPATIBLE                                                   AVI 5                     APP 2
                                                                                                                                                                                                                   AVI 6 (O2 INPUT 1*1)   WITH NARROWBAND O2 SENSORS
                                                                                                                                                                                                                                                                           SHIELDED [GY/O]
                                                                                                                                                                                                              12                                                                                                 SIGNAL GROUND                       S.GND
                                                                                                                                                                                                                                           CAN BE USED AS GENERIC AVI
                                                                                                                                                                 +12V                                                                      20V MAX INPUT VOLTAGE
                                                                CRANK (TRIGGER) INPUT                                                                            SWITCHED                                                                                                  SHIELDED [GY/Y]
                                                                                                                                                                                  11                               AVI 1 (O2 INPUT 2*1)    1.5KHz MAX INPUT FREQUENCY
                                                                                                                                                                                                              13                           NO INTERNAL PULL-UP RESISTOR
                                                                                             [R]                                                                 SIGNAL                                                                    TEMP SENSORS WILL REQUIRE
                                +12V SWITCHED                                                                                                                    GROUND
                                                                                             [L]                        4 CORE [GY]                                               15                                                       EXTERNAL 1K PULL-UP TO 5V

                                SIGNAL GROUND                                                                                                                                                                                              INPUT: 0V - 5V (20V MAXIMUM)
                                                                                                                                                                 CRANK (+)
                                                                                             [Y]                                                                                  1
                      CRANK (TRIGGER) (+)
                                                                                            [G]                                                                                                                    SPI 1                                                   SHIELDED [GY]
                          CRANK (TRIGGER) (-)                                                                                                                    CRANK (-)                                    8
                                                                                                                                                                                  5
                                                                                                                                                                                                                                                      SPI                  SHIELDED [GY/B]
                                                                                                                                                                                                                   SPI 2
                                                                                                                                                                 +12V                                         9                                 4 X SYNCHRONISED
                                                                      CAM (HOME) INPUT                                                                           SWITCHED                                                                         PULSED INPUTS
                                                                                                                                                                                  11                                                        SUPPORTS RELUCTOR INPUTS                                     VEHICLE SPEED SENSORS                 VEHICLE SPEED SENSORS
                                                                                             [R]                                                                 SIGNAL                                                                     SUPPORTS DIGITAL INPUTS                                           RELUCTOR                              HALL EFFECT
                                +12V SWITCHED                                                                                                                    GROUND
                                                                                                                                                                                  15                               SPI 3                    50KHz MAX FREQUENCY            SHIELDED [GY/BR]
                                                                                             [L]                      4 CORE [GY/B]                                                                           10                            25V DC MAX INPUT VOLTAGE
                                SIGNAL GROUND                                                                                                                    CAM (+)                                                                    SWITCHABLE 10K PULL-UP
                                                                                             [Y]                                                                                  2
                                 CAM (HOME) (+)
                                                                                            [G]                                                                                                                                                                                                                                FLEX
                                  CAM (HOME) (-)                                                                                                                 CAM (-)                                                                                                                                                       FUEL SENSOR

                                                                                                                                                                                  6                                SPI 4                                                   SHIELDED [GY/R]
                                                                                                                                                                                                              7

            CRANK AND CAM SENSOR WIRING INFORMATION
                                                                                                                                                                                                                                                                                                                 FREQUENCY BASED FLEX FUEL SENSOR
                                                       Hall Effect Sensor
                                                                                         +12V
           DIGITAL (HALL)                                      +                                                                                          SIGNAL GROUND                                                                            KNOCK
              SENSOR            X indicates not connected                       Signal Ground
                                                                                                                                                                                  15                               KNOCK 1                                                 SHIELDED [GY/G]
                                Please isolate and insulate    -                                                 MAIN HARNESS                                                                                 21                                2 X KNOCK INPUTS
                                to avoid damage to ECU                      Crank (Trigger) (+)
                                                               O                                                CAN CONNECTOR
                                                                            Crank (Trigger) (-)
                                                                       X                                          (DTM04-4P)                                                                                       KNOCK 2                    SUPPORTS PIEZO               SHIELDED [GY/L]
                                                                                                                                                                                                              22                              KNOCK SENSORS
                                                                                                                                                                                                                                              SYNCHRONISED TO
                                                                                                                                                 SWITCHED +13.8V SUPPLY                                                                       ENGINE POSITION
                                                        Reluctor Sensor                                                       [GY/R]
           RELUCTOR (VR)                                                                 +12V
                                                                      X                                                                            FROM ECU RELAY
              SENSOR            X indicates not connected
                                Please isolate and insulate           X
                                                                                Signal Ground                         1                                                                                            SIGNAL GROUND
                                to avoid damage to ECU                      Crank (Trigger) (+)                               [B/W]                       SIGNAL GROUND                                       16                           NOTE: SHIELDED CABLES SHOULD BE
                                                               +                                                      2                                                           15                                                                                                                                          KNOCK SENSORS
                                                               -            Crank (Trigger) (-)
                                                                                                                                                                                                                   SIGNAL GROUND           EARTHED AT ONE END OF THE CABLE ONLY
                                                                                                                                                                   CAN LOW                                    15
                                                                                                                      43                                                          24
                                                                                                                                                                                                                   SIGNAL GROUND                                            [B/W]                                            NOTE: DO NOT CONNECT SENSOR GROUND
                                                                                                                                                                   CAN HIGH                                   14                                                                                     TO SENSORS ONLY
                                                                                                                      34                                                                                                                                                                                                     TO BATTERY, CHASSIS OR ENGINE BLOCK
                                                                                                                                                                                  23
 LOOKING INTO CONNECTOR ON ECU
                                                                                                                                         CAN (ISO 11898)
                                                                                                                                                                                                                   +12V SWITCHED ECU SUPPLY (ECU POWER)                     [R/W]
                                                                                                                                      SUPPORTS SPEEDS UP TO 1MBits/s
                                                                                                                                                                                                              11                                                                                      FROM ECU RELAY IN FUSE BLOCK (R1)

                                                                                                                                       HALTECH BUS
                                                                                                                                       SUPPORTS ALL HALTECH
 1                                                                    7                                                   7            EXPANSION PRODUCTS
                                                                                                       1
                                                                                                                                       VEHICLE BUS
 8                                                                    13
                                                                                                                                       SELECTABLE PRECONFIGURED                LEGEND - WIRE COLOUR                                                             NOTES:
                                                                                                                                       VEHICLE CAN INTERFACE
14                                                                    19                                                                                                       B = BLACK   BR = BROWN   G = GREEN   GY = GREY   L = BLUE
                                                                                                                                       OBDII COMPLIANT
                                                                                                                                                                               O = ORANGE P = PINK R = RED V = VIOLET Y = YELLOW W = WHITE                      *1 RECOMMENDED FUNCTION ALLOCATION,            ELITE 2500 PREMIUM UNIVERSAL HARNESS 2.5M (8')
20                                                                    26                                                                                                       WHEN TWO COLOURS ARE USED IN A WIRE BY THE ALPHABETICAL CODE,                       BUT NOT LIMITED TO
                                                                                                                       26                                                      THE FIRST LETTER INDICATES THE BASIC WIRE COLOUR,                                *2 CAN USE 75A CIRCUIT BREAKER             DOCUMENT REVISION:      6                    HT-141304
                                                                                                           20                                                                  THE SECOND COLOUR INDICATES THE COLOUR OF THE STRIPE.
                                                                                                                                                                                                                                                                *3 DBW AND STEPPER SUPPLY, CURRENT
                                                                                                                                                                                                                                                                                                           DATE: MAY 2024                              SHEET 2 OF 2
                                                                                                                                                                                                                                                                   RETURN PATH
