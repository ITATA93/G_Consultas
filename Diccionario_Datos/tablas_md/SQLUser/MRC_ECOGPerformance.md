# SQLUser.MRC_ECOGPerformance

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ECOG_RowId | bigint | PK |  | NO | - |
| ChildQ13DR | - |  |  | SI | Child Reference: Conductas desadaptativas |
| ECOG_Code | numeric |  |  | NO | Grade |
| ECOG_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| ECOG_CreatedDate | date |  |  | SI | Created Date |
| ECOG_CreatedTime | time |  |  | SI | Created Time |
| ECOG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ECOG_DateFrom | date |  |  | SI | DateFrom |
| ECOG_DateTo | date |  |  | SI | DateTo |
| ECOG_Desc | varchar |  |  | NO | Description |
| ECOG_Owner | varchar |  |  | SI | Code Table Owner |
| ECOG_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| ECOG_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| ECOG_UpdatedDate | date |  |  | SI | Updated Date |
| ECOG_UpdatedTime | time |  |  | SI | Updated Time |
| ECOG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q87Q1 | - |  |  | SI | Eje Diagnóstico |
| Q87Q2 | - |  |  | SI | Diagnóstico |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*