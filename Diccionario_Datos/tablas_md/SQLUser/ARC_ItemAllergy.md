# SQLUser.ARC_ItemAllergy

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALG_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ALG_Allergy_DR | bigint |  | FK | SI | Des Ref Allergy |
| ALG_Childsub | double |  |  | NO | Childsub |
| ALG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALG_CreatedDate | date |  |  | SI | Created Date |
| ALG_CreatedTime | time |  |  | SI | Created Time |
| ALG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALG_DrugMast_DR | bigint |  | FK | SI | Des Ref DrugMast |
| ALG_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| ALG_RowId | varchar |  |  | NO | - |
| ALG_UpdatedDate | date |  |  | SI | Updated Date |
| ALG_UpdatedTime | time |  |  | SI | Updated Time |
| ALG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ159DR | - |  |  | SI | Child Reference: Agudeza Visual (Espec.) |
| Q113Q1 | - |  |  | SI | Localización anatómica |
| Q113Q2 | - |  |  | SI | Sensibilidad táctil |
| Q113Q3 | - |  |  | SI | Sensibilidad térmica |
| Q113Q4 | - |  |  | SI | Sensibilidad nociceptiva |
| Q113Q5 | - |  |  | SI | Propiocepción |
| Q113Q6 | - |  |  | SI | Sensibilidad vibratoria |
| Q113Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*