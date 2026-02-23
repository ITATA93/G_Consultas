# lab.CL_CollectionListNumber

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLN_ParRef | varchar | PK |  | NO | CL_CollectionList Parent Reference |
| CLN_Collector_DR | varchar |  | FK | SI | Collector DR |
| CLN_DateOfCollection | date |  |  | SI | Date Of Collection |
| CLN_DateOfCreation | date |  |  | SI | Date Of Creation |
| CLN_DatePrinted | date |  |  | SI | Date Printed |
| CLN_Number | numeric |  |  | NO | List Number |
| CLN_NumberOfPatients | numeric |  |  | SI | Number Of Patients |
| CLN_PatientType | varchar |  |  | SI | Patient Type |
| CLN_RowID | varchar |  |  | NO | - |
| CLN_TimeOfCreation | time |  |  | SI | Time Of Creation |
| CLN_TimePrinted | time |  |  | SI | Time Printed |
| CLN_UserLocation_DR | varchar |  | FK | SI | User Location DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*