# ECU Map Definitions (SIMK43)
**Source:** https://opengk.org/index.php?title=Map_Definitions
**Used with:** GKFlasher for Blue Tiburon tuning

---

## Key Tuning Maps

| Map Name | Description |
|----------|-------------|
| **c_n_max** | Ignition cut rev limiter |
| **c_n_max_max** | Fuel cut rev limiter |
| **c_n_max_hys** | RPM hysteresis for ignition cut |
| **c_n_max_hys_max** | RPM hysteresis for fuel cut |
| **id_tps_fl__n** | Threshold before full-load / open-loop WOT detection triggers fuel enrichment |
| **ip_ti_fl__n__amp** | Fuel add factor for enrichment during full load open loop |
| **ip_iga_bas__n_32__maf_hb** | **Basic ignition advance angle** (primary timing map) |
| **ip_iga_ref__n_32__maf_hb** | **Reference ignition advance angle** |
| **ip_iga_dif_min_bas** | Influences ignition angle blending between CVVT high/low states |
| **id_maf_tab** | **Mass airflow calibration table** (critical if changing MAF sensor or intake) |
