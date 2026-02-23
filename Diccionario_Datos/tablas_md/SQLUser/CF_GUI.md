# SQLUser.CF_GUI

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GUICF_RowId1 | double | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: SALUD MENTAL |
| GUICF_RowId | double |  |  | NO | GUICF Row ID |
| GUI_AllowChangeLang | varchar |  |  | SI | Enable access to the Change Language functionality |
| GUI_AuditTrailTimelineStyling | varchar |  |  | SI | Use Audit Trail Timeline Styling |
| GUI_DisplaySearchResultsCaption | varchar |  |  | SI | Search Results Caption |
| GUI_DynamicFavourites | bit |  |  | SI | Enable Dynamic Favourites on Lookups |
| GUI_DynamicFavouritesNo | integer |  |  | SI | Number of Dynamic Favourites to display on Lookups... |
| GUI_EnableAssistant | varchar |  |  | SI | Enable TrakCare Assistant |
| GUI_FavIconPath | varchar |  |  | SI | Custom Fav Icon Path |
| GUI_HRTDefaultFont | varchar |  |  | SI | [DEPRECATED]
Deprecated in release: <DeprecatedIn... |
| GUI_NewMenuStyle | varchar |  |  | SI | NewMenuStyle  |
| GUI_OldFPBedStyle | varchar |  |  | SI | OldFPBedStyle |
| GUI_OverlayLookups | varchar |  |  | SI | OverlayLookups  |
| GUI_Owner | varchar |  |  | SI | - |
| GUI_PredictiveLookups | varchar |  |  | SI | PredictiveLookups |
| GUI_SpellcheckerHRT | varchar |  |  | SI | Use Browser Spellchecker for HTML Rich Text Fields |
| GUI_SpellcheckerT | varchar |  |  | SI | Use Browser Spellchecker for Textareas |
| GUI_StaticEpisBannerMenu | varchar |  |  | SI | Enable Static Episode for Patient Banner action me... |
| GUI_SupressMenuIcons | varchar |  |  | SI | SupressMenuIcons |
| GUI_SupressMenuText | varchar |  |  | SI | SupressMenuText |
| GUI_UseSVGAnnotation | varchar |  |  | SI | UseSVGAnnotation |
| Q06Q1 | - |  |  | SI | Objetivos |
| Q06Q2 | - |  |  | SI | Estrategias o Actividades |
| Q06Q3 | - |  |  | SI | Responsables |
| Q06Q4 | - |  |  | SI | Plazo |
| Q06Q5 | - |  |  | SI | Resultados |
| Q06Q6 | - |  |  | SI | Logros |
| Q06Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*