# websys.ComponentItems

**Schema:** websys
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| AttachedFile | bit |  |  | SI | Input type is file. |
| AutoPageDateColumn | varchar |  |  | SI | ab 17.04.08 66199 |
| AutoPageTimeColumn | varchar |  |  | SI | - |
| Caption | varchar |  |  | SI | Default caption - can be translated to foreign lan... |
| CaptionStyle | varchar |  |  | SI | CSS style applied to caption. |
| ClassMethod | varchar |  |  | SI | A class method that is invoked on the server when ... |
| ClassMethodIfDirty | bit |  |  | SI | Only run the class method if something has changes... |
| CommentDisplay | bit |  |  | SI | ab 29.06.07 61702 - text areas in lists get trunca... |
| CommentLength | varchar |  |  | SI | - |
| CustomExpression | varchar |  |  | SI | Applies to custom component items.
Custom items a... |
| CustomLookupBrokerMethod | varchar |  |  | SI | - |
| CustomLookupClassName | varchar |  |  | SI | - |
| CustomLookupProperties | varchar |  |  | SI | - |
| CustomLookupQueryName | varchar |  |  | SI | - |
| CustomTemplate | varchar |  |  | SI | Only applicable for 'Custom' type items
Expressio... |
| DataType | varchar |  |  | SI | Data type of the item.<br>
Use to apply correct c... |
| DefaultValueAlways | bit |  |  | SI | - |
| DefaultValueExpression | varchar |  |  | SI | - |
| Deprecated | bit |  |  | SI | ab 79150 |
| Description | varchar |  |  | SI | - |
| Disabled | bit |  |  | SI | Item is disabled.
Applies to text,textarea,checkb... |
| DisplayAsButton | bit |  |  | SI | - |
| DisplayOnly | bit |  |  | SI | The value item of the item is displayed as text ra... |
| DisplayType | varchar |  |  | SI | The type of Html field used to display the item on... |
| DoNotAdvanceWorkflow | bit |  |  | SI | If checked, clicking this item will not cause the ... |
| DynamicColumn | bit |  |  | SI | Only applicable for table items
If a table item i... |
| DynamicFavourites | bit |  |  | SI | - |
| DynamicFavouritesID | varchar |  |  | SI | - |
| GroupByEnabled | bit |  |  | SI | [DEPRECATED]Deprecated due to all applicable items... |
| GroupByValueExpr | varchar |  |  | SI | Expression that evaluates to a $list of values to ... |
| HelpUrl | varchar |  |  | SI | Url to context specific help.<br>
The URL may be:... |
| Hidden | bit |  |  | SI | Used to include data in an HTML form which is HIDD... |
| ID | varchar |  |  | NO | - |
| IconProfile | varchar |  |  | SI | The property value is an Icon Profile row ID. |
| Image | varchar |  |  | SI | An image to be displayed next to the item.<br>
Ap... |
| IsPIN | bit |  |  | SI | - |
| IsUsername | bit |  |  | SI | ab 5.11.07 - biometrics |
| ItemIdGetExpression | varchar |  |  | SI | Cache expression to get the value of the id for an... |
| LinkBoldExpr | varchar |  |  | SI | ab 24.07.07 64135 |
| LinkComponent | varchar |  |  | SI | The next component used in conjunction with websys... |
| LinkConditionalExp | varchar |  |  | SI | An Expression that sets a variable val to 0 to rem... |
| LinkExpression | varchar |  |  | SI | Cache Expression used to add add name value pairs ... |
| LinkJSFunction | varchar |  |  | SI | ab 11.03.10 - Link to a JavaScript function to eli... |
| LinkUrl | varchar |  |  | SI | A url to link to. Typically this is another CSP pa... |
| LinkWorkFlow | varchar |  |  | SI | A workflow to link to. This is %String as it can b... |
| ListCellStyle | varchar |  |  | SI | Style applied to cell in a list - for example to s... |
| ListboxLookupItem | varchar |  |  | SI | Applies to LISTBOX display types.<br>
Name of Loo... |
| LookupBrokerMethod | varchar |  |  | SI | - |
| LookupClassName | varchar |  |  | SI | Applies to TEXTBOX and LISTBOX display types.<br>... |
| LookupCondExpr | varchar |  |  | SI | 86227: Conditional lookup functionality on compone... |
| LookupCustomComponent | bigint |  |  | SI | component to add to lookup to give extra searching... |
| LookupJavascriptFunction | varchar |  |  | SI | Javascript function to be invoked on the browser w... |
| LookupPredictive | bit |  |  | SI | ab 75433: Predictive Text Lookups |
| LookupProperties | varchar |  |  | SI | Applies to TEXTBOX and LISTBOX display types.<br>... |
| LookupQueryName | varchar |  |  | SI | Applies to TEXTBOX and LISTBOX display types.<br>... |
| LookupUserDefined | bit |  |  | SI | - |
| LookupUserDefinedValues | varchar |  |  | SI | comma separated list if user defined values.
may ... |
| Name | varchar |  |  | SI | The name used to identify the item. |
| NestedComponent | bigint |  |  | SI | Component nested from a list to implement a 'tree-... |
| NestedComponentExpression | varchar |  |  | SI | Populated when nested component is an expression r... |
| NestedCondExpr | varchar |  |  | SI | The expression used to determine wether to include... |
| NestedDisplayAsTree | bit |  |  | SI | Display the nested component as a "tree" (i.e. row... |
| NestedTransExpr | varchar |  |  | SI | Cache script transition expression.
Use to link n... |
| OnChangeJSFunction | varchar |  |  | SI | Javascript function to call when a value is change... |
| OrderByAsc | varchar |  |  | SI | Order By Clause for ascending sequence lists.
Use... |
| OrderByDesc | varchar |  |  | SI | Order By Clause for descending sequence lists.
Us... |
| Password | bit |  |  | SI | Applies to TEXTBOX.<br>
If true, textbox is displ... |
| PasswordKeepVal | bit |  |  | SI | Keep entered password value (default behaviour for... |
| ReadOnly | bit |  |  | SI | The value item of the item is a READONLY field on ... |
| ReasonDeprecated | varchar |  |  | SI | - |
| ReferencedObject | varchar |  |  | SI | An object reference which is used to derive defaul... |
| Required | bit |  |  | SI | The field will be generated in HTML with HTMLCLASS... |
| RunChangeHandlerOnInput | bit |  |  | SI | IF true, adds debounce to the textbox so that the ... |
| SQLColumn | varchar |  |  | SI | - |
| SQLComment | varchar |  |  | SI | - |
| SQLExtendedReference | varchar |  |  | SI | - |
| SQLTable | varchar |  |  | SI | - |
| SQLToVBCodeTable | varchar |  |  | SI | - |
| Sequence | double |  |  | SI | Sequence
Used to control the render sequence of h... |
| ShortcutKey | varchar |  |  | SI | - |
| ShowInNewWindow | varchar |  |  | SI | Parameters to control how the new window is displa... |
| ShowInfoPane | varchar |  |  | SI | ab 80436 - - if value>0 then display info pane, if... |
| Style | varchar |  |  | SI | CSS style applied to to item |
| SwitchItems | varchar |  |  | SI | Only applicable for 'Switch' type items
Comma del... |
| TabSequence | varchar |  |  | SI | Sequence followed when TAB key is used to navigate... |
| Tooltip | varchar |  |  | SI | Tooltip displayed on mouseover events. Typically a... |
| Transform | varchar |  |  | SI | Optional. Used to modify the display value ;noaler... |
| ValueDefault | varchar |  |  | SI | - |
| ValueGet | varchar |  |  | SI | Cache expression to get the value of a property.<B... |
| ValueSet | varchar |  |  | SI | Cache expression to set the value of a property. M... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*