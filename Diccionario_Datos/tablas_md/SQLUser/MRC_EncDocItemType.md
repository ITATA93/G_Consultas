# SQLUser.MRC_EncDocItemType

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOCITEM_RowId | bigint | PK |  | NO | - |
| ChildQ79DR | - |  |  | SI | Child Reference: Pensamiento |
| DOCITEM_AsAction | bit |  |  | SI | Provide as action |
| DOCITEM_CatId | varchar |  |  | SI | Category ID |
| DOCITEM_ClassName | varchar |  |  | SI | web class name |
| DOCITEM_Code | varchar |  |  | NO | code |
| DOCITEM_ComponentList | varchar |  |  | SI | Components which use this Documentation Item Type |
| DOCITEM_CreatedDate | date |  |  | SI | Created Date |
| DOCITEM_CreatedTime | time |  |  | SI | Created Time |
| DOCITEM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOCITEM_DefaultWorkFlow_DR | bigint |  | FK | SI | Default Workflow ID |
| DOCITEM_Desc | varchar |  |  | NO | description |
| DOCITEM_EditWorkFlow_DR | bigint |  | FK | SI | Edit Workflow ID |
| DOCITEM_HasCSFlag | bit |  |  | SI | Has Clinically Significant Flag |
| DOCITEM_HeaderDR | bigint |  | FK | SI | Header link |
| DOCITEM_IsClinicalPathway | bit |  |  | SI | is Clinical Pathway Action |
| DOCITEM_Owner | varchar |  |  | SI | Owner |
| DOCITEM_Sequence | integer |  |  | SI | MREncEntry sequence |
| DOCITEM_System | varchar |  |  | SI | System created |
| DOCITEM_URLEdit | varchar |  |  | SI | URL for editing |
| DOCITEM_URLNew | varchar |  |  | SI | URL for new |
| DOCITEM_UpdatedDate | date |  |  | SI | Updated Date |
| DOCITEM_UpdatedTime | time |  |  | SI | Updated Time |
| DOCITEM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q78Q1 | - |  |  | SI | Área |
| Q78Q2 | - |  |  | SI | Evaluación |
| Q78Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*