# lab.MR_CaseView

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCV_ParRef | varchar | PK |  | NO | MR_Case Parent Reference |
| MRCV_Comments | varchar |  |  | SI | Comments |
| MRCV_DateAppointment | date |  |  | SI | Date Appointment |
| MRCV_DateEnd | date |  |  | SI | Date End |
| MRCV_DateStart | date |  |  | SI | Date Start |
| MRCV_OrderNumber | double |  |  | NO | Order Number |
| MRCV_PersonAttending | varchar |  |  | SI | Person Attending |
| MRCV_Relationship | varchar |  |  | SI | Relationship |
| MRCV_RowID | varchar |  |  | NO | - |
| MRCV_TimeAppointment | time |  |  | SI | Time Appointment |
| MRCV_TimeEnd | time |  |  | SI | Time End |
| MRCV_TimeStart | time |  |  | SI | Time Start |
| MRCV_User1 | varchar |  |  | SI | User 1 |
| MRCV_User2 | varchar |  |  | SI | User 2 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*