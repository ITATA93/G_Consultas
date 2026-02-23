# SQLUser.LB_InstrumentSchedule

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBIS_RowID | bigint | PK |  | NO | - |
| ChildQ165DR | - |  |  | SI | Child Reference: Pupila: Defecto Pupilar Aferente ... |
| LBIS_LabEpisodeNumber | varchar |  |  | SI | The lab episode number |
| LBIS_LabSite_DR | bigint |  | FK | SI | The lab site of the specimen container / material ... |
| LBIS_Material_DR | varchar |  | FK | SI | Material is to be used for the test
The specimen ... |
| LBIS_RequestSpecimenContainer_DR | bigint |  | FK | SI | The Request specimen container that is to be used ... |
| LBIS_ResultReceivedDate | date |  |  | SI | Date the last result was received |
| LBIS_ResultReceivedTime | time |  |  | SI | Time the last result was received |
| LBIS_ScheduleDate | date |  |  | SI | Date the test was scheduled |
| LBIS_ScheduleTime | time |  |  | SI | Time the test was scheduled |
| LBIS_SpecimenContainer_DR | bigint |  | FK | SI | The specimen container that is to be used for the ... |
| LBIS_SpecimenNumber | varchar |  |  | SI | The specimen or material  number |
| LBIS_Status | varchar |  |  | SI | - |
| LBIS_TransmissionDate | date |  |  | SI | Date the test was transmitted last |
| LBIS_TransmissionTime | time |  |  | SI | Time the test was transmitted last |
| Q162Q1 | - |  |  | SI | Area |
| Q162Q2 | - |  |  | SI | Ojo derecho (OD): |
| Q162Q3 | - |  |  | SI | Ojo Izquierdo (OI): |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*