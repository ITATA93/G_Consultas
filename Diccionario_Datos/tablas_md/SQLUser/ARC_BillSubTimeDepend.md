# SQLUser.ARC_BillSubTimeDepend

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TIME_ParRef | varchar | PK |  | NO | ARC_BillSub Parent Reference |
| ChildQ46DR | - |  |  | SI | Child Reference: Lesiones cutáneas |
| Q108Q1 | - |  |  | SI | Hallazgos |
| Q108Q2 | - |  |  | SI | Extremidad superior |
| Q108Q3 | - |  |  | SI | Extremidad inferior |
| Q108Q4 | - |  |  | SI | Ubicación |
| Q108Q5 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TIME_Childsub | double |  |  | NO | Childsub |
| TIME_CreatedDate | date |  |  | SI | Created Date |
| TIME_CreatedTime | time |  |  | SI | Created Time |
| TIME_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TIME_DOWFrom | double |  |  | SI | Day Of Week From |
| TIME_DOWTo | double |  |  | SI | Day Of Week To |
| TIME_DateFrom | date |  |  | SI | Date From |
| TIME_DateTo | date |  |  | SI | Date To |
| TIME_FixedAmt | double |  |  | SI | Fixed Amt |
| TIME_Perc | double |  |  | SI | % Charge |
| TIME_RowId | varchar |  |  | NO | - |
| TIME_TimeFrom | time |  |  | SI | Time From |
| TIME_TimeTo | time |  |  | SI | Time To |
| TIME_UpdatedDate | date |  |  | SI | Updated Date |
| TIME_UpdatedTime | time |  |  | SI | Updated Time |
| TIME_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| TIME_VisitType | varchar |  |  | SI | Visit Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*