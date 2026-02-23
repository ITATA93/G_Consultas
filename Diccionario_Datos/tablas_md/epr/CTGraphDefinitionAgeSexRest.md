# epr.CTGraphDefinitionAgeSexRest

**Schema:** epr
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GASParRef | bigint | PK |  | NO | - |
| GASAgeFrom | integer |  |  | SI | Age From |
| GASAgeTo | integer |  |  | SI | Age To |
| GASAgeUnit | varchar |  |  | SI | Age Unit |
| GASCodeTableTags | varchar |  |  | SI | List of code table Tags |
| GASCreatedDate | date |  |  | SI | Created Date |
| GASCreatedTime | time |  |  | SI | Created Time |
| GASCreatedUserDR | bigint |  | FK | SI | Created User |
| GASOwner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| GASSex | bigint |  |  | SI | Sex |
| GASUpdatedDate | date |  |  | SI | Updated Date |
| GASUpdatedTime | time |  |  | SI | Updated Time |
| GASUpdatedUserDR | bigint |  | FK | SI | Updated User |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*