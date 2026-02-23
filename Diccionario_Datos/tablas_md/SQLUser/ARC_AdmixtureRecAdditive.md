# SQLUser.ARC_AdmixtureRecAdditive

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RECAD_ParRef | bigint | PK |  | NO | ARC_AdmixtureRecipe Parent Reference |
| ChildQ29DR | - |  |  | SI | Child Reference: Pertenencias del Paciente |
| Q24Q1 | - |  |  | SI | Rubor |
| Q24Q2 | - |  |  | SI | Sombras/Delineador |
| Q24Q3 | - |  |  | SI | Labial |
| Q24Q4 | - |  |  | SI | Encrespador |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RECAD_Additive_DR | varchar |  | FK | NO | Additive |
| RECAD_BaseQuantity | double |  |  | SI | Base Quantity |
| RECAD_Carrier | varchar |  |  | SI | Carrier |
| RECAD_Childsub | double |  |  | NO | Childsub |
| RECAD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RECAD_CreatedDate | date |  |  | SI | Created Date |
| RECAD_CreatedTime | time |  |  | SI | Created Time |
| RECAD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RECAD_Density | double |  |  | SI | Density |
| RECAD_MainItem | varchar |  |  | SI | Main Item |
| RECAD_Percentage | double |  |  | SI | Percentage |
| RECAD_Quantity | double |  |  | NO | Quantity |
| RECAD_RowId | varchar |  |  | NO | - |
| RECAD_Significant | varchar |  |  | SI | Significant |
| RECAD_UOM_DR | bigint |  | FK | NO | UOM |
| RECAD_UpdatedDate | date |  |  | SI | Updated Date |
| RECAD_UpdatedTime | time |  |  | SI | Updated Time |
| RECAD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*