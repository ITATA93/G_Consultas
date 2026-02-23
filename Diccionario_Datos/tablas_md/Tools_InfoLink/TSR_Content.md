# Tools_InfoLink.TSR_Content

**Schema:** Tools_InfoLink
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| ContentCode | varchar |  |  | SI | Filled by the Provider specific Logic
Typcially t... |
| ContentDesc | varchar |  |  | SI | Filled by the Provider specific Logic
the single ... |
| DetailStreamDR | longvarbinary |  | FK | SI | optional contain the selected JSON or XML item ret... |
| MappedProperty | varchar |  |  | NO | name of the Property in the Class that was mapped... |
| MappedPropertyRow | varchar |  |  | SI | RowID of the mapped Property - used as short cut
... |
| ObjectClass | varchar |  |  | NO | 	Reference to the context object class,  |
| ObjectGUID | varchar |  |  | SI | 	A reference to the context GUID
	- support GUID ... |
| ObjectRow | varchar |  |  | NO | 	Reference to the context object class and rowid,  |
| ProviderDR | bigint |  | FK | NO | The source InfoLink Provider  |
| RequestFilter | varchar |  |  | SI | 	The (optional)  used filter for that Search Reque... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*