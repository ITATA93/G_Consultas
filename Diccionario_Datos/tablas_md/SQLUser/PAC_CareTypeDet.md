# SQLUser.PAC_CareTypeDet

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_CareType Parent Reference |
| ChildQ15DR | - |  |  | SI | Child Reference: Dairy |
| DET_AdmSource | varchar |  |  | SI | AdmSource |
| DET_CarerAvail | varchar |  |  | SI | CarerAvail |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | DateFrom |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_DischargeType | varchar |  |  | SI | DischargeType |
| DET_FundingSource | varchar |  |  | SI | FundingSource |
| DET_InsType | varchar |  |  | SI | InsType |
| DET_MedicareSuffix | varchar |  |  | SI | MedicareSuffix |
| DET_Rowid | varchar |  |  | NO | - |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q14Q1 | - |  |  | SI | Items |
| Q14Q2 | - |  |  | SI | Likes and dislikes |
| Q14Q3 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*