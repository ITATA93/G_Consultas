# epr_Pref.Observations

**Schema:** epr_Pref
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| PREFAction | varchar |  |  | NO | Action
A=Additional Items are added, S=Items defi... |
| PREFAdditionalCode | varchar |  |  | SI | Unique Identifier for duplicate Items |
| PREFCTObsGroupDR | bigint |  | FK | SI | Reference to the Code Table Observation Group |
| PREFChartContext | varchar |  |  | SI | Chart Context |
| PREFEWSMessage | varchar |  |  | SI | EWS Message |
| PREFEWSTotalIncomplete | bit |  |  | SI | EWS Total Incomplete |
| PREFEndBySystem | varchar |  |  | SI | Ended By System Process (CacheUser) |
| PREFEndByUserDR | bigint |  | FK | SI | Ended By User |
| PREFEndDate | date |  |  | SI | End Date |
| PREFEndTime | time |  |  | SI | End Time |
| PREFHighRange | numeric |  |  | SI | Interim High Range |
| PREFLowRange | numeric |  |  | SI | Interim Low Range |
| PREFObsGroupDR | bigint |  | FK | SI | Reference to restrict this preference for a partic... |
| PREFObsItemDR | bigint |  | FK | NO | Reference to the Code Table Observation Item |
| PREFOverrideCT | bit |  |  | SI | Override MRCObservationGroupItems Code Table of th... |
| PREFPAADMDR | bigint |  | FK | NO | Reference to Episode |
| PREFStartByUserDR | bigint |  | FK | SI | Started By User |
| PREFStartDate | date |  |  | NO | Start Date |
| PREFStartTime | time |  |  | NO | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*