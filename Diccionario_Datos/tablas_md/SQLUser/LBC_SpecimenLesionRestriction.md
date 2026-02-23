# SQLUser.LBC_SpecimenLesionRestriction

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPLR_ParRef | bigint | PK |  | NO | Parent Specimen DR |
| LBCSPLR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPLR_CreatedDate | date |  |  | SI | Created Date |
| LBCSPLR_CreatedTime | time |  |  | SI | Created Time |
| LBCSPLR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSPLR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSPLR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSPLR_Lesion_DR | bigint |  | FK | SI | Lesion DR |
| LBCSPLR_RowID | varchar |  |  | NO | - |
| LBCSPLR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSPLR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSPLR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q56Q1 | - |  |  | SI | Hipótesis Diagnóstico Médico |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*