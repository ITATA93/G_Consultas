# SQLUser.PAC_SnomedRelation

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOR_RowId | bigint | PK |  | NO | - |
| Q08Q1 | - |  |  | SI | Clinician |
| Q08Q2 | - |  |  | SI | Role |
| Q08Q3 | - |  |  | SI | Other (specify) |
| Q08Q4 | - |  |  | SI | Arrival time |
| Q08Q5 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNOR_CharacteristicType | varchar |  |  | SI | Characteristic Type |
| SNOR_CharacteristicType_DR | bigint |  | FK | SI | Characteristic Type ID |
| SNOR_Concept1_DR | bigint |  | FK | SI | Des Ref Concept1 |
| SNOR_Concept2_DR | bigint |  | FK | SI | Des Ref Concept2 |
| SNOR_CreatedDate | date |  |  | SI | Created Date |
| SNOR_CreatedTime | time |  |  | SI | Created Time |
| SNOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOR_EffectiveDate | date |  |  | SI | Effective Date |
| SNOR_Module_DR | bigint |  | FK | SI | Module ID |
| SNOR_Refinability | varchar |  |  | SI | Refinability |
| SNOR_RelID | varchar |  |  | SI | Relation ID |
| SNOR_RelationGroup | integer |  |  | SI | Des Ref Concept |
| SNOR_RelationType | varchar |  |  | SI | Relation Type |
| SNOR_RelationType_DR | bigint |  | FK | SI | Des Ref Concept |
| SNOR_Status | varchar |  |  | SI | Status |
| SNOR_UpdatedDate | date |  |  | SI | Updated Date |
| SNOR_UpdatedTime | time |  |  | SI | Updated Time |
| SNOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*