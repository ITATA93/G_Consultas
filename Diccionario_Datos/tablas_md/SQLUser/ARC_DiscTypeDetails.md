# SQLUser.ARC_DiscTypeDetails

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | ARC_DiscType Parent Reference |
| ChildQ38DR | - |  |  | SI | Child Reference: Pulmonar Alterado |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | Date From |
| DET_DateTo | date |  |  | SI | Date To |
| DET_DiscType | varchar |  |  | SI | Discount Type |
| DET_FixedAmt | double |  |  | SI | Fixed Amt |
| DET_InsCover_DR | bigint |  | FK | SI | Des Ref InsCoverSta |
| DET_PatientType | varchar |  |  | SI | Patient Type |
| DET_Perc | double |  |  | SI | % Charge |
| DET_RowId | varchar |  |  | NO | - |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q30Q1 | - |  |  | SI | Lesión |
| Q30Q2 | - |  |  | SI | Lateralidad |
| Q30Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*