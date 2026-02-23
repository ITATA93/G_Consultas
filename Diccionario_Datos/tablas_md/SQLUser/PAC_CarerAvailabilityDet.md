# SQLUser.PAC_CarerAvailabilityDet

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_CarerAvailability Parent Reference |
| DET_CareTyp | varchar |  |  | SI | Care Type codes |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | Date From |
| DET_DateTo | date |  |  | SI | Date To |
| DET_DischargeType | varchar |  |  | SI | Discharge Type Codes |
| DET_RowId | varchar |  |  | NO | - |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q16Q1 | - |  |  | SI | Items |
| Q16Q2 | - |  |  | SI | Likes and dislikes |
| Q16Q3 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*