# SQLUser.MRC_DRGCodingEdition

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ED_ParRef | bigint | PK |  | NO | MRC_DRGCoding Parent Reference |
| ChildQ65DR | - |  |  | SI | Child Reference: Extremidades |
| ED_Childsub | double |  |  | NO | Childsub |
| ED_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ED_CreatedDate | date |  |  | SI | Created Date |
| ED_CreatedTime | time |  |  | SI | Created Time |
| ED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ED_Edition_DR | bigint |  | FK | SI | Des Ref Edition |
| ED_RowId | varchar |  |  | NO | - |
| ED_UpdatedDate | date |  |  | SI | Updated Date |
| ED_UpdatedTime | time |  |  | SI | Updated Time |
| ED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q58Q1 | - |  |  | SI | Palpación |
| Q58Q2 | - |  |  | SI | Percusión |
| Q58Q3 | - |  |  | SI | Auscultación |
| Q58Q4 | - |  |  | SI | Localización |
| Q58Q5 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*