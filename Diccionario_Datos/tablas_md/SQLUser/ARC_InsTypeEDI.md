# SQLUser.ARC_InsTypeEDI

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EDI_RowId | bigint | PK |  | NO | - |
| ChildQ64DR | - |  |  | SI | Child Reference: EMBARAZOS |
| EDI_Active | varchar |  |  | SI | Active |
| EDI_CacheRoutine | varchar |  |  | SI | Cache Routine |
| EDI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EDI_CreatedDate | date |  |  | SI | Created Date |
| EDI_CreatedTime | time |  |  | SI | Created Time |
| EDI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EDI_FilePrefix | varchar |  |  | SI | FilePrefix |
| EDI_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| EDI_LastFileNumber | double |  |  | SI | LastFileNumber |
| EDI_Owner | varchar |  |  | SI | Owner |
| EDI_Path | varchar |  |  | SI | Path |
| EDI_UpdatedDate | date |  |  | SI | Updated Date |
| EDI_UpdatedTime | time |  |  | SI | Updated Time |
| EDI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q46Q1 | - |  |  | SI | Hallazgo |
| Q46Q2 | - |  |  | SI | Intensidad |
| Q46Q3 | - |  |  | SI | Ubicación |
| Q46Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*