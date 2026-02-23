# SQLUser.PAC_ContOutcome

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTOUTC_RowId | bigint | PK |  | NO | - |
| CONTOUTC_Code | varchar |  |  | NO | Code |
| CONTOUTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTOUTC_CreatedDate | date |  |  | SI | Created Date |
| CONTOUTC_CreatedTime | time |  |  | SI | Created Time |
| CONTOUTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTOUTC_DateFrom | date |  |  | SI | Date From |
| CONTOUTC_DateTo | date |  |  | SI | Date To |
| CONTOUTC_Desc | varchar |  |  | NO | Description |
| CONTOUTC_Owner | varchar |  |  | SI | Owner |
| CONTOUTC_UpdatedDate | date |  |  | SI | Updated Date |
| CONTOUTC_UpdatedTime | time |  |  | SI | Updated Time |
| CONTOUTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ49DR | - |  |  | SI | Child Reference: Central IV TPA Intervention	 |
| Q118Q1 | - |  |  | SI | Central IV CVP Catheter Withdrawn (cm)	 |
| Q118Q2 | - |  |  | SI | Central IV External Catheter Length (cm)	 |
| Q118Q3 | - |  |  | SI | Central Internal Catheter Length (cm)	 |
| Q118Q4 | - |  |  | SI | Central IV Mid Arm Circumference (cm)	 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*