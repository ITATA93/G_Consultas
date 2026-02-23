# SQLUser.PAC_SnomedTerms

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOT_RowId | bigint | PK |  | NO | - |
| ChildQ18DR | - |  |  | SI | Child Reference: Range of movement: active |
| Q17Q1 | - |  |  | SI | Body location |
| Q17Q2 | - |  |  | SI | Muscle tone |
| Q17Q3 | - |  |  | SI | Hypertonia |
| Q17Q4 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNOT_CaseSignificanceId | varchar |  |  | SI | case Significance Id |
| SNOT_Concept_DR | bigint |  | FK | SI | Des Ref Concept |
| SNOT_CreatedDate | date |  |  | SI | Created Date |
| SNOT_CreatedTime | time |  |  | SI | Created Time |
| SNOT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOT_DescId | varchar |  |  | SI | DescId |
| SNOT_DescStatus | varchar |  |  | SI | Description Status - 0 (Active), not 0 (Inactive) |
| SNOT_DescType | varchar |  |  | SI | Description Type - 1 (preferred term), 3 (fully sp... |
| SNOT_EffectiveDate | date |  |  | SI | Effective Date |
| SNOT_InitialCapitalStatus | varchar |  |  | SI | InitialCapitalStatus |
| SNOT_LanguageCode | varchar |  |  | SI | Language Code |
| SNOT_Module_DR | bigint |  | FK | SI | Module ID |
| SNOT_Term | varchar |  |  | SI | Term |
| SNOT_UpdatedDate | date |  |  | SI | Updated Date |
| SNOT_UpdatedTime | time |  |  | SI | Updated Time |
| SNOT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*