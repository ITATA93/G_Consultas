# SQLUser.ARC_InsTypeTariff

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TAR_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ75DR | - |  |  | SI | Child Reference: Examen Neurológico |
| Q55Q1 | - |  |  | SI | Piel |
| Q55Q2 | - |  |  | SI | Evaluación |
| Q55Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TAR_Childsub | double |  |  | NO | Childsub |
| TAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TAR_CreatedDate | date |  |  | SI | Created Date |
| TAR_CreatedTime | time |  |  | SI | Created Time |
| TAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TAR_RowId | varchar |  |  | NO | - |
| TAR_Sequence | double |  |  | NO | Sequence |
| TAR_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| TAR_UpdatedDate | date |  |  | SI | Updated Date |
| TAR_UpdatedTime | time |  |  | SI | Updated Time |
| TAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*