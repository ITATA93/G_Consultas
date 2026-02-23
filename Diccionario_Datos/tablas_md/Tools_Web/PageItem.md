# Tools_Web.PageItem

**Schema:** Tools_Web
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Active | bit |  |  | SI | Active field [1|0] |
| ColOrder | integer |  |  | SI | Order of columns/fields |
| Edit | bit |  |  | SI | Edit field [1|0], this mean will be available or n... |
| Hidden | bit |  |  | SI | Hidden field [1|0] |
| Label | varchar |  |  | NO | Caption that will appear on the page |
| Link | bit |  |  | SI | Link field [1|0] |
| ListBox | bit |  |  | SI | ListBox field [1|0] |
| LookupClass | varchar |  |  | SI | Name of the class to use as lookup. |
| LookupCustomType | varchar |  |  | SI | Code inside websys.CustomTypeItem  |
| LookupExtraParam | varchar |  |  | SI | javascript code to be executed. |
| LookupQuery | varchar |  |  | SI | Name of the query to populate the lookup. |
| PageClass | varchar |  |  | NO | Name of the class that inherit Tools.Web.Page. |
| QueryClass | varchar |  |  | NO | Name of the class where the data will be retrieved... |
| QueryField | varchar |  |  | NO | Name of the property of the class |
| Size | varchar |  |  | SI | Size of the input |
| Style | varchar |  |  | SI | CSS style  |
| TextArea | bit |  |  | SI | TextArea field [1|0] |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*