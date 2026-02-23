# websys.Component

> "A re-usable server side component which may be used on one or more pages.

**Schema:** websys
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "A re-usable server side component which may be used on one or more pages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AccordionCaptions | varchar |  |  | SI | ab 79643 - allow translation of accordion captions |
| AlwaysReload | bit |  |  | SI | When enabled, will always reload the component wit... |
| ApiFlag | bit |  |  | SI | Component has an associated generated API and web ... |
| AutoPageDateField | varchar |  |  | SI | ab 18.03.08 66199 |
| Caption | varchar |  |  | SI | The Default caption for a component. Used in the m... |
| Caption1 | varchar |  |  | SI | - |
| Caption10 | varchar |  |  | SI | - |
| Caption11 | varchar |  |  | SI | - |
| Caption12 | varchar |  |  | SI | - |
| Caption13 | varchar |  |  | SI | - |
| Caption14 | varchar |  |  | SI | - |
| Caption15 | varchar |  |  | SI | - |
| Caption16 | varchar |  |  | SI | - |
| Caption17 | varchar |  |  | SI | - |
| Caption18 | varchar |  |  | SI | - |
| Caption19 | varchar |  |  | SI | - |
| Caption2 | varchar |  |  | SI | - |
| Caption20 | varchar |  |  | SI | - |
| Caption21 | varchar |  |  | SI | - |
| Caption22 | varchar |  |  | SI | - |
| Caption23 | varchar |  |  | SI | - |
| Caption24 | varchar |  |  | SI | - |
| Caption25 | varchar |  |  | SI | - |
| Caption26 | varchar |  |  | SI | - |
| Caption27 | varchar |  |  | SI | - |
| Caption28 | varchar |  |  | SI | - |
| Caption29 | varchar |  |  | SI | - |
| Caption3 | varchar |  |  | SI | - |
| Caption30 | varchar |  |  | SI | - |
| Caption4 | varchar |  |  | SI | - |
| Caption5 | varchar |  |  | SI | - |
| Caption6 | varchar |  |  | SI | - |
| Caption7 | varchar |  |  | SI | - |
| Caption8 | varchar |  |  | SI | - |
| Caption9 | varchar |  |  | SI | - |
| CenterForm | bit |  |  | SI | - |
| ClassName | varchar |  |  | SI | The class on which the component is based.<br>
Ap... |
| CodeTable | bit |  |  | SI | Identifies if a component is updating code table d... |
| CustomListFilter | varchar |  |  | SI | stored in ^websys.TranslationD for udf call to fil... |
| CustomScript | bit |  |  | SI | - |
| Deprecated | bit |  |  | SI | ab 79150 |
| Disabled | varchar |  |  | SI | If set all items within the component will be disa... |
| DisplayAsGrid | bit |  |  | SI | Display a list as a grid. Primarily used where a l... |
| DisplayOnly | bit |  |  | SI | Allow display only view of components at run time |
| DisplayType | varchar |  |  | SI | Type of component.<br>
May be one of:<br>
Find<b... |
| ExpandTree | bit |  |  | SI | - |
| FixHeaderRow | bit |  |  | SI | Flag to indicate if the header row should be fixed |
| FixedWidthColumns | bit |  |  | SI | - |
| FormSizeAndPosition | varchar |  |  | SI | comma separated (pixels)
top, left, height, width |
| FullScreen | bit |  |  | SI | - |
| Generated | bit |  |  | SI | Indicates that this component is a generated compo... |
| GeneratedExpression | varchar |  |  | SI | This expression will recreate the component. |
| GeneratedUpToDate | varchar |  |  | SI | This expression is used to determine whether the g... |
| Help | varchar |  |  | SI | HTML Help text. |
| HideHeadings | varchar |  |  | SI | Hide or Show headings in a table. Can be set a des... |
| HideMenus | varchar |  |  | SI | Hide or Show menus. Can be set a design time or ru... |
| LastUpdateDate | date |  |  | SI | - |
| LastUpdateTime | time |  |  | SI | - |
| ListGroupCollapsedColumn | varchar |  |  | SI | Used in conjunction with 'ListGroupColumn'
List c... |
| ListGroupColumn | varchar |  |  | SI | List column (component item name) that rows should... |
| ListPrint | bit |  |  | SI | - |
| ListRowClass | varchar |  |  | SI | ab 15.03.10 - string or expression which determine... |
| ListRowClassTabOnly | bit |  |  | SI | ab 1.01.10 - 81192 |
| ListRows | varchar |  |  | SI | - |
| LockExtraClass | varchar |  |  | SI | - |
| LockExtraId | varchar |  |  | SI | - |
| Menus | varchar |  |  | SI | Comma separated list of menu names |
| MonitorExtraInfo | bit |  |  | SI | - |
| MultiPart | bit |  |  | SI | Identify HTML FORM as multipart |
| Name | varchar |  |  | NO | A Name that unqiuely identifies a component |
| NumberOfFixedColumns | integer |  |  | SI | Number of fixed columns
Always the left most colu... |
| OnTouchLink | varchar |  |  | SI | TC-2356 - Link which is fired by the On Touch even... |
| OtherScripts | varchar |  |  | SI | Comma separated list of scripts.
Typically used t... |
| PassThruParameters | varchar |  |  | SI | Additional parameters to be passed through during ... |
| QueryName | varchar |  |  | SI | Name of a query which has been pre-defined in the ... |
| QuerySQL | varchar |  |  | SI | Dynamic SQL query used to derive Search criteria f... |
| QuerySQLNames | varchar |  |  | SI | Named parameters derived from SQLQuery |
| QuerySQLParsed | varchar |  |  | SI | The parsed version of the SQL query with :name rep... |
| ReasonDeprecated | varchar |  |  | SI | - |
| Script | bit |  |  | SI | If true component will include coded script file f... |
| ShowNextInNewWindow | varchar |  |  | SI | Applies to List Components.
Will open a new windo... |
| Style | varchar |  |  | SI | CSS Style applied to the component.<br>
Typically... |
| TableDelimiters | varchar |  |  | SI | System default delimiters for each table item for ... |
| TableSequence | varchar |  |  | SI | System default Sequence of table columns.
If not ... |
| Template | varchar |  |  | SI | HTML describing the System default layout.
Templa... |
| TextRepTemplate | longvarchar |  |  | SI | HTML describing the System default text representa... |
| UseFormSizeAndPosition | bit |  |  | SI | - |
| WrapColumns | bit |  |  | SI | - |
| cmpStyle | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*