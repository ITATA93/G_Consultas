# SQLUser.ARC_ItemCPTCode

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPT_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| CPT_ApplyEpisodeDate | varchar |  |  | SI | Apply Episode Date |
| CPT_Childsub | double |  |  | NO | Childsub |
| CPT_Code | varchar |  |  | SI | Code |
| CPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPT_CreatedDate | date |  |  | SI | Created Date |
| CPT_CreatedTime | time |  |  | SI | Created Time |
| CPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPT_DateFrom | date |  |  | SI | Date From |
| CPT_DateTo | date |  |  | SI | Date To |
| CPT_Desc | varchar |  |  | SI | Description |
| CPT_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| CPT_RowId | varchar |  |  | NO | - |
| CPT_UpdatedDate | date |  |  | SI | Updated Date |
| CPT_UpdatedTime | time |  |  | SI | Updated Time |
| CPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ165DR | - |  |  | SI | Child Reference: No Usar |
| Q166Q1 | - |  |  | SI | Ojo |
| Q166Q2 | - |  |  | SI | DPA |
| Q166Q3 | - |  |  | SI | Magnitud |
| Q166Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*