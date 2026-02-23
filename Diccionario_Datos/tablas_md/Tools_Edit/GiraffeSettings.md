# Tools_Edit.GiraffeSettings

**Schema:** Tools_Edit
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AllChartBooks | bit |  |  | SI | - |
| AllCharts | bit |  |  | SI | - |
| AllIconProfiles | bit |  |  | SI | - |
| AllQuestionnaires | bit |  |  | SI | - |
| CodeTableMenu | bit |  |  | SI | - |
| CodeTableMenuByCTEditionManagement | bit |  |  | SI | - |
| CurrentUser | varchar |  |  | SI | - |
| GroupDR | bigint |  | FK | SI | Properties for use with the Tree extract |
| LanguageDR | bigint |  | FK | SI | - |
| MainChart | bit |  |  | SI | - |
| MainChartBook | bit |  |  | SI | - |
| MenuHeader | bit |  |  | SI | - |
| PreviousEpisodeChart | bit |  |  | SI | - |
| ProfileDR | bigint |  | FK | SI | - |
| SideMenu | bit |  |  | SI | - |
| StartWorkFlow | bit |  |  | SI | - |
| StartWorkList | bit |  |  | SI | - |
| SuppressEmptyCodeTables | bit |  |  | SI | - |
| UserDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*