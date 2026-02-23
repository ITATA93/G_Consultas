# websys.SysTranslationItem

**Schema:** websys
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | varchar | PK |  | NO | - |
| Caption | varchar |  |  | SI | Default caption - can be translated to foreign lan... |
| CaptionStyle | varchar |  |  | SI | CSS style applied to caption. |
| CommentLength | varchar |  |  | SI | - |
| CustomLookupBrokerMethod | varchar |  |  | SI | - |
| CustomLookupClassName | varchar |  |  | SI | - |
| CustomLookupProperties | varchar |  |  | SI | Caret is translated into $c(1) for storage. |
| CustomLookupQueryName | varchar |  |  | SI | - |
| DefaultValueAlways | bit |  |  | SI | - |
| DefaultValueExpression | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| DisplayAsButton | bit |  |  | SI | - |
| DisplayOnly | bit |  |  | SI | - |
| DynamicFavourites | bit |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IconProfile | varchar |  |  | SI | - |
| LinkWorkFlow | bigint |  |  | SI | A workflow to link to. |
| LookupUserDefinedValues | varchar |  |  | SI | comma separated list if user defined values.
may ... |
| Name | varchar |  |  | NO | The name used to identify the item. |
| ReadOnly | bit |  |  | SI | The value item of the item is a READONLY field on ... |
| Required | bit |  |  | SI | The field will be generated in HTML with HTMLCLASS... |
| ShortcutKey | varchar |  |  | SI | - |
| ShowInfoPane | varchar |  |  | SI | - |
| Style | varchar |  |  | SI | CSS style applied to to item |
| TabSequence | varchar |  |  | SI | Sequence followed when TAB key is used to navigate... |
| Tooltip | varchar |  |  | SI | Tooltip displayed on mouseover events. Typically a... |
| Transform | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*