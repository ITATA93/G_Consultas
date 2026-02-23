# SQLUser.SS_UserDefControl

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONT_RowId | bigint | PK |  | NO | - |
| CONT_Code | varchar |  |  | NO | Code |
| CONT_CodeTable | varchar |  |  | SI | Code Table |
| CONT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONT_ControlType | varchar |  |  | SI | ControlType |
| CONT_CustomType | varchar |  |  | SI | CustomType |
| CONT_DBField | varchar |  |  | SI | Database Field |
| CONT_DecPlaces | double |  |  | SI | Decimal Places |
| CONT_DeepSeeExpression | varchar |  |  | SI | DeepSeeExpression |
| CONT_Deprecated | varchar |  |  | SI | Deprecated |
| CONT_Desc | varchar |  |  | NO | Description |
| CONT_Generated | varchar |  |  | SI | Generated |
| CONT_Image_DR | bigint |  | FK | SI | Des Ref Image (currently unused as at 21/4/10) |
| CONT_Inactive | varchar |  |  | SI | Inactive |
| CONT_InactiveDate | date |  |  | SI | Inactive Date |
| CONT_MaxValue | double |  |  | SI | MaxValue |
| CONT_MinValue | double |  |  | SI | MinValue |
| CONT_ObsItem_DR | bigint |  | FK | SI | Des Ref ObsItem |
| CONT_Owner | varchar |  |  | SI | Owner |
| CONT_ReasonDeprecated | varchar |  |  | SI | Deprecated Reason |
| CONT_Score | varchar |  |  | SI | Score (currently unused as at 21/4/10) |
| CONT_SingleOption | varchar |  |  | SI | SingleOption |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*