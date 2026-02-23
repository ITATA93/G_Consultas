# SQLUser.SS_ARCOSRestProfile

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OSREST_RowId | bigint | PK |  | NO | - |
| OSREST_ARCOrdSetDateItem_DR | varchar |  | FK | SI | Des Ref ARCOrdSetDateItem |
| OSREST_CanChange | varchar |  |  | SI | Can Change |
| OSREST_Code | varchar |  |  | NO | Code |
| OSREST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OSREST_DateFrom | date |  |  | SI | Date From |
| OSREST_DateTo | date |  |  | SI | Date To |
| OSREST_DecreaseLimit | double |  |  | SI | Decrease Limit |
| OSREST_Desc | varchar |  |  | NO | Description |
| OSREST_FieldComponent | varchar |  |  | SI | Restricted Field Component |
| OSREST_FieldName | varchar |  |  | SI | Restricted Field Name |
| OSREST_IncreaseLimit | double |  |  | SI | Increase Limit |
| OSREST_Owner | varchar |  |  | SI | Owner |
| OSREST_ReasonRequired | varchar |  |  | SI | Reason Required |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*