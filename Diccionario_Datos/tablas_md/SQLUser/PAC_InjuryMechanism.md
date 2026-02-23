# SQLUser.PAC_InjuryMechanism

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INJMECH_RowId | bigint | PK |  | NO | - |
| ChildQ35DR | - |  |  | SI | Child Reference: Dietitian goals |
| INJMECH_Code | varchar |  |  | NO | Code |
| INJMECH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INJMECH_CreatedDate | date |  |  | SI | Created Date |
| INJMECH_CreatedTime | time |  |  | SI | Created Time |
| INJMECH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INJMECH_DateFrom | date |  |  | SI | Date From |
| INJMECH_DateTo | date |  |  | SI | Date To |
| INJMECH_Desc | varchar |  |  | NO | Description |
| INJMECH_NationalCode | varchar |  |  | SI | National Code |
| INJMECH_Owner | varchar |  |  | SI | Owner |
| INJMECH_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| INJMECH_UpdatedDate | date |  |  | SI | Updated Date |
| INJMECH_UpdatedTime | time |  |  | SI | Updated Time |
| INJMECH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q33Q1 | - |  |  | SI | Goal |
| Q33Q2 | - |  |  | SI | Timing |
| Q33Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*