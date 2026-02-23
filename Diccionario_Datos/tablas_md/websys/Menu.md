# websys.Menu

**Schema:** websys
**Columnas:** 49
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActionMenuCaption | varchar |  |  | SI | Caption to be used when this menu is displayed as ... |
| AllowDirectAccess | bit |  |  | SI | Allow third-party Direct acces
This will allow th... |
| Caption | varchar |  |  | SI | - |
| Chart | bigint |  |  | SI | - |
| ChartBook | bigint |  |  | SI | - |
| ConditionalExpression | varchar |  |  | SI | - |
| Deprecated | bit |  |  | SI | - |
| DeviceSettings | varchar |  |  | SI | [DEPRECATED]Previously used by legacy TC Mobile fr... |
| ExternalMenuID | varchar |  |  | SI | - |
| FlowsheetGroup | bigint |  |  | SI | Allows to override flowsheet in access profile |
| ForceSystemUI | bit |  |  | SI | Force this menu to be opened in ME UI |
| Image | varchar |  |  | SI | - |
| InfoPaneWidth | integer |  |  | SI | Info pane width |
| InternalMessage | varchar |  |  | SI | For Copy Menu Headers |
| JavascriptFileName | varchar |  |  | SI | filename of where the JavascriptFunction resides. ... |
| JavascriptFunction | varchar |  |  | SI | - |
| Keywords | varchar |  |  | SI | - |
| LinkComponent | bigint |  |  | SI | Used in conjunction with LinkUrl of websysDefault.... |
| LinkIsAnalytic | bit |  |  | SI | LinkURL refers to a deepsee dashboard
path may be... |
| LinkReport | bigint |  |  | SI | - |
| LinkUrl | varchar |  |  | SI | - |
| Method | varchar |  |  | SI | - |
| Name | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| PreviewLocalPrint | bit |  |  | SI | Used to trigger local printing from report preview... |
| PrintHookFor | bigint |  |  | SI | - |
| PrintLocal | bit |  |  | SI | - |
| PrintPreview | bit |  |  | SI | - |
| ReasonDeprecated | varchar |  |  | SI | - |
| ResponsiveDisplay | varchar |  |  | SI | Allows menu to be displayed only on the specified ... |
| Sequence | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| ShortcutKey | varchar |  |  | SI | - |
| ShowInInfoPane | bit |  |  | SI | whether Menu item is opened in an Info pane |
| ShowInNewWindow | varchar |  |  | SI | - |
| ShowInfoPaneEdit | bit |  |  | SI | show Info pane edit tab |
| ShowInfoPaneSummary | bit |  |  | SI | show Info pane summary tab |
| SubMenuOf | bigint |  |  | SI | - |
| SubMenus | varchar |  |  | SI | - |
| Target | varchar |  |  | SI | name of browser window frame to send the link |
| Tooltip | varchar |  |  | SI | - |
| Type | varchar |  |  | SI | [DEPRECATED]Type is now calculated at runtime in T... |
| UpdateDate | date |  |  | SI | - |
| UpdateTime | time |  |  | SI | - |
| UpdateUser | bigint |  |  | SI | - |
| ValueExpression | varchar |  |  | SI | - |
| WorkFlow | bigint |  |  | SI | Name of workflow |
| Worklist | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*